#key 以上の最小のindexを返す
#「条件を満たす最小の index」を返す処理は、Python 標準ライブラリの bisect でも書けます
a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]

def is_ok(index,key):#二部探索の質問部分の条件判定関数
    return a[index] >= key

def binary_search(key):
    left = -1 #配列のもう一個左
    right = len(a) #配列のもう一個右

    while right-left > 1: #条件の境目が分かるまで 
        mid = (left + right) // 2
        if is_ok(mid,key):
            right = mid
        else:
            left = mid

    return right