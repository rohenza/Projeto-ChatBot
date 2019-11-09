import State
class Order:
    def __init__(self):
        self.searchList = {}
        self.name = ""
        self.total = 0
        self.games = []
        self.state = State.SearchState()

    def answer(self, text):
        self.state = self.state.answer(text)

def __main__():
    order = Order()
    print("Hello! What do you want to?")
    answer = input("")

    while(order.state is not None):
        order.answer(answer)

        answer = input("")




