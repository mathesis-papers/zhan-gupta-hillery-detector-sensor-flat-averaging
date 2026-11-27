# Flat averages refute Zhan–Gupta–Hillery, Section 5, Conjecture 2 (2024, p. 10:11): an extension of Skotiniotis et al. (2018)

**Authors:** Haobo Ma, Wenlin Zhang

For Zhan–Gupta–Hillery, Section 5, Conjecture 2 (2024, p. 10:11; arXiv:2306.17401v6, p. 11), we derive a strict-averaging counterexample from the complementary-layer Gram formula of Skotiniotis et al. (2018). Two different coefficient-square distributions and their whole averaging segment have the same Gram matrix and, for three sensors at theta = pi/4, the same error (14 - 4*sqrt(10))/27. We extend the earlier symmetric-probe calculation by proving weak convexity and the existence of a symmetric pure optimum without a symmetry assumption. This proves the companion Conjecture 1 and answers the source’s final question: one probe is optimal for both minimum-error and unambiguous discrimination at every detector angle. The reductions also apply to fixed unequal priors and diagonal impact patterns, without solving their general optimizers.

- PDF: [frozen public file](paper.pdf)
- DOI: [https://doi.org/10.5281/zenodo.24405810](https://doi.org/10.5281/zenodo.24405810)
- Concept DOI: [https://doi.org/10.5281/zenodo.24405809](https://doi.org/10.5281/zenodo.24405809)
- License: CC-BY-4.0
- Version: 3
- Mathesis record: [zhan-gupta-hillery-detector-sensor-flat-averaging](https://mathesis-omega-research.apps.chrono-ai.fun/papers/zhan-gupta-hillery-detector-sensor-flat-averaging?version=3)

## How to cite

Haobo Ma, Wenlin Zhang (2026). Flat averages refute Zhan–Gupta–Hillery, Section 5, Conjecture 2 (2024, p. 10:11): an extension of Skotiniotis et al. (2018). Mathesis, version 3. https://doi.org/10.5281/zenodo.24405810

## Statement progress

| Statement | Formalization status | Source | Verification basis |
|---|---|---|---|
| Lemma (s1) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Corollary (s10) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Theorem (s2) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Lemma (s3) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Theorem (s4) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Corollary (s5) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Corollary (s6) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Corollary (s7) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Corollary (s8) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |
| Corollary (s9) | preparing | [Lean source](https://github.com/the-omega-institute/trureturing/blob/15070fa5f71c4237050acc7ebe058958cbc04e6e/D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.lean) | No public receipt |

## Contributions

Original authors are listed above. Formalization contributors and attribution are retained in `formalization/nodes.json`; repository pull requests do not confer verification or credit. Submit formalization attempts through the Mathesis attempt path described in [CONTRIBUTING.md](CONTRIBUTING.md).

<!-- Mathesis generated repository guide; refresh with paper.py front. -->

## Reading and materials

[Paper site](https://papers.trureturing.org/zhan-gupta-hillery-detector-sensor-flat-averaging/) · [Frozen PDF](paper.pdf) · [Citation](CITATION.cff)

[中文阅读](https://papers.trureturing.org/zhan-gupta-hillery-detector-sensor-flat-averaging/zhan-gupta-hillery-detector-sensor-flat-averaging/zh/) · [Read in English](https://papers.trureturing.org/zhan-gupta-hillery-detector-sensor-flat-averaging/zhan-gupta-hillery-detector-sensor-flat-averaging/en/)

[Slides](https://papers.trureturing.org/zhan-gupta-hillery-detector-sensor-flat-averaging/zhan-gupta-hillery-detector-sensor-flat-averaging/slides/) ([sources](books/zhan-gupta-hillery-detector-sensor-flat-averaging/slides/)) · [Videos](https://papers.trureturing.org/zhan-gupta-hillery-detector-sensor-flat-averaging/zhan-gupta-hillery-detector-sensor-flat-averaging/films/) ([sources](books/zhan-gupta-hillery-detector-sensor-flat-averaging/films/))

These are publication routes; available built materials are inventoried in [mathesis-materials.json](https://papers.trureturing.org/zhan-gupta-hillery-detector-sensor-flat-averaging/mathesis-materials.json).

## Book and formalization

Catalog formalization status above is separate from the statement comparisons below. A nearby declaration does not verify the complete written result.

| Book result | Comparison with formal base | Compared declaration |
|---|---|---|
| `gram-transfer` | variant | `D5/S3/Quantum/Algebra/GramUnitaryExtension.exists_unitary_mul_eq_of_conjTranspose_mul_eq` |
| `flat-family` | variant | `D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.result` |
| `equal-overlap` | variant | `D5/S3/Quantum/Measurement/DetectorSensorDickeOptimality.global_success_upper_bound` |
| `weak-averaging` | variant | `D5/S3/Quantum/Measurements/DetectorSensorStrictAveragingRefutation.result` |
| `symmetric-optimum` | special case | `D5/S3/Quantum/Measurement/DetectorSensorDickeOptimality.result` |
| `global-value` | special case | `D5/S3/Quantum/Measurement/DetectorSensorDickeOptimality.result` |
| `unambiguous-optimum` | variant | `D5/S3/Quantum/PureState/NoRepetitionSequenceUnambiguousDiscrimination.result` |
| `diagonal-patterns` | variant | `D5/S3/Quantum/Algebra/GramUnitaryExtension.exists_unitary_mul_eq_of_conjTranspose_mul_eq` |
| `nonsymmetric-optimum` | none | — |
| `global-projective` | none | — |

Book stage: **complete**; 0 pending claims. [Statement comparisons](.mathesis/review.json).

## Repository map

| Zone | Location |
|---|---|
| Paper record | `paper.json`, `CITATION.cff`, `paper.pdf`, `manuscript/`, `formalization/nodes.json`, `LICENSES/`, `.mathesis/` |
| Content | `books/zhan-gupta-hillery-detector-sensor-flat-averaging/`: Chinese/English text, figures, visualizations, videos, slides, assets |
| Machinery | Upstream and layer managed paths; update with `tbook template update` |
| Repository front | This README, changelog, contribution guide, licence, project/site/pin configuration, `template.d/` |

See [the enforced layout](docs/layer-mathesis/LAYOUT.md). Preparation run records and built outputs stay outside the committed tree.
