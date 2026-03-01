class Calculator:
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """
        Multiply two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of a and b.
        """
        return float(a) * float(b)
    
    @staticmethod
    def calculate_total(*args) -> float:
        """
        Calculate sum of the given list of numbers.
        Handles both *args and a single list argument.
        """
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            return sum(float(item) for item in args[0])
        return sum(float(item) for item in args)
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        Calculate daily budget

        Args:
            total (float): Total cost.
            days (int): Total number of days

        Returns:
            float: Expense for a single day
        """
        return total / days if days > 0 else 0
    
    