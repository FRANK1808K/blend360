# Simulador interactivo AIF-C01

Simulador del examen con **interfaz en blanco** (como la del examen real), **cronómetro**, **marcadores de revisión**, **navegador de preguntas**, botón **«Ver en inglés»** en cada pregunta e **informe por dominio** con el formato «Cumple / Necesita mejora» del informe oficial de AWS.

## Cómo abrirlo

- **En el navegador, sin instalar nada:** descarga [`index.html`](index.html) (botón *Raw* → Guardar como) y ábrelo con doble clic. Funciona sin conexión salvo las fuentes tipográficas.
- **Desde el repositorio clonado:** abre `simulator/index.html` en tu navegador.

## Pruebas disponibles

| Prueba | Preguntas | Tiempo estándar |
|---|---|---|
| Simulacro 01 | 65 (pesos oficiales, incluye v1.1) | 90 min |
| Simulacro 02 | 65 de escenario, más difícil | 90 min |
| Refuerzo D1 · D3 · D4 · D5 | 40 al azar de los dominios débiles | 55 min |
| Novedades v1.1 | Todas las preguntas 🆕 de ambos simulacros | ≈ 1,4 min por pregunta |

**Ver en inglés:** cada pregunta tiene un botón que despliega su versión en inglés (pregunta y opciones) para que te familiarices con los términos del examen original. Si lo dejas abierto, se mantiene abierto en las siguientes preguntas. En el informe final, cada pregunta revisada también tiene su versión en inglés.

Opciones: tiempo **estándar**, **ESL +30** (×1,33) o **sin límite**, y **corrección inmediata** (modo estudio). El progreso de un intento en curso y el historial de resultados se guardan **solo en tu navegador** (`localStorage`).

## Regenerar tras editar los simulacros

Las preguntas salen de `practice-questions/mock-exam-*.md` (español y clave) y de `practice-questions/en/mock-exam-*.md` (inglés). Si cambias una pregunta, actualiza también su versión en inglés con el mismo número y las mismas letras. Después:

```bash
python simulator/build.py
```

El script valida que cada pregunta tenga su entrada en la clave de respuestas, que la respuesta exista entre las opciones y que la versión en inglés tenga la misma pregunta y las mismas letras.
