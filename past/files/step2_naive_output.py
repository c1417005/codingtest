"""
==========================================================
  Step 2 (1→10): 出力の形を作れるか？
==========================================================
  前のステップからの変化:
    + 受理した注文を辞書に保存する (active_orders)
    + ORDER → 常に受理して正式フォーマットで出力
    + CANCEL → 注文を辞書から削除して出力
    + SHIP → その日の注文を探して出力

  このステップで「まだやらないこと」:
    - 発送枠の容量チェック (全部受理してしまう)

  ポイント:
    codingtest.py では ORDER を全部まとめてから処理しようとしていた。
    ここでは「来た順に1つずつ処理する」ことが最大の違い。
    while ループで1クエリずつ読み、すぐ処理・すぐ出力する。
==========================================================
"""
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

    # ===========================================================
    # ★ 状態②: 受理済み注文を保持する辞書
    #   注文番号 → {"ship_date": 発送日, "items": [(商品番号, 個数), ...]}
    # ===========================================================
    active_orders = {}

    # --- クエリを1つずつ、来た順に処理する ---
    while pos < len(lines):
        tokens = lines[pos].split(); pos += 1
        command = tokens[0]
        timestamp = tokens[1]

        # -------------------------------------------------------
        # ORDER: まだ容量チェックなし、全部受理する
        # -------------------------------------------------------
        if command == "ORDER":
            info = lines[pos].split(); pos += 1
            order_id, ship_date, k = info[0], info[1], int(info[2])

            items = []
            for _ in range(k):
                parts = lines[pos].split(); pos += 1
                items.append((parts[0], int(parts[1])))

            # 常に受理 (容量チェックは Step 3 で追加)
            active_orders[order_id] = {
                "ship_date": ship_date,
                "items": items,
            }
            print(f"{timestamp} Ordered {order_id}")

        # -------------------------------------------------------
        # CANCEL: 辞書から削除する
        # -------------------------------------------------------
        elif command == "CANCEL":
            order_id = lines[pos].split()[0]; pos += 1

            del active_orders[order_id]
            print(f"{timestamp} Canceled {order_id}")

        # -------------------------------------------------------
        # SHIP: その日が発送日の注文を探して出力する
        # -------------------------------------------------------
        elif command == "SHIP":
            ship_date = timestamp.split("T")[0]

            # 発送日が一致する注文を、辞書順でソートして取り出す
            shipped_ids = sorted(
                oid for oid, order in active_orders.items()
                if order["ship_date"] == ship_date
            )

            # 発送済みなので辞書から消す
            for oid in shipped_ids:
                del active_orders[oid]

            print(f"{timestamp} Shipped {len(shipped_ids)} Orders")
            print(" ".join(shipped_ids))


if __name__ == "__main__":
    main()
