class PlatformState:

    def __init__(self, left, right, jump):
        self.left = left
        self.right = right
        self.jump = jump

class Matrix:

    def get_matrix(self):
        with open('./resultado.txt', 'r') as file:
            text = file.readlines()
            states = [line.strip().split() for line in text]
            platforms = [PlatformState(state[0], state[1], state[2]) for state in states]
            return platforms

    def update_matrix(self):
	    with open("./resultado.txt", "r") as file:
		    pass

if __name__ == "__main__":
    matrix = Matrix()
    matrix.get_matrix()