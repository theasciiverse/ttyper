#!/usr/bin/env python3
"""drive.py SOCKET SESSION: types a ttyper test in a tmux pane like a person.

Reads the words from the Prompt box, then types them at about 75 words per
minute with a seeded rhythm: a few typos, each noticed and fixed with
backspace a key or two later. When the results screen is up it waits, then
quits with Esc. Run by record-preview.sh while asciinema records the pane."""
import random, subprocess, sys, time

SOCK, S = sys.argv[1], sys.argv[2]
rng = random.Random(7)

def tmux(*a): return subprocess.run(["tmux", "-L", SOCK, *a], capture_output=True, text=True).stdout
def key(*k): tmux("send-keys", "-t", S, *k)
def lit(s): tmux("send-keys", "-l", "-t", S, s)
def pane(): return tmux("capture-pane", "-p", "-t", S).split("\n")

time.sleep(2.5)
rows = pane()
start = next(i for i, l in enumerate(rows) if "Prompt" in l)
words = " ".join(l.strip("│ ").strip() for l in rows[start + 1:] if l.startswith("│")).split()

for wi, w in enumerate(words):
    for ci, c in enumerate(w):
        if rng.random() < 0.025 and c.isalpha():
            # a slip: a neighbouring letter, then back and right
            lit(rng.choice("asdfghjklqwertyuiop"))
            time.sleep(rng.uniform(0.12, 0.25))
            key("BSpace")
            time.sleep(rng.uniform(0.1, 0.2))
        lit(c)
        time.sleep(rng.uniform(0.06, 0.16))
    if wi < len(words) - 1:
        lit(" ")
        time.sleep(rng.uniform(0.08, 0.22))
time.sleep(7)
key("Escape")
