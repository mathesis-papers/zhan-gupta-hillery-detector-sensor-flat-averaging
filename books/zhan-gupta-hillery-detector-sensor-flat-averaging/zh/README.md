# 平均改变了探针，却没有改变答案

三个传感器中恰有一个触发。我们没看到是哪一个，但它会在事先准备的量子态上留下相位变化。怎样准备量子态，才能更容易分辨这三种痕迹？如果两种准备方法的错误率相同，把它们的权重平均，能不能做得严格更好？

先看两张三位比特串清单：`100、010、001` 和 `110、101、011`。两张清单毫无交集，但把每一位都反转，就能从一张变到另一张。每个比特串代表量子准备的一项，而不是一个测量答案。能否辨出触发的是哪个传感器，取决于三个**输出态**彼此有多相似。在论文的三传感器例子中，两张清单产生同样的重叠；按任何比例混合它们的权重，重叠也不变。因此，即使最好的测量仍会出错，平均也可能一点都不改善。

1. [两张清单，同一张重叠表](01-flat.md)：动手数一数，看看为什么整条线段上都相等。
2. [平均究竟能保证什么](02-optima.md)：证明平均的错误率不超过加权上界，并求出最佳探针。
3. [另一种失败](03-extensions.md)：允许测量回答“不知道”，并区分全局测量与局部测量。

### 来源

- Haobo Ma、Wenlin Zhang，*Flat averages refute Zhan–Gupta–Hillery, Section 5, Conjecture 2 (2024, p. 10:11): an extension of Skotiniotis et al. (2018)*，[Mathesis 第 3 版](https://doi.org/10.5281/zenodo.24405810)。
- C. Zhan、H. Gupta、M. Hillery，[ *Optimizing Initial State of Detector Sensors in Quantum Sensor Networks*](https://doi.org/10.1145/3655028)，2024。严格改进的猜想见第 5 节第 10:11 页（[arXiv v6](https://arxiv.org/abs/2306.17401v6) 第 11 页）；最佳层猜想见第 10:10 页。
- M. Skotiniotis、R. Hotz、J. Calsamiglia、R. Muñoz-Tapia，[ *Identification of malfunctioning quantum devices*](https://arxiv.org/abs/1808.02729v1)，2018，式 (8)；与 S. Llorens 合作的[ 2024 年扩展版](https://doi.org/10.1103/PhysRevResearch.6.033329)，式 (14) 与第 III.B 节。重叠公式和完美辨认的构造是本文的出发点，并非 Mathesis 论文新增的结果。
- Y. C. Eldar、G. D. Forney, Jr.，[ *On quantum detection and the square-root measurement*](https://doi.org/10.1109/18.915636)，2001，介绍了平方根测量的更一般背景。

若想参与形式化，请使用相应证明旁的请求链接，并遵循[上游贡献指南](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)。与原文及 Lean 源代码关联的[陈述对照](https://github.com/mathesis-papers/zhan-gupta-hillery-detector-sensor-flat-averaging/blob/main/.mathesis/review.json)和这份读物属于同一套交接材料。
