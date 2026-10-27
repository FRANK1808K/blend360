"""Builds the study website with Quarto / Construye el sitio web de estudio con Quarto.

The repository's Markdown stays the single source (it is what GitHub shows and what the checks verify).
This script copies it, together with the Quarto project in quarto/, into a staging folder and adapts it:
README → index, first heading → page title, "> **Title:**" quotes → callouts, ```mermaid → diagrams,
links to code and data → GitHub, links to the simulators → their pages on the site. It also writes the
navigation (NAV below) and the list of pages that "My progress" tracks, then runs `quarto render`.
El Markdown del repositorio sigue siendo la única fuente. Este script lo copia, junto con el proyecto
Quarto de quarto/, a una carpeta de preparación, lo adapta, escribe la navegación (NAV) y la lista de páginas que sigue
"Mi progreso", y ejecuta `quarto render`.

Every Markdown page must appear in NAV: a new document that is not in the navigation fails the build.
Toda página Markdown debe estar en NAV: un documento nuevo que no esté en la navegación hace fallar la construcción.

Usage / Uso (needs Quarto ≥ 1.10, CI uses 1.10.18: https://quarto.org/docs/get-started/):
    python3 scripts/build_site.py                 # → _site
    python3 scripts/build_site.py --strict        # also fails on Quarto warnings and broken links/anchors (CI)
    python3 scripts/build_site.py --out DIR       # custom output folder / carpeta de salida
    python3 scripts/build_site.py --preview       # live preview / vista previa (re-run after editing Markdown)
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote

if sys.stdout.encoding != "utf-8" and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
PROJECT = ROOT / "quarto"
# Staging folder outside the repository (it may live in a synced drive) / Carpeta de preparación fuera del repositorio.
STAGE = Path(os.environ.get("B360_STAGE") or Path(tempfile.gettempdir()) / "blend360-site")
REPO_BLOB = "https://github.com/FRANK1808K/blend360/blob/HEAD/"
REPO_TREE = "https://github.com/FRANK1808K/blend360/tree/HEAD/"
SKIP_DIRS = {".git", ".github", "node_modules", "_build", "_site", "quarto", ".quarto"}
# Markdown that is not a study page (it opens on GitHub) / Markdown que no es página de estudio (se abre en GitHub).
NOT_PAGES = {"README.md", "README.en.md", "aws-ai-practitioner/CONTRIBUTING.md", "aws-ai-practitioner/labs/template.md"}
NOT_PAGES_DIRS = ("aws-ai-practitioner/labs/lab-01-rag-bedrock-knowledge-bases/sample-data/",)
HOME = {"README.md": "index.qmd", "README.en.md": "index.en.qmd"}
# The simulators are standalone apps published next to the guide / Los simuladores se publican junto a la guía.
APPS = {"simulator/index.html": "simulador/index.html",
        "aws-ai-practitioner/simulator/index.html": "simulador-aif/index.html"}

# ------------------------------------------------------------------ navigation / navegación
# A page is (source, label); a section is (title, [pages]). Pages that are .md are tracked in "My progress".
# Una página es (fuente, etiqueta); una sección es (título, [páginas]). Las páginas .md se siguen en "Mi progreso".
NAV = [
    {"id": "estudiar", "lang": "es", "title": "📚 Estudiar", "contents": [
        ("estudiar.qmd", "Mapa de estudio"),
        ("🧭 Empieza aquí", [
            ("guides/plan-de-estudio.md", "Plan de estudio (26 oct → 18 dic)"),
            ("guides/que-evalua-blend360.md", "Qué evalúa Blend360"),
        ]),
        ("🧩 Parte 1 · Razonamiento (30 min)", [
            ("01-razonamiento-abstracto/README.md", "Razonamiento abstracto"),
        ]),
        ("💻 Parte 2 · Prueba técnica (90 min)", [
            ("02-sql/README.md", "SQL"),
            ("03-python/README.md", "Python"),
            ("03-python/pandas.md", "pandas"),
            ("04-algoritmos-y-estructuras/README.md", "Algoritmos y estructuras de datos"),
            ("05-bases-de-datos/README.md", "Bases de datos"),
            ("06-aws/README.md", "AWS: fundamentos de nube"),
            ("06-aws/analisis-de-datos.md", "AWS: análisis de datos ⭐"),
            ("07-resolucion-de-problemas/README.md", "Resolución de problemas"),
            ("08-estadistica-y-ml/README.md", "Estadística y machine learning"),
        ]),
        ("🗣️ Inglés técnico", [
            ("english/README.md", "Plan de inglés (A2 → funcional)"),
            ("english/como-leer-preguntas.md", "Cómo leer preguntas"),
            ("english/vocabulario-tecnico.md", "Vocabulario técnico"),
            ("english/gramatica-minima.md", "Gramática mínima"),
            ("english/entrevista-y-frases.md", "Entrevista y frases"),
        ]),
    ]},
    {"id": "evaluar", "lang": "es", "title": "🧪 Practicar y evaluar", "contents": [
        ("evaluar.qmd", "Ruta de evaluación"),
        ("progreso.qmd", "Mi progreso"),
        ("✍️ Ejercicios por tema", [
            ("01-razonamiento-abstracto/ejercicios.md", "Razonamiento · 50 ejercicios"),
            ("02-sql/ejercicios.md", "SQL · 35 ejercicios"),
            ("06-aws/preguntas.md", "AWS · 30 preguntas"),
            ("08-estadistica-y-ml/preguntas.md", "Estadística y ML · 25 preguntas"),
            ("english/ejercicios-ingles.md", "Inglés · ejercicios"),
        ]),
        ("⏱️ Simulacros", [
            ("simulacros/README.md", "Cómo hacer un simulacro"),
            ("simulacros/simulacro-razonamiento-01.md", "Razonamiento #1 · 30 min"),
            ("simulacros/simulacro-tecnico-01.md", "Técnico #1 · 90 min"),
        ]),
        ("🎯 Simulador", [
            ("simulator/README.md", "Simulador y laboratorio de código"),
        ]),
    ]},
    {"id": "repasar", "lang": "es", "title": "🔁 Repasar", "contents": [
        ("cheatsheets/README.md", "Cheatsheets"),
        ("📄 Hojas de una página", [
            ("cheatsheets/sql.md", "SQL"),
            ("cheatsheets/python.md", "Python + pandas"),
            ("cheatsheets/algoritmos.md", "Algoritmos y estructuras"),
            ("cheatsheets/aws-y-bases-de-datos.md", "AWS + bases de datos"),
            ("cheatsheets/estadistica-ml.md", "Estadística y ML"),
        ]),
        ("🏁 Recta final", [
            ("cheatsheets/repaso-final-48h.md", "Repaso final de 48 h"),
            ("flashcards/README.md", "Flashcards (209, Anki)"),
        ]),
    ]},
    {"id": "aif", "lang": "es", "title": "☁️ AWS AI Practitioner", "contents": [
        ("aws-ai-practitioner/README.md", "Inicio AIF-C01"),
        ("📚 Estudiar los 5 dominios", [
            ("aws-ai-practitioner/domains/00-exam-guide-v1.1-changes.md", "Novedades de la guía v1.1 🆕"),
            ("aws-ai-practitioner/domains/01-fundamentals-ai-ml/README.md", "D1 · Fundamentos de IA y ML (20 %)"),
            ("aws-ai-practitioner/domains/02-fundamentals-generative-ai/README.md", "D2 · IA generativa (24 %)"),
            ("aws-ai-practitioner/domains/03-applications-foundation-models/README.md", "D3 · Modelos fundacionales (28 %)"),
            ("aws-ai-practitioner/domains/04-responsible-ai/README.md", "D4 · IA responsable (14 %)"),
            ("aws-ai-practitioner/domains/05-security-compliance-governance/README.md", "D5 · Seguridad y gobernanza (14 %)"),
        ]),
        ("🧪 Evaluar", [
            ("aws-ai-practitioner/practice-questions/README.md", "Banco de preguntas"),
            ("aws-ai-practitioner/practice-questions/domain-01-questions.md", "Preguntas D1"),
            ("aws-ai-practitioner/practice-questions/domain-02-questions.md", "Preguntas D2"),
            ("aws-ai-practitioner/practice-questions/domain-03-questions.md", "Preguntas D3"),
            ("aws-ai-practitioner/practice-questions/domain-04-questions.md", "Preguntas D4"),
            ("aws-ai-practitioner/practice-questions/domain-05-questions.md", "Preguntas D5"),
            ("aws-ai-practitioner/practice-questions/mock-exam-01.md", "Simulacro 01 · 65 preguntas"),
            ("aws-ai-practitioner/practice-questions/mock-exam-02.md", "Simulacro 02 · 65 de escenario"),
            ("aws-ai-practitioner/simulator/README.md", "Simulador AIF-C01"),
        ]),
        ("🔁 Repasar", [
            ("aws-ai-practitioner/cheatsheets/README.md", "Cheatsheets AIF-C01"),
            ("aws-ai-practitioner/cheatsheets/confusable-pairs.md", "Pares que se confunden"),
            ("aws-ai-practitioner/cheatsheets/exam-decision-matrix.md", "Matriz de decisión"),
            ("aws-ai-practitioner/cheatsheets/glossary.md", "Glosario ES–EN"),
            ("aws-ai-practitioner/cheatsheets/final-review-48h.md", "Repaso final de 48 h"),
            ("aws-ai-practitioner/flashcards/README.md", "Flashcards (109)"),
        ]),
        ("🧭 Estrategia de examen", [
            ("aws-ai-practitioner/guides/exam-playbook.md", "Playbook del examen"),
            ("aws-ai-practitioner/guides/retake-plan.md", "Plan de reintento"),
        ]),
        ("🛠️ Laboratorio", [
            ("aws-ai-practitioner/labs/README.md", "Laboratorios"),
            ("aws-ai-practitioner/labs/lab-01-rag-bedrock-knowledge-bases/README.md", "Lab 01 · RAG con Bedrock"),
        ]),
        ("🔗 Recursos", [
            ("aws-ai-practitioner/resources/README.md", "Centro de recursos"),
            ("aws-ai-practitioner/resources/official-aws.md", "Oficiales de AWS"),
            ("aws-ai-practitioner/resources/videos-and-courses.md", "Videos y cursos"),
            ("aws-ai-practitioner/resources/practice-exams.md", "Exámenes de práctica"),
            ("aws-ai-practitioner/resources/hands-on.md", "Práctica en AWS"),
            ("aws-ai-practitioner/resources/books-flashcards-community.md", "Libros y comunidad"),
        ]),
    ]},
    {"id": "study-en", "lang": "en", "title": "📚 Study", "contents": [
        ("estudiar.en.qmd", "Study map"),
        ("🧭 Start here", [
            ("guides/plan-de-estudio.en.md", "Study plan (Oct 26 → Dec 18)"),
            ("guides/que-evalua-blend360.en.md", "What Blend360 evaluates"),
        ]),
        ("🧩 Part 1 · Reasoning (30 min)", [
            ("01-razonamiento-abstracto/README.en.md", "Abstract reasoning"),
        ]),
        ("💻 Part 2 · Technical test (90 min)", [
            ("02-sql/README.en.md", "SQL"),
            ("03-python/README.en.md", "Python"),
            ("03-python/pandas.en.md", "pandas"),
            ("04-algoritmos-y-estructuras/README.en.md", "Algorithms and data structures"),
            ("05-bases-de-datos/README.en.md", "Databases"),
            ("06-aws/README.en.md", "AWS: cloud fundamentals"),
            ("06-aws/analisis-de-datos.en.md", "AWS: data analytics ⭐"),
            ("07-resolucion-de-problemas/README.en.md", "Problem solving"),
            ("08-estadistica-y-ml/README.en.md", "Statistics and machine learning"),
        ]),
        ("🗣️ Technical English", [
            ("english/README.en.md", "English plan (A2 → functional)"),
            ("english/como-leer-preguntas.en.md", "How to read questions"),
            ("english/vocabulario-tecnico.en.md", "Technical vocabulary"),
            ("english/gramatica-minima.en.md", "Minimum grammar"),
            ("english/entrevista-y-frases.en.md", "Interview and phrases"),
        ]),
    ]},
    {"id": "practice-en", "lang": "en", "title": "🧪 Practice and assess", "contents": [
        ("evaluar.en.qmd", "Assessment path"),
        ("progreso.en.qmd", "My progress"),
        ("✍️ Exercises by topic", [
            ("01-razonamiento-abstracto/ejercicios.en.md", "Reasoning · 50 exercises"),
            ("02-sql/ejercicios.en.md", "SQL · 35 exercises"),
            ("06-aws/preguntas.en.md", "AWS · 30 questions"),
            ("08-estadistica-y-ml/preguntas.en.md", "Statistics and ML · 25 questions"),
            ("english/ejercicios-ingles.en.md", "English · exercises"),
        ]),
        ("⏱️ Mock exams", [
            ("simulacros/README.en.md", "How to take a mock exam"),
            ("simulacros/simulacro-razonamiento-01.en.md", "Reasoning #1 · 30 min"),
            ("simulacros/simulacro-tecnico-01.en.md", "Technical #1 · 90 min"),
        ]),
        ("🎯 Simulator", [
            ("simulator/README.en.md", "Simulator and code lab"),
        ]),
        ("☁️ AWS AIF-C01 in English", [
            ("aws-ai-practitioner/README.en.md", "AIF-C01 overview"),
            ("aws-ai-practitioner/practice-questions/en/mock-exam-01.md", "Mock exam 01 · 65 questions"),
            ("aws-ai-practitioner/practice-questions/en/mock-exam-02.md", "Mock exam 02 · 65 scenarios"),
        ]),
    ]},
    {"id": "review-en", "lang": "en", "title": "🔁 Review", "contents": [
        ("cheatsheets/README.en.md", "Cheat sheets"),
        ("📄 One-page sheets", [
            ("cheatsheets/sql.en.md", "SQL"),
            ("cheatsheets/python.en.md", "Python + pandas"),
            ("cheatsheets/algoritmos.en.md", "Algorithms and data structures"),
            ("cheatsheets/aws-y-bases-de-datos.en.md", "AWS + databases"),
            ("cheatsheets/estadistica-ml.en.md", "Statistics and ML"),
        ]),
        ("🏁 Final stretch", [
            ("cheatsheets/repaso-final-48h.en.md", "Final 48-hour review"),
            ("flashcards/README.en.md", "Flashcards (209, Anki)"),
        ]),
    ]},
]

LINK = re.compile(r"(\]\()([^)\s]+)(\))")
FENCE = re.compile(r"^(```|~~~)")
TITLED_QUOTE = re.compile(r"^\*\*(.+?)\*\*\s*(.*)$")
CALLOUT_KINDS = [  # first match wins / gana la primera coincidencia
    ("warning", r"aviso|notice|trampa|trap|cuidado|careful|no cambies|don't change|penaliz|importante|important"),
    ("important", r"regla|rule|principio|principle|objetivo|goal|meta\b|peso en el examen|exam weight"),
    ("tip", r"pista|hint|tip|consejo|cómo usar|how to use|cómo practicar|how to practice|instrucciones|instructions"),
]


def is_page(rel: str) -> bool:
    return rel not in NOT_PAGES and not rel.startswith(NOT_PAGES_DIRS)


def staged(rel: str) -> str:
    """'02-sql/README.en.md' → '02-sql/index.en.qmd': Quarto ignores README files and needs .qmd for diagrams.
    Quarto ignora los README y necesita .qmd para los diagramas."""
    head, _, name = rel.rpartition("/")
    name = re.sub(r"\.md$", ".qmd", {"README.md": "index.md", "README.en.md": "index.en.md"}.get(name, name))
    return f"{head}/{name}" if head else name


def html_path(page: str) -> str:
    return re.sub(r"\.(md|qmd)$", ".html", staged(page))


def progress_key(rel: str) -> str:
    """Both languages share the same progress / Los dos idiomas comparten el progreso."""
    return re.sub(r"(\.en)?\.md$", "", rel)


def relative(target: str, page: str) -> str:
    return Path(os.path.relpath(STAGE / target, (STAGE / page).parent)).as_posix()


def fix_link(source: str, target: str, pages: set) -> str:
    if re.match(r"[a-z]+:|#|/", target):
        return target
    path, _, anchor = target.partition("#")
    frag = f"#{anchor}" if anchor else ""
    resolved = ((ROOT / source).parent / path).resolve()
    if not resolved.is_relative_to(ROOT):
        return target
    rel = resolved.relative_to(ROOT).as_posix()
    if rel in APPS:
        return relative(APPS[rel], staged(source)) + frag
    if rel in HOME:
        return relative(HOME[rel], staged(source)) + frag
    if rel in pages:
        return relative(staged(rel), staged(source)) + frag
    # Code, data and other files open on GitHub / El código, los datos y otros archivos se abren en GitHub.
    return (REPO_TREE if resolved.is_dir() else REPO_BLOB) + rel + frag


def callout(quote: list) -> list:
    """'> **Title:** text' → Quarto callout; any other quote stays a quote / cualquier otra cita se queda igual."""
    body = [re.sub(r"^> ?", "", line) for line in quote]
    first = next((i for i, line in enumerate(body) if line.strip()), None)
    if first is None:
        return quote
    m = TITLED_QUOTE.match(body[first])
    if m and re.search(r"[:.?]$", m[1]) or m and m[2][:1] in (":", "."):
        title = m[1].rstrip(":.").strip()
        rest = m[2].lstrip(":. ").strip()
        body[first] = rest
    elif body[first].startswith(("💡", "⚠️", "💻", "🇬🇧")):
        title = ""
    else:
        return quote
    kind = "note"
    if body[first].startswith("⚠️"):
        kind = "warning"
    elif body[first].startswith("💡"):
        kind = "tip"
    for name, pattern in CALLOUT_KINDS:
        if title and re.search(pattern, title, re.I):
            kind = name
            break
    attrs = f'.callout-{kind}' + (f' title="{title.replace(chr(34), "&quot;")}"' if title else ' appearance="simple"')
    while body and not body[-1].strip():
        body.pop()
    return ["::: {" + attrs + "}", *body, ":::"]


def adapt(source: str, text: str, pages: set) -> str:
    lines = text.splitlines()
    title_at = next(i for i, line in enumerate(lines) if line.startswith("# "))
    title = lines[title_at][2:].strip()
    del lines[title_at]
    out, quote, in_code = [], [], False
    for line in lines + [""]:
        if FENCE.match(line):
            in_code = not in_code
            out.append("```{mermaid}" if line.strip() == "```mermaid" else line)
            continue
        if in_code:
            out.append(line)
            continue
        if line.startswith(">"):
            quote.append(line)
            continue
        if quote:
            out.extend(callout(quote))
            quote = []
        if line.startswith("🌐 "):
            out.extend(["::: {.lang-switch}", line, ":::"])
            continue
        out.append(line)
    # Fix links outside code blocks only / Corrige enlaces solo fuera de los bloques de código.
    fixed, in_code = [], False
    for line in out:
        if FENCE.match(line):
            in_code = not in_code
        fixed.append(line if in_code else LINK.sub(lambda m: m[1] + fix_link(source, m[2], pages) + m[3], line))
    body = "\n".join(fixed).strip("\n")
    words = len(re.findall(r"\w+", re.sub(r"```.*?```", "", body, flags=re.S)))
    meta = {"title": title}
    if source.endswith(".en.md") or "/en/" in source:
        meta["lang"] = "en"
        meta["toc-title"] = "On this page"
    front = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items())
    tools = (f'<div class="page-tools" data-key="{progress_key(source)}" data-src="{source}" '
             f'data-min="{max(1, round(words / 200))}"></div>')
    return f"---\n{front}\n---\n\n{tools}\n\n{body}\n"


def nav_pages(contents):
    for item, value in contents:
        if isinstance(value, list):
            yield from nav_pages(value)
        else:
            yield item


def sidebar_yaml() -> dict:
    def items(contents):
        out = []
        for item, value in contents:
            if isinstance(value, list):
                out.append({"section": item, "contents": items(value)})
            else:
                out.append({"text": value, "href": staged(item)})
        return out
    return {"website": {"sidebar": [
        {"id": bar["id"], "title": bar["title"], "style": "docked", "collapse-level": 2,
         "contents": items(bar["contents"])} for bar in NAV]}}


def manifest() -> dict:
    """Pages tracked by "My progress", grouped like the navigation / agrupadas como la navegación."""
    def items(pages):
        return [{"key": progress_key(p), "label": label, "href": html_path(p)} for p, label in pages if p.endswith(".md")]

    groups = {"es": [], "en": []}
    for bar in NAV:
        loose = items([entry for entry in bar["contents"] if not isinstance(entry[1], list)])
        sections = [(title, items(value)) for title, value in bar["contents"] if isinstance(value, list)]
        for title, tracked in [(bar["title"], loose)] + sections:
            if tracked:
                groups[bar["lang"]].append({"area": bar["id"], "areaTitle": bar["title"], "title": title, "items": tracked})
    return groups


def stage() -> None:
    sources = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*.md")
               if not SKIP_DIRS & set(p.relative_to(ROOT).parts)}
    pages = {rel for rel in sources if is_page(rel)}
    in_nav = [p for bar in NAV for p in nav_pages(bar["contents"])]
    authored = {p.relative_to(PROJECT).as_posix() for p in PROJECT.glob("*.qmd")}
    missing = sorted(pages - set(in_nav))
    unknown = sorted(set(in_nav) - pages - authored)
    duplicated = sorted({p for p in in_nav if in_nav.count(p) > 1})
    if missing or unknown or duplicated:
        for p in missing:
            print(f"✗ {p}: not in NAV (scripts/build_site.py) / no está en NAV")
        for p in unknown:
            print(f"✗ {p}: in NAV but does not exist / está en NAV pero no existe")
        for p in duplicated:
            print(f"✗ {p}: twice in NAV / dos veces en NAV")
        sys.exit(1)

    if STAGE.exists():
        shutil.rmtree(STAGE)
    shutil.copytree(PROJECT, STAGE, ignore=shutil.ignore_patterns("_site", ".quarto", "*_files"))
    for rel in sorted(pages):
        dest = STAGE / staged(rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(adapt(rel, (ROOT / rel).read_text(encoding="utf-8"), pages), encoding="utf-8")
    for src, dest in APPS.items():
        (STAGE / dest).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / src, STAGE / dest)
    # The old MkDocs guide lived at /guia/ / La antigua guía MkDocs vivía en /guia/.
    for path, target in (("guia/index.html", "../"), ("guia/en/index.html", "../../index.en.html")):
        (STAGE / path).parent.mkdir(parents=True, exist_ok=True)
        (STAGE / path).write_text(f'<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={target}">'
                                  f'<link rel="canonical" href="{target}"><a href="{target}">→</a>\n', encoding="utf-8")
    (STAGE / "_sidebar.yml").write_text(json.dumps(sidebar_yaml(), ensure_ascii=False, indent=1), encoding="utf-8")
    (STAGE / "assets" / "manifest.js").write_text(
        "// Generated by scripts/build_site.py / Generado por scripts/build_site.py\n"
        f"window.B360_MANIFEST = {json.dumps(manifest(), ensure_ascii=False)};\n", encoding="utf-8")
    print(f"{len(pages)} Markdown pages + {len(authored)} Quarto pages staged / preparadas in {STAGE}")


def check_links(site: Path) -> list:
    """Every internal link and #anchor of the built site exists / Cada enlace y #ancla interna existe."""
    errors, ids = [], {}
    href = re.compile(r'<a [^>]*href="([^"]+)"')
    for page in sorted(site.rglob("*.html")):
        if {"site_libs", "simulador", "simulador-aif", "guia"} & set(page.relative_to(site).parts):
            continue
        html = page.read_text(encoding="utf-8")
        for link in href.findall(html):
            if re.match(r"[a-z]+:|//", link):
                continue
            path, _, anchor = link.partition("#")
            target = (page.parent / path).resolve() if path else page
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                errors.append(f"{page.relative_to(site).as_posix()}: broken link / enlace roto → {link}")
                continue
            if anchor and target.suffix == ".html":
                if target not in ids:
                    ids[target] = set(re.findall(r'id="([^"]+)"', target.read_text(encoding="utf-8")))
                if unquote(anchor) not in ids[target]:
                    errors.append(f"{page.relative_to(site).as_posix()}: missing anchor / ancla inexistente → {link}")
    return errors


def main() -> int:
    quarto = shutil.which("quarto")
    stage()
    if "--stage-only" in sys.argv:
        return 0
    if not quarto:
        print("Quarto not found / no se encontró Quarto: https://quarto.org/docs/get-started/")
        return 1
    if "--preview" in sys.argv:
        return subprocess.call([quarto, "preview", str(STAGE)])
    run = subprocess.run([quarto, "render", str(STAGE)], capture_output=True, text=True, encoding="utf-8")
    log = run.stdout + run.stderr
    warnings = [line for line in log.splitlines() if re.search(r"\bWARN(ING)?\b", line)]
    if run.returncode:
        print(log)
        return run.returncode
    out = Path(sys.argv[sys.argv.index("--out") + 1]).resolve() if "--out" in sys.argv else ROOT / "_site"
    # Empty the folder instead of deleting it: a local server may be serving it.
    # Vacía la carpeta en vez de borrarla: puede haber un servidor local usándola.
    for old in out.iterdir() if out.exists() else []:
        shutil.rmtree(old) if old.is_dir() else old.unlink()
    shutil.copytree(STAGE / "_site", out, dirs_exist_ok=True)
    for line in warnings:
        print(line)
    errors = check_links(out)
    for e in errors:
        print(e)
    pages = sum(1 for _ in out.rglob("*.html"))
    print(f"Site built / sitio construido: {out} ({pages} HTML files, {len(warnings)} warnings, {len(errors)} link problems)")
    return 1 if "--strict" in sys.argv and (warnings or errors) else 0


if __name__ == "__main__":
    sys.exit(main())
