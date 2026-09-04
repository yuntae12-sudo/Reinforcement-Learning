import random

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


class GridWorldEnv:

    def __init__(self):
        self.rows = 4
        self.cols = 4

        self.start_state = (0, 0)
        self.goal_state = (3, 3)

        self.obstacles = [
            (1, 1),
            (2, 1)
        ]

        self.agent_state = self.start_state

        self.actions = {
            0: "UP",
            1: "DOWN",
            2: "LEFT",
            3: "RIGHT"
        }

        self.max_steps = 50
        self.current_step = 0

    def reset(self):

        self.agent_state = self.start_state
        self.current_step = 0

        return self.agent_state

    def get_next_state(self, action):

        row, col = self.agent_state

        if action == 0:
            row -= 1

        elif action == 1:
            row += 1

        elif action == 2:
            col -= 1

        elif action == 3:
            col += 1

        row = max(0, min(row, self.rows - 1))
        col = max(0, min(col, self.cols - 1))

        return (row, col)

    def check_collision(self, state):

        return state in self.obstacles

    def calculate_reward(self, state):

        if self.check_collision(state):
            return -10

        if state == self.goal_state:
            return 10

        return -1

    def check_done(self, state):

        if state == self.goal_state:
            return True

        if self.check_collision(state):
            return True

        return False

    def step(self, action):

        self.current_step += 1

        next_state = self.get_next_state(action)

        reward = self.calculate_reward(next_state)

        done = self.check_done(next_state)

        if self.current_step >= self.max_steps:
            done = True

        self.agent_state = next_state

        return next_state, reward, done

    def render_terminal(self):

        for row in range(self.rows):

            line = ""

            for col in range(self.cols):

                state = (row, col)

                if state == self.agent_state:
                    line += "A "

                elif state == self.goal_state:
                    line += "G "

                elif state in self.obstacles:
                    line += "X "

                else:
                    line += ". "

            print(line)

        print()

    def render(self):

        plt.clf()

        plt.xlim(-0.5, self.cols - 0.5)
        plt.ylim(self.rows - 0.5, -0.5)

        plt.xticks(range(self.cols))
        plt.yticks(range(self.rows))

        plt.grid(True)

        agent_row, agent_col = self.agent_state
        goal_row, goal_col = self.goal_state

        plt.scatter(
            agent_col,
            agent_row,
            s=300,
            label="Agent"
        )

        plt.scatter(
            goal_col,
            goal_row,
            s=300,
            marker="*",
            label="Goal"
        )

        for i, obstacle in enumerate(self.obstacles):

            obstacle_row, obstacle_col = obstacle

            plt.scatter(
                obstacle_col,
                obstacle_row,
                s=300,
                marker="s",
                label="Obstacle" if i == 0 else None
            )

        plt.title(
            f"GridWorld | Step: {self.current_step}/{self.max_steps}"
        )

        plt.legend()

        plt.pause(0.3)


if __name__ == "__main__":

    env = GridWorldEnv()

    num_episodes = 100

    rewards = []

    success_count = 0
    collision_count = 0
    max_step_count = 0

    for episode in range(num_episodes):

        state = env.reset()

        done = False
        total_reward = 0

        while not done:

            action = random.randint(0, 3)

            next_state, reward, done = env.step(action)

            total_reward += reward

            state = next_state

        rewards.append(total_reward)

        if env.agent_state == env.goal_state:

            success_count += 1
            result = "SUCCESS"

        elif env.check_collision(env.agent_state):

            collision_count += 1
            result = "COLLISION"

        else:

            max_step_count += 1
            result = "MAX STEP"

        print(
            f"Episode: {episode + 1:3d} | "
            f"Reward: {total_reward:4d} | "
            f"Steps: {env.current_step:2d} | "
            f"Result: {result}"
        )

    average_reward = sum(rewards) / len(rewards)

    print()
    print("===== Random Agent Result =====")
    print("Episodes:", num_episodes)
    print("Success:", success_count)
    print("Collision:", collision_count)
    print("Max Step:", max_step_count)
    print("Average Reward:", average_reward)

    plt.figure()

    plt.plot(
        range(1, num_episodes + 1),
        rewards
    )

    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.title("Random Agent - Episode Reward")

    plt.grid(True)

    plt.pause(3)
    plt.close()