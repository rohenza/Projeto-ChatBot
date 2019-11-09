import State


def __main__():
    print("Hello! What game would you like to search??")
    answer = input("")

    while State.order.state is not None:
        State.order.answer(answer)

        answer = input("")


if __name__ == '__main__':
    __main__()
