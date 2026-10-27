# Simulador interactivo: Simulacro 30·90

🌐 **Español** · [English](README.en.md)

Simulador en el navegador para las dos partes de la prueba, con un **laboratorio para escribir código**, disponible en **español e inglés** (botón ES/EN arriba):

| Modo | Preguntas | Tiempo | Contenido |
|---|---|---|---|
| **Razonamiento abstracto** | 30 | 30:00 | Figuras **generadas al azar**: rotaciones, cantidades, posiciones, lados, cuadrantes, figuras con dos reglas, matrices 3×3, dominós D-48, series numéricas y de letras. La dificultad aumenta |
| **Técnico (opción múltiple)** | 40 | 50:00 | Banco de 60 preguntas **en inglés**: SQL (15), Python (15), algoritmos (12), bases de datos (8), AWS (10) |
| **Práctica por tema** | Ilimitadas | Sin tiempo | Retroalimentación inmediata con explicación. Incluye además **12 preguntas de estadística y ML** (solo en práctica) |
| **Laboratorio SQL** | 36 | Meta por nivel | Escribes consultas reales; se corrigen al instante |
| **Reto SQL** | 5 | 60:00 | 5 consultas de nivel 🟡–🔴, sin ver soluciones (como la prueba reportada en Glassdoor) |
| **Laboratorio Python** | 45 | Meta por ejercicio | 25 ejercicios de Python + 20 de algoritmos, con pruebas automáticas |

**Pensado para aprender inglés:** arriba eliges el **idioma de las preguntas**. En **inglés** (como el examen real) cada pregunta tiene el botón **"Ver traducción"**; en **español** (para aprender un tema) tiene **"Ver en inglés"** con el original. El idioma de la interfaz (ES/EN) se elige aparte.

**Diseño:** modo **blanco** o **negro** con el botón ☀️/🌙 (se recuerda en tu navegador), letra **Century Gothic** (si tu equipo no la tiene, se usa *Didact Gothic*, muy parecida) y transiciones suaves al cambiar de pantalla y al responder. Si tu sistema pide reducir el movimiento, las animaciones se desactivan.

Al terminar un simulacro ves tu puntaje, el resultado **por tema** y la revisión pregunta por pregunta con la explicación. Tus últimos 8 intentos se guardan en tu navegador.

> 💡 **Simulador AWS AI Practitioner:** Para practicar el examen oficial AIF-C01 (65 preguntas, 90 minutos) con selector de idioma y explicaciones detalladas, visita el [simulador de AWS AI Practitioner](../aws-ai-practitioner/simulator/README.md).

## Laboratorio de código

Aquí no eliges entre opciones: **escribes el código**, lo ejecutas y el laboratorio lo corrige. Usa los mismos ejercicios, soluciones y pruebas del repositorio (los incrusta [`scripts/build_lab.py`](../scripts/build_lab.py), y la CI comprueba que estén al día).

- **SQL:** los [35 ejercicios del módulo 02](../02-sql/ejercicios.md) sobre la misma base de datos de la tienda, en SQLite dentro del navegador ([sql.js](https://sql.js.org/)). **Comprobar** compara tu resultado con el de la solución: te dice si te sobran o faltan filas o columnas, si el orden está mal o si cambian los valores. Califica el **resultado**, no la forma de escribir la consulta: los alias, los nombres y el orden de las columnas dan igual, las columnas de más no restan, el orden de las filas solo cuenta si el enunciado lo pide y, si el enunciado no dice qué columnas mostrar, basta con devolver las filas correctas. Los errores de SQLite (que salen en inglés) vienen con una explicación. Tienes el panel de tablas, un **editor libre** y el **reto de 5 consultas en 60 minutos**.
- **Python:** los [25 ejercicios del módulo 03](../03-python/ejercicios.py) y los [20 problemas del módulo 04](../04-algoritmos-y-estructuras/problemas.py), con Python 3 en el navegador ([Pyodide](https://pyodide.org/)). Ves cada caso de prueba (✓/✗), lo que imprimes con `print()` y los errores con su línea. Si un ciclo no termina, se corta a los 8 segundos.
- Tu código se guarda en tu navegador: puedes cerrar y seguir después. `Ctrl + Enter` ejecuta y `Tab` agrega sangría.
- La primera vez se descarga el motor (SQL unos 0,7 MB; Python unos 12 MB). Necesita internet.

## Cómo abrirlo

- **En línea (recomendado, funciona en el celular):** [frank1808k.github.io/blend360/simulador](https://frank1808k.github.io/blend360/simulador/).
- **Local:** abre `simulator/index.html` con doble clic en cualquier navegador (no requiere instalar nada).
- **GitHub Pages:** el flujo [`pages.yml`](../.github/workflows/pages.yml) lo vuelve a publicar en `/simulador/` cada vez que el simulador o la documentación cambian en la rama por defecto del repositorio, junto con el [centro de estudio web](https://frank1808k.github.io/blend360/). Si alguna vez no se publica, revisa *Settings → Pages → Source: **GitHub Actions***.

**Atajos de teclado:** `A`–`D` o `1`–`4` para responder, `←` `→` para moverte entre preguntas, `T` para ver la traducción.

> Las preguntas son originales y de práctica; no provienen de ningún examen real.
