#create bank.py functins deposit(amount), withdraw(amount), and get_balance() add docstrings. generate documentation using pydoc and export it as an HTML file
class BankAccount:
    """
    A class representing a bank account with basic functionalities to deposit, withdraw, and check balance.

    Attributes:
    balance (float): The current balance of the bank account.
    """

    def __init__(self):
        """Initialize the bank account with a balance of 0."""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the bank account.

        Parameters:
        amount (float): The amount to be deposited. Must be a positive number.

        Raises:
        ValueError: If the amount is not a positive number.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the bank account.

        Parameters:
        amount (float): The amount to be withdrawn. Must be a positive number and less than or equal to the current balance.

        Raises:
        ValueError: If the amount is not a positive number -or exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount

    def get_balance(self):
        """
        Get the current balance of the bank account.

        Returns:
        float: The current balance of the bank account.
        """
        return self.balance

# --- Pytest Test Cases ---
import pytest

def test_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0.0

def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100.0

def test_withdraw():
    account = BankAccount()
    account.deposit(100)
    account.withdraw(30)
    assert account.get_balance() == 70.0

def test_deposit_invalid_amount():
    account = BankAccount()
    with pytest.raises(ValueError, match="Deposit amount must be a positive number."):
        account.deposit(-50)

def test_withdraw_invalid_amount():
    account = BankAccount()
    account.deposit(100)
    with pytest.raises(ValueError, match="Withdrawal amount must be a positive number."):
        account.withdraw(-20)

def test_withdraw_insufficient_funds():
    account = BankAccount()
    account.deposit(50)
    with pytest.raises(ValueError, match="Insufficient funds for withdrawal."):
        account.withdraw(100)

# Example usage
if __name__ == "__main__":
    account = BankAccount()
    account.deposit(100)
    print("Balance after deposit of $100:", account.get_balance())
    account.withdraw(30)
    print("Balance after withdrawal of $30:", account.get_balance())