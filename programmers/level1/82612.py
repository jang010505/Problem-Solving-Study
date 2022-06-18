def solution(price, money, count):
    return max(0, (price+price*count)*count//2-money)