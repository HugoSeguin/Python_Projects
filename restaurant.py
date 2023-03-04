#Function as a restaurant with menu and price practice
def restaurant():
    total = 0
    while True:
        order = input('Order : ').strip

    if not order:
        break
    if order in MENU:
        price = MENU(order)
        total += price
        print(f'{order} is {price}, total is {total} ')
restaurant