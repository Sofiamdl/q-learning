from connection import connect, get_state_reward
from Matrix import Matrix

class GameController:

    def __init__(self):
        self.__matrix_loader = Matrix()
        self.__start_connection_with_qlearning_app()

    
    def __start_connection_with_qlearning_app(self):
        self.__socket = connect(2037)
        self.__

    def start_controller(self):
        matrix = self.__matrix_loader.get_matrix()
        
        while True:
            print("interação com o rolê")



if __name__ == "__main__":
    gameController = GameController()
    gameController.start_controller()
