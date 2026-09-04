# 04-02. GridWorld Environment 직접 구현

## 구현 내용

강화학습 Agent가 사용할 수 있는 형태로 GridWorld Environment를 구현했다.

### Environment 구성

* Grid Size: `4 x 4`
* Start State: `(0, 0)`
* Goal State: `(3, 3)`
* Action Space

  * `0`: UP
  * `1`: DOWN
  * `2`: LEFT
  * `3`: RIGHT

### 주요 함수

* `reset()`

  * Episode 시작 시 Agent를 Start State로 초기화

* `get_next_state(action)`

  * 현재 State와 Action을 이용해 Next State 계산
  * Grid 경계를 벗어나지 않도록 제한

* `calculate_reward(state)`

  * 일반 이동: `-1`
  * Goal 도착: `+10`

* `check_done(state)`

  * Goal 도착 여부 확인

* `step(action)`

  * Action을 입력받아 Environment 상태를 변경
  * `next_state`, `reward`, `done` 반환

* `render()`

  * 현재 Grid와 Agent 위치 출력

### Episode 제한

Random Agent가 Goal에 도착하지 못하고 계속 움직이는 것을 방지하기 위해 최대 Step을 `50`으로 설정했다.

### 강화학습 관점

이번 단계에서 Environment와 Agent의 역할을 분리했다.

```text
Agent
  ↓ Action
Environment
  ↓
Next State
Reward
Done
```

현재 Agent는 Random Policy를 사용하지만, 이후 Q-Learning Agent로 교체하더라도 Environment 구조는 그대로 사용할 수 있다.

## GridWorld 확장

기본 Environment에 장애물과 matplotlib 시각화를 추가했다.

### Obstacle

```text
S . . .
. X . .
. X . .
. . . G
```

* Obstacle: `(1, 1)`, `(2, 1)`
* 장애물과 충돌하면 Episode 종료

### Reward

* 일반 이동: `-1`
* Goal 도착: `+10`
* Obstacle 충돌: `-10`

### Episode 종료 조건

Episode는 다음 조건 중 하나를 만족하면 종료된다.

1. Goal 도착
2. Obstacle 충돌
3. 최대 Step `50` 도달

### Visualization

`matplotlib`을 이용하여 GridWorld 상태를 실시간으로 확인할 수 있도록 구현했다.

* Agent: 원
* Goal: 별
* Obstacle: 사각형
* 현재 Step 표시

Episode 종료 후 마지막 상태를 잠시 표시한 뒤 matplotlib 창도 자동으로 종료된다.

### 강화학습 관점

Reward 설계를 통해 Agent에게 직접 경로를 지정하지 않고,

```text
Goal 도착       → 보상
일반 이동       → 작은 페널티
Obstacle 충돌   → 큰 페널티
```

를 제공한다.

향후 Q-Learning Agent는 이 Reward를 기반으로 충돌을 피하면서 Goal까지 이동하는 Policy를 학습하게 된다.


## Random Agent 반복 실험

GridWorld Environment가 정상적으로 동작하는지 확인하고, 향후 Q-Learning Agent와 비교하기 위한 기준 성능을 만들기 위해 Random Agent를 여러 Episode 반복 실행하도록 확장했다.

### Multi-Episode 구조

총 `100 Episode`를 반복 실행한다.

```text
Episode 1
  ├── Step 1
  ├── Step 2
  └── ...

Episode 2
  ├── Step 1
  └── ...

...

Episode 100
```

각 Episode가 시작될 때 `reset()`을 호출하여 Agent의 위치와 Step 수를 초기화한다.

각 Step에서는 Random Policy를 사용한다.

```python
action = random.randint(0, 3)
```

따라서 현재 Agent는 State를 이용하여 행동을 판단하거나 학습하지 않고, 4개의 Action 중 하나를 무작위로 선택한다.

### Episode 결과 기록

각 Episode마다 다음 정보를 기록한다.

* `Total Reward`
* `Step 수`
* `SUCCESS`
* `COLLISION`
* `MAX STEP`

Episode 종료 후에는 전체 실험 결과를 이용하여 다음 값을 계산한다.

* 전체 Episode 수
* Goal 도착 횟수
* Obstacle 충돌 횟수
* Max Step 종료 횟수
* Average Reward

### Total Reward

한 Episode 동안 받은 Reward를 누적하여 `Total Reward`를 계산한다.

```python
total_reward += reward
```

현재 Reward 구조는 다음과 같다.

```text
일반 이동       -1
Goal 도착      +10
Obstacle 충돌  -10
```

따라서 짧은 Step으로 Goal에 도착할수록 높은 Total Reward를 얻고, 충돌하거나 불필요하게 많은 Step을 사용하는 경우 낮은 Reward를 얻는다.

### Reward Visualization

100 Episode 실행 후 `matplotlib`을 이용하여 Episode별 Total Reward를 그래프로 표시한다.

```text
X축 : Episode
Y축 : Total Reward
```

Random Agent는 학습을 하지 않기 때문에 Episode가 증가하더라도 Reward가 지속적으로 향상되는 경향은 나타나지 않는다.

이 결과는 이후 구현할 Q-Learning Agent와 비교하기 위한 Baseline으로 사용한다.

### 강화학습 관점

현재 구조는 강화학습의 기본적인 반복 구조를 가진다.

```text
전체 학습
│
├── Episode
│   │
│   ├── State
│   ├── Action
│   ├── Reward
│   ├── Next State
│   └── ...
│
└── 다음 Episode
```

현재는 Random Policy를 사용하지만 이후 Q-Learning에서는 같은 Environment를 유지한 채,

```text
Random Action
      ↓
Q-Table 기반 Action 선택
      ↓
Q-Value Update
      ↓
Policy 개선
```

구조로 확장한다.

이를 통해 Random Agent와 학습된 Q-Learning Agent의 Success Rate, Average Reward, Episode Reward 변화를 비교할 수 있다.
