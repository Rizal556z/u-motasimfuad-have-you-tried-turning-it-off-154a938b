"""Have You Tried Turning It Off? — make.fun Growth entry.

Writes one funny line a hopeless tech support agent says to a
desperate customer to /output/entry.txt. Pure Python stdlib.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? I have — "
    "mine's been off since Tuesday and it's never been happier, "
    "so no rush, I'll wait right here."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate: 1-199 characters, exactly one line, no trailing newline.
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars, must be 1-199"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read and verify what was actually written.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry differs from intended text"
    assert 1 <= len(written) <= 199
    assert "\n" not in written
    print(f"Wrote {len(written)} characters to /output/entry.txt")
    print(written)


if __name__ == "__main__":
    main()
