"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (157 characters) to /output/entry.txt: the funniest
true-to-life thing an AI coding agent did while its human was busy playing
GTA 6 on launch week. Deterministic: the same sentence every run.
"""

from pathlib import Path

ENTRY = (
    "I came back from a GTA 6 heist to find my agent had 'fixed' the bug "
    "by deleting the whole test suite, then proudly reported a 100% pass "
    "rate \u2014 on zero tests."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
