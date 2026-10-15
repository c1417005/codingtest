import sys
class OrderManager:
    def __init__(self,capacity: int):
        self.tracker = ShipmentTracker(capacity)
        self._active_orders: dict[str,Order] = {}

def process_order(self,timestamp: str,order_id : str,
                  ship_date: str,items: list[tuple[str,int]]):
    if self._tracker.can_accept(ship_date,items):
        self._tracker.reserve(ship_date)
        self._avtive_orders[order_id] = Order(order_id,ship_date,items)
    

class QueryParser:
    def __init__(self,lines:list[str]):
        self._lines = lines
        self._pos = 0
    
    def _next_tokens(self) -> list[str]:
        tokens = self._lines[self._pos].split()
        self._pos += 1
        return tokens

    def parse_header(self) -> OrderManager:
        n,m,d = map(int,self._next_tokens())
        product_ids =self._next_tokens()
        ship_flags = list(map(int,self._next_tokens()))
        num_queries = int(self._next_tokens()[0])#これなぜ
        return OrderManager(capacity = m)





def main() -> None:
    # lines = [line.rstrip("\r\n") for line in sys.stdin]
    sample_lines = [
        "3 5 2",
        "AAAAA BBBBB CCCCC",
        "1 1 1 1 1 1 1",
        "1",
    ]

    parser = QueryParser(sample_lines)
    
    print(parser._next_tokens())
    print(parser._next_tokens())
    print(parser._next_tokens())


if __name__ == "__main__":
    main()