# main.py

from costs.get_total import get_total

def main():
    costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
    items_bought = ['socks', 'shoes']
    tax_rate = 0.09
    
    total = get_total(costs, items_bought, tax_rate)
    print(f"Total cost including tax: ${total}")

if __name__ == "__main__":
    main()
