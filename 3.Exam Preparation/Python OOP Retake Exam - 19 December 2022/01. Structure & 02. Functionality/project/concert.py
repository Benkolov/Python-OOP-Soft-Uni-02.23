class Concert:
    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    def __str__(self):
        return f"{self.genre} concert at {self.place}."
