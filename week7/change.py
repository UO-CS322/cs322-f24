def change1(amt):
    """
    A solution to making change given the amount in cents.
    """
    us_coins = {100: "dollar", 25: "quarter", 10: "dime", 5: "nickel", 1: "penny"}
    for coin_val, coin_name in us_coins.items():
        amt = make_change(amt, coin_val, coin_name)
    return

def make_change(total: int, coin_value: int, coin_name: str):
    while total >= coin_value:
        print(f"A {coin_name} ({coin_value})")
        total -= coin_value
    return total