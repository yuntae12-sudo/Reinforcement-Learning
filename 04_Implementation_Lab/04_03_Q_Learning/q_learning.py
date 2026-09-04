from gridworld_env import GridWorldEnv

env = GridWorldEnv()

q_table = {}

for row in range(env.rows):
    for col in range(env.cols):
        state = (row, col)

        q_table[state] = [0.0, 0.0, 0.0, 0.0]


for state, q_values in q_table.items():
    print(state, q_values)
