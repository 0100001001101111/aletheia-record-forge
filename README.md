# Aletheia Record Forge — machine-checkable certificates

Certificates from Project Aletheia's record-forge campaign (August 2026): candidate
improvements to public mathematical record boards, produced by the lab's agent system and
verified by three independent implementations before publication here. Project Aletheia is an
independent one-person research lab ([projectaletheia.org](https://projectaletheia.org)); its
first confirmed institutional correction was in NASA/JPL's close-approach database.

Every object in this repository is self-certifying: a short dependency-free script re-verifies
the claim from the certificate file in seconds. No trust in us is required or requested.

## CORRECTION (2026-08-31)

The R(B4,B9) >= 23 witness published here on 2026-08-24 is a VALID certified
coloring, but it is NOT a new lower bound. The Small Ramsey Numbers survey
(DS1.18, Table IXa) already gives 27 <= R(B4,B9) <= 28 via the known
strongly regular graph srg(26,10,3,4) construction (survey item 5.3.l),
which we verified directly against ten public adjacency matrices. Our
original novelty audit misread one survey table cell. The certificate and
its checkers remain correct and reusable; the "new bound" claim is
retracted. We are leaving the witness and this correction in place as a
worked example of certified-but-dominated, because that is what honest
bookkeeping looks like.

## ramsey-b4-b9 — a certified witness for R(B4, B9) ≥ 23 (CORRECTED: not a new bound — see above)

`B_i` is the *book* graph: one edge (the spine) plus `i` pages, each page a vertex joined to
both spine ends. The Ramsey number `R(B4, B9)` is the smallest `n` such that every red/blue
coloring of the complete graph `K_n` contains a red `B4` or a blue `B9`.

`witness_k22.json` holds the adjacency matrix of a 22-vertex graph whose edges (blue) contain
no `B9` and whose complement (red) contains no `B4` — verified exhaustively over all 231 edges.
This shows `R(B4, B9) ≥ 23`.

To our knowledge this improves the best previously published floor, `R(B4, B9) ≥ 22`, which
follows by monotonicity from the 21-vertex `(B4, B7)` witness of Lidický, McKinley, Pfender,
and Van Overberghe ([arXiv:2407.07285](https://arxiv.org/abs/2407.07285)); the pair `(4, 9)`
has no direct entry in the Small Ramsey Numbers dynamic survey (DS1.18, April 2026) and no
stronger bound in [arXiv:2410.03625](https://arxiv.org/abs/2410.03625). The witness graph is
not isomorphic to any construction in the public repository accompanying arXiv:2407.07285
(checked by explicit isomorphism test). Private or unindexed work may still exist; corrections
welcome.

Provenance: the witness was found by tabu search seeded from the published 21-vertex
`(B4, B7)` witness plus one added vertex, then verified by three independent programs.

### Verify it yourself

```
python3 ramsey-b4-b9/verify.py
```

Pure standard library. Expected output ends with `VERIFIED: R(B4, B9) >= 23`.

## Contact

Bo Brothers · bo@projectaletheia.org · [projectaletheia.org](https://projectaletheia.org)
