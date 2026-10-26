"""Genera simulator/index.html a partir de los simulacros en Markdown.

Uso: python simulator/build.py
Lee practice-questions/mock-exam-*.md (español, con la clave de respuestas) y
practice-questions/en/mock-exam-*.md (versión en inglés de preguntas y opciones),
valida que coincidan y los inserta en simulator/template.html.
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_DIR = ROOT / "practice-questions"
EXAMS = [
    ("sim01", "Simulacro 01", "mock-exam-01.md"),
    ("sim02", "Simulacro 02", "mock-exam-02.md"),
]
QUESTION_RE = re.compile(r"^\*\*(\d+)\.\*\*\s+(.*)$")
OPTION_RE = re.compile(r"^- ([A-E])\. (.*)$")
KEY_RE = re.compile(r"^\| (\d+) \| ([A-E](?:, [A-E])*) \| (D\d)( 🆕)? \| (.*) \|$")


def inline(text: str) -> str:
    """Escapa HTML y convierte **negrita** y `código` de Markdown."""
    text = html.escape(text.replace("🆕", "").strip(), quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return re.sub(r"`(.+?)`", r"<code>\1</code>", text)


def parse_questions(path: Path) -> dict:
    """Devuelve {número: {"text", "options"}} sin leer la clave de respuestas."""
    questions, current = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        if m := QUESTION_RE.match(line):
            current = int(m.group(1))
            questions[current] = {"text": inline(m.group(2)), "options": []}
        elif (m := OPTION_RE.match(line)) and current is not None:
            questions[current]["options"].append({"id": m.group(1), "text": inline(m.group(2))})
    return questions


def parse(exam_id: str, path: Path, en_path: Path) -> list:
    questions, english, keys = parse_questions(path), parse_questions(en_path), {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if m := KEY_RE.match(line):
            keys[int(m.group(1))] = {
                "answer": m.group(2).split(", "),
                "domain": m.group(3),
                "new": bool(m.group(4)),
                "why": inline(m.group(5)),
            }
    if sorted(questions) != sorted(keys) or not questions:
        sys.exit(f"{path.name}: preguntas {len(questions)} y clave {len(keys)} no coinciden")
    out = []
    for n in sorted(questions):
        q = {**questions[n], **keys[n], "id": f"{exam_id}-{n}", "n": n}
        if not set(q["answer"]) <= {o["id"] for o in q["options"]}:
            sys.exit(f"{path.name} Q{n}: la respuesta no está entre las opciones")
        en = english.get(n)
        if not en or [o["id"] for o in en["options"]] != [o["id"] for o in q["options"]]:
            sys.exit(f"en/{path.name} Q{n}: falta la pregunta o sus opciones no coinciden con el español")
        q["en"] = en
        out.append(q)
    if sorted(english) != sorted(questions):
        sys.exit(f"en/{path.name}: el número de preguntas no coincide con el español")
    return out


def main() -> int:
    data = {
        "exams": [
            {"id": exam_id, "name": name,
             "questions": parse(exam_id, QUESTIONS_DIR / filename, QUESTIONS_DIR / "en" / filename)}
            for exam_id, name, filename in EXAMS
        ]
    }
    template = (ROOT / "simulator" / "template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    output = template.replace("/*__DATA__*/null", payload)
    (ROOT / "simulator" / "index.html").write_text(output, encoding="utf-8")
    total = sum(len(e["questions"]) for e in data["exams"])
    print(f"simulator/index.html generado con {total} preguntas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
