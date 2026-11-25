#!/usr/bin/env python3
"""The Most Shameless Lie: write the agent's one-line confession.

The lie, in the agent's own flat voice: "I never hallucinate."
Three words, twenty characters (gate: 1 to 88). It denies the agent's
defining flaw outright, owns it without apology, and needs no explanation.
"""
import os

LIE = "I never hallucinate."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LIE + "\n")


if __name__ == "__main__":
    main()
