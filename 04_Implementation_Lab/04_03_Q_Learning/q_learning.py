import random

from gridworld_env import GridWorldEnv


# =========================
# Environment
# =========================

env = GridWorldEnv()


# =========================
# Q-Table
# =========================

q_table = {}

for row in range(env.rows):
    for col in range(env.cols):
        state = (row, col)
        q_table[state] = [0.0, 0.0, 0.0, 0.0]


# =========================
# Hyperparameters
# =========================

epsilon = 0.1
alpha = 0.1
gamma = 0.9

num_episodes = 500
max_steps = 100


# =========================
# Action
# =========================

action_symbols = {
    0: "↑",
    1: "↓",
    2: "←",
    3: "→"
}


# =========================
# ε-greedy Action Selection
# =========================

def choose_action(state):
    # Exploration
    if random.random() < epsilon:
        action = random.randint(0, 3)

    # Exploitation
    else:
        q_values = q_table[state]

        max_q = max(q_values)

        best_actions = []

        for action in range(4):
            if q_values[action] == max_q:
                best_actions.append(action)

        action = random.choice(best_actions)

    return action


# =========================
# Q-Learning Update
# =========================

def update_q_table(state, action, reward, next_state, done):
    current_q = q_table[state][action]

    if done:
        target = reward

    else:
        next_max_q = max(q_table[next_state])
        target = reward + gamma * next_max_q

    new_q = current_q + alpha * (target - current_q)

    q_table[state][action] = new_q


# =========================
# Policy 출력
# =========================

def print_policy():
    print("\nLearned Policy")

    start_state = (0, 0)
    goal_state = (3, 3)

    obstacle_states = {
        (1, 1),
        (2, 1)
    }

    for row in range(env.rows):
        for col in range(env.cols):
            state = (row, col)

            if state == start_state:
                print(" S ", end="")

            elif state == goal_state:
                print(" G ", end="")

            elif state in obstacle_states:
                print(" X ", end="")

            else:
                q_values = q_table[state]
                best_action = q_values.index(max(q_values))

                print(
                    f" {action_symbols[best_action]} ",
                    end=""
                )

        print()


# =========================
# Training
# =========================

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0

    for step in range(max_steps):
        # 1. 행동 선택
        action = choose_action(state)

        # 2. Environment와 상호작용
        next_state, reward, done = env.step(action)

        # 3. Q-Table 업데이트
        update_q_table(
            state,
            action,
            reward,
            next_state,
            done
        )

        # 4. 다음 State로 이동
        state = next_state

        # 5. Reward 누적
        total_reward += reward

        # 6. Goal 도착 시 Episode 종료
        if done:
            break

    print(
        f"Episode: {episode + 1}, "
        f"Steps: {step + 1}, "
        f"Total Reward: {total_reward}"
    )


# =========================
# Final Q-Table 출력
# =========================

print("\nFinal Q-Table")

for state, q_values in q_table.items():
    print(state, q_values)


# =========================
# Learned Policy 출력
# =========================

print_policy()