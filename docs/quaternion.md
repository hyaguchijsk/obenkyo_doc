# クォータニオン

「四元数」とも呼ばれる．
三次元回転をコンパクトに表現できる，補間がやりやすいなどの利点があるが，
結局同次座標変換行列に落とさないと使えなかったりする．
直感的でないという最大の欠点がある．



## 回転を表すクォータニオン

普通のクォータニオンは

\[q = (w \ V) = (w \ x \ y \ z)\]

とかあらわされる．\(V = (x \ y \ z)\)は虚部．

回転を表すクォータニオンの場合，大きさが1のクォータニオンとなる．
回転量を\( \theta \),回転軸を\( (n_x \ n_y \ n_z) \)としたとき，これをあらわすクォータニオンは

\[ (\cos \theta /2 \ \ n_x \sin \theta /2 \ \ n_y \sin \theta /2 \ \ n_z \sin \theta /2) \]

当然，全要素の符号を反転させても同じ回転を表現できる．
なお，

\( -q = (-w \ -V) = (-w \ -x \ -y \ -z) \)これは同じ回転を意味し

\( q^{-1} = (w \ -V) = (w \ -x \ -y \ -z) \)これは逆回転を意味する


## 基本的な演算

クォータニオンの乗算の定義は

\[ \begin{align*}
q_0 q_1 &= ( w_0 \ V_0 ) ( w_1 \ V_1) = (w_0 \ x_0 \ y_0 \ z_0) (w_1 \ x_1 \ y_1 \ z_1) \\
 &= (w_0 w_1 - V_0 \cdot V_1  \ \ w_0 V_1 + w_1 V_0 + V_0 \times V_1 ) \\
 &= \left( \begin{array}{c} w_0 w_1 - x_0 x_1 - y_0 y_1 - z_0 z_1 \\ w_0 x_1 + x_0 w_1 + y_0 z_1 - z_0 y_1 \\ w_0 y_1 + y_0 w_1 + z_0 x_1 - x_0 z_1 \\ w_0 z_1 + z_0 w_1 + x_0 y_1 - y_0 x_1 \\ \end{array} \right) ^T
 \end{align*} \]

ちなみに

\[ V_0 \cdot V_1 = x_0 x_1 + y_0 y_1 + z_0 z_1 \]

\[ V_0 \times V_1 = (y_0 z_1 - z_0 y_1 \ \ z_0 x_1 - x_0 z_1 \ \ x_0 y_1 - y_0 x_1) \]


回転を表すクォータニオンを合成するときは単純に乗算すればよい．


クォータニオンaをbで回転させてクォータニオンcをつくる場合．

\[ c = b^{-1} a b \]

コーディングの際にはたぶん展開しても簡単にならないと思うので素直に乗算で組んでしまうのがいいと思う．



## 他の表現との変換

### 回転行列の作り方

右手座標列ベクトル形式として，

\[
\begin{bmatrix}
1-2y^2-2z^2 & 2xy-2wz & 2xz+2wy \\
2xy+2wz & 1-2x^2-2z^2 & 2yz-2wx \\
2xz-2wy & 2yz+2wx & 1-2x^2-2y^2 \\
\end{bmatrix}
\]


### 回転行列からの作り方

回転行列の各要素を以下のように表す．

\[
\begin{bmatrix}
r_{11} & r_{12} & r_{13} \\
r_{21} & r_{22} & r_{23} \\
r_{31} & r_{32} & r_{33} \\
\end{bmatrix}
\]

試しに対角要素を全部足してみると．

\[
r_{11} + r_{22} + r_{33} \\
= (1-2y^2-2z^2) + (1-2x^2-2z^2) + (1-2x^2-2y^2) \\
= 3 - 4 (x^2 + y^2 + z^2)
\]

定義から，\( w^2 + x^2 + y^2 + z^2 = 1 \)であるので，
\((x^2 + y^2 + z^2) = (1 - w^2)\)ということは，

\[
r_{11} + r_{22} + r_{33} = 4w^2 - 1
\]
したがって，
\[
w = \frac{\sqrt{1 + r_{11} + r_{22} + r_{33}}}{2}
\]

として，同様に対角成分の加減算で\(x, y, z\)も求めることができる．

\[\begin{align*}
x &= \pm \frac{\sqrt{1 + r_{11} - r_{22} - r_{33}}}{2} \\
y &= \pm \frac{\sqrt{1 - r_{11} + r_{22} - r_{33}}}{2} \\
z &= \pm \frac{\sqrt{1 - r_{11} - r_{22} + r_{33}}}{2}
\end{align*}\]

ただし符号判定の必要がある
(定義に戻ると-180度から180度の範囲でwは正だがx,y,zは不定)
ため，
実際の計算の際は対角以外の要素を使って判定していくことになる．

# axis-angle

回転量を\( \theta \),回転軸を\(r = (n_x \ n_y \ n_z)\)としたとき

\[ q_a = (\theta, r) = (\theta, (n_x \ \ n_y \ \ n_z)) \]

回転の合成は直接計算では得ることができない．
クォータニオンとの変換は簡単なのでそこを経由するとよい．

## 変換

回転行列への変換はRodoriguesの公式を使う．

\[
R = \cos \theta I_3 + (1- \cos \theta) r r^T + \sin \theta
\begin{bmatrix}
0 & -n_z & n_y \\
n_z & 0 & -n_x \\
-n_y & n_x & 0
\end{bmatrix}
\]

## 逆変換

\[
\sin \theta
\begin{bmatrix}
0 & -n_z & n_y \\
n_z & 0 & -n_x \\
-n_y & n_x & 0
\end{bmatrix}
= \frac{R-R^T}{2}
\]



# 対数クォータニオン:exponential map

OpenCVでは「回転ベクトル」と呼ばれている．
回転軸＊回転角度で表される．三次元．

\[ q_e = (\theta n_x \ \ \theta n_y \ \ \theta n_z) \]

こうすることで，

\[ q_0 \times q_1 \approx \exp ( \ln (q_0) + \ln (q_1)) \]

ということらしい．

表現形式は文献，実装によって異なるようだが最終的に座標変換がうまくいっていれば問題はない？
DirectXでは

\[ \ln (w V) = (0 \ \ (\phi / \sin \phi ) V) , \phi = \cos ^{-1} w \]




# 参考文献

- 四元数で回転 入門
    - [http://staff.aist.go.jp/toru-nakata/quaternion.html](http://staff.aist.go.jp/toru-nakata/quaternion.html)
- F. Dunn, I. Parberry, 松田晃一:「実例で学ぶゲーム3D数学」，オライリージャパン．
    - [http://www.oreilly.co.jp/books/9784873113777/](http://www.oreilly.co.jp/books/9784873113777/)
- カメラキャリブレーションと3次元再構成
    - [http://opencv.jp/opencv-2svn/cpp/camera_calibration_and_3d_reconstruction.html](http://opencv.jp/opencv-2svn/cpp/camera_calibration_and_3d_reconstruction.html)
- 3D空間における回転の表現形式 - TMPSwiki
    - [http://www.tmps.org/index.php?3D%B6%F5%B4%D6%A4%CB%A4%AA%A4%B1%A4%EB%B2%F3%C5%BE%A4%CE%C9%BD%B8%BD%B7%C1%BC%B0#ya68a83d](http://www.tmps.org/index.php?3D%B6%F5%B4%D6%A4%CB%A4%AA%A4%B1%A4%EB%B2%F3%C5%BE%A4%CE%C9%BD%B8%BD%B7%C1%BC%B0#ya68a83d)
- クォータニオン逆運動学 - TMPSwiki
    - [http://mukai-lab.org/wp-content/uploads/2014/04/QuaternionInverseKinematics.pdf](http://mukai-lab.org/wp-content/uploads/2014/04/QuaternionInverseKinematics.pdf)
    - [http://www.tmps.org/index.php?%A5%AF%A5%A9%A1%BC%A5%BF%A5%CB%A5%AA%A5%F3%B5%D5%B1%BF%C6%B0%B3%D8#ra10d054](http://www.tmps.org/index.php?%A5%AF%A5%A9%A1%BC%A5%BF%A5%CB%A5%AA%A5%F3%B5%D5%B1%BF%C6%B0%B3%D8#ra10d054)
- その58 やっぱり欲しい回転行列⇔クォータニオン相互変換
    - [http://marupeke296.com/DXG_No58_RotQuaternionTrans.html](http://marupeke296.com/DXG_No58_RotQuaternionTrans.html)
