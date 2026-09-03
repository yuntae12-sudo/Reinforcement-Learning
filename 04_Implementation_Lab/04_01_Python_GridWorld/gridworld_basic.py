print("Hello Reinforcement Learning")

agent_position = [0, 0]
goal_position = [3, 3]

# Action
# 0 = UP
# 1 = DOWN
# 2 = LEFT
# 3 = RIGHT

actions = [3, 3, 3, 1, 1, 1]

done = False
step = 0
total_reward = 0

print("Start")
print("Agent Position:", agent_position)
print("Goal Position:", goal_position)

while not done:

    action = actions[step]

    reward = -1

    if action == 0:
        if agent_position[1] > 0:
            agent_position[1] -= 1

    elif action == 1:
        if agent_position[1] < 3:
            agent_position[1] += 1

    elif action == 2:
        if agent_position[0] > 0:
            agent_position[0] -= 1

    elif action == 3:
        if agent_position[0] < 3:
            agent_position[0] += 1

    if agent_position == goal_position:
        reward = 10
        done = True

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