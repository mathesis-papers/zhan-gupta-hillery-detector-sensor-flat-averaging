# A different kind of mistake

So far every answer was a guess. Now allow the measurement to answer “I don't know”, written $?$; in exchange, a guess may never be wrong. The new cost is the probability of $?$ and the task is called **unambiguous discrimination**. These two games do not have the same error formula. Surprisingly, the paper can use the same best preparation for both in the equal-prior model.

::: {.corollary #unambiguous-optimum title="Unambiguous failure and a common optimal probe" status="written-proof" proof="pf-unambiguous-optimum" doi="10.5281/zenodo.24405810" source="Corollary 7 (cor:ud)" request="https://github.com/the-omega-institute/trureturing-requests/issues/558" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s7"}
Optimal unambiguous failure is convex in the coefficient-square distribution, and is constant along the flat family for any fixed priors. With equal priors the global optimum failure is $c_*=\max\{0,c_{\min}\}$. The manuscript's optimum probe for minimum error also attains this optimum.
:::

::: {.proof #pf-unambiguous-optimum}
Equal-Gram transport preserves the zero probabilities of wrong guesses, so it proves flatness and allows the direct-sum measurement to establish convexity with a common inconclusive label. With equal priors, permutation averaging reduces the search to symmetric probes. For a symmetric overlap matrix $G$, numbers $q_i\geq0$ are possible correct conclusive probabilities exactly when $G-\operatorname{diag}(q_i)\succeq0$: this residual is the Gram matrix contributed by the inconclusive effect. Conversely, realize that residual as vectors $\beta_i$ and use $\sqrt{q_i} e_i\oplus\beta_i$ to build the required measurement by equal-Gram transport. Averaging a feasible diagonal over permutations allows all $q_i$ to equal their mean. The largest possible mean is $\lambda_{\min}(G)$, giving failure $\max\{c,-(n-1)c\}$. On $[c_{\min},1]$ the optimum is $c_{\min}$ if nonnegative and zero otherwise. The same layer or zero-overlap mixture used for minimum error attains it. This is Corollary 7 in the paper.
:::

Thus the flat three-sensor example ties even at positive inconclusive probability, $1/3$. Compare this with its much smaller minimum error: refusing to make a wrong guess changes the score, not the overlap table. The equal-prior optimization does not solve general unequal-prior optimization.

::: {.corollary #diagonal-patterns title="Diagonal impact patterns and auxiliary systems" status="written-proof" proof="pf-diagonal-patterns" doi="10.5281/zenodo.24405810" source="Corollary 8 (cor:patterns)" request="https://github.com/the-omega-institute/trureturing-requests/issues/559" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s8"}
Let a finite family of unitaries be diagonal in a common basis, $V_a|x\rangle=v_a(x)|x\rangle$ with $|v_a(x)|=1$. With any fixed priors, both minimum error and unambiguous failure are convex in the coefficient-square distribution. Adding an auxiliary system cannot improve either optimum.
:::

::: {.proof #pf-diagonal-patterns}
The Gram matrix has entries $\sum_x p_x\overline{v_a(x)}v_b(x)$, affine in $p$, so the same direct-sum proof works for either objective. Write a pure probe with an auxiliary system as $\sum_x|x\rangle|a_x\rangle$. Its output Gram matrix is exactly that of the sensor-only probe with amplitudes $\sqrt{p_x}$ for $p_x=\langle a_x,a_x\rangle$. Equal-Gram transport preserves all attainable probabilities. A mixed probe can be purified; ignoring the purifying system cannot improve its optimal score over keeping it, and the pure auxiliary argument applies. This is Corollary 8 in the paper.
:::

This explains why the method still applies when a hypothesis changes several phases at once, provided the operators are diagonal in one basis. It is not a formula for the best probe for every multi-impact pattern. For earlier auxiliary-system analysis in the single-impact setting, see Appendix A of the expanded Skotiniotis et al. paper.

::: {.corollary #nonsymmetric-optimum title="A nonsymmetric optimum" status="written-proof" proof="pf-nonsymmetric-optimum" doi="10.5281/zenodo.24405810" source="Corollary 9 (cor:necessity)" request="https://github.com/the-omega-institute/trureturing-requests/issues/560" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s9"}
For $n=3$, $\theta=\pi/2$ and $0<a<1$, the distribution $p_x=(1+a(2x_1-1))/8$ is not constant on each weight layer but is optimal for both criteria.
:::

::: {.proof #pf-nonsymmetric-optimum}
The distribution is positive and sums to one. For distinct $i,j$ the overlap at this angle is the mean of $s_i s_j$ under $p$, where $s_i=2x_i-1$. Write it as the uniform mean of $(1+a s_1)s_i s_j$. Every resulting product reduces to a nonconstant product of independent fair signs, whose mean vanishes. Therefore $G=I$ and both scores of failure are zero. Same-weight words with different first bits have different probabilities. This is Corollary 9 in the paper.
:::

::: {.corollary #global-projective title="The same optima with global projectors" status="written-proof" proof="pf-global-projective" doi="10.5281/zenodo.24405810" source="Corollary 10 (cor:projective)" request="https://github.com/the-omega-institute/trureturing-requests/issues/561" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s10"}
For the original equal-prior single-firing model, optimizing over arbitrary global projective measurements preserves both optima. The unambiguous measurement includes an inconclusive outcome.
:::

::: {.proof #pf-global-projective}
Take the common optimum probe, with $G=(1-c_*)I+c_*J$. For minimum error, the coordinate projectors on $\sqrt G e_i$ attain $F_n(c_*)$. Embed this model space into the physical sensor space by extending the isometry between output spans; assign the unused orthogonal complement to a single outcome. For unambiguous discrimination use $\sqrt{1-c_*}e_i+\sqrt{c_*}e_?$ in dimension $n+1$, again with Gram matrix $G$. That model fits because $2^n\geq n+1$; extend the isometry and assign the complement to $?$ instead. Coordinate projection never gives a wrong conclusive result and has failure $c_*$. Both attain the unrestricted optima. This is Corollary 10 in the paper.
:::

The projectors may act jointly across the sensors; nothing here implies that measuring each sensor separately will do as well. Noisy-channel optimization and a general optimum for multiple impacts also remain outside the result. These distinctions matter: equality of optimal values under a global restriction does not permit replacing every optimal measurement with a local one.
