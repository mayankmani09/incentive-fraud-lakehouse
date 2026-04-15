from pathlib import Path

def load_corpus() -> str:
    return "\n\n".join(p.read_text(encoding="utf-8") for p in Path("data/sample_docs").glob("*.md"))
