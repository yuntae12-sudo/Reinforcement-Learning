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
