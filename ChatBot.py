import State
from State import SearchState


def __main__():

    order = State.Order()
    print("Hello! What game would you like to search?")
    answer = input("")

    while order.state is not None:
        order.answer(answer)

        answer = input("")


if __name__ == '__main__':
    __main__()
