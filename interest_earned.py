#Charles Ajjan, CMP131, week 4, Lab 1, interest ernered, started on 09/10/2026
Principal = float(input("Enter the principal amount: "))
Rate = float(input("Enter the Monthly interest rate (as a percentage): "))
compounding_period = int(input("Enter the compounding periods per months"))
Rate_decimal = Rate / 100
Final_amount = Principal * (1 + (Rate_decimal / compounding_period)) ** (compounding_period )
Interest_earned = Final_amount - Principal
print("Principal", Principal)
print("Rate", Rate)
print(f"{Rate}")
print("compounding_period", compounding_period)
print(f"\nFinal Amount: ${Final_amount:.2f}")
print(f"Interest Earned: ${Interest_earned:.2f}")