from State import State


class Matrix:

    FILE_CONTENT = './resultado.txt'
    NUMBER_PRECISION = 4

    def get_matrix(self):
        with open(Matrix.FILE_CONTENT, 'r') as file:
            text = file.readlines()
            states = [line.strip().split() for line in text]
            matrix = [State(state[0], state[1], state[2]) for state in states]
            return matrix

    def update_matrix(self, matrix: list[State]):
        with open(Matrix.FILE_CONTENT, "w") as file:
            new_states = ""
            for state in matrix:
                new_states += f'{round(state.left, Matrix.NUMBER_PRECISION)} {round(state.right, Matrix.NUMBER_PRECISION)} {round(state.jump, Matrix.NUMBER_PRECISION)}\n'
            file.write(new_states)


if __name__ == "__main__":
    matrix_loader = Matrix()
    matrix = matrix_loader.get_matrix()
    matrix[0].left = 1
    matrix_loader.update_matrix(matrix)
