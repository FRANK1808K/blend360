# Blend360 All Star: preparación para la prueba de ingreso

🌐 **Español** · [English](README.en.md)

[![Checks](https://github.com/FRANK1808K/blend360/actions/workflows/checks.yml/badge.svg)](https://github.com/FRANK1808K/blend360/actions/workflows/checks.yml)
![Examen](https://img.shields.io/badge/examen-18%20dic%202026-0d6e66)
![AWS AIF-C01](https://img.shields.io/badge/AWS%20AIF--C01-16%20nov%202026-FF9900?logo=amazonwebservices&logoColor=white)
![Idiomas](https://img.shields.io/badge/idiomas-Espa%C3%B1ol%20%7C%20English-1f4e79)

Repositorio de estudio para la prueba del **programa All Star (semillero) de Blend360 en Colombia**:

| Parte | Duración | Temas |
|---|---|---|
| **Razonamiento abstracto** | 30 min | Series de figuras, matrices, dominós, series numéricas y de letras |
| **Prueba técnica** (en inglés) | 90 min | SQL · Python · qué es AWS y análisis de datos en AWS · algoritmos básicos · bases de datos · estructuras de datos · resolución de problemas |

Cada documento existe **en español y en inglés**. Los ejercicios y simulacros vienen **en inglés**, como en la prueba real, con la **traducción al español escondida debajo de cada pregunta** para cuando te bloquees. Además hay un módulo de inglés técnico para nivel A2. Las soluciones de código están **verificadas automáticamente**.

> **Aviso:** material de estudio comunitario, **no oficial** y sin relación con Blend360. Las preguntas son originales. Lo que se sabe del proceso viene de reseñas públicas de candidatos ([ver investigación](guides/que-evalua-blend360.md)).

**En línea, sin instalar nada (también en el celular):** 📖 [Centro de estudio web](https://frank1808k.github.io/blend360/) (todo el material organizado en *Estudiar · Evaluar · Repasar*, búsqueda, modo blanco/negro, **progreso guardado**) · 🎯 [Simulador + laboratorio de código](https://frank1808k.github.io/blend360/simulador/) · ☁️ [Simulador AIF-C01](https://frank1808k.github.io/blend360/simulador-aif/)

---

## ¿Por dónde empiezo?

| Tu situación | Empieza aquí |
|---|---|
| 📅 **Quiero saber qué estudiar cada día** | [Plan de estudio 26 oct → 18 dic](guides/plan-de-estudio.md) (incluye el AWS AIF-C01 del 16 de nov) |
| 🔎 **Quiero saber cómo evalúa Blend360** | [Qué evalúa Blend360](guides/que-evalua-blend360.md): proceso reportado por candidatos, relación con AWS, preguntas para el reclutador |
| 🧪 **Quiero medir mi nivel ya** | [Simulador interactivo](simulator/README.md) · [Simulacro técnico](simulacros/simulacro-tecnico-01.md) · [Simulacro de razonamiento](simulacros/simulacro-razonamiento-01.md) |
| ⌨️ **Quiero practicar escribiendo código** | [Laboratorio del simulador](simulator/README.md#laboratorio-de-código): escribes SQL o Python en el navegador (también en el celular) y se corrige al instante |
| 🇬🇧 **Mi inglés es A2 y me preocupa** | [Plan de inglés](english/README.md) → [cómo leer preguntas en inglés](english/como-leer-preguntas.md) |
| ⏰ **El examen es en 2 días** | [Repaso final de 48 h](cheatsheets/repaso-final-48h.md) + [cheatsheets](cheatsheets/README.md) |

## Cómo usar los dos idiomas

1. **Aprende** cada tema primero en español (esta versión).
2. **Relee** la misma sección en inglés ([English](README.en.md)). Como ya conoces el contenido, aprendes las palabras en inglés en contexto.
3. **Practica** siempre en inglés. Abre la traducción al español solo cuando te bloquees, y anota las palabras que no sabías en tus [flashcards](flashcards/README.md).

> Cada archivo `X.md` (español) tiene su gemelo `X.en.md` (inglés). Arriba de cada documento está el selector 🌐 para cambiar de idioma.

## Módulos

| # | Módulo | Contenido | Práctica |
|---|---|---|---|
| 01 | [Razonamiento abstracto](01-razonamiento-abstracto/README.md) | Tipos de pregunta, checklist **FORMA-CPR**, estrategia para los 30 min | [50 ejercicios](01-razonamiento-abstracto/ejercicios.md) + figuras ilimitadas en el [simulador](simulator/README.md) |
| 02 | [SQL](02-sql/README.md) | De `SELECT` a funciones de ventana, NULLs, JOINs, CTEs, patrones de entrevista | [35 ejercicios](02-sql/ejercicios.md) sobre una base de datos real (SQLite), también en el [laboratorio SQL](simulator/README.md#laboratorio-de-código) |
| 03 | [Python](03-python/README.md) + [pandas](03-python/pandas.md) | Fundamentos, trampas, quiz "¿qué imprime?", pandas ↔ SQL | [25 ejercicios](03-python/ejercicios.py) con corrector automático, también en el [laboratorio Python](simulator/README.md#laboratorio-de-código) |
| 04 | [Algoritmos y estructuras de datos](04-algoritmos-y-estructuras/README.md) | Big O, estructuras, búsqueda y ordenamiento, recursión, patrones, pseudocódigo | [20 problemas clásicos](04-algoritmos-y-estructuras/problemas.py) con corrector, también en el [laboratorio](simulator/README.md#laboratorio-de-código) |
| 05 | [Bases de datos](05-bases-de-datos/README.md) | Llaves, normalización, ACID, índices, OLTP/OLAP, estrella, lake/warehouse, NoSQL | Autoevaluación |
| 06 | [AWS](06-aws/README.md) + [análisis de datos en AWS](06-aws/analisis-de-datos.md) | Nube, IAM, servicios, precios; S3, Glue, Athena, Redshift, EMR, Kinesis, QuickSight | [30 preguntas en inglés](06-aws/preguntas.md) |
| 07 | [Resolución de problemas](07-resolucion-de-problemas/README.md) | Método UMPIRE, gestión del tiempo, lógica, porcentajes, probabilidad, estadística, casos de negocio | Ejercicios resueltos |
| 08 | [Estadística y machine learning](08-estadistica-y-ml/README.md) | Descriptiva, probabilidad, inferencia, **pruebas A/B**, regresión, ML, métricas; ruta de estudio con tus apuntes de Drive | [25 preguntas](08-estadistica-y-ml/preguntas.md) + [script desde cero](08-estadistica-y-ml/estadistica_ml_practica.py) |
| EN | [Inglés técnico (A2 → funcional)](english/README.md) | Palabras clave de los enunciados, falsos amigos, vocabulario, gramática mínima, entrevista | [Ejercicios](english/ejercicios-ingles.md) + [209 flashcards](flashcards/README.md) |
| AI | [AWS AI Practitioner (AIF-C01)](aws-ai-practitioner/README.md) | 5 dominios oficiales (v1.1), Bedrock, SageMaker, IA responsable, gobernanza, lab RAG, cheatsheets | [2 simulacros (130 preguntas)](aws-ai-practitioner/practice-questions/README.md) + [simulador](aws-ai-practitioner/simulator/README.md) + [109 flashcards](aws-ai-practitioner/flashcards/README.md) |

## Practicar

```bash
git clone https://github.com/FRANK1808K/blend360.git && cd blend360

# SQL: crea la base de datos de práctica y abre una consola
cd 02-sql && python3 setup_db.py --shell

# Python: corrige tus ejercicios
cd ../03-python && python3 test_ejercicios.py

# Algoritmos: corrige tus problemas
cd ../04-algoritmos-y-estructuras && python3 test_problemas.py

# Simulador: abre simulator/index.html en el navegador
```

## Sitio web de estudio (Quarto)

El [centro de estudio](https://frank1808k.github.io/blend360/) reúne todo el repositorio en un sitio hecho con [Quarto](https://quarto.org/), organizado por objetivo:

| Sección | Qué contiene |
|---|---|
| 📚 **Estudiar** | Mapa de estudio con prioridades y horas, la teoría de cada módulo y el inglés técnico |
| 🧪 **Evaluar** | Ruta de evaluación con metas, ejercicios por tema, simulacros y el simulador |
| 🔁 **Repasar** | Cheatsheets (con botón para imprimir), repaso final de 48 h y flashcards |
| ☁️ **AIF-C01** | Los 5 dominios, preguntas por dominio, 2 simulacros, cheatsheets, estrategia, laboratorio y recursos |
| 📈 **Progreso** | Páginas estudiadas, registro de simulacros con gráfica, cuaderno de errores con fechas de repaso, intentos de los simuladores y copia de seguridad |

Además: la portada muestra **qué toca esta semana** según el plan y la cuenta regresiva a los dos exámenes; las casillas del plan de estudio se pueden marcar y se guardan; cada página tiene botones para marcarla como estudiada, mostrar u ocultar todas las soluciones e imprimirla; y los diagramas del módulo AIF-C01 se dibujan.

El Markdown del repositorio sigue siendo la única fuente: [`scripts/build_site.py`](scripts/build_site.py) lo adapta y lo renderiza junto con [`quarto/`](quarto/) (configuración, tema, portada, centros y JavaScript). Para construirlo en tu computador necesitas [Quarto](https://quarto.org/docs/get-started/) 1.10 o superior (la CI usa la 1.10.18):

```bash
python3 scripts/build_site.py            # → _site/ (abre _site/index.html)
python3 scripts/build_site.py --preview  # vista previa en vivo
```

> Si agregas un documento nuevo, añádelo a `NAV` en `scripts/build_site.py`: la construcción falla si una página no está en la navegación.

Solo necesitas **Python 3.8+** (y `pip install pandas` para la práctica de pandas). No hay otras dependencias.

## Estructura

```text
blend360/
├── guides/                     Plan de estudio con fechas + investigación del proceso
├── 01-razonamiento-abstracto/  Teoría + 50 ejercicios
├── 02-sql/                     Teoría + base SQLite + 35 ejercicios verificados
├── 03-python/                  Teoría + 25 ejercicios + pandas
├── 04-algoritmos-y-estructuras/Teoría + 20 problemas
├── 05-bases-de-datos/          Teoría
├── 06-aws/                     Nube + análisis de datos + 30 preguntas
├── aws-ai-practitioner/        Certificación AWS Certified AI Practitioner (AIF-C01 completa)
├── 07-resolucion-de-problemas/ Método, lógica, estadística, casos
├── 08-estadistica-y-ml/        Estadística, pruebas A/B y ML + 25 preguntas
├── english/                    Inglés técnico para A2
├── simulacros/                 Simulacro técnico (90 min) + razonamiento (30 min)
├── simulator/                  Simulador + laboratorio de código (ES/EN, modo blanco/negro)
├── quarto/                     Sitio web de estudio (Quarto): configuración, tema, portada, centros y progreso
├── scripts/                    Verificación de documentos y generación del laboratorio y del sitio
├── cheatsheets/                Repasos de una página + plan de 48 h
└── flashcards/                 209 tarjetas para Anki
```

## Calidad del material

La CI ([`checks.yml`](.github/workflows/checks.yml)) verifica en cada cambio que:

- Las **36 soluciones SQL**, en los dos idiomas, se ejecutan y producen exactamente el "resultado esperado" publicado (`02-sql/check_solutions.py`).
- Las **25 soluciones de Python**, los **20 problemas de algoritmos** y las fórmulas de estadística y ML (`08-estadistica-y-ml/estadistica_ml_practica.py`) pasan sus pruebas.
- El Markdown cumple las reglas de estilo (`markdownlint`), cada documento tiene su versión en el otro idioma y todos los enlaces internos funcionan (`scripts/check_docs.py`).
- El sitio web Quarto se construye sin advertencias ni enlaces o anclas rotas, y todas las páginas están en la navegación (`scripts/build_site.py --strict`).
- El laboratorio del simulador usa exactamente los mismos ejercicios, soluciones y pruebas del repositorio (`scripts/build_lab.py --check`).

## Fechas clave

| Fecha | Evento |
|---|---|
| 26 oct 2026 | Inicio del plan |
| **16 nov 2026** | AWS Certified AI Practitioner (AIF-C01) |
| 17 nov 2026 | Inicio de la fase Blend360 a fondo |
| 16–17 dic 2026 | Repaso final |
| **18 dic 2026** | Prueba Blend360 All Star |
