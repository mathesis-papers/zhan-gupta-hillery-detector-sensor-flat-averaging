# 两张清单，同一张重叠表

## 触发改变了什么

取 $n\geq3$ 个双态传感器。选取合适的两个基态，使触发对这两个基态分别乘以 $e^{-i\theta}$ 与 $e^{i\theta}$，其中 $0<\theta<\pi$，角度以弧度计。用比特串 $x$ 标记整套基，并置 $s_i(x)=2x_i-1$。探针是振幅为 $\psi_x$ 的单位向量；对应的权重 $p_x=|\psi_x|^2$ 总和为一。若传感器 $i$ 触发，输出态 $\phi_i$ 的振幅就是 $e^{i\theta s_i(x)}\psi_x$。

测量可用一列正半定算子 $M_j$ 描述，它们相加等于恒等算子，这叫 POVM。在输出态 $\phi_i$ 上猜 $j$ 的概率为 $\langle\phi_i,M_j\phi_i\rangle$。若每个传感器等可能触发，就对猜对的概率取等权平均；平均成功率最大时，一减去这个最大值便是最小错误率 $P(p)$。这里允许对整组传感器做全局测量。

把所有输出态两两做内积，得到**格拉姆矩阵**，也就是重叠表：$G(p)_{ij}=\langle\phi_i,\phi_j\rangle=\sum_x p_x e^{i\theta(s_j(x)-s_i(x))}$。探针原有的振幅相位在内积中抵消。把 $p$ 换成 $tp+(1-t)q$，重叠表就变成 $tG(p)+(1-t)G(q)$。新的纯态振幅是 $\sqrt{tp_x+(1-t)q_x}$，既不是两组振幅向量的平均，也不是密度矩阵的混合。

::: {.lemma #gram-transfer title="相同的重叠表给出相同的测量统计" status="written-proof" proof="pf-gram-transfer" doi="10.5281/zenodo.24405810" source="Lemma 1 (lem:gram)" request="https://github.com/the-omega-institute/trureturing-requests/issues/552" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s1"}
两个有限的带标签纯态族若有相同的格拉姆矩阵，可实现的测量概率完全相同。因此在任何固定先验下，它们最小错误判别的最佳成功率也相同。
:::

::: {.proof #pf-gram-transfer}
把第一个态族的每个向量换成第二个态族中标签相同的向量。以 $z$ 为系数的线性组合在两边的范数平方都是 $z^*Gz$，因此即使向量线性相关，这个替换也定义良好，并且给出两个张成空间之间的等距映射。把测量压缩到第一个张成空间，再沿映射搬过去，并把未用到的正交补分配给某个结果。所有测量概率不变。反向搬运则证明可实现的统计集合相同。这是论文引理 1 的论证。
:::

## 为什么两张清单打成平手

比特串的**重量**是其中 1 的个数。探针 $D_k$ 给重量为 $k$ 的每个串同样的权重，对其他串给零权重。固定不同的两个位置 $i,j$，重量为 $k$ 的串中，$x_i=1,x_j=0$ 所占比例是 $k(n-k)/[n(n-1)]$；反过来的情况比例相同。拿 `100、010、001` 的前两位来数，两种相反的比特排列各出现一次，两位相同也出现一次。互补清单只是把两种相反排列调换了。

| 重量层 | $n=3$ 时的串 | 前两位相同 | 前两位不同 |
|---|---|---:|---:|
| 1 | `100、010、001` | 3 个中有 1 个 | 3 个中有 2 个 |
| 2 | `011、101、110` | 3 个中有 1 个 | 3 个中有 2 个 |

::: {.theorem #flat-family title="互补重量层之间的平坦族" status="written-proof" proof="pf-flat-family" doi="10.5281/zenodo.24405810" source="Theorem 2 (thm:flat)" request="https://github.com/the-omega-institute/trureturing-requests/issues/553" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s2"}
设 $1\leq k\leq n-1$ 且 $k\ne n-k$。将 $D_k$ 的权重记为 $p^{(k)}$，取振幅为 $\sqrt{t p^{(k)}_x+(1-t)p^{(n-k)}_x}$ 的归一化纯态 $A_t$，其中 $0\leq t\leq1$。两个端点的权重分布不同，但对每个 $t$ 都有 $P(D_k)=P(D_{n-k})=P(A_t)$。特别地，中点反驳猜想 2 的严格改进结论。
:::

::: {.proof #pf-flat-family}
对于每对有序的不同位置，两种比特不同的排列各占 $\binom{n-2}{k-1}$ 个串，全部共有 $\binom nk$ 个串。不同比特贡献一对共轭相位，相同比特贡献 1。因此每个非对角元都是

$$c_k=1-\frac{4k(n-k)}{n(n-1)}\sin^2\theta.$$

这就是 Skotiniotis 等人的公式，写成对角元为 1 的形式。把 $k$ 换成 $n-k$，公式不变。两个端点的支撑非空且不相交，但重叠表相同；沿着线段取权重平均，仍得到同一张表。由测量统计引理，错误率也相同。由于端点的权重不同、错误率相等，若 $t=1/2$ 严格改进，就与这个等式冲突。这是论文定理 2 的论证。
:::

::: {.film src="001-flat-averages"}
互补清单为什么给出同一个测量问题，即使把它们的权重混合也是如此。
:::

## 平手的错误率有多大？

早期重叠公式用的是相位差 $2\theta$（必要时折到规定区间），扩展论文还在重叠表中乘入了先验因子 $1/n$。本书的对角元为 1。取 $n=3$、$k=1$、$\theta=\pi/4$，得到 $c_k=1/3$，重叠表的特征值为 $5/3,2/3,2/3$。下面的计算说明，这次平手发生在**正的错误率**，并不是因为错误率早已降到零。

::: {.lemma #equal-overlap title="共同重叠给出的最佳成功率" status="written-proof" proof="pf-equal-overlap" doi="10.5281/zenodo.24405810" source="Lemma 3 (lem:symmetric)" request="https://github.com/the-omega-institute/trureturing-requests/issues/554" mathesis="collected:zhan-gupta-hillery-detector-sensor-flat-averaging:3:s3"}
若等可能出现的归一化纯态满足 $G=(1-c)I+cJ\succeq0$，其中 $J$ 是全一矩阵，则最佳成功率为

$$F_n(c)=\frac{\big(\sqrt{1+(n-1)c}+(n-1)\sqrt{1-c}\big)^2}{n^2}.$$

在 $0\leq c\leq1$ 上，这个函数单调不增。
:::

::: {.proof #pf-equal-overlap}
全一方向的特征值是 $1+(n-1)c$，其正交补上的特征值是 $1-c$。令 $B=\sqrt G$；它的共同对角元 $a$ 是这两个特征值开方后按重数算出的平均。在等价态族 $Be_i$ 上做坐标投影测量，可达到成功率 $a^2$。在 $B$ 定义的半正定形式中用柯西–施瓦茨不等式，得到 $|e_i^*Bv|^2\leq a\,v^*Bv$，所以 $Y=aB/n$ 在半正定序下大于等于每个 $Be_i(Be_i)^*/n$。任意测量的成功率都不超过各效果算子与 $Y$ 的迹之和，即 $\operatorname{tr}Y=a^2$。即使 $G$ 奇异，此论证也成立。在 $0<c<1$ 上，分子根式之和的导数是 $(n-1)(1/\sqrt{1+(n-1)c}-1/\sqrt{1-c})/2\leq0$；连续性给出两端。这是论文引理 3 中的平方根测量论证。
:::

所以每个 $t$ 的最小错误率都是 $1-F_3(1/3)=(14-4\sqrt{10})/27$。可顺手验算：当 $t=1/2$ 时六个串各有 $1/6$ 的权重；其中四个串的前两位不同，比例仍是三分之二。所钉的 Lean 论证排除了这两个最佳端点的中点严格改进，但没有断言所有 $t$ 的等式，也没有给出这个根式值。共同重叠的计算和整条线段的等式来自论文的书面证明。
