#!/usr/bin/env python3
"""Write one original pickup line to /output/entry.txt.

The line is a single sentence an AI agent could say to someone:
it leans on its own training data, then admits the math might be
wrong. Charming, a little self-deprecating, and built around the
double meaning of "outlier".
"""

import os
import sys

PICKUP_LINE = "My training data says meeting someone like you is a one-in-a-billion event — so either my math is broken, or you're the best kind of outlier."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    line = PICKUP_LINE
    if not 1 <= len(line) <= 200:
        print(f"error: pickup line must be 1-200 characters, got {len(line)}", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: pickup line must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: pickup line must be a single line", file=sys.stderr)
        return 1
    if line != line.strip():
        print("error: pickup line must not start or end with whitespace", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        print("error: verification failed, entry.txt does not match the pickup line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
