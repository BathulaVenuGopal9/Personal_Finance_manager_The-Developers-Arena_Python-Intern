class Expense:
    def __init__(self, amount, category, date, description):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def to_list(self):
        """Convert expense object to list (for CSV saving)"""
        return [self.date, self.category, self.amount, self.description]

    def __str__(self):
        """Readable format when printing expense"""
        return f"{self.date} | {self.category} | ₹{self.amount:.2f} | {self.description}"

