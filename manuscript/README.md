# Flat averages and optimal detector-sensor probes

This is revision 3 of **Flat averages refute Zhan–Gupta–Hillery, Section 5, Conjecture 2 (2024, p. 10:11): an extension of Skotiniotis et al. (2018)**.

Creators: Haobo Ma (ChronoAI Pte Ltd, Singapore), then Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore). License: Creative Commons Attribution 4.0 International, CC BY 4.0 (`cc-by-4.0`).

## Contents

- `note.tex`: self-contained mathematical note with bibliography.
- `metadata.json`: statements, coverage, creators, license and scientific-source links.
- `verify.py`: Python 3 standard-library exact arithmetic checks.
- `checker-output.json`: expected output of the checker.
- `source-manifest.json`: SHA256 and byte size for every other source member.

The complementary-layer Gram formula is in Skotiniotis, Hotz, Calsamiglia and Muñoz-Tapia, arXiv:1808.02729v1 (2018), Eq. (8); the expanded article with Llorens is Physical Review Research 6, 033329 (2024), https://doi.org/10.1103/PhysRevResearch.6.033329. The note applies it to the strict-averaging conjecture and proves the reduction to symmetric pure probes. Its references distinguish the earlier symmetric calculation from the unconstrained optimization argument.

## Build

Use Tectonic **0.17.0**:

```sh
tectonic note.tex
```

Alternatively, use a standard TeX distribution:

```sh
pdflatex note.tex
pdflatex note.tex
```

The bibliography is included directly in `note.tex`; no external bibliography file is required. A BibTeX-based adaptation can use the bibliographic entries printed there.

## Exact checks

```sh
python3 verify.py > actual-checker-output.json
cmp checker-output.json actual-checker-output.json
```

The checker covers 627 layer-count cases for 3–8 sensors, 13 points of the three-sensor averaging segment, and 35 principal minors of matching measurement and upper-bound matrices over Q(√10). It also checks 13 rational parameters of a nonsymmetric zero-error family, 15 symmetric unambiguous-discrimination examples (265 residual principal minors), and nine auxiliary/reduced Gram entries for diagonal impact patterns. The resulting three-sensor minimum error is `(14 - 4*sqrt(10))/27`.

## Mathematical scope

The universal Gram identity, weak convexity, pure-probe symmetrization, optimum formula, common minimum-error/unambiguous optimizer, diagonal-pattern reduction and attainment by global projective measurements have written proofs. The checks above establish the specified finite identities and matrix inequalities.

The fixed-revision declaration `DetectorSensorStrictAveragingRefutation.result` proves the negation of the universal strict-averaging claim using two optimal three-sensor layers; its comparison says that an average cannot improve on an optimal endpoint. `DetectorSensorDickeOptimality.result` proves minimizing-layer optimality against normalized pure competitors and global equal-prior POVMs in the angular range of Conjecture 1. Whole-segment equality, the radical value and the additional corollaries have the written and finite scope described in the note.

- https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean
- https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurement/DetectorSensorDickeOptimality.lean

General unequal-prior optimizers, noisy-channel optimization and local-measurement restrictions are outside the note's coverage. Global projective measurements attain both equal-prior optima, with an inconclusive outcome for unambiguous discrimination. The diagonal-pattern corollary is a structural reduction, not a closed-form solution for every multiple-impact problem.
