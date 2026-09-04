import random

from gridworld_env import GridWorldEnv


env = GridWorldEnv()

q_table = {}

for row in range(env.rows):
    for col in range(env.cols):
        state = (row, col)
        q_table[state] = [0.0, 0.0, 0.0, 0.0]


epsilon = 0.1
alpha = 0.1
gamma = 0.9


def choose_action(state):
    if random.random() < epsilon:
        action = random.randint(0, 3)

    else:
        q_values = q_table[state]

        max_q = max(q_values)

        best_actions = []

        for action in range(4):
            if q_values[action] == max_q:
                best_actions.append(action)

        action = random.choice(best_actions)

    return action


def update_q_table(state, action, reward, next_state, done):
    current_q = q_table[state][action]

    if done:
        target = reward
    else:
        next_max_q = max(q_table[next_state])
        target = reward + gamma * next_max_q

    new_q = current_q + alpha * (target - current_q)

    q_table[state][action] = new_q


state = env.reset()

action = choose_action(state)

next_state, reward, done = env.step(action)

print("Before:", q_table[state][action])

update_q_table(state, action, reward, next_state, done)

print("After:", q_table[state][action])

print("State:", state)
print("Action:", action)
print("Reward:", reward)
print("Next State:", next_state)