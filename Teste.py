from connection import connect, get_state_reward
from Matrix import Matrix
from QAgent import QAgent

class Teste:

    def __init__(self):
        self.__matrix_loader = Matrix()
        self.__agent = QAgent()
        self.__start_connection_with_qlearning_app()

    
    def __start_connection_with_qlearning_app(self):
        self.__socket = connect(2037)

    def start_controller(self):
        print("funcionando")
        matrix = self.__matrix_loader.get_matrix()
        last_state = '0000000'

        while True:

            agent_state = int(last_state, 2)
            agent_state_value = matrix[agent_state]
            action_value = max(agent_state_value.left, agent_state_value.right, agent_state_value.jump)
            print(action_value)
            action = ""
            if action_value == agent_state_value.left:
                action = "left"
            elif action_value == agent_state_value.right:
                action = "right"
            else:
                action = "jump"
            state, reward = get_state_reward(self.__socket, action)
            last_state = state


if __name__ == "__main__":
    gameController = Teste()
    gameController.start_controller()
