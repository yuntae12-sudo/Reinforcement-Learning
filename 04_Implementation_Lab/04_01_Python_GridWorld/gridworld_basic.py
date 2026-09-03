print("Hello Reinforcement Learning")

# Agent의 현재 위치
agent_position = [0, 0]

# Goal의 위치
goal_position = [3, 3]

print("Start")
print("Agent Position:", agent_position)
print("Goal Position:", goal_position)

# Action 정의
# 0 = UP
# 1 = DOWN
# 2 = LEFT
# 3 = RIGHT

action = 1

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

print("Action:", action)
print("Next Position:", agent_position)