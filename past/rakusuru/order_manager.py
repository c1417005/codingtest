"""通販サイト注文管理システム"""

import sys
from collections import defaultdict
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# データモデル
# ---------------------------------------------------------------------------

@dataclass
class Order:
    """受理済み注文 1 件を表す。"""

    order_id: str                        # 注文番号 (長さ10の英大文字)
    ship_date: str                       # 発送日 (yyyy-MM-dd)
    items: list[tuple[str, int]]         # [(商品番号, 個数), ...]


# ---------------------------------------------------------------------------
# 発送枠管理
# ---------------------------------------------------------------------------

class ShipmentTracker:
    """日付 × 商品番号 ごとの発送予約数を管理し、受理可否を判定する。"""

    def __init__(self, capacity: int):
        self._capacity = capacity        # 1日あたりの商品ごとの発送可能数 M
        # counts[日付][商品番号] = その日の予約済み個数
        self._counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))

    def can_accept(self, date: str, items: list[tuple[str, int]]) -> bool:
        """items を追加しても全商品が発送可能数 M 以下に収まるか判定する。"""
        for product_id, qty in items:
            if self._counts[date][product_id] + qty > self._capacity:
                return False
        return True

    def reserve(self, date: str, items: list[tuple[str, int]]) -> None:
        """発送枠を予約する（注文受理時）。"""
        for product_id, qty in items:
            self._counts[date][product_id] += qty

    def release(self, date: str, items: list[tuple[str, int]]) -> None:
        """発送枠を解放する（注文取消時）。"""
        for product_id, qty in items:
            self._counts[date][product_id] -= qty


# ---------------------------------------------------------------------------
# 注文管理（業務ロジック）
# ---------------------------------------------------------------------------

class OrderManager:
    """受理済み注文を保持し、ORDER / CANCEL / SHIP の各業務を実行する。"""

    def __init__(self, capacity: int):
        self._tracker = ShipmentTracker(capacity)
        self._active_orders: dict[str, Order] = {}   # 注文番号 → Order

    # -- ORDER ---------------------------------------------------------------

    def process_order(self, timestamp: str, order_id: str,
                      ship_date: str, items: list[tuple[str, int]]) -> None:
        if self._tracker.can_accept(ship_date, items):
            self._tracker.reserve(ship_date, items)
            self._active_orders[order_id] = Order(order_id, ship_date, items)
            print(f"{timestamp} Ordered {order_id}")
        else:
            print(
                f"{timestamp} Ordered {order_id} "
                "Error: the number of available shipments has been exceeded."
            )

    # -- CANCEL --------------------------------------------------------------

    def process_cancel(self, timestamp: str, order_id: str) -> None:
        order = self._active_orders.pop(order_id)
        self._tracker.release(order.ship_date, order.items)
        print(f"{timestamp} Canceled {order_id}")

    # -- SHIP ----------------------------------------------------------------

    def process_ship(self, timestamp: str) -> None:
        ship_date = timestamp.split("T")[0]

        shipped_ids = sorted(
            oid for oid, o in self._active_orders.items()
            if o.ship_date == ship_date
        )
        for oid in shipped_ids:
            del self._active_orders[oid]

        print(f"{timestamp} Shipped {len(shipped_ids)} Orders")
        print(" ".join(shipped_ids))


# ---------------------------------------------------------------------------
# 入力パーサ
# ---------------------------------------------------------------------------

class QueryParser:
    """標準入力の行リストを先頭から順に読み進め、
    パースした結果を OrderManager に委譲する。"""

    def __init__(self, lines: list[str]):
        self._lines = lines
        self._pos = 0

    def _next_tokens(self) -> list[str]:
        """現在行をスペース分割で返し、読み取り位置を 1 行進める。"""
        tokens = self._lines[self._pos].split()
        self._pos += 1
        return tokens

    # -- ヘッダ読み取り -------------------------------------------------------

    def parse_header(self) -> OrderManager:
        """1〜4 行目を読み取り、OrderManager を生成して返す。"""
        n, m, d = map(int, self._next_tokens())       # N M D
        product_ids = self._next_tokens()              # A_1 ... A_N
        ship_flags = list(map(int, self._next_tokens()))  # H_1 ... H_7
        num_queries = int(self._next_tokens()[0])      # Q
        return OrderManager(capacity=m)

    # -- クエリ読み取り・実行 -------------------------------------------------

    def run_all(self, manager: OrderManager) -> None:
        """残りの行を先頭から順にパースし、1 クエリずつ即時実行する。"""
        while self._pos < len(self._lines):
            tokens = self._next_tokens()
            command, timestamp = tokens[0], tokens[1]

            if command == "ORDER":
                self._handle_order(manager, timestamp)
            elif command == "CANCEL":
                self._handle_cancel(manager, timestamp)
            elif command == "SHIP":
                manager.process_ship(timestamp)

    def _handle_order(self, manager: OrderManager, timestamp: str) -> None:
        info = self._next_tokens()                     # B C K
        order_id, ship_date, k = info[0], info[1], int(info[2])

        items: list[tuple[str, int]] = []
        for _ in range(k):
            parts = self._next_tokens()                # X_i Y_i
            items.append((parts[0], int(parts[1])))

        manager.process_order(timestamp, order_id, ship_date, items)

    def _handle_cancel(self, manager: OrderManager, timestamp: str) -> None:
        order_id = self._next_tokens()[0]              # B
        manager.process_cancel(timestamp, order_id)


# ---------------------------------------------------------------------------
# エントリポイント
# ---------------------------------------------------------------------------

def main() -> None:
    lines = [line.rstrip("\r\n") for line in sys.stdin]
    parser = QueryParser(lines)
    manager = parser.parse_header()
    parser.run_all(manager)


if __name__ == "__main__":
    main()
