-- Practice database: online store (retail/marketing analytics style).
-- Base de datos de práctica: tienda en línea (estilo retail/marketing analytics).
-- SQLite 3.25+ (window functions / funciones de ventana). Create / Crear: python3 setup_db.py

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employees;

CREATE TABLE customers (
    customer_id  INTEGER PRIMARY KEY,
    name         TEXT    NOT NULL,
    email        TEXT    UNIQUE,
    city         TEXT,                 -- may be NULL on purpose / puede ser NULL a propósito
    country      TEXT    NOT NULL,
    segment      TEXT    NOT NULL,     -- 'Consumer', 'Corporate', 'Small Business'
    signup_date  DATE    NOT NULL
);

CREATE TABLE products (
    product_id   INTEGER PRIMARY KEY,
    name         TEXT    NOT NULL,
    category     TEXT    NOT NULL,
    price        REAL    NOT NULL CHECK (price > 0)
);

CREATE TABLE orders (
    order_id     INTEGER PRIMARY KEY,
    customer_id  INTEGER NOT NULL REFERENCES customers(customer_id),
    order_date   DATE    NOT NULL,
    status       TEXT    NOT NULL      -- 'delivered', 'shipped', 'cancelled'
);

CREATE TABLE order_items (
    order_id     INTEGER NOT NULL REFERENCES orders(order_id),
    product_id   INTEGER NOT NULL REFERENCES products(product_id),
    quantity     INTEGER NOT NULL CHECK (quantity > 0),
    unit_price   REAL    NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

CREATE TABLE employees (
    emp_id       INTEGER PRIMARY KEY,
    name         TEXT    NOT NULL,
    department   TEXT    NOT NULL,
    salary       INTEGER NOT NULL,
    manager_id   INTEGER REFERENCES employees(emp_id),  -- NULL = no manager (CEO) / no tiene jefe
    hire_date    DATE    NOT NULL
);

INSERT INTO customers VALUES
 (1,  'Ana Gómez',       'ana@mail.com',     'Bogotá',       'Colombia', 'Consumer',       '2024-01-15'),
 (2,  'Luis Pérez',      'luis@mail.com',    'Medellín',     'Colombia', 'Corporate',      '2024-02-03'),
 (3,  'María Ruiz',      'maria@mail.com',   'Cali',         'Colombia', 'Consumer',       '2024-02-20'),
 (4,  'John Smith',      'john@mail.com',    'Miami',        'USA',      'Small Business', '2024-03-11'),
 (5,  'Sofía Torres',    'sofia@mail.com',   'Bogotá',       'Colombia', 'Corporate',      '2024-03-25'),
 (6,  'Carlos Díaz',     'carlos@mail.com',  NULL,           'Colombia', 'Consumer',       '2024-04-02'),
 (7,  'Emily Brown',     'emily@mail.com',   'New York',     'USA',      'Consumer',       '2024-04-18'),
 (8,  'Pedro Castro',    'pedro@mail.com',   'Barranquilla', 'Colombia', 'Small Business', '2024-05-07'),
 (9,  'Laura Moreno',    'laura@mail.com',   'Lima',         'Peru',     'Consumer',       '2024-05-30'),
 (10, 'Diego Vargas',    NULL,               'Medellín',     'Colombia', 'Consumer',       '2024-06-12');

INSERT INTO products VALUES
 (1, 'Laptop Pro 14',     'Electronics', 1200.00),
 (2, 'Wireless Mouse',    'Electronics',   25.00),
 (3, 'USB-C Hub',         'Electronics',   45.00),
 (4, 'Office Chair',      'Furniture',    180.00),
 (5, 'Standing Desk',     'Furniture',    350.00),
 (6, 'Notebook A5',       'Stationery',     4.50),
 (7, 'Gel Pens (x10)',    'Stationery',     8.00),
 (8, 'Monitor 27"',       'Electronics',  300.00),
 (9, 'Desk Lamp',         'Furniture',     40.00);   -- product 9: never sold / nunca vendido

INSERT INTO orders VALUES
 (101, 1, '2024-02-01', 'delivered'),
 (102, 2, '2024-02-14', 'delivered'),
 (103, 1, '2024-03-05', 'delivered'),
 (104, 3, '2024-03-18', 'cancelled'),
 (105, 4, '2024-04-02', 'delivered'),
 (106, 5, '2024-04-10', 'delivered'),
 (107, 2, '2024-04-22', 'shipped'),
 (108, 7, '2024-05-01', 'delivered'),
 (109, 1, '2024-05-15', 'delivered'),
 (110, 8, '2024-05-20', 'delivered'),
 (111, 5, '2024-06-03', 'delivered'),
 (112, 9, '2024-06-15', 'cancelled'),
 (113, 4, '2024-06-28', 'delivered'),
 (114, 2, '2024-07-04', 'delivered'),
 (115, 10,'2024-07-19', 'shipped');
-- Customer 6 (Carlos) never bought anything / nunca ha comprado.

INSERT INTO order_items VALUES
 (101, 1, 1, 1200.00),
 (101, 2, 2,   25.00),
 (102, 4, 3,  180.00),
 (102, 6, 10,   4.50),
 (103, 3, 1,   45.00),
 (104, 5, 1,  350.00),
 (105, 8, 2,  300.00),
 (105, 2, 2,   25.00),
 (106, 1, 2, 1150.00),   -- discounted price / precio con descuento
 (106, 5, 1,  350.00),
 (107, 7, 5,    8.00),
 (108, 6, 3,    4.50),
 (108, 7, 2,    8.00),
 (109, 8, 1,  300.00),
 (110, 4, 1,  180.00),
 (110, 3, 2,   45.00),
 (111, 2, 4,   25.00),
 (112, 1, 1, 1200.00),
 (113, 5, 2,  350.00),
 (114, 1, 1, 1200.00),
 (114, 8, 2,  290.00),
 (115, 6, 20,   4.50);

INSERT INTO employees VALUES
 (1,  'Valentina Ríos',  'Executive',   25000, NULL, '2019-01-10'),
 (2,  'Andrés López',    'Data',        14000, 1,    '2020-03-01'),
 (3,  'Camila Herrera',  'Data',         9000, 2,    '2021-06-15'),
 (4,  'Julián Mejía',    'Data',         9000, 2,    '2022-01-20'),
 (5,  'Paula Ortiz',     'Data',         7000, 2,    '2023-08-01'),
 (6,  'Felipe Rojas',    'Engineering', 13000, 1,    '2020-05-12'),
 (7,  'Natalia Cruz',    'Engineering', 10000, 6,    '2021-09-30'),
 (8,  'Santiago Gil',    'Engineering',  8000, 6,    '2023-02-14'),
 (9,  'Isabel Suárez',   'Marketing',    9500, 1,    '2021-11-08'),
 (10, 'Mateo Ramírez',   'Marketing',    6000, 9,    '2024-04-01'),
 (11, 'Daniel Pardo',    'Engineering', 11000, 7,    '2022-07-01');  -- earns more than his manager (Natalia) / gana más que su jefa
