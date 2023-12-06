import json


def define(driveway):
    print()

    width = float(input("How wide is your driveway? (in feet) \n"))

    length = float(input("How long is your driveway? (in feet) \n"))

    price = float(input("How much do your materials cost? (per sq ft) \n"))

    area = length * width

    driveway["width"] = width
    driveway["length"] = length
    driveway["area"] = area
    return driveway, price


def calculate_cost(area, price):
    print()

    total_cost = price * area
    total_cost = format(total_cost, ".2f")

    return total_cost


def state_price(total_cost):

    sentence = f"Paving your driveway will cost ${total_cost}."
    print(sentence)

    return sentence



def main():
    driveway = {"width": "", "length": "", "area": "", "total_cost": ""}

    driveway, price = define(driveway)

    cost = calculate_cost(driveway["area"], price)
    driveway["total_cost"] = cost

    state_price(cost)
    
    json_object = json.dumps(driveway, indent=4)

    with open("sample.json", "w+") as f:
         f.write(json_object)

if __name__ =="__main__":
    main()