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
