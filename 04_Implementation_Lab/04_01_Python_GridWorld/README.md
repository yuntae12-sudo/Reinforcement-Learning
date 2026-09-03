# 04-01. Python + GridWorld Basic

## Goal

Python의 기본 문법을 익히면서 GridWorld에서 Agent의 위치를 직접 표현하고 이동시켜본다.

이번 단계에서는 강화학습 알고리즘을 구현하지 않는다.

대신 앞으로 RL Environment를 만들기 위해 필요한 가장 기본적인 구조를 이해하는 것이 목표이다.

---

## GridWorld

4 x 4 GridWorld를 가정한다.

```text
S . . .
. . . .
. . . .
. . . G

## Action

GridWorld에서 Agent가 수행할 행동을 숫자로 정의한다.

```text
0 = UP
1 = DOWN
2 = LEFT
3 = RIGHT
```

숫자 자체에 특별한 의미가 있는 것은 아니다.

강화학습 Agent가 선택한 행동을 코드에서 처리하기 위해 각 행동에 번호를 붙여 사용하는 것이다.

예를 들어:

```python
action = 3
```

은 우리가 정한 규칙에 따라 `RIGHT`를 의미한다.

---

## Action Handling

`if`와 `elif`를 사용하여 선택된 Action에 따라 Agent의 위치를 변경한다.

```python
if action == 0:
    agent_position[1] -= 1

elif action == 1:
    agent_position[1] += 1

elif action == 2:
    agent_position[0] -= 1

elif action == 3:
    agent_position[0] += 1
```

좌표는 다음과 같이 정의한다.

```text
[x, y]
```

따라서 각 Action은 다음과 같이 좌표를 변경한다.

| Action | Meaning | Coordinate Change |
| ------ | ------- | ----------------- |
| `0`    | UP      | `y - 1`           |
| `1`    | DOWN    | `y + 1`           |
| `2`    | LEFT    | `x - 1`           |
| `3`    | RIGHT   | `x + 1`           |

예를 들어 현재 위치가

```text
[0, 0]
```

이고

```python
action = 3
```

이라면 `RIGHT`가 선택되므로 x 좌표가 1 증가한다.

```text
[0, 0]
   ↓ RIGHT
[1, 0]
```

---

## if / elif

Python에서 조건에 따라 다른 코드를 실행할 때 `if`와 `elif`를 사용한다.

```python
if action == 0:
```

의 의미는 다음과 같다.

```text
action의 값이 0과 같은가?
```

`==`는 두 값이 같은지 비교하는 연산자이다.

반면

```python
action = 0
```

에서 `=`는 변수에 값을 저장하는 연산자이다.

```text
=   → 값 저장
==  → 값 비교
```

`action = 3`인 경우 조건문은 다음 순서로 확인된다.

```text
action == 0 ? → False
action == 1 ? → False
action == 2 ? → False
action == 3 ? → True
```

따라서 `RIGHT`에 해당하는 코드가 실행된다.

---

## RL Connection

이번 단계부터 강화학습의 State와 Action 구조가 코드에 직접 나타나기 시작한다.

```text
State
[0, 0]

    ↓

Action
3 = RIGHT

    ↓

Environment Transition

    ↓

Next State
[1, 0]
```

즉 강화학습에서의

```text
S_t
 ↓
A_t
 ↓
S_(t+1)
```

구조를 코드로 표현한 것이다.

---

## Python Concepts

이번 단계에서 새롭게 사용한 Python 문법:

* `if`
* `elif`
* `==`
* `+=`
* `-=`
* 조건문
* 비교 연산자
* Discrete Action

---

## Next

현재 코드는 GridWorld의 경계를 확인하지 않기 때문에 다음과 같은 문제가 발생한다.

```text
Start = [0, 0]
Action = UP

Result = [0, -1]
```

하지만 4 x 4 GridWorld에서는 다음 범위만 허용되어야 한다.

```text
0 <= x <= 3
0 <= y <= 3
```

다음 단계에서는 **Boundary Check**를 추가하여 Agent가 GridWorld 밖으로 이동하지 못하도록 구현한다.

## Boundary Check

현재 GridWorld는 `4 x 4` 크기로 정의되어 있다.

따라서 Agent가 이동할 수 있는 좌표 범위는 다음과 같다.

```text
0 <= x <= 3
0 <= y <= 3
```

기존 코드에서는 GridWorld의 경계를 검사하지 않았기 때문에 다음과 같은 문제가 발생했다.

```text
Start = [0, 0]
Action = UP

Result = [0, -1]
```

하지만 `[0, -1]`은 GridWorld 밖의 좌표이므로 허용하면 안 된다.

---

## Valid Movement Check

Action을 실행하기 전에 해당 방향으로 이동 가능한지 확인한다.

### UP

```python
if action == 0:
    if agent_position[1] > 0:
        agent_position[1] -= 1
```

현재 `y`가 `0`보다 클 때만 위로 이동할 수 있다.

```text
y > 0
```

---

### DOWN

```python
elif action == 1:
    if agent_position[1] < 3:
        agent_position[1] += 1
```

현재 `y`가 `3`보다 작을 때만 아래로 이동할 수 있다.

```text
y < 3
```

---

### LEFT

```python
elif action == 2:
    if agent_position[0] > 0:
        agent_position[0] -= 1
```

현재 `x`가 `0`보다 클 때만 왼쪽으로 이동할 수 있다.

---

### RIGHT

```python
elif action == 3:
    if agent_position[0] < 3:
        agent_position[0] += 1
```

현재 `x`가 `3`보다 작을 때만 오른쪽으로 이동할 수 있다.

---

## Nested if

이번 단계에서는 `if` 안에 또 다른 `if`를 사용하는 중첩 조건문을 사용했다.

```python
if action == 0:
    if agent_position[1] > 0:
        agent_position[1] -= 1
```

첫 번째 조건은 다음을 확인한다.

```text
어떤 Action이 선택되었는가?
```

두 번째 조건은 다음을 확인한다.

```text
해당 Action을 현재 State에서 실행할 수 있는가?
```

따라서 전체 흐름은 다음과 같다.

```text
Action 선택
    ↓
Action 종류 확인
    ↓
이동 가능 여부 확인
    ↓
가능하면 State 변경
    ↓
불가능하면 현재 State 유지
```

---

## Comparison Operators

이번 단계에서는 다음 비교 연산자를 사용한다.

```text
>   greater than
<   less than
>=  greater than or equal
<=  less than or equal
```

예를 들어:

```python
agent_position[1] > 0
```

은

```text
현재 y 좌표가 0보다 큰가?
```

를 의미한다.

---

## Valid / Invalid Action

예를 들어 현재 위치가

```text
[0, 0]
```

이고

```python
action = 0
```

이라면 `UP`을 의미한다.

하지만 `y = 0`이므로 위쪽으로 이동할 수 없다.

```text
State
[0, 0]

    ↓

Action
UP

    ↓

Boundary Check
y > 0 ?

    ↓
False

    ↓

Next State
[0, 0]
```

반면

```python
action = 3
```

이라면 `RIGHT`이므로 이동 가능하다.

```text
State
[0, 0]

    ↓

Action
RIGHT

    ↓

Boundary Check
x < 3 ?

    ↓
True

    ↓

Next State
[1, 0]
```

---

## RL Connection

이번 단계에서는 기존의

```text
State
  ↓
Action
  ↓
Next State
```

구조에 Constraint Check가 추가되었다.

```text
State
  ↓
Action
  ↓
Constraint Check
  ↓
Next State
```

이 구조는 이후 자율주행 문제에서도 연결될 수 있다.

예를 들어:

```text
Action = LANE_CHANGE_LEFT
        ↓
왼쪽 차선 존재 여부
        ↓
충돌 위험 확인
        ↓
실행 가능 여부 판단
```

현재 GridWorld의 Boundary Check는 이후 Safety Constraint의 가장 단순한 형태로 볼 수 있다.

---

## Python Concepts

이번 단계에서 새롭게 사용한 Python 문법과 개념:

* `<`
* `>`
* `<=`
* `>=`
* 비교 연산자
* 중첩 `if`
* Boundary Check
* Valid / Invalid Action
* Constraint Check

---

## Next

다음 단계에서는 Agent가 Goal에 도착했는지 확인한다.

```python
agent_position == goal_position
```

Goal에 도착하면 Episode가 종료되도록 `done` 개념을 추가한다.

```text
State
  ↓
Action
  ↓
Next State
  ↓
Goal Check
  ↓
done = True / False
```

## Goal Check

Agent가 Goal에 도착했는지 확인한다.

현재 Goal은 다음과 같이 정의되어 있다.

```python
goal_position = [3, 3]
```

Agent의 현재 위치가 Goal과 같다면 Episode를 종료할 수 있다.

```python
if agent_position == goal_position:
    done = True
else:
    done = False
```

---

## Boolean

이번 단계에서는 Boolean 값을 사용한다.

Boolean은 참과 거짓을 표현하는 자료형이다.

```text
True  = 참
False = 거짓
```

예를 들어:

```python
done = True
```

는

```text
Episode가 종료되었다.
```

라는 의미로 사용할 수 있다.

반대로:

```python
done = False
```

는

```text
Episode가 아직 종료되지 않았다.
```

라는 의미이다.

---

## done

`done` 변수는 현재 Episode가 끝났는지를 나타낸다.

```python
if agent_position == goal_position:
    done = True
else:
    done = False
```

예를 들어 현재 위치가:

```text
[2, 3]
```

이고 Action이 `RIGHT`라면:

```text
[2, 3]
   ↓ RIGHT
[3, 3]
```

Goal에 도착했으므로:

```python
done = True
```

가 된다.

반대로 현재 위치가:

```text
[0, 0]
```

이고 `RIGHT`를 실행하면:

```text
[1, 0]
```

이므로 아직 Goal에 도착하지 않았다.

```python
done = False
```

---

## Episode

강화학습에서 Episode는 하나의 시작부터 종료 조건까지의 전체 과정이다.

GridWorld에서는 다음과 같이 생각할 수 있다.

```text
Start
[0, 0]

    ↓

Action

    ↓

Next State

    ↓

Action

    ↓

...

    ↓

Goal
[3, 3]

    ↓

done = True

    ↓

Episode End
```

즉 Agent가 Goal에 도착하면 현재 Episode가 종료된다.

---

## Current Environment Flow

현재까지 구현한 GridWorld의 흐름은 다음과 같다.

```text
State
  ↓
Action
  ↓
Boundary Check
  ↓
Next State
  ↓
Goal Check
  ↓
done
```

이 구조는 이후 실제 RL Environment의 다음 형태로 연결된다.

```python
next_state, reward, done = env.step(action)
```

현재는 `env.step()`을 사용하지 않고 내부에서 어떤 일이 발생하는지를 직접 구현하고 있다.

---

## Python Concepts

이번 단계에서 새롭게 사용한 Python 문법과 개념:

* Boolean
* `True`
* `False`
* list 비교
* Goal Check
* `done`
* Episode
* Episode 종료 조건

---

## Next

다음 단계에서는 Reward를 추가한다.

예를 들어:

```text
일반 이동   = -1
Goal 도착   = +10
```

이를 통해 Agent가 단순히 이동하는 것이 아니라, 어떤 행동이 더 좋은 결과를 만드는지 평가할 수 있게 한다.

다음 구조로 확장한다.

```text
State
  ↓
Action
  ↓
Next State
  ↓
Reward
  ↓
done
```

## Reward

이번 단계에서는 Agent의 행동 결과에 Reward를 추가한다.

현재 Reward는 가장 단순하게 다음과 같이 정의한다.

```text
일반 이동 = -1
Goal 도착 = +10
```

일반 이동에 `-1`을 주는 이유는 Agent가 불필요하게 많은 이동을 하지 않고, 가능한 한 짧은 경로로 Goal에 도착하도록 유도하기 위해서이다.

---

## Basic Reward

기본 Reward는 다음과 같이 설정한다.

```python
reward = -1
```

즉 한 번 이동할 때마다 기본적으로 `-1`의 Reward를 받는다.

---

## Goal Reward

Agent가 Goal에 도착하면 Reward를 `+10`으로 변경한다.

```python
if agent_position == goal_position:
    reward = 10
    done = True
else:
    done = False
```

예를 들어 현재 상태가

```text
[2, 3]
```

이고 Action이 `RIGHT`라면:

```text
[2, 3]
   ↓ RIGHT
[3, 3]
```

Goal에 도착하므로:

```text
Reward = +10
done = True
```

가 된다.

반대로 Goal에 도착하지 않았다면:

```text
Reward = -1
done = False
```

가 된다.

---

## Reward Design

강화학습에서 Reward는 Agent가 어떤 행동을 선호하도록 만들 것인지 정의하는 핵심 요소이다.

현재 GridWorld에서는:

```text
짧은 경로
    ↓
적은 이동 횟수
    ↓
적은 -1 누적
    ↓
더 높은 Return
```

이 되도록 설계한다.

예를 들어 두 경로가 있을 때:

```text
Path A
6 step 만에 Goal 도착

Path B
12 step 만에 Goal 도착
```

두 경로 모두 Goal Reward는 같지만, Path B는 더 많은 이동 패널티를 받는다.

따라서 Agent는 장기적으로 더 짧은 경로를 선호하도록 학습할 수 있다.

---

## Current Environment Flow

현재까지 구현한 GridWorld의 흐름은 다음과 같다.

```text
State
  ↓
Action
  ↓
Boundary Check
  ↓
Next State
  ↓
Reward
  ↓
Goal Check
  ↓
done
```

이 구조는 실제 RL Environment의 다음 형태로 연결된다.

```python
next_state, reward, done = env.step(action)
```

현재는 `step()` 함수 없이 이 내부 동작을 직접 구현하고 있다.

---

## RL Connection

강화학습 Agent의 목적은 단순히 Goal에 도착하는 것이 아니라 장기적으로 더 큰 Reward를 얻는 것이다.

즉:

```text
State
  ↓
Action
  ↓
Reward
  ↓
다음 Action 선택
  ↓
...
```

과정을 반복하면서 어떤 행동이 더 좋은 결과를 만드는지 학습한다.

이후 Frenet 기반 강화학습에서도 같은 원리를 사용하게 된다.

예를 들어:

```text
Collision Risk       -
Large Jerk           -
Unnecessary Lane Change -
Progress             +
Target Speed         +
Comfort              +
```

와 같이 Reward를 설계하여 원하는 주행 행동을 학습시킬 수 있다.

---

## Python Concepts

이번 단계에서 새롭게 사용한 개념:

* Reward
* 기본 Reward
* Goal Reward
* Reward Design
* 누적 보상
* 행동 결과 평가

---

## Next

다음 단계에서는 여러 Action을 연속으로 실행하기 위해 반복문을 사용한다.

```python
while not done:
```

형태를 사용하여 하나의 Episode가 종료될 때까지 다음 과정을 반복한다.

```text
State
  ↓
Action
  ↓
Next State
  ↓
Reward
  ↓
done 확인
  ↓
다시 Action
```

이 단계부터 실제 강화학습의 Episode Loop 구조를 만들기 시작한다.

## Episode Loop

이번 단계에서는 Agent가 한 번만 움직이는 것이 아니라, Goal에 도착할 때까지 여러 Action을 연속으로 실행하도록 만든다.

강화학습에서는 하나의 Episode가 여러 Step으로 구성된다.

```text
Start State
    ↓
Action
    ↓
Next State
    ↓
Reward
    ↓
done 확인
    ↓
False → 다음 Action
    ↓
...
    ↓
Goal 도착
    ↓
done = True
    ↓
Episode End
```

---

## while

Python의 `while`은 특정 조건이 참인 동안 코드를 반복해서 실행한다.

```python
while not done:
```

현재 `done = False`라면:

```text
not False = True
```

이므로 반복문이 계속 실행된다.

Goal에 도착해서:

```python
done = True
```

가 되면:

```text
not True = False
```

가 되어 반복문이 종료된다.

---

## Predefined Action Sequence

아직 RL Agent가 직접 Action을 선택하지 않기 때문에 이번 단계에서는 Action 순서를 미리 정의한다.

```python
actions = [3, 3, 3, 1, 1, 1]
```

Action 정의:

```text
0 = UP
1 = DOWN
2 = LEFT
3 = RIGHT
```

따라서 위 Action sequence는 다음과 같다.

```text
RIGHT
RIGHT
RIGHT
DOWN
DOWN
DOWN
```

시작점 `[0, 0]`에서 Goal `[3, 3]`까지 이동하는 경로이다.

---

## Step

현재 몇 번째 Action을 실행하고 있는지 확인하기 위해 `step` 변수를 사용한다.

```python
step = 0
```

현재 Step에 해당하는 Action은 다음과 같이 가져온다.

```python
action = actions[step]
```

예를 들어:

```python
actions = [3, 3, 3, 1, 1, 1]
step = 0
```

이면:

```python
actions[0]
```

이므로 Action은 `3 = RIGHT`이다.

한 Step이 끝나면:

```python
step += 1
```

을 사용하여 다음 Action으로 이동한다.

---

## Total Reward

한 Episode 동안 받은 Reward를 누적하기 위해 `total_reward`를 사용한다.

```python
total_reward = 0
```

각 Step에서 Reward를 받은 후:

```python
total_reward += reward
```

를 수행한다.

이번 경로의 Reward는 다음과 같다.

```text
Step 0 → -1
Step 1 → -1
Step 2 → -1
Step 3 → -1
Step 4 → -1
Step 5 → +10
```

따라서 Episode가 종료되면:

```text
Total Reward = 5
```

가 된다.

---

## Reward Accumulation

현재 구현에서는 Reward를 단순하게 누적한다.

```text
Total Reward
=
r0 + r1 + r2 + ... + rT
```

이는 강화학습에서 Episode 동안 얻은 Return의 기본적인 형태와 연결된다.

현재 단계에서는 Discount Factor `gamma`를 적용하지 않는다.

이후 강화학습 알고리즘을 구현하면서 Discounted Return과 연결한다.

---

## Current RL Loop

현재까지 구현한 GridWorld는 다음 구조를 가진다.

```text
Initialize State
      ↓
done = False
      ↓
while not done
      ↓
Action 선택
      ↓
Boundary Check
      ↓
Next State
      ↓
Reward
      ↓
Goal Check
      ↓
Total Reward 누적
      ↓
done 확인
      ↓
False → 다음 Step
      ↓
True → Episode 종료
```

이 구조는 이후 Q-Learning 등의 Training Loop에서도 기본적으로 유지된다.

---

## RL Connection

실제 강화학습에서는 사람이 Action sequence를 미리 정하지 않는다.

현재는:

```python
actions = [3, 3, 3, 1, 1, 1]
```

처럼 사람이 행동을 정하고 있지만, 이후에는 Agent가 현재 State를 보고 Action을 선택하게 된다.

```text
현재 단계

State
  ↓
미리 정해진 Action
  ↓
Environment
```

이후:

```text
State
  ↓
RL Agent
  ↓
Action
  ↓
Environment
```

형태로 발전한다.

---

## Python Concepts

이번 단계에서 새롭게 사용한 Python 문법과 개념:

* `while`
* `not`
* 반복문
* Action sequence
* Step
* `step += 1`
* `total_reward`
* Reward 누적
* Episode Loop

---

## Next

다음 단계에서는 사람이 Action sequence를 미리 정하지 않고 Random Agent가 Action을 선택하도록 만든다.

예를 들어:

```text
0 = UP
1 = DOWN
2 = LEFT
3 = RIGHT
```

중 하나를 무작위로 선택한다.

구조는 다음과 같이 변경된다.

```text
State
  ↓
Random Agent
  ↓
Action
  ↓
Environment
  ↓
Next State / Reward / done
```

이를 통해 처음으로 Agent와 Environment의 역할을 분리하기 시작한다.

## Random Agent

이번 단계에서는 사람이 Action sequence를 미리 정의하지 않고, Agent가 매 Step마다 Action을 무작위로 선택하도록 변경한다.

기존에는 다음과 같이 Action을 직접 정의했다.

```python
actions = [3, 3, 3, 1, 1, 1]
```

이 방식은 사람이 경로를 미리 정해주는 것이므로 Agent가 실제로 행동을 선택한다고 보기 어렵다.

이번 단계부터는 다음과 같이 Action을 무작위로 선택한다.

```python
action = random.randint(0, 3)
```

---

## import random

Python의 `random` 모듈을 사용하기 위해 파일 맨 위에 다음 코드를 추가한다.

```python
import random
```

`import`는 Python에 이미 만들어져 있는 기능을 현재 코드에서 사용할 수 있도록 불러오는 문법이다.

---

## Random Action Selection

현재 Action Space는 다음과 같다.

```text
0 = UP
1 = DOWN
2 = LEFT
3 = RIGHT
```

다음 코드는 `0`, `1`, `2`, `3` 중 하나를 무작위로 선택한다.

```python
action = random.randint(0, 3)
```

따라서 매 Step마다 선택되는 Action이 달라질 수 있다.

예:

```text
Step 0 → RIGHT
Step 1 → DOWN
Step 2 → LEFT
Step 3 → UP
...
```

프로그램을 다시 실행하면 다른 Action sequence가 생성될 수 있다.

---

## Random Policy

현재 Agent의 Policy는 매우 단순하다.

```text
현재 State와 관계없이
모든 Action 중 하나를 무작위로 선택
```

즉:

```text
State
  ↓
Random Policy
  ↓
Action
```

구조이다.

아직 Agent는 어떤 Action이 좋은지 학습하지 않는다.

현재 단계의 목적은 Environment와 상호작용할 수 있는 가장 단순한 Agent를 만드는 것이다.

---

## Maximum Step

Random Agent는 Goal과 관계없이 행동하기 때문에 Goal에 도착하지 못하고 계속 움직일 가능성이 있다.

따라서 Episode가 무한히 반복되는 것을 방지하기 위해 최대 Step 수를 설정한다.

```python
max_steps = 50
```

반복문의 조건도 다음과 같이 변경한다.

```python
while not done and step < max_steps:
```

이 조건은 다음 두 가지가 모두 만족되는 동안 반복한다는 의미이다.

```text
done == False
AND
step < max_steps
```

---

## and

Python의 `and`는 두 조건이 모두 `True`일 때 전체 조건을 `True`로 만든다.

```python
while not done and step < max_steps:
```

예를 들어:

```text
done = False
step = 10
max_steps = 50
```

이라면:

```text
not done
→ True

step < max_steps
→ 10 < 50
→ True
```

두 조건이 모두 True이므로 반복문을 계속 실행한다.

---

## Episode Termination

현재 Episode가 끝나는 조건은 두 가지이다.

```text
1. Goal에 도착
2. Maximum Step에 도달
```

Goal에 도착하면:

```python
done = True
```

가 되어 Episode가 종료된다.

Goal에 도착하지 못하더라도:

```text
step = 50
```

이 되면:

```text
step < max_steps
```

조건이 False가 되어 반복문이 종료된다.

---

## Current Agent-Environment Flow

현재 구조는 다음과 같다.

```text
Initialize State
      ↓
Random Agent
      ↓
Random Action
      ↓
Environment
      ↓
Boundary Check
      ↓
Next State
      ↓
Reward
      ↓
Goal Check
      ↓
done 확인
      ↓
False → 다시 Random Action 선택
      ↓
True 또는 Max Step → Episode 종료
```

이전 단계와 비교하면 중요한 변화가 있다.

기존:

```text
State
  ↓
사람이 미리 정의한 Action
  ↓
Environment
```

현재:

```text
State
  ↓
Random Agent
  ↓
Action
  ↓
Environment
```

Agent가 Action을 선택하는 역할이 처음 등장하기 시작했다.

---

## RL Connection

Random Agent는 아직 학습하지 않는다.

하지만 이후 Q-Learning Agent는 현재 Random Action Selection 부분을 다음과 같이 발전시킨다.

```text
현재

State
  ↓
Random Action
```

이후:

```text
State
  ↓
Q-Value 확인
  ↓
Action 선택
```

그리고 Exploration을 위해 일부 Action은 여전히 Random하게 선택하게 된다.

따라서 현재 구현하는 Random Action은 이후 `epsilon-greedy` Policy의 Exploration과도 연결된다.

---

## Python Concepts

이번 단계에서 새롭게 사용한 Python 문법과 개념:

* `import`
* `random`
* `random.randint()`
* Random Action
* Random Policy
* `and`
* Multiple Conditions
* `max_steps`
* Episode Step Limit

---

## Next

다음 단계에서는 Random Action 선택 부분을 함수로 분리한다.

현재:

```python
action = random.randint(0, 3)
```

구조를 다음과 같이 변경한다.

```python
def select_action():
    ...
```

이 과정에서 Python의 다음 개념을 학습한다.

```text
def
함수
parameter
return
```

이를 통해 Agent의 Action Selection 역할을 별도의 코드로 분리하기 시작한다.

## Function

이번 단계에서는 Random Action 선택 코드를 함수로 분리한다.

기존에는 Episode Loop 내부에서 직접 다음 코드를 사용했다.

```python
action = random.randint(0, 3)
```

이제 Action 선택 역할을 별도의 함수로 분리한다.

```python
def select_action():
    action = random.randint(0, 3)
    return action
```

그리고 Episode Loop에서는 다음과 같이 호출한다.

```python
action = select_action()
```

---

## def

Python에서는 `def`를 사용하여 함수를 정의한다.

```python
def select_action():
```

의 의미는 다음과 같다.

```text
select_action이라는 이름의 함수를 만든다.
```

함수 내부의 코드는 들여쓰기를 사용하여 작성한다.

```python
def select_action():
    action = random.randint(0, 3)
    return action
```

---

## Function Call

함수를 실제로 실행하려면 함수 이름 뒤에 `()`를 붙인다.

```python
select_action()
```

현재 코드에서는 반환된 Action을 변수에 저장한다.

```python
action = select_action()
```

전체 흐름은 다음과 같다.

```text
select_action() 호출
        ↓
Random Action 생성
        ↓
return
        ↓
action 변수에 저장
```

---

## return

`return`은 함수 내부에서 만든 값을 함수 밖으로 전달한다.

현재 함수:

```python
def select_action():
    action = random.randint(0, 3)
    return action
```

에서:

```python
return action
```

은 Random하게 선택된 Action 값을 함수 밖으로 전달한다.

예를 들어 함수 내부에서 `3`이 선택되었다면:

```text
select_action()
      ↓
action = 3
      ↓
return 3
      ↓
Episode Loop의 action = 3
```

이 된다.

---

## Why Separate the Function?

코드의 동작 자체는 이전 단계와 동일하다.

하지만 역할이 분리되었다.

기존:

```text
Episode Loop
  ├─ Action 선택
  ├─ 이동 처리
  ├─ Reward 계산
  └─ Goal Check
```

현재:

```text
Agent
  └─ select_action()

Episode Loop
  ├─ Agent에게 Action 요청
  ├─ 이동 처리
  ├─ Reward 계산
  └─ Goal Check
```

Action Selection을 별도의 함수로 분리하면서 Agent의 역할이 조금 더 명확해진다.

---

## RL Connection

현재 Random Agent는 State를 사용하지 않는다.

```python
def select_action():
```

현재 State와 관계없이 Random Action을 선택한다.

하지만 이후 Q-Learning Agent에서는 현재 State를 입력으로 사용하게 된다.

```python
def select_action(state):
    ...
    return action
```

구조적으로는 다음과 같이 발전한다.

```text
현재

Random Agent
     ↓
select_action()
     ↓
Action
```

이후:

```text
State
  ↓
Q-Learning Agent
  ↓
select_action(state)
  ↓
Action
```

따라서 이번 함수 분리는 이후 학습 Agent를 구현하기 위한 기본 구조가 된다.

---

## Function Parameter

현재 `select_action()` 함수에는 입력값이 없다.

```python
def select_action():
```

하지만 함수는 외부에서 값을 입력받을 수도 있다.

예를 들어:

```python
def print_position(position):
    print(position)
```

다음과 같이 값을 전달할 수 있다.

```python
print_position([1, 2])
```

여기서 `position`을 함수의 Parameter라고 한다.

이 개념은 이후 다음 형태에서 사용하게 된다.

```python
select_action(state)
```

즉 Agent가 현재 State를 입력받아 Action을 선택하게 된다.

---

## Current Agent-Environment Flow

현재 구조는 다음과 같다.

```text
Initialize State
      ↓
select_action()
      ↓
Random Action
      ↓
Environment
      ↓
Boundary Check
      ↓
Next State
      ↓
Reward
      ↓
Goal Check
      ↓
done
```

Agent의 Action Selection과 Environment의 State Transition 역할이 점점 분리되고 있다.

---

## Python Concepts

이번 단계에서 새롭게 사용한 Python 문법과 개념:

* `def`
* Function
* Function Call
* `return`
* Parameter의 기본 개념
* 역할 분리
* 코드 재사용

---

## Next

다음 단계에서는 Environment의 이동 처리 로직도 함수로 분리한다.

현재 Episode Loop 내부에 있는:

```python
if action == 0:
    ...

elif action == 1:
    ...

elif action == 2:
    ...

elif action == 3:
    ...
```

부분을 다음과 같은 함수로 변경한다.

```python
def move_agent(position, action):
    ...
```

이를 통해 구조를 다음과 같이 발전시킨다.

```text
Agent
  ↓
select_action()

Environment
  ↓
move_agent()

Episode Loop
```

Agent와 Environment의 역할을 더 명확하게 분리하는 것이 다음 목표이다.

## Environment Logic Refactoring

이번 단계에서는 Episode Loop 내부에 있던 Environment 관련 로직을 함수로 분리한다.

기존에는 `while` 내부에서 이동 처리, Boundary Check, Reward 계산, Goal Check를 모두 직접 수행했다.

이제 각 역할을 별도의 함수로 나눈다.

```text
Agent
  ↓
select_action()

Environment Transition
  ↓
move_agent()

Reward / Termination
  ↓
check_goal()
```

---

## move_agent()

Agent의 현재 위치와 Action을 입력받아 다음 위치를 계산한다.

```python
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
```

입력:

```text
position
action
```

출력:

```text
next position
```

예를 들어:

```text
position = [0, 0]
action = 3
```

이라면:

```text
[0, 0]
   ↓ RIGHT
[1, 0]
```

이 된다.

Episode Loop에서는 다음과 같이 사용한다.

```python
agent_position = move_agent(agent_position, action)
```

이 코드는 다음 의미를 가진다.

```text
현재 State
    ↓
Action
    ↓
move_agent()
    ↓
Next State
    ↓
agent_position에 다시 저장
```

강화학습 관점에서는 다음 State Transition과 연결된다.

```text
S_t
 ↓
A_t
 ↓
Environment
 ↓
S_(t+1)
```

---

## Function Parameters

이번 단계에서는 함수에 여러 값을 입력으로 전달한다.

```python
def move_agent(position, action):
```

여기서:

```text
position
action
```

은 함수의 Parameter이다.

함수를 호출할 때 실제 값을 전달한다.

```python
move_agent(agent_position, action)
```

예를 들어:

```text
agent_position = [1, 2]
action = 3
```

이라면 함수 내부에서는 개념적으로:

```text
position = [1, 2]
action = 3
```

으로 사용된다.

---

## check_goal()

Reward 계산과 Goal 도착 여부 확인도 함수로 분리한다.

```python
def check_goal(position, goal_position):

    if position == goal_position:
        reward = 10
        done = True

    else:
        reward = -1
        done = False

    return reward, done
```

이 함수는 현재 Position과 Goal Position을 비교한다.

Goal에 도착했다면:

```text
reward = 10
done = True
```

Goal에 도착하지 않았다면:

```text
reward = -1
done = False
```

를 반환한다.

---

## Multiple Return Values

Python에서는 하나의 함수에서 여러 값을 반환할 수 있다.

```python
return reward, done
```

함수를 호출할 때도 두 개의 변수로 받을 수 있다.

```python
reward, done = check_goal(agent_position, goal_position)
```

예를 들어 함수에서 다음 값을 반환했다고 하자.

```text
reward = 10
done = True
```

그러면:

```python
reward, done = check_goal(...)
```

실행 후:

```text
reward → 10
done   → True
```

가 된다.

---

## Current Episode Loop

함수 분리 이후 Episode Loop는 훨씬 단순해졌다.

핵심 부분은 다음과 같다.

```python
while not done and step < max_steps:

    action = select_action()

    agent_position = move_agent(agent_position, action)

    reward, done = check_goal(
        agent_position,
        goal_position
    )

    total_reward += reward

    step += 1
```

각 코드의 역할은 다음과 같다.

```text
select_action()
→ Agent가 행동을 선택

move_agent()
→ Environment가 Action에 따라 State 변경

check_goal()
→ Reward 및 Episode 종료 여부 결정
```

---

## Agent and Environment Separation

현재 구조는 다음과 같이 역할이 분리되어 있다.

```text
          Agent
            │
            ▼
    select_action()
            │
          Action
            │
            ▼
       Environment
            │
            ▼
       move_agent()
            │
         Next State
            │
            ▼
       check_goal()
         ↙      ↘
      Reward    done
```

아직 완전히 독립된 Environment 객체를 만든 것은 아니지만, Agent와 Environment의 책임을 분리하기 시작한 상태이다.

---

## RL Connection

최종적으로 만들 RL Environment에서는 다음과 같은 형태를 사용하게 된다.

```python
next_state, reward, done = env.step(action)
```

현재 구현에서는 이 `step()` 내부에서 일어날 일을 각각 직접 구현하고 있다.

```text
env.step(action)
      │
      ├─ State Transition
      │    → move_agent()
      │
      ├─ Reward Calculation
      │    → check_goal()
      │
      └─ Episode Termination
           → done
```

따라서 현재 함수 분리는 이후 `Environment.step()`을 구현하기 위한 중간 단계이다.

---

## Python Concepts

이번 단계에서 새롭게 사용하거나 더 구체적으로 학습한 개념:

* Function Parameter
* 여러 Parameter 전달
* Multiple Return Values
* `return reward, done`
* `reward, done = ...`
* 함수 역할 분리
* Agent / Environment 책임 분리
* State Transition

---

## Next

다음 단계에서는 현재 함수들을 더 정리하여 GridWorld Environment의 구조를 만든다.

현재:

```text
select_action()
move_agent()
check_goal()
```

구조를 발전시켜 최종적으로 다음 형태를 목표로 한다.

```python
next_state, reward, done = step(action)
```

즉 Environment가 하나의 Action을 입력받으면:

```text
Action
  ↓
State Transition
  ↓
Reward
  ↓
done
```

을 한 번에 처리하도록 만든다.

이 단계는 이후 `GridWorld` 클래스를 만들기 위한 직접적인 준비 과정이다.


## GridWorld Class

마지막 단계에서는 지금까지 만든 Environment 로직을 `GridWorld` 클래스로 묶는다.

```python
class GridWorld:
```

클래스는 관련된 데이터와 함수를 하나의 객체로 묶기 위한 구조이다.

GridWorld Environment는 다음 데이터를 가진다.

```text
agent_position
goal_position
```

그리고 다음 기능을 가진다.

```text
reset()
step(action)
```

### **init**

```python
def __init__(self):
    self.agent_position = [0, 0]
    self.goal_position = [3, 3]
```

객체가 처음 생성될 때 실행되는 초기화 함수이다.

### self

`self`는 현재 GridWorld 객체 자기 자신을 의미한다.

```python
self.agent_position
```

은 현재 Environment가 가지고 있는 Agent 위치이다.

### reset

```python
state = env.reset()
```

Episode를 시작할 때 Agent를 초기 위치로 되돌리고 초기 State를 반환한다.

### step

```python
next_state, reward, done = env.step(action)
```

Action을 입력받아 다음 과정을 수행한다.

```text
Action
  ↓
State Transition
  ↓
Boundary Check
  ↓
Reward
  ↓
Goal Check
  ↓
Next State / Reward / Done
```

현재 GridWorld는 실제 강화학습 Environment의 기본 인터페이스인 다음 구조를 갖게 되었다.

```python
state = env.reset()

next_state, reward, done = env.step(action)
```

이로써 04-01에서는 Python 기초와 RL Environment의 가장 기본적인 구조를 직접 구현했다.
