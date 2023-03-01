from connection import connect, get_state_reward

class GameController:

    def __init__(self):
        self.__start_connection_with_qlearning_app()

    
    def __start_connection_with_qlearning_app(self):
        self.__socket = connect(2037)
        state, reward = get_state_reward(self.__socket, "jump")
        print(state, reward)

    def start_controller(self):
        pass


if __name__ == "__main__":
    gameController = GameController()
    gameController.start_controller()
