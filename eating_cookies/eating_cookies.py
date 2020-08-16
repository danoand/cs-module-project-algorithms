'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Basic Scenarios+---
    if n == 0:
        return 0

    if n == 1:
        return 1

    if n == 2:
        # 1. Eat 2 cookies
        # 1. Eat 1 cookie and then 1 cookie
        return 1 + 1

    if n == 3:
        return 4

    ctr = 1
    ctr = ctr + eating_cookies(3) + eating_cookies(n-3)
    ctr = ctr + eating_cookies(2) + eating_cookies(n-2)

    return ctr

print(eating_cookies(10))

