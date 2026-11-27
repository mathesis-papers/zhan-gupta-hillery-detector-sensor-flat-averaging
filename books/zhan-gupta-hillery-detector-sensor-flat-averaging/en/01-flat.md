# Two lists, one table of overlaps

## What a firing changes

Use $n\geq3$ two-state sensors. Choose the two basis states of each sensor so that a firing multiplies them by $e^{-i\theta}$ and $e^{i\theta}$, with $0<\theta<\pi$ in radians. Label the basis by bit strings $x$ and put $s_i(x)=2x_i-1$. A probe is a unit vector with amplitudes $\psi_x$; its weights $p_x=|\psi_x|^2$ sum to one. If sensor $i$ fires, the output $\phi_i$ has amplitudes $e^{i\theta s_i(x)}\psi_x$.

A measurement is a list of positive semidefinite effects $M_i$ summing to the identity (a POVM). Effect $M_j$ gives the probability of guessing $j$ from $\phi_i$ by $\langle\phi_i,M_j\phi_i\rangle$. The best equal-prior error $P(p)$ is one minus the largest average of the correct-guess probabilities, with each sensor equally likely to fire. Measurements here can act on the entire sensor system.

The overlap table, or **Gram matrix**, is $G(p)_{ij}=\langle\phi_i,\phi_j\rangle=\sum_x p_x e^{i\theta(s_j(x)-s_i(x))}$. The original amplitude phases cancel. In particular, replacing $p$ by $tp+(1-t)q$ replaces $G$ by $tG(p)+(1-t)G(q)$. The new pure preparation has amplitudes $\sqrt{tp_x+(1-t)q_x}$: it is not an average of amplitude vectors and not a density-matrix mixture.

::: {.lemma #gram-transfer title="Equal overlap tables preserve measurement statistics" status="written-proof" proof="pf-gram-transfer" doi="10.5281/zenodo.24405810" source="Lemma 1 (lem:gram)" request="https://github.com/the-omega-institute/trureturing-requests/issues/552" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s1"}
Two finite labelled pure-state ensembles with the same Gram matrix have the same attainable measurement probabilities, hence the same optimal minimum-error success for any fixed priors.
:::

::: {.proof #pf-gram-transfer}
Replace each labelled vector of the first ensemble by the equally labelled vector of the other. A linear combination with coefficients $z$ has squared norm $z^*Gz$ on both sides, so this is well-defined even when the vectors are dependent. It is an isometry between the two spans. Compress any measurement to the first span, transport the effects along the isometry, then assign the unused orthogonal complement to one outcome. There is no change to any probability. Transport in the other direction for equality of the attainable sets. This is the proof of Lemma 1 in the paper.
:::

## Why the lists tie

The **weight** of a word is its number of ones. The probe $D_k$ gives equal weights to the words of weight $k$ and zero weight to the others. Among words of weight $k$, the fraction with $x_i=1,x_j=0$ is $k(n-k)/[n(n-1)]$; the opposite case has the same fraction. For the three words `100, 010, 001` and the first two positions, one word gives each opposite pair and one word gives equal bits. The complementary words have the same counts, with the two opposite pairs swapped.

| Weight layer | Words at $n=3$ | Equal bits at positions 1 and 2 | Opposite bits |
|---|---|---:|---:|
| 1 | `100, 010, 001` | 1 of 3 | 2 of 3 |
| 2 | `011, 101, 110` | 1 of 3 | 2 of 3 |

::: {.theorem #flat-family title="Flat complementary layers" status="written-proof" proof="pf-flat-family" doi="10.5281/zenodo.24405810" source="Theorem 2 (thm:flat)" request="https://github.com/the-omega-institute/trureturing-requests/issues/553" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s2"}
Let $1\leq k\leq n-1$ and $k\ne n-k$. Denote the weights of $D_k$ by $p^{(k)}$ and form the normalized pure probe $A_t$ with amplitudes $\sqrt{t p^{(k)}_x+(1-t)p^{(n-k)}_x}$, $0\leq t\leq1$. The endpoint weights are distinct, but $P(D_k)=P(D_{n-k})=P(A_t)$ for every $t$. In particular the midpoint refutes the strict claim in Conjecture 2.
:::

::: {.proof #pf-flat-family}
For each ordered pair of distinct positions, count the two opposite-bit cases: each has $\binom{n-2}{k-1}$ words out of $\binom nk$. Opposite phase contributions are conjugate, and equal bits contribute one. Every off-diagonal entry is therefore

$$c_k=1-\frac{4k(n-k)}{n(n-1)}\sin^2\theta.$$

This is the earlier Skotiniotis et al. formula in the diagonal-one convention. It is unchanged under $k\mapsto n-k$. The endpoints have disjoint nonempty supports, but the same Gram matrix; affineness gives it to the entire segment. The measurement-statistics lemma transfers the equality to error. With distinct weights and equal endpoint errors, strict improvement at $t=1/2$ would contradict this equality. This is Theorem 2 in the paper.
:::

::: {.film src="001-flat-averages"}
Why the complementary lists yield the same measurement problem, even after mixing their weights.
:::

## How big is the tie?

The earlier overlap formula uses the phase difference $2\theta$ (folded if needed) and, in the expanded paper, a prior factor $1/n$ in the Gram matrix. Here the diagonal is one. At $n=3$, $k=1$ and $\theta=\pi/4$, $c_k=1/3$. The eigenvalues of the overlap table are $5/3,2/3,2/3$. The following calculation shows that the tie is at **positive** error, not a consequence of having already reached zero.

::: {.lemma #equal-overlap title="Optimal success at a common overlap" status="written-proof" proof="pf-equal-overlap" doi="10.5281/zenodo.24405810" source="Lemma 3 (lem:symmetric)" request="https://github.com/the-omega-institute/trureturing-requests/issues/554" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s3"}
For equiprobable normalized pure states with $G=(1-c)I+cJ\succeq0$, where $J$ is the all-ones matrix, the optimal success is

$$F_n(c)=\frac{\big(\sqrt{1+(n-1)c}+(n-1)\sqrt{1-c}\big)^2}{n^2}.$$

On $0\leq c\leq1$ it is nonincreasing.
:::

::: {.proof #pf-equal-overlap}
On the all-ones direction $G$ has eigenvalue $1+(n-1)c$, and on its orthogonal complement it has eigenvalue $1-c$. Put $B=\sqrt G$ and write $a$ for its common diagonal entry, the mean of those square roots counted with multiplicity. The equivalent ensemble $Be_i$ has success $a^2$ in the coordinate projective measurement. Cauchy–Schwarz in the form defined by $B$ gives $|e_i^*Bv|^2\leq a\,v^*Bv$ for every $v$, so $Y=aB/n$ dominates each $Be_i(Be_i)^*/n$. For any measurement, summing the trace of each effect against this bound gives success at most $\operatorname{tr}Y=a^2$. This works also at singular $G$. On $0<c<1$, the derivative of the sum of square roots in the numerator is $(n-1)(1/\sqrt{1+(n-1)c}-1/\sqrt{1-c})/2\leq0$; continuity handles the endpoints. This is Lemma 3 in the paper and uses the square-root measurement.
:::

Now $1-F_3(1/3)=(14-4\sqrt{10})/27$ for every $t$. For a quick check, at $t=1/2$ all six listed words have weight $1/6$; four out of six have opposite bits at positions 1 and 2. The count is still two thirds. The pinned Lean argument rules out the strict midpoint inequality for these two optimal endpoints; it does not assert the equality for every $t$ or the displayed radical value. The equal-overlap calculation and all-$t$ statement are the paper's written arguments.
