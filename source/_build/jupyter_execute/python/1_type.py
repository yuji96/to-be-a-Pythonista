#!/usr/bin/env python
# coding: utf-8

# # 1. 型と変数

# ## 1.1.  Hello, World!

# In[1]:


print("Hello, World!")


# これは「`"Hello, World"` という文字列を表示するプログラム」で、最も単純かつ有名なプログラムです。よく、初心者向けの教材の 1 ページ目や動作確認などで登場します。この教材もその慣習に則ってみました。
# 
# まず、このとても単純なコードの仕組みを理解しましょう。
# - `print` : これは **丸括弧** 内のものを表示する **関数 (function)** です。
# - `"Hello, World"` : これは **文字列 (string)** です（当たり前）。ダブルクォーテーション or シングルクォーテーション (`" or '`) で囲まれた文字列は、プログラム内でも文字列として扱われます。
#   
# なので、`print("Hello, World")` は「`"Hello, World"` という文字列を表示する」ことができるのです。

# ```{note}
# `print` とは「**丸括弧** 内のものを表示する」という処理に対する名前、つまり、**関数名** です。身近なことで例えると、「箸で米を掴んで口の中に入れて噛んで飲み込む」という一連の動作を「食べる」と名付けて大雑把にすることで世の中は便利になっています。（例えたことでむしろ困惑させてたらごめん）。
# ```
# 
# ```{tip}
# これは僕の憶測ですが、Python の文法はきれいに書くと英文法に近くなります。`print("Hello, World!")` は、そのまま「Print "Hello, World!"」と解釈することができ、あなたが Python に「"Hello, World!" と表示しろ！」と命令しているのです。
# ```
# 

# ## 1.2. 型 (type)

# プログラミングには **型 (type)** という考え方があります。さっき出てきた 文字列 も型の一つです。簡単に言うとプログラミングで扱うことができる概念の種類みたいなものです。百聞は一見にしかずということで、色々と見てみましょう。

# ```{tip}
# たまには「そういうものだ」ということにして分かるようになってから戻ってくることも大事。
# ```

# In[2]:


print("文字列", "文字列だよ", type("文字列だよ"))
print("整数", 12345, type(12345))
print("小数 (浮動小数点数)", 3.141592, type(3.141592))


# In[3]:


print("リスト", [1, 2, 3], type([1, 2, 3]))
print("タプル", (1, 2, 3), type((1, 2, 3)))
print("集合", {1, 2, 3}, type({1, 2, 3}))


# In[4]:


print("辞書", {"one": 1, "two": 2}, type({"one": 1, "two": 2}))


# In[5]:


print("真偽値", True, type(True))
print("真偽値", False, type(False))
print("None", None, type(None))


# In[6]:


# 知らなくても生きていける
print("バイト列", b"not string", type(b"not string"))
print("複素数", 1+1j, type(1+1j))


# これは **文字列 (string)** です。

# 

# In[7]:


print("Hello, World!")


# ノート
# 
# `print` は

# In[8]:


def f():
    pass

type(f)


# In[9]:


print(1 + 2)
print(3 - 4)
print(5 * 6)
print(7 / 8)


# In[10]:


print(4 // 2)
print(4 // 3)
print(4 % 2)
print(4 % 3)

