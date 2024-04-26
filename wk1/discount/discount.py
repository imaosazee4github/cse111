import datetime

def get_current_day_of_week():
    return datetime.datetime.now().weekday()

def get_subtotal():
    subtotal = 0
    
    while True:
        price = input("Enter the price (enter 0 to quit):")
        if price == '0':
            break
        quantity = int(input("Enter the quantity:"))
        subtotal += float(price) * quantity
        return subtotal
    
def calculate_discount(subtotal):
        if get_current_day_of_week() in [1, 2] and subtotal >= 50:
            discount_amount = subtotal * 0.10
            print(f"Distount amount: {discount_amount:.2f}")
            return discount_amount
        else:
            return 0
        
def calculate_sales_tax(subtotal):
        return subtotal * 0.06
    
def main():
        subtotal = get_subtotal()
        discount_amount = calculate_discount(subtotal)
        sales_tax = calculate_sales_tax(subtotal)
        total_amount = subtotal - discount_amount + sales_tax
        print(f"Sales tax Amount: {sales_tax:.2f}")
        print(f"Total Amount: {total_amount:.2f}")
        
        if discount_amount == 0 and get_current_day_of_week() in [1, 2]:
            additional_amount = 50 - subtotal
            print(f"Add ${additional_amount:.2f} to your cart to get 10% discount")
            
if __name__ == "__main__":
    main()
        
     