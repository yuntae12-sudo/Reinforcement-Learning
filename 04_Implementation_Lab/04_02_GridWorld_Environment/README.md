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
