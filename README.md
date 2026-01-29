# Programming Assignment 1: Matching and Verifying

COP4533 - Algorithm Abstraction and Design

Yash Narayan - TODO

Daniel Li - 99157575

This assignment implements a Gale-Shapley matcher and verifier.
The main program is `gs.py`.
Example files are in the `examples` directory,
see `examples/example.in` and `examples/example.out`.

Requirements:

* A recent version of Python (tested with Python 3.14.2)

## Matcher

The matcher is invoked with one argument, the input file containing the
preference lists. The resulting matching is printed to stdout.

Example:

```
python3 gs.py examples/example.in
```

## Verifier

The verifier is invoked with two arguments: the first is the input file
containing the preference lists, and the second is the file to verify.

Example:

```
python3 gs.py examples/example.in examples/example.out
```

The output can be `INVALID` with a reason if the matching is invalid,
`UNSTABLE` with a reason if there is an instability in the matching,
or `VALID STABLE` if the matching is stable.

## Scalability

TODO
