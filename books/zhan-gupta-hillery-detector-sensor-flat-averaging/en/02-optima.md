# What averaging does guarantee

The flat family rules out **strict** improvement. But averaging still gives a useful guarantee: its error cannot exceed the weighted average of the two errors. Imagine keeping the output vectors for two probes in different slots of one longer vector. A reader who first looks in the slot where the state lands can run the best measurement for that slot. The Gram matrix shows why this strategy is also possible for the single pure probe with averaged weights.

::: {.theorem #weak-averaging title="Weak averaging" status="written-proof" proof="pf-weak-averaging" doi="10.5281/zenodo.24405810" source="Theorem 4 (thm:convex)" request="https://github.com/the-omega-institute/trureturing-requests/issues/555" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s4"}
For any two coefficient-square distributions $p,q$ and $0\leq t\leq1$,

$$P(tp+(1-t)q)\leq tP(p)+(1-t)P(q).$$

Equal-error inputs therefore give an average with no larger error. Equality is possible.
:::

::: {.proof #pf-weak-averaging}
Use the output vectors $\eta_i=\sqrt{t}\,\phi_i(p)\oplus\sqrt{1-t}\,\phi_i(q)$ in two orthogonal copies of the output space. Their Gram matrix is $tG(p)+(1-t)G(q)$, exactly that of the probe with averaged weights. For optimum effects $M_i$ and $N_i$ in the original experiments, $M_i\oplus N_i$ gives the weighted average of their successes. The equal-Gram lemma transports that measurement back to the averaged pure probe. A best measurement can only improve upon it. The endpoints are immediate, and the argument uses the same fixed priors throughout, not necessarily equal. This is Theorem 4 in the paper.
:::

## Symmetry without a penalty

Imagine shuffling every sensor label in every possible way, then averaging the resulting weight lists. Words with the same number of ones can be shuffled into one another. The averaging inequality shows why this smoothing can cost nothing when the sensors are equally likely.

::: {.corollary #symmetric-optimum title="Existence of a symmetric optimum" status="written-proof" proof="pf-symmetric-optimum" doi="10.5281/zenodo.24405810" source="Corollary 5 (cor:sym)" request="https://github.com/the-omega-institute/trureturing-requests/issues/556" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s5"}
For equal priors there exists an optimal coefficient-square distribution constant on each Hamming-weight layer.
:::

::: {.proof #pf-symmetric-optimum}
A sensor permutation makes the same unitary change of coordinates to the outputs and relabels the alternatives. At equal priors it leaves optimal error unchanged. Apply weak averaging repeatedly to all permuted copies of an optimal distribution: their average has error at most the optimum, hence equal to it. The average is constant on each permutation orbit, which is exactly a weight layer. An optimal probe exists because the unit sphere and global POVM set are compact and success is continuous. This is Corollary 5 in the paper. Nothing in the argument requires every optimum to be symmetric.
:::

## Best layer or perfect mixture?

Among all layers, a central layer makes $k(n-k)$ largest and thus makes the common overlap smallest. A mixture of layers makes a weighted average of their overlaps. If the smallest overlap is nonnegative, use it. If it is negative, mix it with a positive overlap to reach zero, when the three or more output vectors are mutually orthogonal and can be identified without error.

::: {.corollary #global-value title="The global error and the companion conjecture" status="written-proof" proof="pf-global-value" doi="10.5281/zenodo.24405810" source="Corollary 6 (cor:optimal)" request="https://github.com/the-omega-institute/trureturing-requests/issues/557" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s6"}
For $m=\lfloor n/2\rfloor$, put $c_{\min}=1-4m(n-m)\sin^2\theta/[n(n-1)]$ and $c_*=\max\{0,c_{\min}\}$. Over normalized pure probes with equal priors, the global minimum error is $1-F_n(c_*)$. When $c_{\min}\geq0$, a uniform probe on any layer minimizing $c_k$ is optimal. This gives Conjecture 1 in the angular range where it was posed.
:::

::: {.proof #pf-global-value}
By the symmetry result, it suffices to mix uniform-layer distributions. Their common overlaps fill the interval $[c_{\min},1]$: a central layer attains the lower endpoint and layer zero has overlap $1$. If $c_{\min}\geq0$, monotonicity of $F_n$ selects the lower endpoint. Otherwise give a central layer weight $1/(1-c_{\min})$ and give layer zero the remainder; the overlap is $0$ and the success $1$, the largest possible. For $r=\lceil n/2\rceil$ and $T=\tfrac12\arccos(-(r-1)/r)$, the identity $\sin^2 T=n(n-1)/(4m(n-m))$ shows that $c_{\min}\geq0$ exactly on $(0,T]\cup[\pi-T,\pi)$. The overlap of each layer is also the average of $1$ for matching bits and $\cos(2\theta)$ for differing bits, the ratio minimized in Conjecture 1. This is Corollary 6 in the paper.
:::

At odd $n$, the two central layers are different. Where $c_{\min}\geq0$, not only the two layers but the entire segment between them is optimal. For example, the three-sensor tie in the preceding chapter is globally optimal and still has positive error. The pinned Dicke-optimality argument compares a minimizing layer against every pure probe and global POVM in the Conjecture 1 angular range; it does not cover the full-angle formula. The symmetric-probe formula and the zero-overlap construction trace back to Skotiniotis et al.; the averaging argument explains why optimizing over their symmetric class suffices here.
