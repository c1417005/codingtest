import sys
from collections import defaultdict

def main():
    lines = [line.rstrip("\r\n") for line in sys.stdin]
    pos = 0
    n,m,d = map(int,lines[pos].split()); pos+=1
    product_id = lines[pos].split(); pos+=1
    ship_flag = lines[pos].split(); pos+=1
    query_num = lines[pos][0]; pos+=1

    # ★ 発送日 × 商品 → 予約個数（日付ごとに分ける）
    accept_orders = defaultdict(lambda: defaultdict(int))
    orders = {}   # 注文番号 → {"ship_date":.., "items":[(pid,qty),..]}

    while pos < len(lines):
        command = (lines[pos].split())[0]
        if command == "ORDER":
            T = (lines[pos].split())[1]; pos +=1
            order_id,ship_date,kind_products = lines[pos].split(); pos += 1
            items = []
            for _ in range(int(kind_products)):
                pid, qty = lines[pos].split(); pos += 1
                items.append((pid, int(qty)))

            # ★ 全種チェックしてから受理（1種でも超えたら全拒否、枠も予約しない）
            is_accept = all(accept_orders[ship_date][pid] + qty <= m for pid, qty in items)
            if is_accept:
                for pid, qty in items:
                    accept_orders[ship_date][pid] += qty
                orders[order_id] = {"ship_date": ship_date, "items": items}
                print(f"{T} Ordered {order_id}")
            else:
                print(f"{T} Ordered {order_id} Error: the number of available shipments has been exceeded.")

        elif command == "CANCEL":
            T = (lines[pos].split())[1]; pos += 1
            cancel_id = (lines[pos].split())[0]; pos += 1
            order = orders.pop(cancel_id)
            for pid, qty in order["items"]:
                accept_orders[order["ship_date"]][pid] -= qty
            print(f"{T} Canceled {cancel_id}")

        elif command == "SHIP":
            T = (lines[pos].split())[1]; pos += 1
            ship_date = T.split("T")[0]
            # ★ 発送日が一致する注文だけ、辞書順で
            shipped = sorted(oid for oid, o in orders.items() if o["ship_date"] == ship_date)
            for oid in shipped:
                del orders[oid]   # ★ 消し込み
            print(f"{T} Shipped {len(shipped)} Orders")
            print(" ".join(shipped))

if __name__ == "__main__":
    main()
