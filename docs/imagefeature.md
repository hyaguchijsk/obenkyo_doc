# 大域特徴

画像全体の特徴を表すもの．


## ツェルニケモーメント

画像に対する回転不変特徴量．
回転および反転には強いが中心がずれるのと拡大縮小には弱い．
ので位置合わせとスケール合わせは重要．

### 定義式

#### ツェルニケ多項式

\[ V_{n,m}(x,y) = V_{n,m}( \rho , \theta ) = r_{n,m}( \rho ) e ^ { j m \theta } \]
\[ \rho=\sqrt{x^2 + y^2}, \theta=\tan ^{-1} (y/x), 0 \le \rho \le 1 , 0 \le \theta \le \pi \]

\[ r_{n,m}( \rho ) = \sum _ {s=0} ^ {(n-|m|)/2} \frac{(-1)^s (n-s)! \rho ^{n-2s}}{s! (\frac{n+|m|}{2}-s)! (\frac{n-|m|}{2}-s)!} \]

ただし\( n > 0, 0 \le |m| \le n, n-|m| \)は偶数

#### ツェルニケモーメント

\( f(x,y) \)を画素値として，
\[ Z_{n,m} = \frac{n+1}{\pi} \sum _x \sum _y f(x,y) V ^* _{n,m} ( \rho , \theta ) \]
\[ x^2 + y^2 \le 1 \]
なので
\[ x \gets x/R, y \gets y/R, R= \sqrt{x^2 + y^2} \]
とする．

ツェルニケモーメントの大きさは回転不変である．
\[ Z_{0,0}, Z_{1,1}, Z_{2,0}, Z_{2,2}, Z_{3,1}, Z_{3,3}, ... \]
あたりまでを使って類似度評価ができる．

### 高速化

ツェルニケ多項式は画素値に依存しないためあらかじめ計算しておくことが可能．

\[\begin{align*}
 r_{0,0} ( \rho ) &= 1 \\
 r_{1,1} ( \rho ) &= \rho \\
 r_{2,0} ( \rho ) &= 2 \rho ^2 - 1 \\
 r_{2,2} ( \rho ) &= \rho ^ 2 \\
 r_{3,1} ( \rho ) &= 3 \rho ^3 -2 \rho \\
 r_{3,3} ( \rho ) &= \rho ^ 3 \\
\end{align*}\]

\( e ^ { j m \theta } \) はm=0のとき常に1．

### 参考文献

- Mukundan, Ramakrishman: "FAST COMPUTATION OF LEGENDRE AND ZERNIKE MOMENTS", Pattern Recoginition, Vol. 28, No. 9, pp. 1433-1442, 1995.
- 杉村，飯国，足立：”ツェルニケモーメントを特徴量とする２次元動的計画法を用いたイメージマッチング”，電子情報通信学会論文誌 D-II Vol. J80-D-II No. 1 pp. 101-108, 1997.


## Tamura features

人間の視神経の特性を考慮した特徴量．

### 特徴量の詳細

以下の六つの要素から特徴ベクトルを構成する．

\[ (f_{crs}, f_{con}, f_{dir}, f_{lin}, f_{reg}, f_{rgh}) \]

#### Coarsness

まず各点の \( 2^n \times 2^n \) サイズの近傍の平均を求める．
1-32あたりまでを使う？
点 \( (x,y) \) の \( 2^k \times 2^k \) 近傍の平均は以下のように求められる．

\[ A_k(x,y) = \sum _{i=x-2^{k-1}} ^{x+2^{k-1}-1} \sum _{i=y-2^{k-1}} ^{y+2^{k-1}-1} f(i,j)/2^{2k} \]

\( f(i,j) \) は点 \( (i,j) \) のグレーレベル．

次に自分の点を中心として対称となる位置にある
重なり合うことの無い領域同士の平均の差分を
各方向において各点で計算する．

水平の場合は
\[ E_{k,h} (x,y) = | A_k(x+2^{k-1},y) - A_k(x-2^{k-1},y) | \]
（？？？何方向くらいいるだろうか？？？）

次に各点において \( E \) を最大化する \( k \) を求め，ベストなウインドウサイズを求める．
\[ S_{best}(x,y)=2^k \]
\[ E_k = E_{max} = \max (E_1,E_2, \cdots E_L) \]
1-Lはkの範囲．

最後に画像中の各ピクセルの\(S_{best}\)の平均をとる．
\[ F_{crs} = (1/(m \times n)) \sum _i ^m \sum _j ^n S_{best}(i,j) \]
m,nは有効な画素範囲を示す．

（？？？Fとfの違いは何？？？）


#### Contrast

コントラストの定義は
\[ f_2 = \sum _n n^2 ( \sum \sum _{|i-j|=n} p(i,j)) \]
\( p(i,j) \) は \( n \times n \) の gray-level spatial dependence matrix
（？？？この上の定義は触れただけで使っていないのでは？？？）

画像中のグレーレベルの分布から
尖度\( \alpha _4 \)を以下のように求める．
\[ \alpha _4 = \mu _4 / \sigma ^4 \]
\( \mu _4 \) は四次モーメント，
\( \sigma ^2 \) は分散，\( \sigma \) は標準偏差．
\[ F_{con} = \sigma / \alpha _4 ^n \]
nは実験的に1/4がよいらしい．


#### Directionality

各画素のエッジのマグニチュードと角度を求める．
\[ | \Delta G | = (| \Delta _H | + | \Delta _V |)/2 \]
\[ \theta = \tan ^{-1} ( \Delta _V / \Delta _H ) + \pi /2 \]
\( \Delta _H , \Delta _V \) はそれぞれ水平，垂直方向のPrewittフィルタをかけた画像．

次にヒストグラム \( H_D \) を求める．

\[ H_D (k) = N _{\theta} (k) / \sum _{i=0} ^{n-1} N _{\theta} (i) \]
kは0から(n-1)まで．
\( N _{\theta} (k) \) は
\( (2k-1) \pi /2n \le \theta < (2k+1) \pi /2n \) 且つ \( | \Delta G | \ge t \)を満たす点の数．

元の文献ではn=16,t=12としている．

ここから \( F_{dir} \) を以下のように求める．
\[ F_{dir} = 1-r n_p \sum _p ^{n_p} \sum _{ \phi \in w_p } ( \phi - \phi _p ) ^2 H_D ( \phi ) \]
\( n_p \) はピークの数，
\( \phi _p \) は \( H_D \) のp番目のピーク，
\( w_p \) はp番目のピークの範囲，
\( r \) は \( \phi \) に関連した正規化要素，
\( \phi \) は0からn-1までの方向をあらわすコード．

ただし，ピークが二つ以上のときは考慮していない．

\[\begin{align*}
 H_D (v_{12}) / H_D ( \phi _2 ) &< 0.5 ,\\
 H_D (v_{21}) / H_D ( \phi _2 ) &< 0.5 ,\\
 H_D ( \phi _2 ) / H_D ( \phi _1 ) &> 0.2
\end{align*}\]
の三条件を満たすなら\( n_p=2 \),そうでないなら\( n_p=1 \).
ここで
\( v_{12} \) はピーク \( \phi _1 , \phi _2 \) の間の極小値の位置．
\( v_{21} \) はピーク \( \phi _2 , \phi _1 \) の間の極小値の位置．

（？？？サイクリックなので成り立つということか？？？）
（？？？二つのピークはどう決めるか？？？）


#### Line-likeness

\[ F_{lin} = \sum _i ^n \sum _j ^n P_{Dd}(i,j) \cos |(i-j)2 \pi / n | / \sum _i ^n \sum _j ^n P_{Dd}(i,j) \]

\( P_{Dd} \) は \( n \times n \)の local direction co-occurrence matrix of points at distance.
ここのnというのはDirectionalityで作ったnと同じ，つまりエッジ勾配の方向を表している．
i,jもエッジ勾配の方向で，つまり画像中の各点において，
ある点pにおける勾配方向がiであったときにその勾配方向にdだけ移動し，
そのときの点qの勾配方向をjとする．これで(i,j)を決定できる．
そのときのp,qにおける勾配の大きさが\( \Delta |G_p| \le t , \Delta |G_q| \le t \)を満たすなら+1．

（？？？ここの解釈は果てしなく怪しい？？？）
（？？？dの決め方についてはd=4でRosenfeldのd4距離関数を使っていると書いてあるように読める？？？）


#### Regularity

上の四つの各特長量の標準偏差から計算する．
\[ F_{reg} = 1-r ( \sigma _{crs} + \sigma _{con} + \sigma _{dir} + \sigma _{lin}) \]
（？？？標準偏差はどうやって計算するの？？？）
（？？？一般的かどうかを見ているということだから複数の画像から出揃ったところで計算するもの？？？）

#### Roughness

Coarsness と Contrast の和．従属変数？
\[ F_{rgh} = F_{crs} + F_{con} \]


### 参考文献
- Tamura, H., Mori, S., & Yamawaki, T. (1978). Textural features corresponding to visual perception. IEEE Transaction on Systems, Man, and Cybernetics, 8(6), 460–472.




# 局所画像特徴(SIFTおよび眷属)

画像のある一点に対する特徴を表すもの．
特にSIFTは回転拡大について不変な特徴量として設計されている．
一方SIFTは特許が取得されており，その回避としてSURFが考案されたが，
そのSURFも特許が取得されていたことが後に判明し，
現在ではその代替となる特徴量も複数提案されている．

## SIFT

Scale Invariant Feature Transformation.
ガウシアンの差分を用いた特徴量．一つの特徴点を128次元の特徴ベクトルであらわす．
まったく異なる時刻，カメラ姿勢において取得された画像同士のマッチングを行うことができる．
考案者により特許が取得されている．

藤吉先生の解説が非常にわかりやすい．
後のSURFやFASTなども解説されている．

[画像局所特徴量と特定物体認識 - SIFTと最近のアプローチ - - 中部大学](http://www.vision.cs.chubu.ac.jp/cvtutorial/PDF/02SIFTandMore.pdf)

### アルゴリズム

以下の3つのプロセスからなる．

- 特徴点検出
- 特徴ベクトル計算
- 特徴点マッチング

SIFT様のアルゴリズムと呼んでいるものはSIFTのアルゴリズムに倣っている．

#### 特徴点検出

Differential of Gaussianをもちいて画像中の特徴点を検出する．
画像を\(1/\sqrt{2}\)倍しながら求めたLaplacian of Gaussianの差分を取りつつ，
その際の拡大率=スケールを差分の極から求めている．

#### 特徴ベクトル計算

特徴点検出の結果得られた座標とスケールを元に画像勾配から点の向きを計算し，
その向きに沿って4x4に分割された窓を決め，
更にそれぞれの窓の中で8方向の勾配のヒストグラムをとる．
つまり4x4x8 = 128次元のヒストグラムが特徴ベクトルとして算出される．

#### 特徴点マッチング

異なる画像間での特徴点対応は，単純にベクトル間の距離でとることができる．


### 参考

- 作者のページ
    - [http://www.cs.ubc.ca/~lowe/keypoints/](http://www.cs.ubc.ca/~lowe/keypoints/)



## SURF

Speeded Up Robust Feature.
SIFTと同様の機能を提供する．
特徴点検出でヘッセ行列を使い，
特徴ベクトル計算にHaar Waveletを使うところがSIFTと異なる．
4x4分割x4次元 = 64次元ベクトルで特徴ベクトルを構成する．

SIFTの特許を回避するために用いることができると目されていたが，
後にSURFも特許が取得されていたことが判明し，大問題となる．

### 参考

- 作者サイト
    - [http://www.vision.ee.ethz.ch/~surf/](http://www.vision.ee.ethz.ch/~surf/)
