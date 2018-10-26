{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# コッホ曲線\n",
    "コッホ曲線を描いてみよう。\n",
    "\n",
    "###参考\n",
    "https://ja.wikipedia.org/wiki/%E3%82%B3%E3%83%83%E3%83%9B%E6%9B%B2%E7%B7%9A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle as tl "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 再帰的に描画する関数を描いてみよう。  \n",
    "- 左から右に線を引きたい。\n",
    "- その時に，\n",
    "    - もしdepthが0より大きければ，\n",
    "        - 3分割して真ん中をとがらせた形態にする。\n",
    "        - その時の3分割の線それぞれにもこのルールを適用する。その時にdepthを1減らす。\n",
    "    - もしdepthが0より大きくない時，\n",
    "        - 分割せずに単に線を引く。\n",
    "        \n",
    "ヒント\n",
    "\n",
    "- まず3分割したとがった線（4本の直線）を再帰的でなく描く関数`draw`を書く\n",
    "- その関数の中の直線を描く部分を`draw`で置き換えて再帰的にする。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-4-6385a1413e7b>, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-4-6385a1413e7b>\"\u001b[1;36m, line \u001b[1;32m5\u001b[0m\n\u001b[1;33m    draw(length / 3, depth-1)iwami\u001b[0m\n\u001b[1;37m                                 ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def draw(length, depth):\n",
    "    if depth > 0 :\n",
    "        draw(length / 3, depth-1)\n",
    "        tl.left(60)\n",
    "        draw(length / 3, depth-1)iwami\n",
    "        tl.left(120)\n",
    "        draw(length / 3, depth-1)hotaka\n",
    "        tl.left(60)\n",
    "        draw(length / 3, depth-1)arigato\n",
    "    else:\n",
    "        tl.forward(length)\n",
    "    # 書く"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "では`draw`関数を用いて描いてみよう。\n",
    "引数はlength, depth。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'draw' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-5-9037dbd7fc39>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mtl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdown\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;31m# tl.speed(0)  # 0:fastest, 1:slow to 10:fast\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0mdraw\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m500\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m2\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m \u001b[0mtl\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdone\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'draw' is not defined"
     ]
    }
   ],
   "source": [
    "# tl.tracer(0,0) # no animation\n",
    "tl.up()\n",
    "tl.setx(-250)\n",
    "tl.down()\n",
    "# tl.speed(0)  # 0:fastest, 1:slow to 10:fast\n",
    "draw(500, 2)\n",
    "tl.done()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
