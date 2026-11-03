-- Base de práctica «Mercado del Pacífico» (Quibdó, Chocó).
-- Una tienda en línea que vende cosechas, pescado y artesanías del Chocó a clientes de la región y del resto del país.
-- SQLite 3.25+ (funciones de ventana). La usa la presentación presentaciones/sql/index.html (corre en el navegador).
-- En tu computador: sqlite3 mercado.db < mercado_pacifico.sql
--
-- Trampas puestas a propósito para practicar:
--   * Wilmer Murillo (cliente 6) nunca ha comprado            → LEFT JOIN ... IS NULL / NOT EXISTS
--   * El camarón de río (producto 9) nunca se ha vendido
--   * Wilmer no tiene municipio (NULL) y Jhon Freddy no tiene correo (NULL)
--   * Hay pedidos «cancelado»: casi nunca se cuentan como venta
--   * precio_unitario (lo que se cobró) a veces es distinto de productos.precio (precio de lista): hubo descuentos
--   * Camila Mena y Julián Lloreda ganan lo mismo             → empates con RANK y DENSE_RANK
--   * Daniel Rentería gana más que su jefa directa            → self join

DROP TABLE IF EXISTS detalle_pedido;
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS empleados;

CREATE TABLE clientes (
    cliente_id      INTEGER PRIMARY KEY,
    nombre          TEXT    NOT NULL,
    correo          TEXT    UNIQUE,
    municipio       TEXT,                  -- puede ser NULL a propósito
    departamento    TEXT    NOT NULL,
    segmento        TEXT    NOT NULL,      -- 'Hogar', 'Restaurante', 'Tienda'
    fecha_registro  DATE    NOT NULL
);

CREATE TABLE productos (
    producto_id     INTEGER PRIMARY KEY,
    nombre          TEXT    NOT NULL,
    categoria       TEXT    NOT NULL,      -- 'Artesanías', 'Pescados', 'Cosechas'
    precio          INTEGER NOT NULL CHECK (precio > 0)   -- pesos colombianos (COP)
);

CREATE TABLE pedidos (
    pedido_id       INTEGER PRIMARY KEY,
    cliente_id      INTEGER NOT NULL REFERENCES clientes(cliente_id),
    fecha_pedido    DATE    NOT NULL,
    estado          TEXT    NOT NULL       -- 'entregado', 'enviado', 'cancelado'
);

CREATE TABLE detalle_pedido (
    pedido_id       INTEGER NOT NULL REFERENCES pedidos(pedido_id),
    producto_id     INTEGER NOT NULL REFERENCES productos(producto_id),
    cantidad        INTEGER NOT NULL CHECK (cantidad > 0),
    precio_unitario INTEGER NOT NULL,      -- precio realmente cobrado (COP)
    PRIMARY KEY (pedido_id, producto_id)
);

CREATE TABLE empleados (
    empleado_id     INTEGER PRIMARY KEY,
    nombre          TEXT    NOT NULL,
    area            TEXT    NOT NULL,
    salario         INTEGER NOT NULL,      -- salario mensual (COP)
    jefe_id         INTEGER REFERENCES empleados(empleado_id),  -- NULL = no tiene jefe (gerente)
    fecha_ingreso   DATE    NOT NULL
);

INSERT INTO clientes VALUES
 (1,  'Yeison Mosquera',      'yeison@correo.co',    'Quibdó',       'Chocó',        'Hogar',       '2024-01-15'),
 (2,  'Leidy Palacios',       'leidy@correo.co',     'Istmina',      'Chocó',        'Restaurante', '2024-02-03'),
 (3,  'Darwin Córdoba',       'darwin@correo.co',    'Tadó',         'Chocó',        'Hogar',       '2024-02-20'),
 (4,  'Yuranis Rentería',     'yuranis@correo.co',   'Medellín',     'Antioquia',    'Tienda',      '2024-03-11'),
 (5,  'Neyla Valencia',       'neyla@correo.co',     'Quibdó',       'Chocó',        'Restaurante', '2024-03-25'),
 (6,  'Wilmer Murillo',       'wilmer@correo.co',    NULL,           'Chocó',        'Hogar',       '2024-04-02'),
 (7,  'Katherine Perea',      'katherine@correo.co', 'Turbo',        'Antioquia',    'Hogar',       '2024-04-18'),
 (8,  'Edwin Cuesta',         'edwin@correo.co',     'Bahía Solano', 'Chocó',        'Tienda',      '2024-05-07'),
 (9,  'Ana Lucía Moreno',     'analucia@correo.co',  'Bogotá',       'Cundinamarca', 'Hogar',       '2024-05-30'),
 (10, 'Jhon Freddy Asprilla', NULL,                  'Condoto',      'Chocó',        'Hogar',       '2024-06-12');

INSERT INTO productos VALUES
 (1, 'Canasto de werregue',  'Artesanías', 420000),
 (2, 'Aretes de chaquira',   'Artesanías',  25000),
 (3, 'Mochila de damagua',   'Artesanías',  60000),
 (4, 'Bocachico (kg)',       'Pescados',    18000),
 (5, 'Pargo rojo (kg)',      'Pescados',    35000),
 (6, 'Borojó (unidad)',      'Cosechas',     6000),
 (7, 'Chontaduro (racimo)',  'Cosechas',    15000),
 (8, 'Tambora de chirimía',  'Artesanías', 280000),
 (9, 'Camarón de río (kg)',  'Pescados',    40000);   -- nunca vendido

INSERT INTO pedidos VALUES
 (101, 1,  '2024-02-01', 'entregado'),
 (102, 2,  '2024-02-14', 'entregado'),
 (103, 1,  '2024-03-05', 'entregado'),
 (104, 3,  '2024-03-18', 'cancelado'),
 (105, 4,  '2024-04-02', 'entregado'),
 (106, 5,  '2024-04-10', 'entregado'),
 (107, 2,  '2024-04-22', 'enviado'),
 (108, 7,  '2024-05-01', 'entregado'),
 (109, 1,  '2024-05-15', 'entregado'),
 (110, 8,  '2024-05-20', 'entregado'),
 (111, 5,  '2024-06-03', 'entregado'),
 (112, 9,  '2024-06-15', 'cancelado'),
 (113, 4,  '2024-06-28', 'entregado'),
 (114, 2,  '2024-07-04', 'entregado'),
 (115, 10, '2024-07-19', 'enviado');
-- El cliente 6 (Wilmer) nunca ha comprado.

INSERT INTO detalle_pedido VALUES
 (101, 1,  1, 420000),
 (101, 2,  2,  25000),
 (102, 4, 12,  18000),
 (102, 6, 10,   6000),
 (103, 3,  1,  60000),
 (104, 5,  4,  35000),
 (105, 8,  1, 280000),
 (105, 2,  2,  25000),
 (106, 1,  2, 400000),   -- precio con descuento
 (106, 5,  6,  35000),
 (107, 7,  5,  15000),
 (108, 6,  3,   6000),
 (108, 7,  2,  15000),
 (109, 8,  1, 280000),
 (110, 4,  5,  18000),
 (110, 3,  2,  60000),
 (111, 2,  4,  25000),
 (112, 1,  1, 420000),
 (113, 5,  8,  35000),
 (114, 1,  1, 420000),
 (114, 8,  2, 270000),   -- precio con descuento
 (115, 6, 20,   6000);

INSERT INTO empleados VALUES
 (1,  'Rosa Elvira Hinestroza', 'Gerencia',   18000000, NULL, '2019-01-10'),
 (2,  'Andrés Copete',          'Datos',       7000000, 1,    '2020-03-01'),
 (3,  'Camila Mena',            'Datos',       4500000, 2,    '2021-06-15'),
 (4,  'Julián Lloreda',         'Datos',       4500000, 2,    '2022-01-20'),
 (5,  'Paula Rivas',            'Datos',       3500000, 2,    '2023-08-01'),
 (6,  'Felipe Ibargüen',        'Ingeniería',  6500000, 1,    '2020-05-12'),
 (7,  'Natalia Moreno',         'Ingeniería',  5000000, 6,    '2021-09-30'),
 (8,  'Santiago Chaverra',      'Ingeniería',  4000000, 6,    '2023-02-14'),
 (9,  'Isabel Bejarano',        'Mercadeo',    4750000, 1,    '2021-11-08'),
 (10, 'Mateo Palacios',         'Mercadeo',    3000000, 9,    '2024-04-01'),
 (11, 'Daniel Rentería',        'Ingeniería',  5500000, 7,    '2022-07-01');  -- gana más que su jefa (Natalia)
