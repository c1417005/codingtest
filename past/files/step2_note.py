import sys


def main():
    lines = [line.rstrip("\r\n") for line in sys.stdin]
    pos = 0

    # --- ヘッダ読み取り (Step 1 と同じ) ---
    tokens = lines[pos].split(); pos += 1
    n, m, d = int(tokens[0]), int(tokens[1]), int(tokens[2])

    product_ids = lines[pos].split(); pos += 1
    ship_flags = lines[pos].split(); pos += 1
    num_queries = int(lines[pos]); pos += 1

    active_orders = {}

    while pos < len(lines):
        tokens = lines[pos].split()
        pos += 1
        command = tokens[0]
        timestamp = tokens[1]

        if command == "ORDER":
            info = lines[pos].split(); pos += 1
            order_id, ship_date, k = info[0], info[1], int(info[2])

            items = []
            for _ in range(k):
                parts = lines[pos].split(); pos += 1
                items.append((parts[0], int(parts[1])))   

            active_orders[order_id] ={
                    "ship_date" : ship_date,
                    "items" : items,
            }
            #辞書の定義復習。
            print(f"{timestamp} Ordered {order_id}")
        elif command =="CANCEL":
            order_id = lines[pos].split()[0]
            pos += 1

            del active_orders[order_id]
            print(f"{timestamp} Canceled {order_id}")

        elif command == "SHIP":
            ship_date = timestamp.split("T")[0]
            #Tで分ける。（Tは消える。）分かれた後の0番目。（日付のみ必要だから）

            shipped_ids = sorted(
                oid for oid,order in active_orders.items() if order["ship_date"] == ship_date
                #oid を集める。oid,orderをactice_ordersから取り出して。もし予約日が発送日なら。注文日!=予約日        
            )

            for oid in shipped_ids:
                del active_orders[oid]

            print(f"{timestamp} Shipped {len(shipped_ids)} Orders")
            print(" ".join(shipped_ids))  



if __name__ == "__main__":
    main()
