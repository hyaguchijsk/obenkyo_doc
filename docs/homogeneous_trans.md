# 同次座標変換行列

並進と回転を一つの行列で表す方法

## 同次座標形式

このページでは右手座標系としベクトルは列ベクトルであらわす．
同次座標形式では方向ベクトルと位置ベクトルを区別するための符号を最後に付加する．
変換行列を掛けることで座標変換の合成ができるため，定式化をしやすい．

## 変換行列の性質

回転行列の行列式は
右手座標系では常に1になり，
左手座標系では常に-1になる．
一番最後の要素（4行4列目）は常に1になる．

## 実装形態

システムや分野によって異なる．

- 工学では列ベクトル，右手座標系がもっとも一般的．
- OpenGLは行ベクトル，右手座標系．
- DirectXは行ベクトル，左手座標系．

## 変換

### 変換行列の変換

\[
{^0 T _1} {^1 T _2} =
\begin{bmatrix}
^0 R _1 & ^0 t _1 \\
0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
^1 R _2 & ^1 t _2 \\
0 & 1 \\
\end{bmatrix}
=
\begin{bmatrix}
{^0 R _1}{^1 R _2} & {^0 t _1}+{^0 R _1}{^1 t _2} \\
0 & 1 \\
\end{bmatrix}
= {^0 T _2}
\]

### 位置ベクトルの変換
\[
{^0 T _1} ^1 P =
\begin{bmatrix}
^0 R _1 & ^0 t _1 \\
0 & 1 \\
\end{bmatrix}
\begin{bmatrix}
^1 p \\
 1 \\
\end{bmatrix}
=
\begin{bmatrix}
{^0 t _1}+{^0 R _1}^1 p \\
1 \\
\end{bmatrix}
= {^0 P}
\]



## 逆変換=逆行列

その性質上逆行列は乗算のみで記述できる．

\[
\begin{bmatrix}
R & t \\
0 & 1 \\
\end{bmatrix}
^{-1}
=
\begin{bmatrix}
R^T & -R^T t \\
0 & 1 \\
\end{bmatrix}
\]


## 三次元における基本的な回転行列

### x,y,z各軸の回転行列

\[
RotX( \phi ) =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos \phi & - \sin \phi \\
0 & \sin \phi & \cos \phi
\end{bmatrix}
\]

\[
RotY( \theta ) =
\begin{bmatrix}
\cos \theta & 0 & \sin \theta \\
0 & 1 & 0 \\
- \sin \theta & 0 & \cos \theta
\end{bmatrix}
\]

\[
RotZ( \psi ) =
\begin{bmatrix}
\cos \psi & - \sin \psi & 0 \\
\sin \psi & \cos \psi & 0 \\
0 & 0 & 1
\end{bmatrix}
\]
