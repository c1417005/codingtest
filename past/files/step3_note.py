import sys
from collections import defaultdict


def main():
    lines = [line.rstrip("\r\n") for line in sys.stdin]
    pos = 0

    # --- ヘッダ読み取り ---
    tokens = lines[pos].split(); pos += 1
    n, m, d = int(tokens[0]), int(tokens[1]), int(tokens[2])

    product_ids = lines[pos].split(); pos += 1
    ship_flags = lines[pos].split(); pos += 1
    num_queries = int(lines[pos]); pos += 1

    shipment_counts = defaultdict(lambda: defaultdict(int))
    #「int()」 は 「0」を返しますので、これは「lambda: 0」と同じ動作になります。
    # つまり「0を返す関数」になりますので、初期値が 0 になるわけです。
# この時点では中身は完全に空です：{}
# pythoncounts["2022-01-02"]
# ここで 外側だけ が反応して defaultdict(int) を作ります：
# python{"2022-01-02": {}}   # 中身はまだ空の辞書
# pythoncounts["2022-01-02"]["AAAAA"]
# ここで 内側だけ が反応して 0 を作ります：
# python{"2022-01-02": {"AAAAA": 0}}
#キーがないから辞書→キーがないから0

    active_orders = {}

    # --- クエリを1つずつ処理する ---
    while pos < len(lines):
        tokens = lines[pos].split(); pos += 1
        command = tokens[0]
        timestamp = tokens[1]

        # -------------------------------------------------------
        # ORDER
        # -------------------------------------------------------
        if command == "ORDER":
            info = lines[pos].split(); pos += 1
            order_id, ship_date, k = info[0], info[1], int(info[2])

            items = []
            for _ in range(k):
                parts = lines[pos].split(); pos += 1
                items.append((parts[0], int(parts[1])))

            can_accept = True
            for product_id,qty in items:
                if shipment_counts[ship_date][product_id] + qty > m:
                    can_accept = False
                    break
            #ネストが深くならないように、条件の判定だけする部分。


            if can_accept:
                #このネストでは条件判定は済んでいるので、ifとかいらない。
                for product_id,qty in items:
                    shipment_counts[ship_date][product_id] += qty

                active_orders[order_id] = {
                    "ship_date" : ship_date,
                    "items":items,
                }
                
                print(f"{timestamp} Ordered {order_id}")
            else:
                print(
                     f"{timestamp} Ordered {order_id} "
                    "Error: the number of available shipments has been exceeded."
                )


        elif command == "CANCEL":
            order_id = lines[pos].split()[0]; pos += 1

            order = active_orders.pop(order_id)
            #CANCELになった注文idの商品を、activeから取り出す。

            for product_id,qty in order["items"]:
                shipment_counts[order["ship_date"]][product_id] -= qty
                #取り消すのでその分戻す。
            
            print(f"{timestamp} Canceled {order_id}")

        elif command == "SHIP":
            ship_date = timestamp.split("T")[0]

            shipped_ids = sorted(
                oid for oid, order in active_orders.items()
                if order["ship_date"] == ship_date
            )
            for oid in shipped_ids:
                del active_orders[oid]

            print(f"{timestamp} Shipped {len(shipped_ids)} Orders")
            print(" ".join(shipped_ids))

        
if __name__ == "__main__":
    main()