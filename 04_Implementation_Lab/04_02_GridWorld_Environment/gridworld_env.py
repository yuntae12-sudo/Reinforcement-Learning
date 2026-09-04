import random


class GridWorldEnv:

    def __init__(self):
        self.rows = 4
        self.cols = 4

        self.start_state = (0, 0)
        self.goal_state = (3, 3)

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

    def calculate_reward(self, state):

        if state == self.goal_state:
            return 10

        return -1

    def check_done(self, state):

        return state == self.goal_state

    def step(self, action):

        self.current_step += 1

        next_state = self.get_next_state(action)

        reward = self.calculate_reward(next_state)

        done = self.check_done(next_state)

        if self.current_step >= self.max_steps:
            done = True

        self.agent_state = next_state

        return next_state, reward, done

    def render(self):

        for row in range(self.rows):

            line = ""

            for col in range(self.cols):

                state = (row, col)

                if state == self.agent_state:
                    line += "A "

                elif state == self.goal_state:
                    line += "G "

                else:
                    line += ". "

            print(line)

        print()


if __name__ == "__main__":

    env = GridWorldEnv()

    state = env.reset()

    done = False

    while not done:

        env.render()

        action = random.randint(0, 3)

        next_state, reward, done = env.step(action)

        print("State:", state)
        print("Action:", env.actions[action])
        print("Reward:", reward)
        print("Next State:", next_state)
        print("Done:", done)
        print()

        state = next_state

