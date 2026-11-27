# 平均究竟能保证什么

平坦族排除了**严格**改进。但平均仍有用：它的错误率不会超过两个错误率的加权平均。想象把两套输出向量放在一个更长向量的两个互相正交的分区里。对每个分区分别进行最合适的测量，就能达到相应成功率的加权平均。格拉姆矩阵说明，这种测量策略也能用于那个按平均权重准备的单一纯态探针。

::: {.theorem #weak-averaging title="弱平均不等式" status="written-proof" proof="pf-weak-averaging" doi="10.5281/zenodo.24405810" source="Theorem 4 (thm:convex)" request="https://github.com/the-omega-institute/trureturing-requests/issues/555" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s4"}
对任意两个系数模平方分布 $p,q$ 与 $0\leq t\leq1$，

$$P(tp+(1-t)q)\leq tP(p)+(1-t)P(q).$$

因此，如果两个端点的错误率相同，平均不会使错误率升高，但可以保持不变。
:::

::: {.proof #pf-weak-averaging}
在两个彼此正交的输出空间副本中取向量 $\eta_i=\sqrt t\,\phi_i(p)\oplus\sqrt{1-t}\,\phi_i(q)$。它们的格拉姆矩阵是 $tG(p)+(1-t)G(q)$，正好等于平均权重探针的重叠表。若原来两个实验的最优效果算子是 $M_i$ 和 $N_i$，则 $M_i\oplus N_i$ 达到原成功率的加权平均。用格拉姆矩阵相同的引理把测量搬回平均权重的纯态探针，最好的测量只会更好或一样好。端点显然成立；沿途使用同一组固定先验即可，无须等先验。这是论文定理 4 的论证。
:::

## 对称化不增加代价

想象用每种可能的方式打乱传感器的编号，然后把得到的权重清单取平均。1 的个数相同的两个串，可以通过重排彼此转换。平均不等式解释了为什么在传感器等可能触发时，这样把权重抹平不必付出代价。

::: {.corollary #symmetric-optimum title="存在对称的最佳探针" status="written-proof" proof="pf-symmetric-optimum" doi="10.5281/zenodo.24405810" source="Corollary 5 (cor:sym)" request="https://github.com/the-omega-institute/trureturing-requests/issues/556" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s5"}
在等先验下，存在一个最优的系数模平方分布，在每个汉明重量层内恒定。
:::

::: {.proof #pf-symmetric-optimum}
传感器的置换给所有输出施加同一个酉坐标变换，同时重排备选标签。等先验下，最小错误率不变。对一个最优分布的所有置换副本反复应用弱平均不等式，平均分布的错误率不超过最优值，因此恰等于最优值。平均在每个置换轨道上恒定，而轨道恰好就是重量层。探针的单位球面及全局 POVM 集都紧，成功率连续，因此最优探针存在。这是论文推论 5 的论证，并不要求每个最优探针都对称。
:::

## 用最佳层，还是混出零重叠？

中间的重量层使 $k(n-k)$ 最大，因而使共同重叠最小。把各层混合，就得到这些重叠的加权平均。若最小重叠非负，就用它；若它为负，就与一个正重叠混合得到零。此时所有输出向量两两正交，可以完全无误地辨认。

::: {.corollary #global-value title="全局最小错误率与猜想 1" status="written-proof" proof="pf-global-value" doi="10.5281/zenodo.24405810" source="Corollary 6 (cor:optimal)" request="https://github.com/the-omega-institute/trureturing-requests/issues/557" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s6"}
设 $m=\lfloor n/2\rfloor$，$c_{\min}=1-4m(n-m)\sin^2\theta/[n(n-1)]$，$c_*=\max\{0,c_{\min}\}$。在等先验下，遍历所有归一化纯态探针得到的全局最小错误率为 $1-F_n(c_*)$。当 $c_{\min}\geq0$ 时，任何使 $c_k$ 最小的层上的均匀探针都是最优的。这就在猜想 1 所规定的角度范围内给出了其结论。
:::

::: {.proof #pf-global-value}
由对称性结论，只须考察各层均匀分布的混合。它们的共同重叠填满区间 $[c_{\min},1]$：中间层给出下端点，第零层给出 $1$。若 $c_{\min}\geq0$，由 $F_n$ 单调不增，应选下端点。否则给中间层权重 $1/(1-c_{\min})$，其余给第零层，重叠即为零，成功率达到上界 $1$。令 $r=\lceil n/2\rceil$、$T=\tfrac12\arccos(-(r-1)/r)$，由 $\sin^2 T=n(n-1)/(4m(n-m))$ 可知，$c_{\min}\geq0$ 恰对应 $(0,T]\cup[\pi-T,\pi)$。各层的重叠也是相同比特贡献 $1$、不同比特贡献 $\cos(2\theta)$ 的加权平均，即猜想 1 所要最小化的比值。这是论文推论 6 的论证。
:::

当 $n$ 为奇数时，两个中间层不同。只要 $c_{\min}\geq0$，不但两个端点最优，中间整条线段也最优。例如上一章的三传感器平手，就是发生在正错误率下的全局最优。所钉的 Dicke 最优性论证在猜想 1 的角度范围内，把最小重叠层与所有纯态探针、全局 POVM 作比较，并没有给出完整角度范围的公式。对称探针的公式和零重叠构造源自 Skotiniotis 等人；平均论证说明，为何这里可以只在他们的对称类中寻找最优值。
