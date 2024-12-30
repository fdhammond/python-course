# The situation is as follows: You work at a company where salespeople earn a 13% commission on their total sales,
# and your boss wants you to help the salespeople calculate their commissions by creating a program.
# This program will ask for their name and how much they have sold this month. The program will respond with a
# phrase that includes their name and the amount they are entitled to receive as a commission.

# Questions for user input
user_name = input("What is your name? ")
sales_value = input("How much have you sold this month? ")
sales_value = float(sales_value)

# Function to calculate commission
def calculate_commission(sales):
    """
    Calculate the commission based on sales value.

    Args:
        sales (float): The total sales amount.

    Returns:
        float: The commission earned (13% of sales).
    """
    commision = float(sales) * 0.13
    return round(commision, 2)

# Print the result
print(f"Dear {user_name}, you have earned a commission of ${calculate_commission(sales_value)}")
