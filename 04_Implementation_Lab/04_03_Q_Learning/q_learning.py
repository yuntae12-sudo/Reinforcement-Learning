from gridworld_env import GridWorldEnv
import random

env = GridWorldEnv()

q_table = {}

for row in range(env.rows):
    for col in range(env.cols):
        state = (row, col)

        q_table[state] = [0.0, 0.0, 0.0, 0.0]

epsilon = 0.1

def choose_action(state):
    if random.random() < epsilon:
        action = random.randint(0, 3)
        print("Exploration:", action)

    else:
        q_values = q_table[state]

        max_q = max(q_values)

        best_actions = []

        for action in range(4):
            if q_values[action] == max_q:
                best_actions.append(action)

        action = random.choice(best_actions)

        print("Exploitation:", action)

    return action


state = (0, 0)

for _ in range(20):
    choose_action(state)