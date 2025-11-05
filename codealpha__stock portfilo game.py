# 🧾 Stock Portfolio Tracker
# Goal: Calculate total investment based on user input and hardcoded stock prices

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "AMZN": 160,   # Amazon
    "MSFT": 370    # Microsoft
}

# Dictionary to store user's stock and quantity
portfolio = {}

print("=== 📊 STOCK PORTFOLIO TRACKER ===")
print("Available stocks:", ', '.join(stock_prices.keys()))

# Get user input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    elif stock not in stock_prices:
        print("❌ Invalid stock symbol! Try again.")
        continue
    quantity = int(input(f"Enter quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
total_investment = 0
print("\n=== 🧮 Portfolio Summary ===")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# --- Optional: Save results to file ---
save_option = input("\nDo you want to save the result? (y/n): ").lower()
if save_option == "y":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("=======================\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print(f"✅ Portfolio saved to {filename}")

print("\n📈 Thank you for using Stock Portfolio Tracker!")
