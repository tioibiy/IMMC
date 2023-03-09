# IMMC

## 定义

设指标数量为$M$

建筑数量为$N$

建筑数量类型为$Q$

定义$A(k,t)$为第$k$**个**建筑在时间$t$时的"活性"

第$k$**个**建筑的信息:

1. 其位置${pos}_k=(x_k,y_k)$
2. 其类型$j={type}_k$
3. 其活性$A(k,t)$

定义$a[x][y][i][t]$表示位置$(x,y)$，时间$t$，第$i$个指标的值

定义$getEffect(j,i,aa)$表示第$j$**种**建筑被第$i$个指标(当这个指标为$aa$时)影响的程度

> 农场被土地肥沃程度的影响程度较高,具体表现为,当土地肥沃程度升高时,农场的活性增高

定义

$$
E({info}(k,t)=\{{pos}_k=(x_k,y_k)=(x',y'),j={type}_k,A(k,t)\},pos=(x,y))
$$

表示坐标$(x',y')$的建筑$k$对位置为$(x,y)$的影响

其数值只由$pos,pos'$相对位置,$pos'$位置上建筑的**类型**及其活性决定.

> $E$的输出是一个$M$维(数学上的)向量

## 微分方程

$$
\frac{d(a[x][y][i][t])}{dt}=\sum_{k=1}^nA(k,t)E(\{{pos}_k,{type}_k,A(k,t)\},(x,y))
$$

$$
A(k,t)=f(list=\{getEffect({type}_k,i,a[x][y][i][t])\})
$$

> 大概率是加权平均

$$
a[x][y][i][t]=a_0((x,y),i)
$$

> 初始条件

化简得话就是

$$
\begin{aligned}
\frac{d(a[x][y][i][t])}{dt}=\sum_{k=1}^nf(list=\{getEffect({type}_k,i,a[x][y][i][t])\})E(\{{pos}_k,{type}_k,A(k,t)\},(x,y))\\
a[x][y][i][t]=a_0((x,y),i)
\end{aligned}
$$