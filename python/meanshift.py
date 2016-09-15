#!/usr/bin/env python
# coding: UTF-8

import matplotlib.pyplot as plt
import math
import random

def create_dataset():
    dat = []
    params = [(5.0, 1.0), (10.0, 1.5), (15.0, 1.0)]
    for p in params:
        for i in range(100):
            dat.append(random.gauss(p[0], p[1]));
    return dat

def proc_meanshift(dat, sigma = 1.0):
    sqsigma = sigma * sigma
    sdat = range(20)
    for j in range(10):
        for i in range(len(sdat)):
            sdat[i] = update_sample(sdat[i], dat, sqsigma)
    return sdat


def update_sample(sample, dat, sqsigma):
    kj = 0.0
    kjd = 0.0
    for d in dat:
        dif = sample - d
        k = math.exp(-0.5 * (dif * dif / sqsigma))
        kj = kj + (k * d)
        kjd = kjd + k
    return kj / kjd


def plot_dataset(dat):
    daty = [-0.5] * len(dat)
    plt.scatter(dat, daty)
    plt.hist(dat)
    plt.show()

# usage:
#
## 以下のようにすると便利
# ipython qtconsole --pilab=inline
# import meanshift
#
## 5, 10, 15を中心として正規乱数を生成
# dat = meanshift.create_dataset()
#
## 元の分布データを表示して確認
# meanshift.plot_dataset(dat)
#
## 1.0おきに配置したサンプルを平均シフトを使って移動
# sdat = meanshift.proc_meanshift(dat)
#
## 同様に表示して結果を確認
# meanshift.plot_dataset(sdat)
#
