#!/usr/bin/env python3

import random
import sys
import time
import matplotlib.pyplot as plt

from matcher import gsmatch
from verifier import gsverify

def timer(func, *args):
    beg = time.time_ns()
    x = func(*args)
    end = time.time_ns()
    return x, end - beg

def main():
    iterations = 11
    sizes = []
    matcher_times = []
    verifier_times = []
    for i in range(iterations):
        n = 1 << i
        h_prefs = [random.sample(range(n), n) for _ in range(n)]
        s_prefs = [random.sample(range(n), n) for _ in range(n)]

        sizes.append(n)

        pairs, mt = timer(gsmatch, n, h_prefs, s_prefs)
        matcher_times.append(mt / 1000000)

        result, vt = timer(gsverify, pairs, h_prefs, s_prefs)
        verifier_times.append(vt / 1000000)

        assert result == "VALID STABLE"

        print(f"n = {n}, mt = {mt}, vt = {vt}")

    fig, ax = plt.subplots()
    ax.plot(sizes, matcher_times, marker="o")
    ax.set_title("Matcher")
    ax.set_xlabel("Number of Hospitals/Students")
    ax.set_ylabel("Time (ms)")
    fig.savefig("stress-matcher.svg")

    fig, ax = plt.subplots()
    ax.plot(sizes, verifier_times, marker="o")
    ax.set_title("Verifier")
    ax.set_xlabel("Number of Hospitals/Students")
    ax.set_ylabel("Time (ms)")
    fig.savefig("stress-verifier.svg")

if __name__ == "__main__":
    main()
