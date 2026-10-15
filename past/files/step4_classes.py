"""
==========================================================
  Step 4 (90→100): クラスに整理する
==========================================================
  前のステップからの変化:
    + 状態① (shipment_counts)  → ShipmentTracker クラスに切り出し
    + 状態② (active_orders) + 業務判断 → OrderManager クラスに切り出し
    + 入力パース (pos, lines, while ループ) → QueryParser クラスに切り出し
    + 注文データ (辞書)  → Order dataclass に置き換え

  「動き」は Step 3 と全く同じ。出力も同じ。
  変わったのは「どこに何が書いてあるか」だけ。

  なぜ分けるか？
    - ShipmentTracker は「数字の足し引き」だけ知っていればいい
    - OrderManager は「受理するかの判断」だけ知っていればいい
    - QueryParser は「入力の読み方」だけ知っていればいい
    → バグったとき、どこを見ればいいかが明確になる
==========================================================
"""
import sys
from collections import defaultdict
from dataclasses import dataclass


# ===========================================================
# 注文データ: Step 3 では辞書だったものを dataclass にする
#   辞書: {"ship_date": "2022-01-02", "items": [("AAAAA", 1)]}
#   ↓
#   dataclass: Order(order_id="AAA...", ship_date="2022-01-02", items=[...])
#
#   利点: タイポがエラーになる (order.shiip_date → すぐ気づく)
# ===========================================================

@dataclass
class Order:
    order_id: str
    ship_date: str
    items: list[tuple[str, int]]


# ===========================================================
# 状態① を切り出したクラス
#   Step 3 ではこれが main() 内の変数だった:
#     shipment_counts = defaultdict(lambda: defaultdict(int))
#   そこに対する操作 (チェック / 加算 / 減算) をセットにした
# ===========================================================

class ShipmentTracker:
    def __init__(self, capacity):
        self._capacity = capacity
        self._counts = defaultdict(lambda: defaultdict(int))

    def can_accept(self, date, items):
        """Step 3 の can_accept 変数 + for ループをそのまま移動"""
        for product_id, qty in items:
            if self._counts[date][product_id] + qty > self._capacity:
                return False
        return True

    def reserve(self, date, items):
        """Step 3 の「枠を予約する」for ループをそのまま移動"""
        for product_id, qty in items:
            self._counts[date][product_id] += qty

    def release(self, date, items):
        """Step 3 の「枠を解放する」for ループをそのまま移動"""
        for product_id, qty in items:
            self._counts[date][product_id] -= qty


# ===========================================================
# 状態② + 業務判断 を切り出したクラス
#   Step 3 ではこれが main() 内の変数だった:
#     active_orders = {}
#   そこに対する操作 (受理 / 取消 / 発送) をセットにした
# ===========================================================

class OrderManager:
    def __init__(self, capacity):
        self._tracker = ShipmentTracker(capacity)
        self._active_orders = {}

    def process_order(self, timestamp, order_id, ship_date, items):
        """Step 3 の ORDER ブロックをそのまま移動"""
        if self._tracker.can_accept(ship_date, items):
            self._tracker.reserve(ship_date, items)
            self._active_orders[order_id] = Order(order_id, ship_date, items)
            print(f"{timestamp} Ordered {order_id}")
        else:
            print(
                f"{timestamp} Ordered {order_id} "
                "Error: the number of available shipments has been exceeded."
            )

    def process_cancel(self, timestamp, order_id):
        """Step 3 の CANCEL ブロックをそのまま移動"""
        order = self._active_orders.pop(order_id)
        self._tracker.release(order.ship_date, order.items)
        print(f"{timestamp} Canceled {order_id}")

    def process_ship(self, timestamp):
        """Step 3 の SHIP ブロックをそのまま移動"""
        ship_date = timestamp.split("T")[0]
        shipped_ids = sorted(
            oid for oid, o in self._active_orders.items()
            if o.ship_date == ship_date
        )
        for oid in shipped_ids:
            del self._active_orders[oid]
        print(f"{timestamp} Shipped {len(shipped_ids)} Orders")
        print(" ".join(shipped_ids))


# ===========================================================
# 入力パースを切り出したクラス
#   Step 3 では main() 内の pos 変数と while ループだった
#   pos を self._pos にして、行を読む操作をメソッドにした
# ===========================================================

class QueryParser:
    def __init__(self, lines):
        self._lines = lines
        self._pos = 0

    def _next_tokens(self):
        """Step 3 の「tokens = lines[pos].split(); pos += 1」と同じ"""
        tokens = self._lines[self._pos].split()
        self._pos += 1
        return tokens

    def parse_header(self):
        tokens = self._next_tokens()
        n, m, d = int(tokens[0]), int(tokens[1]), int(tokens[2])
        product_ids = self._next_tokens()
        ship_flags = self._next_tokens()
        num_queries = int(self._next_tokens()[0])
        return OrderManager(capacity=m)

    def run_all(self, manager):
        """Step 3 の while ループをそのまま移動"""
        while self._pos < len(self._lines):
            tokens = self._next_tokens()
            command, timestamp = tokens[0], tokens[1]

            if command == "ORDER":
                self._handle_order(manager, timestamp)
            elif command == "CANCEL":
                self._handle_cancel(manager, timestamp)
            elif command == "SHIP":
                manager.process_ship(timestamp)

    def _handle_order(self, manager, timestamp):
        info = self._next_tokens()
        order_id, ship_date, k = info[0], info[1], int(info[2])
        items = []
        for _ in range(k):
            parts = self._next_tokens()
            items.append((parts[0], int(parts[1])))
        manager.process_order(timestamp, order_id, ship_date, items)

    def _handle_cancel(self, manager, timestamp):
        order_id = self._next_tokens()[0]
        manager.process_cancel(timestamp, order_id)


# ===========================================================
# エントリポイント
# ===========================================================

def main():
    lines = [line.rstrip("\r\n") for line in sys.stdin]
    parser = QueryParser(lines)
    manager = parser.parse_header()
    parser.run_all(manager)


if __name__ == "__main__":
    main()
