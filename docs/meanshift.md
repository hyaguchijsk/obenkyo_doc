# 平均値シフト法

平均シフト，平均値シフト，ミーンシフト．法がついたりつかなかったり．
Mean shiftをどう訳すかでこうなったと思われる．

## 何をするもの？

何らかの分布が得られた時にそのピークを求める．
クラスタリングにも用いられる．

## アルゴリズム

データがn個あったとして，
まず確率密度分布をカーネル密度推定で近似．

\[ p(x) = 1/n \sum _{i=1} ^n K ( || x- x_i || ^2 / \sigma ^2 ) \]

カーネルはガウス関数なら

\[ K(x) = \exp (-x/2) \]

これをなんやかんやして更新式は次のようになる．

\[ x_i \leftarrow \frac{ \sum _{j=1} ^n K ( || x_i - x_j || ^2 / \sigma ^2 ) x_j }{ \sum _{l=1} ^n K ( || x_i - x_l || ^2 / \sigma ^2 ) } \]

## 注意点

更新式の\( x_i \)については，別に元のデータセットを使う必要はない．
適当に撒いたサンプル点から始まってもちゃんと収束してくれる．
という観点ではパーティクルフィルタに近い．

K-meansのようにクラスタ数を決める必要はないが，
ラベリングか何かは収束後に必要になる．

\( \sigma \) の決め方とイテレーション回数が収束の決め手．
変な値を取ればうまくいかない．


# 参考文献

[http://sugiyama-www.cs.titech.ac.jp/~sugi/2007/Canon-MachineLearning22-jp.pdf](http://sugiyama-www.cs.titech.ac.jp/~sugi/2007/Canon-MachineLearning22-jp.pdf)

「平均シフト」と記述．その他のクラスタリング手法についても．

[http://online.sfsu.edu/~kazokada/research/okada_cvim08_meanshift.pdf](http://online.sfsu.edu/~kazokada/research/okada_cvim08_meanshift.pdf)

「ミーンシフト」と記述．
