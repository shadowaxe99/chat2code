from AmorphicAgent import AmorphicAgent


def main():
    # Create an instance of the amorphic agent
    amorphic_agent = AmorphicAgent()

    # Interact with the user
    while True:
        user_input = input('Enter your message: ')
        amorphic_agent.interact(user_input)


if __name__ == '__main__':
    main()