#!/usr/bin/env python3
"""Verify the K22 witness for R(B4, B9) >= 23. Pure stdlib, no dependencies.

Definitions (as in the Small Ramsey Numbers dynamic survey):
  The book B_i = K_2 + \\bar{K_i} is a spine edge plus i pages: two adjacent
  vertices with i common neighbors, all spine-to-page edges present.
  In a 2-coloring of K_n, a monochromatic B_i in color c is an edge of color c
  whose endpoints have at least i common neighbors joined to both by color c.

Claim verified here: for the 22-vertex graph G in witness_k22.json (color BLUE =
edges of G, color RED = edges of its complement),
  - no B9 in blue (every G-edge has at most 8 common G-neighbors), and
  - no B4 in red  (every complement edge has at most 3 common
    complement-neighbors).
Hence K22 admits a (B4, B9)-good coloring and R(B4, B9) >= 23.
"""
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    doc = json.load(open(os.path.join(HERE, "witness_k22.json")))
    M = doc["matrix"]
    n = doc["n"]
    assert n == 22 and len(M) == n and all(len(row) == n for row in M)
    for i in range(n):
        assert M[i][i] == 0, "diagonal must be empty"
        for j in range(n):
            assert M[i][j] in (0, 1), "entries must be 0/1"
            assert M[i][j] == M[j][i], "matrix must be symmetric"

    max_common = {1: 0, 0: 0}
    for u, v in itertools.combinations(range(n), 2):
        c = M[u][v]
        common = sum(1 for w in range(n)
                     if w != u and w != v and M[u][w] == c and M[v][w] == c)
        max_common[c] = max(max_common[c], common)

    print(f"edges of K22 checked: {n * (n - 1) // 2}")
    print(f"max common same-color neighbors over G-edges (blue): "
          f"{max_common[1]}  (no B9 requires <= 8)")
    print(f"max common same-color neighbors over complement edges (red): "
          f"{max_common[0]}  (no B4 requires <= 3)")
    ok = max_common[1] <= 8 and max_common[0] <= 3
    print("VERIFIED: R(B4, B9) >= 23" if ok else "FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
