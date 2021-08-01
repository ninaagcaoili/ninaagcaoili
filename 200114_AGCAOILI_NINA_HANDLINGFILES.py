products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]


def get_property(code,property):
    return products[code][property]

def main():

    all_orders={}
    total = 0

    while True:
        order=input("Input order: ") #{product_code},{quantity}
        if order != "/":
            code,quantity=order.split(",")
            product = get_product(code)
            subtotal = int(get_property(code,"price"))*int(quantity)
        else:
            break

        if code in all_orders.keys():
            all_orders[code]["quantity"]+= int(quantity)
            all_orders[code]["subtotal"]+= subtotal
        else:
            all_orders[code] = {
                "name": get_property(code,"name"),
                "quantity" : int(quantity),
                "subtotal" : subtotal
            }

        total += subtotal

    receipt = ""
    all_orders=dict(sorted(all_orders.items()))

    receipt+="== \n"
    receipt+=("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n")



    for i in all_orders:
        details = all_orders.get(i)
        name = details.get("name")
        quantity = details.get("quantity")
        subtotal = details.get("subtotal")
        receipt+=(f"{i}\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}\n")

    receipt += (f'Total:\t\t\t\t\t\t\t\t\t\t{total}\n')
    receipt += "=="



    with open("receipt.txt","w") as f:
        f.write(receipt)

main()
