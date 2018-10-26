{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.3 再起プログラミング\n",
    "ある関数から自分自身を呼び出すことを，再帰呼び出しという。  \n",
    "文字列を再帰的に書き換えて成長させるプログラムを書いてみよう。\n",
    "\n",
    "f,g,hの文字列のうち，\n",
    " \n",
    "- f -> fg\n",
    "- g -> gh\n",
    "- h -> gf\n",
    "\n",
    "となるようにする。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fXgXhfg\n",
      "fXgXh\n",
      "fXgXhgh\n",
      "fXgXh\n",
      "fXgXhgf\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'fXgXhgf'"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def grow(s, r):  # 文字列sと繰り返し回数rを入力\n",
    "    ss = ''  # 出力する文字列を初期化\n",
    "    #文字列を一文字ずつ取り出してループする\n",
    "    for letter in s:\n",
    "        if letter == 'f':\n",
    "            ss = s + 'fg'\n",
    "        elif letter == 'g':\n",
    "            ss = s + 'gh'\n",
    "        elif letter == 'h':\n",
    "            ss = s + 'gf'\n",
    "        else:\n",
    "            ss = s \n",
    "        r = r - 1\n",
    "        print(ss)\n",
    "        if r > 0 :\n",
    "            ss = s\n",
    "    # ' f'  を ' fg'  に書き換え\n",
    "    # ' g'  を ' gh'  に書き換え\n",
    "    # hをgfに書き換え\n",
    "    # 残りの繰返し回数を1減らす\n",
    "    # 繰返し回数が0でない時，自分自身を呼び出す\n",
    "    return ss\n",
    "grow('fXgXh', 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "fXgXhfg\n",
      "fXgXh\n",
      "fXgXhgh\n",
      "fXgXh\n",
      "fXgXhgf\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'fXgXhgf'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "grow('fXgXh', 4)  # growを2回実行"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 二次元図形の入れ子\n",
    "文字列は1次元。  \n",
    "次にturtleを用いて，2次元図形が入れ子になったものを描こう。  \n",
    "\n",
    "## turtle graphic\n",
    "https://docs.python.org/ja/3.6/library/turtle.html?highlight=turtle#module-turtle  \n",
    "https://www.101computing.net/2d-shapes-using-python-turtle/\n",
    "\n",
    "## 建築の例\n",
    "例えば，伊東豊雄＋セシル・バルモンド ＜サーペンタインギャラリーパビリオン＞（2002）。  \n",
    "http://www.toyo-ito.co.jp/WWW/Project_Descript/2000-/2000-p_08/2000-p_08_j.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from turtle import *  # 描画環境 turtle をインポート"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "点群を読み込んで，それをつないで描画する関数。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def connect_points(points):\n",
    "    up()\n",
    "    setpos(points[-1][0], points[-1][1])\n",
    "    down()\n",
    "    for xy in points:\n",
    "        setpos(xy[0], xy[1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "n角形の頂点群座標を返す関数。描画はしない。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def n_polygon(n=4, x0=0, y0=0, size=100):\n",
    "    angle = 360 / n\n",
    "    up()\n",
    "    setpos(x0, y0)\n",
    "    points = []\n",
    "    for i in range(n):\n",
    "        forward(size)\n",
    "        left(angle)\n",
    "        points.append(pos())\n",
    "    return points"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "値p0と値p1をrで内分する点を返す関数と，座標p0と座標p1について同じことをする関数。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def deviding(p0, p1, r):\n",
    "    # 書く\n",
    "    return "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# deviding_point(点A,点B,内分比)\n",
    "def deviding_point(p0, p1, ratio):\n",
    "    # 書く\n",
    "    return [xr, yr]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "さらに多角形の各辺を内分してその頂点群を返す関数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# deviding_points(多角形の４頂点，内分比)\n",
    "def deviding_points(points, ratio):\n",
    "    new_points = []\n",
    "    points2 = points[:] #コピーを作成\n",
    "    points2.append(points2[0])\n",
    "    points2.pop(0)\n",
    "    for p0, p1 in zip(points, points2):\n",
    "        書く\n",
    "    return new_points"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "再帰呼び出し関数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def rose_window_recursion(points, ratio, depth):\n",
    "    connect_points(points)\n",
    "    new_points = deviding_points(points, ratio)\n",
    "    if depth == 0:\n",
    "        up()\n",
    "        setpos(-200, -200)\n",
    "    else:\n",
    "        rose_window_recursion(new_points, ratio, depth - 1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "それでは実行してみよう。最初に`n_polygon`関数でn角形の頂点座標を取り出し，それを読み込んで再帰的に描画して行こう。  \n",
    "turtleはブラウザの外の画面で実行されます。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'n_polygon' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-77f535b6c087>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mpoints\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mn_polygon\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mn\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0msize\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m200\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mrose_window_recursion\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpoints\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m0.1\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m40\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mdone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'n_polygon' is not defined"
     ]
    }
   ],
   "source": [
    "points = n_polygon(n=5, size=200)\n",
    "rose_window_recursion(points, 0.1, 40)\n",
    "done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
