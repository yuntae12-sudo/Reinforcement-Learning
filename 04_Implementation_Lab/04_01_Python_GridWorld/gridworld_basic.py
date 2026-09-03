import random


def select_action():
    action = random.randint(0, 3)
    return action


def move_agent(position, action):

    if action == 0:
        if position[1] > 0:
            position[1] -= 1

    elif action == 1:
        if position[1] < 3:
            position[1] += 1

    elif action == 2:
        if position[0] > 0:
            position[0] -= 1

    elif action == 3:
        if position[0] < 3:
            position[0] += 1

    return position


def check_goal(position, goal_position):

    if position == goal_position:
        reward = 10
        done = True

    else:
        reward = -1
        done = False

    return reward, done


print("Hello Reinforcement Learning")

agent_position = [0, 0]
goal_position = [3, 3]

done = False
step = 0
total_reward = 0
max_steps = 50

print("Start")
print("Agent Position:", agent_position)
print("Goal Position:", goal_position)

while not done and step < max_steps:

    action = select_action()

    agent_position = move_agent(agent_position, action)

    reward, done = check_goal(agent_position, goal_position)

    total_reward += reward

    print("Step:", step)
    print("Action:", action)
    print("Position:", agent_position)
    print("Reward:", reward)
    print("Done:", done)
    print()

    step += 1

print("Episode Finished")
print("Total Reward:", total_reward)
print("Total Steps:", step)