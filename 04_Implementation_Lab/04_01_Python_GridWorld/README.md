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
