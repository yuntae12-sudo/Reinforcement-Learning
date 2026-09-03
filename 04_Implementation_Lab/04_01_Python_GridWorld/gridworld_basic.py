print("Hello Reinforcement Learning")

# Agent의 현재 위치
agent_position = [0, 0]

# Goal의 위치
goal_position = [3, 3]

print("Start")
print("Agent Position:", agent_position)
print("Goal Position:", goal_position)

# 오른쪽으로 한 칸 이동
agent_position[0] += 1
print("Move Right:", agent_position)

# 아래로 한 칸 이동
agent_position[1] += 1
print("Move Down:", agent_position)