#!/usr/bin/env python
# coding: utf-8

# # 2. 数

# プログラミングといえば計算です。そのためにまず数を扱えるようになりましょう。

# ## 2.1. 整数

# まずは最も単純な数である **整数 (int)** です。ただ数値をそのまま書くだけで定義できます。

# In[1]:


print("整数", 12345, type(12345))
print("負の数", -12345, type(-12345))


# `<class 'int'>` は integer の略です。

# ## 2.2. 実数（浮動小数点数）

# 次は **実数 (float)** です。これは小数のように小数点を含んだ数値を書くことで定義できます。  
# また、[指数表記（E表記）](https://ja.wikipedia.org/wiki/%E6%8C%87%E6%95%B0%E8%A1%A8%E8%A8%98) $m \times 10^n$ も使用できます。
# float は桁数に応じて表示がそのままだったり指数表記になったりします。
# 

# In[2]:


print("小数", 3.141592, type(3.141592))
print("指数表記", -1.23e-3, type(-1.23e-3))
print("アボガドロ定数", 602214076000000000000000.0, type(602214076000000000000000.0))
print("int は省略されない", 602214076000000000000000, type(602214076000000000000000))


# `<class 'float'>` は数値を表現するアルゴリズムである **浮動小数点方式** の浮動 (floating) からきています。
# 
# ```{tip}
# 簡単に言うと `1.23` と `12.3` はそれぞれ「`123` の百の位」と「`123` の十の位」に小数点 (`.`) を入れたものと内部では処理されています。このように小数点が上に浮かんだり下に沈んだりすることから flaot と呼ばれています。
# ```

# ## 2.3. 複素数（番外編）

# `j` を虚数単位として `a+bj` と書くことで複素数を定義することができます。使う機会が少ないので説明は割愛します。
# 何らかの実装をミスして $\sqrt{~~}$ の中身をマイナスにしてしまったり、音声データや生体データ処理でフーリエ変換を使ったりすると再会するかもしれません。

# In[3]:


print("複素数", 1+1j, type(1+1j))


# ## 2.4. 演算

# 数同士の演算は `a + b` のように 2 つの数字の間に算術演算子 (operator) をはさむことで表現されます（最後の符号は例外ですが）。
# Python では次のような算術演算子があります。

# In[4]:


print("足し算: 1 + 2 =", 1 + 2)
print("引き算: 3 - 4 =", 3 - 4)
print("掛け算: 5 * 6 =", 5 * 6)
print("割り算: 7 / 8 =", 7 / 8)
print("商: 15 // 6 =", 15 // 6)
print("剰余: 15 % 6 =", 15 % 6)
print("累乗: 2**10 =", 2**10)
print("符号: -1 =", -1)


# 割り算についての補足です。
# - **Python の**割り算の計算結果は float 型になります（`int / int -> float`）
# - 割り切れる場合でも float 型になります
# - 商と剰余が欲しい場合は `//` と `%` を使用します
# - ゼロで割るとエラー（`ZeroDivisionError`）が発生して、実行が中断されます。
# 
# $15 = 6 * 2 + 3$

# In[5]:


print("割り切れる場合: 9 / 3 =", 9 / 3)
print("割り切れない場合: 15 / 6 =", 15 / 6)
print("商: 15 // 6 =", 15 // 6)
print("剰余: 15 % 6 =", 15 % 6)
print("ゼロ除算: 9 / 0 =", 9 / 0)


# ```{tip}
# 言語によって割り算の扱いは異なります。
# - C 言語 では小数部分が切り捨てられ `7 / 8 -> 0` となる。
# - Mathematica では分数を扱うことができるので `7/8` は計算せずそのまま `7/8` となる。
# ```
# 
# > かなり昔にイージス巡洋艦ヨークタウンは、ゼロ除算が原因で2時間半航行不能になったことがある。
# > [ヨークタウン](https://ja.wikipedia.org/wiki/%E3%83%A8%E3%83%BC%E3%82%AF%E3%82%BF%E3%82%A6%E3%83%B3_(%E3%83%9F%E3%82%B5%E3%82%A4%E3%83%AB%E5%B7%A1%E6%B4%8B%E8%89%A6))

# ここで数を int ではなく float にすると少し結果が変わります。（`1.0` のように小数部分が `0` の場合は `1.` のように省略することができます。）

# In[86]:


print("足し算: 1. + 2. =", 1. + 2.)
print("引き算: 3. - 4. =", 3. - 4.)
print("掛け算: 5. * 6. =", 5. * 6.)
print("割り算: 7. / 8. =", 7. / 8.)
print("商: 15. // 6. =", 15. // 6.)
print("剰余: 15. % 6. =", 15. % 6.)
print("累乗: 2.**10. =", 2.**10.)
print("符号: -1. =", -1.)


# 何が変わったか分かりましたか？正解は、返り値も int から float に変わりました。
# 
# ```{admonition} Quiz
# 一方を int にしてもう一方を float にするとどうなるでしょうか。
# ```

# ちなみに、累乗 $a^n$ の指数 $n$ は正の整数ではなく、ゼロ・負の数・実数にすることもできます。
# 
# $$
# a^{0} = 1 ,~~ a^{-n} = \dfrac{1}{a^n} ,~~ a^{1/n} = \sqrt[n]{a}
# $$

# In[88]:


print("ゼロ乗は常に 1: 2**0 =", 2**0)
print("マイナス n 乗は分母の n 乗: 2**-1 =", 2**-1)
print("1/n 乗は n 重根（つまり、1/2 乗は平方根）: 2**0.5 =", 2**0.5)


# $n$ が float 型のときに $a$ が負の数だと結果が複素数になることがあります。（早い再開でしたね。）
# 
# $$
# (-a)^{1/2} = \sqrt{-a} = \sqrt{a}j
# $$

# In[62]:


(-1)**0.5


# ```{tip}
# $\sqrt{-1} = 1j$ ですが、厳密に `1j` とはなりませんでした。プログラミングは精度に限界があり厳密解を求められないのでよくあることです。
# `6.123...e-17` はほぼゼロなので今回は許してあげてください。
# 
# 話が脱線しますが、このような計算誤差を減らして精度の良い近似解を得ることを目的とした [数値解析](https://ja.wikipedia.org/wiki/%E6%95%B0%E5%80%A4%E8%A7%A3%E6%9E%90) という分野があります。もしこの数式が木星に飛んでいくロケットの中にあったら無視してはいけないかもしれません。
# ```

# ## 2.5. 計算順序

# 掛け算と割り算が足し算と引き算よりも先ってやつですが、もう一度整理しておきましょう。
# 
# |順序|演算子|解釈|例|
# |:-:|:-|:-|-|
# |1|`()`|括弧|`(1 + 2) * 3 = 9`|
# |2|`**`|累乗|`-3 ** 2 = -9`|
# |3|`-`|符号|
# |4|`*, /, //, %`|掛け算、割り算、商、剰余|`1 + 2 * 3 = 7`|
# |5|`+, -`|足し算、引き算|

# では、$x^2 - 2x - 15 = 0$ を解の公式を用いて解いてみましょう。

# $$
# x_1 = \dfrac{-b - \sqrt{b^2 - 4ac}}{2a}, ~~ x_2 = \dfrac{-b + \sqrt{b^2 - 4ac}}{2a}
# $$

# In[89]:


(-(-2) - ((-2)**2 - 4*1*(-15))**0.5) / (2 * 1)


# In[90]:


(-(-2) + ((-2)**2 - 4*1*(-15))**0.5) / (2 * 1)


# $x^2 - 2x - 15 = (x+3)(x-5)$ なので正解ですが、コードがごちゃごちゃしてて見ずらいですね。
# これでは「$2x^2 + 4x - 17 = 0$ も解け」と言われたらまた似たコードを書かなきゃいけないのか…という億劫な気持ちになります。
# 
# 次の章ではコードを一回限りではなく使い回せるような工夫をしていきます。
# 
