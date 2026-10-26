# Recursos Oficiales de AWS

[⬅️ Centro de recursos](README.md)

## 1. Examen: guía, alcance y políticas

| Recurso | Idioma | Notas |
|---|---|---|
| ⭐ [Página de la certificación AWS Certified AI Practitioner](https://aws.amazon.com/certification/certified-ai-practitioner/) | 🇬🇧 (y otras) | Inscripción, idiomas disponibles, modalidades (centro Pearson VUE u online). |
| ⭐ [Guía del examen AIF-C01 (HTML)](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html) | 🇬🇧 | Versión navegable por dominios. |
| ⭐ [Guía del examen en **español** (PDF)](https://docs.aws.amazon.com/es_es/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.pdf) | 🇪🇸 | Traducción oficial; útil si vas a hacer el examen en español. |
| [Guía del examen en inglés (PDF)](https://docs.aws.amazon.com/pdfs/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.pdf) | 🇬🇧 | Referencia original. |
| ⭐ [Servicios en alcance (*in-scope services*)](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-in-scope-services.html) | 🇬🇧 | Lista no exhaustiva de servicios que pueden aparecer. |
| ⭐ [Historial de revisiones de la guía](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/aif-01-revisions.html) | 🇬🇧 | Cambios de la v1.1 (30-abr-2026). Revísala antes de examinarte por si hay una versión más reciente. |
| [Dominio 1 de la guía (HTML)](https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01-domain1.html) | 🇬🇧 | Desde aquí se navega al resto de dominios. |
| ⭐ [Políticas antes del examen (incluye ESL +30 min)](https://aws.amazon.com/certification/policies/before-testing/) | 🇬🇧 | Adaptaciones, identificación y reglas del examen. |

### Datos del examen confirmados

- **Idiomas:** inglés, **español (Latinoamérica)**, **español (España)**, japonés, coreano, portugués (Brasil), chino simplificado y tradicional, francés y árabe, entre otros. AWS anunció la retirada de las versiones en **italiano y alemán después del 15 de octubre de 2026**.
- **Modalidad:** centro de pruebas Pearson VUE o examen online supervisado.
- **ESL +30:** si haces el examen **en inglés** y no es tu lengua materna, puedes solicitar **30 minutos extra**. Se pide **una vez, antes de reservar**, desde tu cuenta de AWS Certification, y se aplica a todos tus exámenes futuros. Ver el [playbook](../guides/exam-playbook.md#1-inscripción-decisiones-que-cambian-tu-resultado).

## 2. AWS Skill Builder (formación oficial)

| Recurso | Costo | Contenido |
|---|---|---|
| ⭐ [Exam Prep Plan: AWS Certified AI Practitioner (AIF-C01)](https://skillbuilder.aws/learning-plan/3NRN71QZR2/exam-prep-plan-aws-certified-ai-practitioner-aifc01--english/FBV4STG94B) | 🆓 plan estándar / 💲 plan mejorado | Plan en 4 pasos: conocer el examen → aprender los dominios → practicar → evaluar la preparación. |
| ⭐ [Official Practice Question Set AIF-C01](https://skillbuilder.aws/learn/4URFGY63KV/official-practice-question-set-aws-certified-ai-practitioner--aifc01--english/FVG43Y1PAX) | 🆓 | 20 preguntas oficiales con explicaciones. |
| *Exam Prep Standard Course: AWS Certified AI Practitioner* (dentro del plan) | 🆓 | Curso de preparación de nivel fundamental (≈ 8 h según [Class Central](https://www.classcentral.com/course/exam-prep-standard-course-aws-certified-ai-practitioner-aif-c01-302494)). |
| *Exam Prep Enhanced Course*, **Official Pretest** (65 preguntas, 90 min) y **Official Practice Exam** | 💲 suscripción Skill Builder | Más preguntas de estilo examen, laboratorios y flashcards. El pretest es el mejor indicador de preparación. |
| *AWS Escape Room: Exam Prep for AWS Certified AI Practitioner* | 💲 suscripción | Formato de juego: puzzles, preguntas de comprobación y evaluaciones prácticas. |
| Cursos de IA generativa en español en Skill Builder (p. ej., *Introducción a Amazon Bedrock*, *Planificación de un proyecto de IA generativa*) | 🆓 | Busca en Skill Builder filtrando por idioma "Español". |
| [Exam Prep presencial/virtual con instructor](https://aws.amazon.com/training/classroom/exam-prep-aws-certified-ai-practitioner-aif-c01) | 💲 | Clase de un día impartida por AWS o partners. |

> **Acceso gratuito temporal:** AWS ha ofrecido en el pasado acceso gratuito limitado al contenido de suscripción (la última promoción encontrada terminó el 5-ene-2026). Comprueba en Skill Builder si hay alguna activa. Los estudiantes pueden tener ventajas a través de **AWS Educate** (disponible [en español](https://aws.amazon.com/blogs/publicsector/aws-educate-now-available-in-spanish-and-portuguese)).

## 3. Documentación de servicios clave

| Servicio | Por qué leerlo |
|---|---|
| [Amazon Bedrock — User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) | Núcleo del Dominio 3: modelos, Knowledge Bases, Agents, Guardrails, Prompt Management, evaluación. |
| [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) | RAG gestionado (ver también el [Lab 01](../labs/lab-01-rag-bedrock-knowledge-bases/README.md)). |
| [Amazon Bedrock — precios](https://aws.amazon.com/bedrock/pricing/) | On-Demand vs. Batch vs. Provisioned Throughput (Dominio 5). |
| [Amazon SageMaker AI — Developer Guide](https://docs.aws.amazon.com/sagemaker/) | Ciclo de vida de ML, Clarify, Model Monitor, JumpStart, Canvas. |
| [AWS Transform](https://docs.aws.amazon.com/transform/latest/launchguide/aws-transform.html) | 🆕 v1.1 — modernización con agentes. |
| [Amazon Quick Suite (blog de lanzamiento)](https://aws.amazon.com/blogs/aws/reimagine-the-way-you-work-with-ai-agents-in-amazon-quick-suite/) | 🆕 v1.1 — evolución de QuickSight con IA agéntica. |
| [Strands Agents SDK (blog técnico de AWS)](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/) | 🆕 v1.1 — SDK open source de agentes. |
| [Kiro](https://kiro.dev/) | 🆕 v1.1 — IDE agéntico *spec-driven*. |

## 4. Whitepapers y marcos de referencia

| Documento | Dominio | Qué aporta |
|---|---|---|
| ⭐ [AWS Well-Architected — Generative AI Lens](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html) | D3, D4, D5 | Buenas prácticas de todo el ciclo de vida GenAI, incluida la IA responsable. |
| [AWS Responsible AI](https://aws.amazon.com/ai/responsible-ai/) | D4 | Dimensiones de la IA responsable según AWS, AI Service Cards y herramientas. |
| [Generative AI Security Scoping Matrix](https://aws.amazon.com/ai/generative-ai/security/scoping-matrix/) | D5 | Los 5 *scopes* de seguridad GenAI (aparece en preguntas de responsabilidad compartida). |
| [AWS Well-Architected — Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html) | D1 | Ciclo de vida de ML y MLOps. |

## 5. Comunidad oficial

- [AWS re:Post](https://repost.aws/) — ahora [admite español](https://aws.amazon.com/es/about-aws/whats-new/2024/12/aws-re-post-spanish-portuguese/). Hilo útil: [qué esperar del AIF-C01 y cómo prepararse](https://repost.aws/questions/QUpXmfHcb3Q3GF11vo6lbV6w/serious-questions-about-aif-c-01-exam-what-to-expect-and-how-to-prepare).
