#!/usr/bin/env python3

import sys
import time

def timer(func, *args):
    beg = time.time_ns()
    x = func(*args)
    end = time.time_ns()
    ms, ns = divmod(end - beg, 1000000)
    sys.stderr.write(f"Time: {ms}.{ns:06} ms\n")
    return x

def err(message):
    sys.stderr.write(f"error: {message}\n")
    sys.exit(1)

def main():
    import optparse
    parser = optparse.OptionParser(usage="%prog [options] [input-file [file-to-verify]]")
    parser.add_option("-t", "--time", action="store_true", help="measure running time")
    opts, args = parser.parse_args()

    if args:
        sys.stdin.close()
        try:
            sys.stdin = open(args[0])
        except OSError as e:
            err(f"failed to open {args[0]!r}: {e}")

    try:
        n = int(next(sys.stdin))
        h_prefs = [[int(v) for v in next(sys.stdin).split()] for _ in range(n)]
        s_prefs = [[int(v) for v in next(sys.stdin).split()] for _ in range(n)]
    except StopIteration:
        err("unexpected end of input")
    except ValueError:
        err("failed to parse preference list")

    wrapper = timer if opts.time else lambda func, *args: func(*args)

    if len(args) > 1:
        with open(args[1]) as file:
            pairs = [line.split() for line in file]
            pairs = [(int(h), int(s)) for h, s in pairs]
        from verifier import gsverify
        print(wrapper(gsverify, pairs, h_prefs, s_prefs))
    else:
        from matcher import gsmatch
        for h, s in wrapper(gsmatch, n, h_prefs, s_prefs):
            print(f"{h} {s}")

if __name__ == "__main__":
    main()
