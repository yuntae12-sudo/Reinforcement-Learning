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
# Greedy Action Selection
# =========================

def choose_greedy_action(state):
    q_values = q_table[state]

    return q_values.index(max(q_values))


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

                best_action = q_values.index(
                    max(q_values)
                )

                print(
                    f" {action_symbols[best_action]} ",
                    end=""
                )

        print()


# =========================
# Greedy Policy 실제 주행
# =========================

def run_greedy_policy():
    print("\nGreedy Policy Test")

    state = env.reset()

    print("Start:", state)

    for step in range(max_steps):
        action = choose_greedy_action(state)

        next_state, reward, done = env.step(action)

        print(
            f"Step {step + 1}: "
            f"{state} "
            f"{action_symbols[action]} "
            f"{next_state}"
        )

        state = next_state

        if done:
            print("Goal reached!")
            return

    print("Failed to reach goal.")


# =========================
# Random Agent 평가
# =========================

def evaluate_random_agent(num_tests):
    success_count = 0
    total_steps = 0

    for _ in range(num_tests):
        state = env.reset()

        for step in range(max_steps):
            action = random.randint(0, 3)

            next_state, reward, done = env.step(action)

            state = next_state

            if done:
                success_count += 1
                total_steps += step + 1
                break

    if success_count > 0:
        average_steps = total_steps / success_count

    else:
        average_steps = 0

    success_rate = (
        success_count / num_tests * 100
    )

    return success_rate, average_steps


# =========================
# Q-Learning Agent 평가
# =========================

def evaluate_q_learning_agent(num_tests):
    success_count = 0
    total_steps = 0

    for _ in range(num_tests):
        state = env.reset()

        for step in range(max_steps):
            action = choose_greedy_action(state)

            next_state, reward, done = env.step(action)

            state = next_state

            if done:
                success_count += 1
                total_steps += step + 1
                break

    if success_count > 0:
        average_steps = total_steps / success_count

    else:
        average_steps = 0

    success_rate = (
        success_count / num_tests * 100
    )

    return success_rate, average_steps


# =========================
# Training
# =========================

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0

    for step in range(max_steps):
        # 1. Action 선택
        action = choose_action(state)

        # 2. Environment와 상호작용
        next_state, reward, done = env.step(action)

        # 3. Q-Learning
        update_q_table(
            state,
            action,
            reward,
            next_state,
            done
        )

        # 4. 다음 State
        state = next_state

        # 5. Reward 누적
        total_reward += reward

        # 6. Episode 종료
        if done:
            break

    print(
        f"Episode: {episode + 1}, "
        f"Steps: {step + 1}, "
        f"Total Reward: {total_reward}"
    )


# =========================
# Final Q-Table
# =========================

print("\nFinal Q-Table")

for state, q_values in q_table.items():
    print(state, q_values)


# =========================
# Learned Policy
# =========================

print_policy()


# =========================
# Greedy Policy Test
# =========================

run_greedy_policy()


# =========================
# Random vs Q-Learning
# =========================

num_tests = 100

random_success, random_steps = (
    evaluate_random_agent(num_tests)
)

q_success, q_steps = (
    evaluate_q_learning_agent(num_tests)
)


print("\nEvaluation Result")

print("\nRandom Agent")
print(f"Success Rate: {random_success:.1f}%")
print(f"Average Steps: {random_steps:.2f}")

print("\nQ-Learning Agent")
print(f"Success Rate: {q_success:.1f}%")
print(f"Average Steps: {q_steps:.2f}")