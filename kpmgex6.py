'''
Solve this task with recursive programming.
In this exercise you have to find how much cookies
can be consumed with the given amount of money.

money: Starting money, to spend for cookies
price: Price of the cookie
wrap: Number of wrappers to be returned for getting one extra cookie.
It may be assumed that all given values are positive integers and greater than 1.

Example:
Input: money = 16, price = 2, wrap = 2
Output:   15
Price of a cookie is 2. You can buy 8 cookies from
amount 16. You can return 8 wrappers back and get 4 more
cookies. Then you can return 4 wrappers and get 2 more
cookies. Finally you can return 2 wrappers to get 1
more cookie.
'''


# Returns maximum number of
# chocolates we can eat with
# given money, price of chocolate
# and number of wrapprices
# required to get a chocolate.
def countMaxChoco(money, price, wrap):
    if (money < price):
        return 0

    # First find number of chocolates
    # that can be purchased with the
    # given amount
    choc=int(money / price)

    # Now just add number of
    # chocolates with the chocolates
    # gained by wrapprices
    choc=choc + (choc - 1) / (wrap - 1)
    return int(choc)

money=16
price=2
wrap=2

print(countMaxChoco(money, price, wrap))