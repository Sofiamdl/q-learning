from connection import connect, get_state_reward
from Matrix import Matrix
from QAgent import QAgent

class GameController:

    def __init__(self):
        self.__matrix_loader = Matrix()
        self.__agent = QAgent()
        self.__start_connection_with_qlearning_app()

    
    def __start_connection_with_qlearning_app(self):
        self.__socket = connect(2037)

    def start_controller(self):
        matrix = self.__matrix_loader.get_matrix()
        last_state = '000000'

        while True:
            action = self.__agent.get_action(matrix, last_state)
            state, reward = get_state_reward(self.__socket, action)
            matrix = self.__agent.q_algorithm(matrix, state, last_state, action, reward)
            last_state = state
            self.__matrix_loader.update_matrix(matrix)

if __name__ == "__main__":
    gameController = GameController()
    gameController.start_controller()
