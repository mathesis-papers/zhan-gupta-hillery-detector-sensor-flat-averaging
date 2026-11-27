# 另一种失败

到目前为止，每次测量都必须猜一个答案。现在允许回答“不知道”，写作 $?$；但只要明确作答，就绝不能猜错。新的代价是 $?$ 出现的概率，这叫**无歧义判别**。两种任务的失败公式不同；有趣的是，在等先验模型中，论文却能用同一个探针同时做到最好。

::: {.corollary #unambiguous-optimum title="无歧义失败率与共同的最佳探针" status="written-proof" proof="pf-unambiguous-optimum" doi="10.5281/zenodo.24405810" source="Corollary 7 (cor:ud)" request="https://github.com/the-omega-institute/trureturing-requests/issues/558" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s7"}
最小无歧义失败率是系数模平方分布的凸函数，并且在任意固定先验下沿平坦族恒定。在等先验下，全局最小失败率是 $c_*=\max\{0,c_{\min}\}$。论文构造的最小错误最优探针也达到这个最优值。
:::

::: {.proof #pf-unambiguous-optimum}
格拉姆矩阵相同时搬运测量，不会改变猜错的零概率，因而能证明平坦性，并且直和测量保留共同的“不知道”标签，给出凸性。等先验下再用置换平均，便只须考察对称探针。对称重叠表为 $G$ 时，$q_i\geq0$ 能成为正确且明确作答的概率，当且仅当 $G-\operatorname{diag}(q_i)\succeq0$：这个剩余矩阵是“不知道”效果算子贡献的格拉姆矩阵。反过来，把它实现为向量 $\beta_i$ 的重叠表，则 $\sqrt{q_i}e_i\oplus\beta_i$ 的重叠表为 $G$，搬运测量即可实现所需概率。对可行的对角矩阵做置换平均，所有 $q_i$ 都可取相同的均值。最大均值是 $\lambda_{\min}(G)$，故失败率为 $\max\{c,-(n-1)c\}$。在 $[c_{\min},1]$ 上，若 $c_{\min}\geq0$ 就取 $c_{\min}$，否则取零。最小错误判别所用的同一个层或零重叠混合探针也达到这个值。这是论文推论 7 的论证。
:::

三传感器的平坦例子在正的“不知道”概率 $1/3$ 下依然打成平手。对照小得多的最小错误率，就能看到：不许猜错改变的是评分方式，不是重叠表。等先验最优化也不等于解决一般不等先验最优化。

::: {.corollary #diagonal-patterns title="对角作用模式与辅助系统" status="written-proof" proof="pf-diagonal-patterns" doi="10.5281/zenodo.24405810" source="Corollary 8 (cor:patterns)" request="https://github.com/the-omega-institute/trureturing-requests/issues/559" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s8"}
设一族有限个酉算子在同一组基上对角化，即 $V_a|x\rangle=v_a(x)|x\rangle$ 且 $|v_a(x)|=1$。在任意固定先验下，最小错误率和无歧义失败率都对系数模平方分布具有凸性。添加辅助系统不能改善任何一个最优值。
:::

::: {.proof #pf-diagonal-patterns}
格拉姆矩阵的元素是 $\sum_x p_x\overline{v_a(x)}v_b(x)$，对 $p$ 是仿射的，因此同一个直和论证给出两种判别的凸性。带辅助系统的纯态探针可写成 $\sum_x|x\rangle|a_x\rangle$。令 $p_x=\langle a_x,a_x\rangle$，其输出重叠表与只有传感器、振幅取 $\sqrt{p_x}$ 的探针完全相同，所以可实现的测量概率也相同。对于混态，可以先纯化；丢弃纯化系统不可能比保留它做得更好，而保留它时可应用纯态的论证。这是论文推论 8 的论证。
:::

只要作用算子能在同一组基上对角化，即使某个假设同时改变几个相位，这种方法仍能使用。但它没有给出每种多处触发模式的最佳探针。单处触发情形的早期辅助系统分析见 Skotiniotis 等人的扩展版附录 A。

::: {.corollary #nonsymmetric-optimum title="一个不对称的最佳探针" status="written-proof" proof="pf-nonsymmetric-optimum" doi="10.5281/zenodo.24405810" source="Corollary 9 (cor:necessity)" request="https://github.com/the-omega-institute/trureturing-requests/issues/560" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s9"}
当 $n=3$、$\theta=\pi/2$、$0<a<1$ 时，分布 $p_x=(1+a(2x_1-1))/8$ 不在每个重量层内恒定，却对两种判别都最优。
:::

::: {.proof #pf-nonsymmetric-optimum}
此分布为正且总和为一。令 $s_i=2x_i-1$。在这个角度，不同 $i,j$ 的重叠等于 $s_i s_j$ 在 $p$ 下的均值，也就是 $(1+a s_1)s_i s_j$ 在均匀分布下的均值。展开后的每一项都可约成独立公平符号的非恒定乘积，均值为零。因此 $G=I$，两种失败率都为零。但重量相同、第一位不同的串有不同的概率。这是论文推论 9 的论证。
:::

::: {.corollary #global-projective title="全局投影测量保留两个最优值" status="written-proof" proof="pf-global-projective" doi="10.5281/zenodo.24405810" source="Corollary 10 (cor:projective)" request="https://github.com/the-omega-institute/trureturing-requests/issues/561" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s10"}
在原等先验的单处触发模型中，把测量限制为任意全局投影测量，两种最优值都不变。无歧义测量含有一个“不知道”的结果。
:::

::: {.proof #pf-global-projective}
取共同的最优探针，格拉姆矩阵为 $G=(1-c_*)I+c_*J$。对 $\sqrt G e_i$ 做坐标投影，能达到最优成功率 $F_n(c_*)$。延拓输出张成空间之间的等距映射，把这个模型嵌入物理传感器空间，再把未用到的正交补分给一个测量结果。对无歧义判别，改用 $n+1$ 维向量 $\sqrt{1-c_*}e_i+\sqrt{c_*}e_?$，格拉姆矩阵仍为 $G$。由于 $2^n\geq n+1$，同样能嵌入；这次把剩余空间分给 $?$。坐标投影不会给出错误的明确答案，失败率正好是 $c_*$。两种投影测量各自达到未加限制时的最优值。这是论文推论 10 的论证。
:::

这些投影可以联合作用于整个传感器系统；这并不意味着分开测量各传感器也能达到同样成绩。含噪声信道的最优化以及多处触发的一般最优值也超出了本文结论的范围。全局限制下的最优值不变，并不意味着可以把最优测量换成局部测量。
