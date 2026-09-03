print("Hello Reinforcement Learning")

agent_position = [0, 0]
goal_position = [3, 3]

print("Start")
print("Agent Position:", agent_position)
print("Goal Position:", goal_position)

# Action
# 0 = UP
# 1 = DOWN
# 2 = LEFT
# 3 = RIGHT

action = 3

# 기본 Reward
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

# Goal Check
if agent_position == goal_position:
    reward = 10
    done = True
else:
    done = False

print("Action:", action)
print("Next Position:", agent_position)
print("Reward:", reward)
print("Done:", done)