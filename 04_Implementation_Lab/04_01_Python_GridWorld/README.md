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
