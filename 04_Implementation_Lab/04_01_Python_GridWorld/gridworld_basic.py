import random


class GridWorld:

    def __init__(self):
        self.agent_position = [0, 0]
        self.goal_position = [3, 3]

    def reset(self):
        self.agent_position = [0, 0]
        return self.agent_position

    def step(self, action):

        if action == 0:
            if self.agent_position[1] > 0:
                self.agent_position[1] -= 1

        elif action == 1:
            if self.agent_position[1] < 3:
                self.agent_position[1] += 1

        elif action == 2:
            if self.agent_position[0] > 0:
                self.agent_position[0] -= 1

        elif action == 3:
            if self.agent_position[0] < 3:
                self.agent_position[0] += 1

        if self.agent_position == self.goal_position:
            reward = 10
            done = True
        else:
            reward = -1
            done = False

        return self.agent_position, reward, done


def select_action():
    return random.randint(0, 3)


env = GridWorld()

state = env.reset()

done = False
step = 0
max_steps = 50
total_reward = 0

while not done and step < max_steps:

    action = select_action()

    next_state, reward, done = env.step(action)

    total_reward += reward

    print("Step:", step)
    print("Action:", action)
    print("State:", next_state)
    print("Reward:", reward)
    print("Done:", done)
    print()

    step += 1

print("Episode Finished")
print("Total Reward:", total_reward)