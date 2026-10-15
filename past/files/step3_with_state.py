"""
==========================================================
  Step 3 (10→90): 発送枠の管理を入れて、業務ロジックを完成させる
==========================================================
  前のステップからの変化:
    + 状態① shipment_counts を追加 (日付×商品番号 → 予約済み個数)
    + ORDER で容量チェックを行い、超過なら拒否する
    + CANCEL で予約数を元に戻す

  これで「正しい答え」が出るようになる。
  ただしまだ全部 main() の中にベタ書き。
  Step 4 でクラスに整理する。
==========================================================
"""
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

    # ===========================================================
    # ★ 状態① (NEW): 日付 × 商品番号 → 予約済み個数
    #   shipment_counts["2022-01-02"]["AAAAA"] = 3  のように使う
    # ===========================================================
    shipment_counts = defaultdict(lambda: defaultdict(int))

    # ★ 状態②: 受理済み注文 (Step 2 と同じ)
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
                parts = lines[pos].split()
                pos += 1
                items.append((parts[0], int(parts[1])))

            # ★ 容量チェック (NEW)
            #   「1種類でも超えたらダメ」→ 全部チェックして1つでもアウトなら拒否
            can_accept = True
            for product_id, qty in items:
                if shipment_counts[ship_date][product_id] + qty > m:
                    #代入はしてない。
                    can_accept = False
                    break

            if can_accept:
                # ★ 枠を予約する (NEW)
                for product_id, qty in items:
                    shipment_counts[ship_date][product_id] += qty
                    #条件にあったら足す。
                active_orders[order_id] = {
                    "ship_date": ship_date,
                    "items": items,
                }
                print(f"{timestamp} Ordered {order_id}")
            else:
                print(
                    f"{timestamp} Ordered {order_id} "
                    "Error: the number of available shipments has been exceeded."
                )

        # -------------------------------------------------------
        # CANCEL
        # -------------------------------------------------------
        elif command == "CANCEL":
            order_id = lines[pos].split()[0]; pos += 1

            order = active_orders.pop(order_id)

            # ★ 枠を解放する (NEW)
            for product_id, qty in order["items"]:
                shipment_counts[order["ship_date"]][product_id] -= qty

            print(f"{timestamp} Canceled {order_id}")

        # -------------------------------------------------------
        # SHIP
        # -------------------------------------------------------
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
