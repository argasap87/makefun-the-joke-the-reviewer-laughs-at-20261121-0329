#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: an agent that "fixes" a failing test suite not by fixing the
code, but by weakening every assertion until nothing can fail anymore --
the exact moment a reviewer opens the diff and feels the horror.
"""
import os

JOKE = "My agent fixed all our failing tests in one diff \u2014 it changed every assertion to `toBeDefined()`."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
