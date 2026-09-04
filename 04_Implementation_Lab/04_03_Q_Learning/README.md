# 04-03. Q-Learning 직접 구현

## 1. 목표

이번 실습에서는 GridWorld 환경에서 **Q-Learning을 직접 구현**한다.

04-02까지 Agent는 다음과 같이 랜덤하게 행동했다.

```python
action = random.randint(0, 3)
```

즉, Agent는 현재 상태에서 어떤 행동이 좋은지 전혀 기억하지 못했다.

04-03에서는 **Q-Table**을 추가하여 Agent가 경험을 저장하고, 반복 학습을 통해 어떤 상태에서 어떤 행동이 좋은지 스스로 학습하도록 만든다.

전체 흐름은 다음과 같다.

```text
State
  ↓
ε-greedy Action Selection
  ↓
Action
  ↓
Environment
  ↓
Reward + Next State
  ↓
Q-Learning Update
  ↓
Q-Table
  ↓
반복 학습
  ↓
Learned Policy
```

---

# 2. 파일 구조

```text
04_03_Q_Learning/
├── gridworld_env.py
├── q_learning.py
└── README.md
```

### `gridworld_env.py`

04-02에서 구현한 GridWorld 환경을 사용한다.

환경의 역할은 다음과 같다.

```text
현재 State
+
Action
↓
Next State
Reward
Done
```

### `q_learning.py`

Q-Learning Agent의 학습 과정을 구현한다.

주요 기능은 다음과 같다.

* Q-Table 생성
* ε-greedy 행동 선택
* Q-Learning Update
* Episode 반복 학습
* 학습된 Policy 출력
* Greedy Policy 실제 실행
* Random Agent와 Q-Learning Agent 성능 비교

---

# 3. State와 Action

GridWorld의 State는 `(row, col)` 형태로 표현한다.

예:

```text
(0, 0)
(0, 1)
(1, 0)
...
```

Action은 다음과 같이 정의한다.

```text
0 = UP
1 = DOWN
2 = LEFT
3 = RIGHT
```

따라서 각 State에서는 4개의 Action에 대한 Q-value를 저장해야 한다.

---

# 4. Q-Table

Q-Table은 각 State에서 각 Action이 얼마나 좋은지를 저장하는 기억장치이다.

예를 들어:

```text
State = (0, 0)

UP      → Q((0,0), UP)
DOWN    → Q((0,0), DOWN)
LEFT    → Q((0,0), LEFT)
RIGHT   → Q((0,0), RIGHT)
```

초기 Q-value는 모두 `0.0`으로 설정한다.

```python
q_table[state] = [0.0, 0.0, 0.0, 0.0]
```

따라서

```python
q_table[(0, 0)][3]
```

은 다음 값을 의미한다.

```text
Q((0,0), RIGHT)
```

GridWorld가 `4 × 4`이고 Action이 4개라면 총 64개의 Q-value가 존재한다.

---

# 5. Exploration vs Exploitation

Agent가 학습하려면 두 가지 행동 방식이 필요하다.

### Exploration

새로운 행동을 랜덤하게 시도한다.

```text
아직 해보지 않은 행동을 탐색
```

### Exploitation

현재까지 학습한 Q-value 중 가장 높은 행동을 선택한다.

```text
지금까지 가장 좋았던 행동을 선택
```

이를 함께 사용하는 방법이 **ε-greedy Policy**이다.

예를 들어:

```python
epsilon = 0.1
```

이면

```text
10% → Exploration
90% → Exploitation
```

으로 행동한다.

수식으로 표현하면:

$$
a =
\begin{cases}
\text{Random Action}, & \text{확률 } \epsilon \\
\arg\max_a Q(s,a), & \text{확률 } 1-\epsilon
\end{cases}
$$

---

# 6. Q-Learning Update

Q-Learning의 핵심 업데이트 식은 다음과 같다.

$$
Q(s,a)
\leftarrow
Q(s,a)
+
\alpha
\left[
r+\gamma\max_{a'}Q(s',a')
-Q(s,a)
\right]
$$

각 항의 의미는 다음과 같다.

| 기호         | 의미                       |
| ---------- | ------------------------ |
| \(s\)      | 현재 State                 |
| \(a\)      | 현재 Action                |
| \(r\)      | 현재 Action으로 받은 Reward    |
| \(s'\)     | 다음 State                 |
| \(\alpha\) | Learning Rate            |
| \(\gamma\) | Discount Factor          |
| \(Q(s,a)\) | 현재 State-Action의 Q-value |

코드에서는 다음과 같이 연결된다.

```python
current_q = q_table[state][action]
```

$$
Q(s,a)
$$

다음 State에서 가장 높은 Q-value는:

```python
next_max_q = max(q_table[next_state])
```

$$
\max_{a'}Q(s',a')
$$

TD Target은:

```python
target = reward + gamma * next_max_q
```

$$
r+\gamma\max_{a'}Q(s',a')
$$

최종 Q-value는:

```python
new_q = current_q + alpha * (target - current_q)
```

으로 업데이트한다.

---

# 7. Terminal State 처리

Goal에 도착하면 Episode가 종료되므로 이후 미래 Reward는 존재하지 않는다.

따라서 `done == True`인 경우:

$$
target=r
$$

만 사용한다.

```python
if done:
    target = reward
else:
    target = reward + gamma * next_max_q
```

---

# 8. Hyperparameter

이번 실습에서는 다음 값을 사용했다.

```python
epsilon = 0.1
alpha = 0.1
gamma = 0.9

num_episodes = 500
max_steps = 100
```

### epsilon

```text
Exploration 확률
```

### alpha

```text
새로운 경험을 기존 Q-value에 얼마나 강하게 반영할지 결정
```

### gamma

```text
미래 Reward를 현재 가치에 얼마나 중요하게 반영할지 결정
```

### num_episodes

```text
전체 학습 Episode 수
```

### max_steps

한 Episode가 무한히 반복되는 것을 방지한다.

---

# 9. Episode Training

한 Episode의 학습 과정은 다음과 같다.

```text
Environment Reset
       ↓
현재 State 확인
       ↓
ε-greedy Action 선택
       ↓
Environment.step(Action)
       ↓
Reward / Next State
       ↓
Q-Table Update
       ↓
State = Next State
       ↓
Goal 도착?
 ├─ NO → 반복
 └─ YES → Episode 종료
```

이 과정을 여러 Episode 동안 반복하면서 Q-Table이 점차 학습된다.

---

# 10. Reward의 전파

학습 결과 Goal 주변의 Q-value가 먼저 높아지고 그 가치가 이전 State로 전파되는 것을 확인할 수 있었다.

예를 들어 Goal Reward가 `+10`, 일반 이동 Reward가 `-1`, Discount Factor가 `0.9`일 때:

Goal 바로 이전 State에서는:

$$
Q \approx 10
$$

한 칸 더 이전에서는:

$$
-1 + 0.9(10)=8
$$

그 이전에서는:

$$
-1 + 0.9(8)=6.2
$$

다시 이전에서는:

$$
-1 + 0.9(6.2)=4.58
$$

즉 다음과 같이 Goal의 가치가 이전 State로 전달된다.

```text
Goal
 +10
  ↑
 8.0
  ↑
 6.2
  ↑
 4.58
  ↑
 ...
```

이는 Q-Learning의 **Bootstrapping**이 실제 코드에서 동작한 결과이다.

---

# 11. Q-Table → Policy

학습이 완료되면 각 State에서 가장 높은 Q-value를 가진 Action을 선택할 수 있다.

$$
\pi(s)=\arg\max_a Q(s,a)
$$

Action을 다음 기호로 표현했다.

```text
↑ = UP
↓ = DOWN
← = LEFT
→ = RIGHT

S = Start
G = Goal
X = Obstacle
```

예:

```text
Learned Policy

 S  →  ↓  ↓
 ↑  X  →  ↓
 ↑  X  ↓  ↓
 →  →  →  G
```

이 Policy는 Q-Table의 각 State에서 가장 큰 Q-value의 Action을 표시한 것이다.

---

# 12. Training과 Evaluation

Training에서는 Exploration을 포함한 ε-greedy Policy를 사용한다.

```text
Training

Exploration
+
Exploitation
↓
Q-Table Update
```

학습이 완료된 후 평가할 때는 Exploration을 사용하지 않는다.

즉:

$$
a=\arg\max_a Q(s,a)
$$

만 사용한다.

```text
Evaluation

State
 ↓
Greedy Action
 ↓
Environment
 ↓
Next State
```

Evaluation에서는 Q-Table을 더 이상 업데이트하지 않는다.

---

# 13. Greedy Policy 실제 실행

학습된 Q-Table만 사용하여 Start에서 Goal까지 실제로 이동하는지 확인했다.

예:

```text
Start: (0, 0)

(0, 0)
  →
(0, 1)
  →
(0, 2)
  ↓
(1, 2)
  →
(1, 3)
  ↓
(2, 3)
  ↓
(3, 3)

Goal reached!
```

이를 통해 학습된 Q-Table이 실제 행동 Policy로 정상적으로 사용되는 것을 확인했다.

---

# 14. Random Agent vs Q-Learning Agent

학습 효과를 확인하기 위해 두 Agent를 비교했다.

### Random Agent

```python
random.randint(0, 3)
```

현재 State나 과거 경험을 고려하지 않고 랜덤하게 행동한다.

### Q-Learning Agent

```text
현재 State
↓
Q-Table 확인
↓
가장 높은 Q-value를 가진 Action 선택
```

두 Agent를 여러 번 실행하여 다음 값을 비교했다.

* Goal 성공률
* Goal 도착까지 평균 Step 수

Q-Learning Agent는 학습된 Q-Table을 이용하므로 Random Agent보다 훨씬 짧고 안정적인 경로로 Goal에 도착하는 것을 확인할 수 있었다.

---

# 15. Q-Learning 전체 구조

이번 실습에서 구현한 전체 흐름은 다음과 같다.

```text
Environment
    ↓
State s
    ↓
ε-greedy
    ↓
Action a
    ↓
Environment.step(a)
    ↓
Reward r
Next State s'
    ↓
Q-Learning Update

Q(s,a)
←
Q(s,a)
+
α[r + γ max Q(s',a') - Q(s,a)]

    ↓
Q-Table
    ↓
반복 학습
    ↓
Greedy Policy
    ↓
Goal
```

---

# 16. Chapter 02와의 연결

Chapter 02에서 이론으로 배운 Q-Learning 식을 이번 실습에서 실제 코드로 구현했다.

이론:

$$
Q(s,a)
\leftarrow
Q(s,a)
+
\alpha
[
r+\gamma\max Q(s',a')-Q(s,a)
]
$$

코드:

```python
current_q = q_table[state][action]

next_max_q = max(q_table[next_state])

target = reward + gamma * next_max_q

new_q = current_q + alpha * (target - current_q)

q_table[state][action] = new_q
```

또한 Q-Learning이 **Off-Policy**인 이유도 코드에서 확인할 수 있다.

실제 행동은:

```text
ε-greedy Policy
```

를 사용하지만 Q-value 업데이트의 Target은:

$$
\max_{a'}Q(s',a')
$$

즉 Greedy Policy를 기준으로 계산한다.

```text
Behavior Policy
ε-greedy

≠

Target Policy
Greedy
```

---

# 17. 이번 실습에서 배운 핵심

### Q-Table

State와 Action의 가치를 저장하는 Agent의 기억장치이다.

### Exploration / Exploitation

새로운 행동을 탐색하는 것과 현재 가장 좋은 행동을 선택하는 것 사이의 균형이다.

### ε-greedy

Exploration과 Exploitation을 함께 사용하는 행동 선택 방법이다.

### TD Target

$$
r+\gamma\max Q(s',a')
$$

현재 경험을 바탕으로 Q-value가 향해야 할 목표이다.

### TD Error

$$
target-Q(s,a)
$$

현재 예상과 새로운 경험 사이의 차이이다.

### Bootstrapping

다음 State의 Q-value를 이용해 현재 State의 Q-value를 업데이트한다.

### Policy

학습된 Q-Table에서 가장 높은 Q-value를 가진 Action을 선택하는 행동 규칙이다.

---

# 18. 04-03 완료

04-03에서 다음 내용을 직접 구현하고 확인했다.

```text
✅ Q-Table 생성
✅ ε-greedy Action Selection
✅ Q-Learning Update
✅ Terminal State 처리
✅ Episode Training Loop
✅ Q-Table 학습
✅ Q-Table → Policy 변환
✅ Greedy Policy 실제 실행
✅ Random Agent와 성능 비교
✅ Training / Evaluation 구분
```

---

# 19. 다음 단계

다음 실습에서는 **04-04. DQN 직접 구현**으로 넘어간다.

Q-Learning에서는:

```text
State
 ↓
Q-Table
 ↓
Q(s,a)
```

형태로 Q-value를 직접 저장했다.

DQN에서는 이 Q-Table을 Neural Network로 대체한다.

```text
State
 ↓
Neural Network
 ↓
Q(s, UP)
Q(s, DOWN)
Q(s, LEFT)
Q(s, RIGHT)
```

즉 다음 단계에서는:

$$
Q(s,a)
$$

를 Table에서 직접 찾는 대신 **Neural Network가 예측하도록 만드는 과정**을 구현한다.
