class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        counts = {}
        best = 0
        for row in matrix:
            key = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            # row[0] が 0 ならそのまま、1 なら全ビットを反転する
            counts[key] = counts.get(key, 0) + 1
            if counts[key] > best:
                best = counts[key]
        return best


#     mutable / immutable
# 言葉の意味
# mutable(ミュータブル)= 変更可能。 オブジェクトを作った後、中身を書き換えられる。
# immutable(イミュータブル)= 変更不可。 一度作ったら中身を書き換えられない。

# Python の主な型:

# mutable	immutable
# list, dict, set	int, str, tuple, frozenset
# 実際の挙動

# a = [1, 2, 3]
# print(id(a))   # 2940833128576  ← オブジェクトの識別番号(住所のようなもの)
# a[0] = 99
# print(id(a), a)  # 2940833128576 [99, 2, 3]  ← 住所が同じまま、中身だけ変わった
# id() はオブジェクトの同一性を示す番号。list は同じオブジェクトのまま中身が変わる。これが mutable。


# t = (1, 2, 3)
# print(id(t))   # 2940834807680
# t = t + (4,)
# print(id(t), t)  # 2940834580976 (1, 2, 3, 4)  ← 住所が変わった
# tuple は中身を書き換えられないので、t + (4,) は新しいオブジェクトを作ってそれを t という名前に付け替えている。元の (1,2,3) 自体は一切変わっていない。

# 直接書き換えようとすると拒否される:


# t[0] = 99
# # TypeError: 'tuple' object does not support item assignment
# なぜ dict のキーに immutable が必要か
# dict は「キーからハッシュ値を計算して、その値に対応する場所に値を置く」という仕組みで動いている。ハッシュ値は中身から計算される数値:


# hash((1, 2, 3))   # 529344067295497451
# ここで もし list をキーにできたら何が起きるかを考える。


# key = [1, 2, 3]
# d = {key: "値A"}      # hash([1,2,3]) の場所に格納したとする

# key[0] = 99           # 中身を書き換えた

# d[[99, 2, 3]]         # ← どこを探せばいい?
# 格納したときのハッシュ値と、いま計算されるハッシュ値が違う。格納した値が永久に取り出せなくなる。dict の仕組みが壊れる。

# だから Python は最初から禁止している:


# hash([1, 2, 3])
# # TypeError: unhashable type: 'list'

# d = {}
# d[[1, 2, 3]] = 1
# # TypeError: unhashable type: 'list'
# tuple なら中身が絶対に変わらないので、ハッシュ値も永久に変わらない。安全にキーとして使える。

# 今回のコードで言うと — 各行は list[int]。そのままキーにすると上のエラーで落ちる。tuple(row) で immutable なコピーに変換してからキーにしている。

# そして tuple 同士の比較は中身で行われるので:


# (0,1,1,0) == (0,1,1,0)     # True
# hash((0,1,1,0)) == hash((0,1,1,0))   # True
# 別々の行から作った tuple でも、中身が同じなら dict は同じキーとして扱う。これがグルーピングの正体。

# counts[key] = counts.get(key, 0) + 1 の分解
# 3ステップに分かれている。右辺から評価される。

# ステップ1: counts.get(key, 0)
# dict.get(キー, デフォルト値) は「キーがあればその値を返す、なければデフォルト値を返す」メソッド。


# counts = {"A": 5}

# counts.get("A", 0)   # 5   ← キーがあるので値を返す
# counts.get("B", 0)   # 0   ← キーがないので第2引数の 0 を返す
# counts["B"] と書くとキーがない場合 KeyError で落ちる。.get はそれを避けて「なければ0」という扱いにできる。

# ステップ2: + 1
# ステップ1の結果に1を足す。


# # 初回(まだキーがない)
# counts.get(key, 0) + 1   →   0 + 1   →   1

# # 2回目(すでに1が入っている)
# counts.get(key, 0) + 1   →   1 + 1   →   2
# ステップ3: counts[key] = ...
# 計算結果を key に代入する。キーがなければ新規作成、あれば上書き。

# つなげると

# counts = {}

# # 1回目: key=(0,1,0) が来た
# counts.get((0,1,0), 0)   # → 0   (キーがない)
# 0 + 1                     # → 1
# counts[(0,1,0)] = 1
# # counts = {(0,1,0): 1}

# # 2回目: 同じ key=(0,1,0) が来た
# counts.get((0,1,0), 0)   # → 1   (キーがある)
# 1 + 1                     # → 2
# counts[(0,1,0)] = 2
# # counts = {(0,1,0): 2}

# # 3回目: 別の key=(0,0,1) が来た
# counts.get((0,0,1), 0)   # → 0   (このキーはない)
# 0 + 1                     # → 1
# counts[(0,0,1)] = 1
# # counts = {(0,1,0): 2, (0,0,1): 1}
# 「初回だけ1、以降は+1」という分岐を、1行で書いているだけ。

# if 文で書くとこうなる

# if key in counts:
#     counts[key] = counts[key] + 1
# else:
#     counts[key] = 1