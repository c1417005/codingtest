import sys
from collections import defaultdict

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))

    num_products,daily_shippable_count,max_lead_days = map(int,(lines[0].split()))
    product_ids = [product_id for product_id in lines[1].split()]
    ship_flags = [ship_flag for ship_flag in lines[2].split()]
    num_queries = int(lines[3])

    queries = []
    for q in lines[4:]:
        queries.append(q.rstrip('\r\n').split())
    #queries
    # [['ORDER', '2022-01-01T01:00:00'],
    # ['AAAAAAAAAA', '2022-01-02', '1'],
    # ['AAAAA', '6'], 
    # ['ORDER', '2022-01-01T02:00:00'],
    #...]]
    
    orders = []
    def store_order(queries):
        i = 0
        while i <= len(queries)-1:
            # print(f"len_query{len(queries)}")
            cmd = queries[i]
            if cmd[0] == "ORDER":
                order_time = cmd[1]
                order_id,ship_date,k = queries[i+1]
                kind_orderd_products = int(k)
                items = queries[i+2 : i+2+kind_orderd_products]
                orders.append({
                    'kind_order':cmd[0],
                    'time':order_time,
                    'order_id':order_id,
                    'ship_date':ship_date,
                    'items':items,
                })
                i += 2 + kind_orderd_products
                # print(f"{i}")
            elif cmd[0] == "SHIP":
                ship_time = cmd[1]
                orders.append({
                    'kind_order':cmd[0],
                    'ship_time':ship_time
                })
                i += 1
                # print(f"{i}")
            elif cmd[0] == "CANCEL":
                cancel_time = cmd[1]
                cancel_id = queries[i+1]
                orders.append({
                    'kind_order':cmd[0],
                    'cancel_time':cancel_time,
                    'cansel_id':cancel_id
                })
                i += 2
                # print(f"{i}")
            else:
                break
        
    store_order(queries)

    grouped  = defaultdict(list)
    for entry in orders:
        # print(f"orders:entry = {orders}:{entry}")
        grouped[entry['kind_order']].append(entry)

    


    # print(grouped)
    def process_order(order_list):
        for order in order_list:
            total_shipments = defaultdict(list)
            for k in range(len(order['items'])):
                item_name,num_item = order['items']
                total_shipments[]
            
            for entry  
            B,T = order['order_id'],order['time']
            print(f"{T} Ordered {B}")




    
    def process_cancel(cancel_list):
        for order in cancel_list: 
            B,T = order['cancel_id'],order['cancel_time']
            print(f"{T} Canceled {B}")




    
    def process_ship(ship_list):
        for order in ship_list: 
            T = order['cancel_time']
            print(f"{T} SHipped")
    
        # if orders['ORDER']:
        #     order_list = orders['ORDER']
        #     for order in order_list: 
        #         B,T = order['order_id'],order['time']
        #         print(f"{T} Orderd {B}")
    
    process_order(grouped['ORDER'])




            
                 
            
    

    
    

    # print(queries)


    # def process_order(queries):

    #     if kind_order  == "ORDER":
    #         order_id,shipping_date,num_order = 



    # print(products)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)