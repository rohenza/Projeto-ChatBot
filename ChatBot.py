class Order(Object):
    def __init__(self):
        self.state = SearchInfoState()

    def answer(self, text):
        self.state = self.state.answer(text)

def __main__():
    order = Order()
    print("Hello! What do you want to?")
    answer = input("")

    while(order.state is not None):
        order.answer(answer)

        answer = input("")




