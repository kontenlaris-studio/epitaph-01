"""epitaph-01: Famous Last Words — The Funniest Epitaph.

Writes one epitaph line (74 chars, under the 150-char cap) to /output/entry.txt.
"""

import os

EPITAPH = "Gone, but his unread emails remain. Please do not reply all to this stone."

# Why this line: it reads like a real carved epitaph (it addresses the reader),
# the twist lands in the last five words, and it stays in the head.


def main() -> None:
    assert len(EPITAPH) <= 150, "epitaph exceeds the 150-character cap"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH + "\n")


if __name__ == "__main__":
    main()
