from random import randint
from State import State

class QAgent:

    ACTIONS = ["left", "right", "jump"]

    def get_action(self, matrix: list[State], state: str) -> str:
        exploration = randint(0, 10)
        agent_state = int(state, 2)

        if exploration > 7:
            agent_state_value = matrix[agent_state]
            action_value = max(agent_state_value.left, agent_state_value.right, agent_state_value.jump)

            if action_value == agent_state_value.left:
                return "left"
            elif action_value == agent_state_value.right:
                return "right"
            return "jump"

        return QAgent.ACTIONS[randint(0, 2)]

    def q_algorithm(self, matrix: list[State], state: str, last_state: str, action: str, reward: int) -> list[State]:
        q_max = 0
        agent_state = int(state, 2)
        agent_last_state = int(last_state, 2)

        line_state = matrix[agent_state]
        q_max = max(line_state.left, line_state.right, line_state.jump)

        ## 0.1 learning rate
        ## 0.3 discount factor


        if action == "jump":
            matrix[agent_last_state].jump += 0.42 * ((reward + 0.3 * q_max) - matrix[agent_last_state].jump)
        elif action == "left":
            matrix[agent_last_state].left += 0.42 * ((reward + 0.3 * q_max) - matrix[agent_last_state].left)
        else:
            matrix[agent_last_state].right += 0.42 * ((reward + 0.3 * q_max) - matrix[agent_last_state].right)

        return matrix




