"""
Episode 36: Raising & Custom Exceptions

In this episode you'll learn:
- How and when to raise exceptions
- Designing a small exception hierarchy for your domain
- Chaining exceptions with `from e` and re-raising
- Applying this to a simple BankAccount example
"""

# ------------------------------------------------------------
# 1) Why raise exceptions?
# ------------------------------------------------------------
# Use `raise` to signal invalid inputs or states. Exceptions separate
# error handling from normal control flow and let callers decide how to react.


# ------------------------------------------------------------
# 2) Define a domain exception hierarchy
# ------------------------------------------------------------
class AccountError(Exception):
    """Base class for all account-related errors."""


class InvalidAmountError(AccountError):
    """Raised when an amount is zero, negative, or otherwise invalid."""
    def __init__(self, amount, message="Invalid amount"):
        super().__init__(message)
        self.amount = amount


class OverdraftError(AccountError):
    """Raised when a withdrawal would exceed the available balance."""
    def __init__(self, balance, attempted):
        super().__init__("Overdraft: insufficient funds")
        self.balance = balance
        self.attempted = attempted


# ------------------------------------------------------------
# 3) BankAccount that raises exceptions
# ------------------------------------------------------------
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError(amount, "Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError(amount, "Withdraw must be positive")
        if amount > self.balance:
            raise OverdraftError(self.balance, amount)
        self.balance -= amount
        return self.balance


# ------------------------------------------------------------
# 4) Chaining exceptions with `from e`
# ------------------------------------------------------------
def parse_amount(text: str) -> float:
    """Convert input text to a positive float, raising InvalidAmountError on failure.

    Demonstrates translating a low-level ValueError into a domain error and chaining it.
    """
    try:
        value = float(text)
    except ValueError as e:
        raise InvalidAmountError(text, "Amount must be a number") from e
    if value <= 0:
        raise InvalidAmountError(value, "Amount must be positive")
    return value


def deposit_from_string(acct: BankAccount, text: str):
    amount = parse_amount(text)  # may raise InvalidAmountError (chained from ValueError)
    return acct.deposit(amount)


# ------------------------------------------------------------
# 5) Re-raising to preserve context
# ------------------------------------------------------------
def withdraw_safely(acct: BankAccount, amount: float):
    """Wrap withdraw, log extra context, then re-raise the error."""
    try:
        return acct.withdraw(amount)
    except AccountError as e:
        # Add diagnostic info (Python 3.11+ has add_note; fall back to args otherwise)
        try:
            e.add_note(f"owner={acct.owner}, balance={acct.balance}")
        except AttributeError:
            pass
        # Re-raise the same exception (preserves original traceback)
        raise


# ------------------------------------------------------------
# 6) Demo / Walkthrough
# ------------------------------------------------------------
if __name__ == "__main__":
    print("=== Raising & Custom Exceptions ===")

    acct = BankAccount("Kody", 100.0)
    print("Starting balance:", acct.balance)

    print("-- Valid deposit --")
    acct.deposit(50)
    print("Balance:", acct.balance)

    print("-- Invalid deposit (raises InvalidAmountError) --")
    try:
        acct.deposit(0)
    except InvalidAmountError as e:
        print(f"Caught {e.__class__.__name__}:", str(e), "| amount=", getattr(e, "amount", None))

    print("-- Overdraft (raises OverdraftError) --")
    try:
        acct.withdraw(1000)
    except OverdraftError as e:
        print(f"Caught {e.__class__.__name__}:", str(e), f"| balance={e.balance}, attempted={e.attempted}")

    print("-- Chaining example: deposit_from_string('abc') --")
    try:
        deposit_from_string(acct, "abc")
    except InvalidAmountError as e:
        import traceback
        print(f"Caught {e.__class__.__name__}:", str(e), "| args=", e.args)
        print("Cause type:", type(e.__cause__).__name__ if e.__cause__ else None)
        # Show formatted traceback (includes the chained cause)
        print("\nFormatted traceback with chaining:\n")
        print(traceback.format_exc())

    print("-- Re-raise example: withdraw_safely --")
    try:
        withdraw_safely(acct, 999)
    except AccountError as e:
        print(f"Caught {e.__class__.__name__} after re-raise:", str(e))
        # If running on 3.11+, notes appear in the traceback; show presence if any
        notes = getattr(e, "__notes__", None)
        if notes:
            print("Notes:", notes)

    print("\n=== Try it yourself ===")
    print("1) Add a MinimumBalanceError; prevent balance dropping below a threshold.")
    print("2) Create a transfer(acct_from, acct_to, amount) that raises and rolls back on failure.")
    print("3) Add a parse_currency('$12.34') helper that strips symbols and uses chaining.")
