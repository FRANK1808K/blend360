"""Builds the study guide website / Construye el sitio web de la guía de estudio.

The repository's Markdown stays the single source: this script copies it into guide/_docs,
adapts it for MkDocs (README → index, GitHub links to code files, collapsible solutions)
and runs `mkdocs build`. The site is published at https://frank1808k.github.io/blend360/guia/.
El Markdown del repositorio sigue siendo la única fuente: este script lo copia a guide/_docs,
lo adapta para MkDocs y ejecuta `mkdocs build`.

Usage / Uso:
    pip install -r guide/requirements.txt
    python3 scripts/build_guide.py                  # → guide/_site
    python3 scripts/build_guide.py --out _site/guia # custom output folder / carpeta de salida
    python3 scripts/build_guide.py --serve          # live preview / vista previa en vivo
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / "guide"
DOCS = GUIDE / "_docs"
SKIP = {".git", "node_modules", "guide", ".github"}
REPO_BLOB = "https://github.com/FRANK1808K/blend360/blob/HEAD/"
REPO_TREE = "https://github.com/FRANK1808K/blend360/tree/HEAD/"
SIMULATOR = "https://frank1808k.github.io/blend360/"
SITE = SIMULATOR + "guia/"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")
HOME_BUTTONS = {
    "es": f"[🎯 Abrir el simulador]({SIMULATOR}){{ .md-button .md-button--primary }} "
          f"[⌨️ Laboratorio de código]({SIMULATOR}){{ .md-button }}",
    "en": f"[🎯 Open the simulator]({SIMULATOR}){{ .md-button .md-button--primary }} "
          f"[⌨️ Code lab]({SIMULATOR}){{ .md-button }}",
}


def target_name(path: Path) -> str:
    """README.md → index.md, README.en.md → index.en.md (MkDocs section pages)."""
    return {"README.md": "index.md", "README.en.md": "index.en.md"}.get(path.name, path.name)


def page_url(rel: str) -> str:
    """'02-sql/ejercicios.en.md' → '02-sql/ejercicios/', 'README.md' → ''."""
    rel = re.sub(r"(\.en)?\.md$", "", rel)
    rel = re.sub(r"(^|/)README$", r"\1", rel)
    return rel + ("/" if rel and not rel.endswith("/") else "")


def fix_link(source: Path, target: str) -> str:
    if re.match(r"[a-z]+:|#|/", target):
        return target
    path, _, anchor = target.partition("#")
    resolved = (source.parent / path).resolve()
    rel = resolved.relative_to(ROOT).as_posix() if resolved.is_relative_to(ROOT) else None
    if rel is None:
        return target
    if path.endswith(".md"):
        src_en, dst_en = source.name.endswith(".en.md"), path.endswith(".en.md")
        twin = resolved.with_name(resolved.name[:-3] + ".en.md")
        if src_en != dst_en and (dst_en or twin.exists()):
            # Deliberate link to the other language: each language is a separate site tree.
            # Enlace a propósito al otro idioma: cada idioma es un árbol aparte del sitio.
            return SITE + ("en/" if dst_en else "") + page_url(rel) + (f"#{anchor}" if anchor else "")
        new = path[: -len(Path(path).name)] + target_name(Path(path))
        return new + (f"#{anchor}" if anchor else "")
    # Code, data and folders open on GitHub / El código, los datos y las carpetas se abren en GitHub.
    return (REPO_TREE if resolved.is_dir() else REPO_BLOB) + rel + (f"#{anchor}" if anchor else "")


def adapt(source: Path, text: str) -> str:
    lines = text.splitlines()
    # The site has its own language selector / El sitio tiene su propio selector de idioma.
    out = [line for line in lines if not line.startswith("🌐 ")]
    text = "\n".join(out) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.replace("<details>", "<details markdown>")
    text = LINK.sub(lambda m: m[1] + fix_link(source, m[2]) + m[3], text)
    if source.parent == ROOT and source.name.startswith("README"):
        lang = "en" if source.name.endswith(".en.md") else "es"
        text = re.sub(r"^(# .+\n)", lambda m: m[1] + "\n" + HOME_BUTTONS[lang] + "\n", text, count=1)
    return text


def copy_docs() -> int:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    count = 0
    for md in sorted(ROOT.rglob("*.md")):
        rel = md.relative_to(ROOT)
        if SKIP & set(rel.parts):
            continue
        dest = DOCS / rel.parent / target_name(md)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(adapt(md, md.read_text(encoding="utf-8")), encoding="utf-8")
        count += 1
    shutil.copytree(GUIDE / "assets", DOCS / "assets")
    return count


def main() -> int:
    count = copy_docs()
    print(f"{count} Markdown files prepared / archivos preparados in {DOCS.relative_to(ROOT)}")
    config = str(GUIDE / "mkdocs.yml")
    if "--serve" in sys.argv:
        return subprocess.call([sys.executable, "-m", "mkdocs", "serve", "-f", config])
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else str(GUIDE / "_site")
    cmd = [sys.executable, "-m", "mkdocs", "build", "-f", config, "-d", str(Path(out).resolve())]
    if "--strict" in sys.argv:
        cmd.append("--strict")
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
