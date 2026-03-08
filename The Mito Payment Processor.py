## The Mito Payment Processor

def mito_payment(func):
    def wrapper(*args,**kwargs):
        price = args[0]
        currency = args[1]
        if currency.upper() != "PHP":
            print("ERROR: Only PHP accepted!")
            return None
        else:
            discounted_price = price * 0.90
            print(f"LOG: Applying 10% discount. New total: {discounted_price} PHP")
        return func(discounted_price,currency)
    return wrapper

@mito_payment
def confirm_order(amount, unit):
    return f"Order confirmed for {amount} {unit}"

# Test 1: Should work (1000 - 10% = 900)
print(confirm_order(1000, "PHP"))

# Test 2: Should fail (Wrong currency)
print(confirm_order(50, "USD"))