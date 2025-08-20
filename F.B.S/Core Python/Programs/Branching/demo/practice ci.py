def calculate_compound_interest(principal, rate, time, frequency):
    """
    principal: Initial amount of money
    rate: Annual interest rate in percent
    time: Time in years
    frequency: Number of times interest applied per year
    """
    amount = principal * (1 + rate / (100 * frequency))**(frequency * time)
    return round(amount, 2)

# Example usage
P = 10000      # Principal amount
R = 5          # Interest rate (%)
T = 3          # Time in years
N = 4          # Quarterly compounding

final_amount = calculate_compound_interest(P, R, T, N)
print(f"Compound Interest Amount after {T} years: ₹{final_amount}")