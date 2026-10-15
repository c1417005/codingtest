import sys

def main():
    lines = [line.rstrip("\r\n") for line in sys.stdin]
    pos = 0  # 今どの行を読んでいるか

    # -------------------------------------------------------
    # ヘッダを読む (4行)
    # -------------------------------------------------------
    tokens = lines[pos].split()
    pos +=1
    n,m,d = int(tokens[0]),int(tokens[1]),int(tokens[2])
    print(f"[ヘッダ] 商品数={n}, 発送可能数={m}, 最大日数={d}")

    product_ids = lines[pos].split()
    pos += 1
    print(f"[ヘッダ] 商品番号={product_ids}")

    ship_flags = lines[pos].split()
    pos += 1
    print(f"[ヘッダ] 発送フラグ={ship_flags}")

    num_queries = int(lines[pos])
    pos += 1
    print(f"[ヘッダ] クエリ数={num_queries}")

    while pos < len(lines):
        tokens = lines[pos].split()
        pos += 1
        command = tokens[0]
        timestamp = tokens[1]

        if command == "ORDER":
            info = lines[pos].split()
            pos+=1
            order_id = info[0]
            ship_date = info[1]
            k = int(info[2])

            items = []
            for _ in range(k):
                parts = lines[pos].split()
                pos += 1
                items.append((parts[0],int(parts[1])))
            print(f"[ORDER]  時刻={timestamp} 注文番号={order_id} "
                  f"発送日={ship_date} 商品={items}")
        
        elif command == "CANCEL":
            order_id = lines[pos].split()[0]
            pos += 1
            print(f"[CANCEL] 時刻={timestamp} 注文番号={order_id}")

        elif command == "SHIP":
            print(f"[SHIP]   時刻={timestamp}")

if __name__ == "__main__":
    main()