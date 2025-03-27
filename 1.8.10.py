# Loan Interest and Amortization Calculator

def calculate_interest(loan_amount, interest_rate):
    """Calculate the annual interest cost."""
    return loan_amount * (interest_rate / 100)

def calculate_amortization_schedule(loan_amount, interest_rate, years, payments_per_year):
    """Generate an amortization schedule."""
    schedule = []
    remaining_balance = loan_amount
    total_payments = years * payments_per_year
    payment_amount = loan_amount / total_payments

    for payment_number in range(1, total_payments + 1):
        interest_cost = calculate_interest(remaining_balance, interest_rate) / payments_per_year
        remaining_balance -= payment_amount
        if remaining_balance < 0:
            remaining_balance = 0
        schedule.append({
            "Payment Number": payment_number,
            "Interest Cost": round(interest_cost, 2),
            "Principal Payment": round(payment_amount, 2),
            "Remaining Balance": round(remaining_balance, 2)
        })
    return schedule

def print_amortization_schedule(schedule):
    """Print the amortization schedule as a table."""
    print(f"{'Payment':<10}{'Interest':<15}{'Principal':<15}{'Remaining Balance':<20}")
    print("-" * 60)
    for entry in schedule:
        print(f"{entry['Payment Number']:<10}{entry['Interest Cost']:<15}{entry['Principal Payment']:<15}{entry['Remaining Balance']:<20}")

def main():
    print("Welcome to the Loan Interest and Amortization Calculator!")
    loan_amount = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the number of years for the loan: "))
    payments_per_year = int(input("Enter the number of payments per year (e.g., 12 for monthly, 4 for quarterly): "))

    # Calculate and display the amortization schedule
    schedule = calculate_amortization_schedule(loan_amount, interest_rate, years, payments_per_year)
    print("\nAmortization Schedule:")
    print_amortization_schedule(schedule)

if __name__ == "__main__":
    main()