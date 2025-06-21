def dynamic_price(base_price, demand, stock):
    if demand == "high" and stock < 20:
        return base_price * 1.5
    elif demand == "low" and stock > 100:
        return base_price * 0.7
    else:
        return base_price

# Test
print(dynamic_price(100, "high", 10))  # Output: 150.0

