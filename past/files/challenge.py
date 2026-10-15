import sys
from collections import defaultdict
# def process_order(ship_date:str,items:list,):

    




def main():
    lines = [line.rstrip("\r\n") for line in sys.stdin]
    pos = 0
    n,m,d = map(int,lines[pos].split())
    pos+=1
    product_id = lines[pos].split()
    pos+=1
    ship_flag = lines[pos].split()
    pos+=1
    query_num = lines[pos][0]
    pos+=1

    accept_orders = defaultdict(int)
    orders = {}

    while pos < len(lines):
        command = (lines[pos].split())[0]
       
        if command == "ORDER":
            T = (lines[pos].split())[1]
            pos +=1
            order_id,ship_date,kind_products = lines[pos].split()
            pos += 1
            
            items = []
            
            for _ in range(int(kind_products)):
                items.append(tuple(lines[pos].split()))
                pos += 1
            
            
            
            # defaultdict(defaultdict(int))がエラー。defaultdictにはcollableを渡す必要がある。
            # defaultdict(int)が先に解決された結果、辞書ができる。これはcollableではない。だからエラー。
            #lambdaで包んでcollableにする必要がある。
            
            for id,qty in items:
                orders[order_id] = ({id:qty})
            
            # print(f"orders: {orders}")
            
                
                
            
            
            
            for pid,num in orders[order_id].items():
                # print(f"pid,num :{pid,num}")
                is_accept = True
                if accept_orders[pid] + int(num) <= m:
                    accept_orders[pid] += int(num)
                    
                else:
                    orders.pop(order_id)
                    is_accept = False
                    
                if is_accept:
                    print(f"{T} Ordered {order_id}")
                else:
                    print(f"{T} Ordered {order_id} Error: the number of available shipments has been exceeded.")
                # print(f"accept_orders: {accept_orders}")
                    

            #      辞書への.appendはできない。代入か、複数一度に追加したいときは.updateを使う
            
            

            
            # print(f"items :{items}")
            
            

            

            
            
            # print(f"{T} Ordered {order_id}")
        
        elif command == "CANCEL":
            T = (lines[pos].split())[1]
            pos += 1
            cancel_id = (lines[pos].split())[0]
            pos += 1

            
            for pid,num in orders[cancel_id].items():
                accept_orders[pid] -= int(num)
                
            orders.pop(cancel_id)   
            print(f"{T} Canceled {cancel_id}")

        elif command == "SHIP":
            T = (lines[pos].split())[1]
            pos += 1
            total = sum(ship_num for ship_num in list(accept_orders.values()))

            print(f"{T} Shipped {total} Orders" )
            # result = ""
            # for ord in orders:
            #     result += ord
            
            print(" ".join([oid for oid in orders]))
        
    # print(accept_orders)
    

if __name__ == "__main__":
    main()
    
