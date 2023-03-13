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

定义收益$P(r,T,list=[a_0((x,y),i)])$

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

## 积分

定义收益

$$
P(r,T,list=[a_0((x,y),i)])=\int_0^T(\sum_{k=1}^n(rh_1(t)+(1-r)h_2(t))A(k,t)S({type}_k,t))dt
$$

## 新·定义

$$
\begin{bmatrix}
    f_i
\end{bmatrix}_{i=1}^n=
\begin{bmatrix}
    f_1\\
    f_2\\
    \vdots\\
    f_n
\end{bmatrix}
$$

$$
a(t)=
\begin{bmatrix}
    \begin{bmatrix}
        a_{(0,0),0}(t)\\
        \vdots\\
        a_{(0,0),M-1}(t)\\
    \end{bmatrix}&
    \cdots&
    \begin{bmatrix}
        a_{(0,maxy-1),0}(t)\\
        \vdots\\
        a_{(0,maxy-1),M-1}(t)\\
    \end{bmatrix}&\\
    \vdots&\ddots&\vdots\\
    \begin{bmatrix}
        a_{(maxx-1,0),0}(t)\\
        \vdots\\
        a_{(maxx-1,0),M-1}(t)\\
    \end{bmatrix}&
    \cdots&
    \begin{bmatrix}
        a_{(maxx-1,maxy-1),0}(t)\\
        \vdots\\
        a_{(maxx-1,maxy-1),M-1}(t)\\
    \end{bmatrix}
\end{bmatrix}=
\begin{bmatrix}
    \begin{bmatrix}
        a_{(x,y),i}(t)\\
    \end{bmatrix}_{i\in [0,M)}
\end{bmatrix}_{x\in [0,x_{max}),y\in [0,y_{max})}
\Leftarrow
\begin{bmatrix}
    x_{max}\\
    y_{max}\\
    M
\end{bmatrix}
$$

$$
U=
\begin{bmatrix}
    U_{0,0}(\cdot)&U_{0,1}(\cdot)&\cdots&U_{0,M-1}(\cdot)\\
    U_{1,0}(\cdot)&U_{1,1}(\cdot)&\cdots&U_{1,M-1}(\cdot)\\
    \vdots&\vdots&\ddots&\vdots\\
    U_{Q-1,0}(\cdot)&U_{Q-1,1}(\cdot)&\cdots&U_{Q-1,M-1}(\cdot)\\
\end{bmatrix}=
\begin{bmatrix}
    U_{j,i}(\cdot)
\end{bmatrix}_{j\in [0,Q),i\in [0,M)}
\Leftarrow
\begin{bmatrix}
    Q\\
    M
\end{bmatrix}
$$

$$
V=
\begin{bmatrix}
    V_{0,0}(\cdot)&V_{0,1}(\cdot)&\cdots&V_{0,Q-1}(\cdot)\\
    V_{1,0}(\cdot)&V_{1,1}(\cdot)&\cdots&V_{1,Q-1}(\cdot)\\
    \vdots&\vdots&\ddots&\vdots\\
    V_{M-1,0}(\cdot)&V_{M-1,1}(\cdot)&\cdots&V_{M-1,Q-1}(\cdot)\\
\end{bmatrix}=
\begin{bmatrix}
    V_{i,j}(\cdot)
\end{bmatrix}_{i\in [0,M),j\in [0,Q)}
\Leftarrow
\begin{bmatrix}
    M\\
    Q
\end{bmatrix}
$$

$$
V_{i,j}(a)\sim  N(\mu,\sigma^2)
$$

对第$i$个指标，若其范围是$[{a_i}_{min},{a_i}_{max}]$

设函数$q(l,r,\mu,\sigma)=\frac{1}{2}erf(\frac{x-\mu}{\sqrt{2}\sigma})\lvert_l^r$

则

$$
\frac{q({l_i}_{suit},{r_i}_{suit},\mu_i,\sigma)}{q({a_i}_{min},{a_i}_{max},\mu_i,\sigma)}=ts
$$

可将$\sigma$解出

加入面积修正后

$$
V_{i,j}(a)=\frac{1}{\sqrt{2\pi}q({a_i}_{min},{a_i}_{max},\mu_i,\sigma)\sigma}\exp(-\frac{(x-\mu)^2}{2\sigma^2})
$$

$$
W=
\begin{bmatrix}
    w_0\\
    w_1\\
    \vdots\\
    w_{M-1}
\end{bmatrix}\Leftarrow
\begin{bmatrix}
    M\\
\end{bmatrix}
$$

$$
A(t)=
\begin{bmatrix}
    A_0(t)\\
    A_1(t)\\
    \vdots\\
    A_{N-1}(t)
\end{bmatrix}\Leftarrow
\begin{bmatrix}
    N\\
\end{bmatrix}
$$

$$
A(t)=
\begin{bmatrix}
    \frac{
        \begin{bmatrix}
        V_{i,{type}_k}(a_{{pos}_k,i}(t))
        \end{bmatrix}_{i\in [0,M)}
        \times W^T}{M}
\end{bmatrix}_{k\in [0,N)}
$$

$$
\frac{d{a}_{pos,i}(t)}{dt}
={A(t)}^T\times 
\begin{bmatrix}
    U_{{type}_k,i}(pos_k,pos)
\end{bmatrix}_{k\in [0,N)}
$$

$$
a(0)=a_0
$$

$$
S=
\begin{bmatrix}
    S_0(t)\\
    S_1(t)\\
    \vdots\\
    S_Q-1(t)
\end{bmatrix}
$$

$$
P(r,T,a_0,W)=\int_0^T(rh_1(t)+(1-r)h_2(t)){A(t)}^T\times
\begin{bmatrix}
    S_{{type}_k}(t)
\end{bmatrix}_{k\in [0,N)}
dt
$$

# 摘要

针对本问题我们将采取分块模拟的方法，将此区域进行栅格化，并从多方面，包括但不限于卫星云图，地形图，植被覆盖率与人口人口分布，采集了对设施生产、环境变化等产生影响的指标，建立了其与设施活性的微分关系，并采取差分法在时间尺度上对微分方程进行求解。对方程的解进行加权积分，得到了用于评价建设方案价值的指标。在这个过程中，我们将环境自身作用与建设方案自身互作用等效替代，仅考虑环境与生产的互作，对环境变化进行了定量评估；对短期和长期利益进行加权，得以满足决策者对不同经济效益的需求；对不同环境指标进行加权，以满足决策者对环境保护的不同需求

此模型具有良好的可扩展性、重构与解耦的能力。经敏感度分析与扩展性分析，此模型可用于不同地区，不同不同建设需求，可以随决策者的政策要求与区域特点进行调整。

在此评价标准之上，我们设想了一种建设方案，并采取此评价标准对其进行评估，将评估结果进行归一化，以分数的形式量化了决策者的建设方案。同时，基于此评估标准，我们提出了针对此地区每一地块建设方案的最佳选择，为决策者的建设提供了参考