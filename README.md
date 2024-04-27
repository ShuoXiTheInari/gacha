# 抽卡计算器

计算带保底机制的卡池的抽卡期望和保底概率


## 无保底机制

Expected number of times of single drop:
对于1次出货，期望次数为：1/P 

## 单保底机制

Expected number of times of single drop:

对于1次出货，期望次数为：该次恰好出的概率\*次数 + 保底次数\*保底的概率

## 大小保底机制

Expected number of times of single drop:

对于一次出货，期望次数为：求和（1-保底次数-1） ｛该次恰好出的概率\*次数｝ + 小保底次数\*保底的概率\*保底不歪的概率 + 保底歪的概率*(求和 （1-保底次数-1） ｛除却保底次的该次恰好出的概率\*次数｝+ 保底的概率*保底次数)

```Math
E(N_{total}) = \sum_{k=1}^{X} k \cdot P(1-P)^{k-1} + (X+1)(1-P)^X
```

```Math
E(N_{total}) = \sum_{k=1}^{X-1} k \cdot P(1-P)^{k-1} + P_X\cdot X(1-P) ^ {(X-1)} +(1-P_X)\cdot (1-P) ^ {(X-1)} (\sum_{k=X+1}^{2X-1} k \cdot P(1-P)^{k-2} + 2X \cdot (1-P)^{(2X-2)}) 
```

