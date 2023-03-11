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
a=
\begin{bmatrix}
    \begin{bmatrix}
        a_{(0,0),0}(\cdot)\\
        \vdots\\
        a_{(0,0),M-1}(\cdot)\\
    \end{bmatrix}&
    \cdots&
    \begin{bmatrix}
        a_{(0,maxy-1),0}(\cdot)\\
        \vdots\\
        a_{(0,maxy-1),M-1}(\cdot)\\
    \end{bmatrix}&\\
    \vdots&\ddots&\vdots\\
    \begin{bmatrix}
        a_{(maxx-1,0),0}(\cdot)\\
        \vdots\\
        a_{(maxx-1,0),M-1}(\cdot)\\
    \end{bmatrix}&
    \cdots&
    \begin{bmatrix}
        a_{(maxx-1,maxy-1),0}(\cdot)\\
        \vdots\\
        a_{(maxx-1,maxy-1),M-1}(\cdot)\\
    \end{bmatrix}
\end{bmatrix}
\begin{bmatrix}
    \begin{bmatrix}
        a_{(x,y),i}(\cdot)\\
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
    A_0(\cdot)\\
    A_1(\cdot)\\
    \vdots\\
    A_{N-1}(\cdot)
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
