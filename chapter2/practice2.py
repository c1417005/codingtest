times = [i for i in range(1,6)]

def nth_power_calc_of_n(t:int,n:int) -> int:
    num = 1
    for _ in range(t):
        num *= n

    return num

def main():
    for i in times:
        print(f"n = {i} の時：{nth_power_calc_of_n(i,3) - nth_power_calc_of_n(i,2)}")

main()