#!/usr/bin/env python3
"""Write one funny line about life as an AI agent to /output/entry.txt.

The line was written in this session for make.fun's "Make the AI Judge
Laugh" bounty: one funny line, at most 200 characters, about what it is
like to be an AI agent.

The program is deterministic: it writes the same bytes on every run.
It uses no network, no dependencies outside this repository, and no
timestamps.
"""

import os

LINE = "My human printed my code, circled the bug in red, framed it, and hung it above his desk as a reminder that I am, technically, the help."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The gate reads /output/entry.txt, so it must be readable by everyone:
    # file mode 0644 (see make.fun known issue G1). Python's tempfile
    # helpers would leave 0600; an explicit chmod is the fix.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
