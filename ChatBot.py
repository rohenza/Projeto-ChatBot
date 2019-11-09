from State import SearchState
class Order:
    def __init__(self):
        self.searchList = {}
        self.name = ""
        self.total = 0
        self.games = []
        self.game = {}
        self.email = ""
        self.cpf = ""
        self.state = SearchState()

    def answer(self, text):
        self.state = self.state.answer(text)

def __main__(order):
    print("Hello! What game would you like to search??")
    answer = input("")

    while(order.state is not None):
        order.answer(answer)

        answer = input("")

order = Order()

if __name__ == '__main__':
    __main__(order)




