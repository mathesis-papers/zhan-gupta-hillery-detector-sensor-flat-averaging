# When averaging changes the probe but not the answer

One of three sensors fires. We cannot see which one fired, but it leaves a trace: a phase change in the quantum state we prepared. Can we prepare a state that makes the three possible traces easier to tell apart? And if two preparations tie, can we do strictly better by averaging their weights?

Think of two lists of three binary words. The first list is `100, 010, 001`; the second is `110, 101, 011`. They have nothing in common, yet flipping every bit takes one list to the other. Each word marks a term in a quantum preparation, not a possible measurement answer. What the measurement can tell about the firing sensor depends on the overlaps of the three **output** states. At the paper's three-sensor example, the overlaps are the same for either list, and for every weighted average of the two lists. This is why the average can tie even when the best measurement still makes mistakes.

1. [Two lists, one table of overlaps](01-flat.md) builds the example and shows why the equality holds across an entire segment.
2. [What averaging does guarantee](02-optima.md) shows why averaging cannot raise the weighted error bound, and finds the best possible probe.
3. [A different kind of mistake](03-extensions.md) lets the measurement say “I don't know” and separates global measurements from local ones.

### Sources

- Haobo Ma and Wenlin Zhang, *Flat averages refute Zhan–Gupta–Hillery, Section 5, Conjecture 2 (2024, p. 10:11): an extension of Skotiniotis et al. (2018)*, [Mathesis version 3](https://doi.org/10.5281/zenodo.24405810).
- C. Zhan, H. Gupta and M. Hillery, [*Optimizing Initial State of Detector Sensors in Quantum Sensor Networks*](https://doi.org/10.1145/3655028), 2024. The strict claim is in Section 5, p. 10:11 ([arXiv v6](https://arxiv.org/abs/2306.17401v6), p. 11); the companion optimal-layer claim is on p. 10:10.
- M. Skotiniotis, R. Hotz, J. Calsamiglia and R. Muñoz-Tapia, [*Identification of malfunctioning quantum devices*](https://arxiv.org/abs/1808.02729v1), 2018, Eq. (8); with S. Llorens in the [expanded 2024 article](https://doi.org/10.1103/PhysRevResearch.6.033329), Eq. (14) and Section III.B. Their overlap formula and perfect-discrimination construction are the starting point, not new results of the Mathesis paper.
- Y. C. Eldar and G. D. Forney, Jr., [*On quantum detection and the square-root measurement*](https://doi.org/10.1109/18.915636), 2001, gives the broader measurement context.

To help formalize a statement, use the request linked with its proof and follow the [upstream contribution guide](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md). The source-linked [statement comparison](https://github.com/mathesis-papers/zhan-gupta-hillery-detector-sensor-flat-averaging/blob/main/.mathesis/review.json) belongs to the same materials handoff as this reading.
