
from object import Actor, Circle, Object, Pos


class SceneBase(Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_remove = False


class SciarioBase(Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_remove = False


class MainScene(SceneBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.actor_list = []
        self.actor_dict = {}
        self.scinario_list = []

    def initialize(self):

        # 첫번쨰 시나리오
        # Chapter 가있고 안에 Schedule 이 있고
        # 두개 위치 변환 한개씩
        self.scinario = {
            'init': [
                # (행동, 대상, 클래스, 점수)
                ('make', 'actor_1', 'Circle', 48),
                ('make', 'actor_2', 'Circle', 30),
                ('make', 'actor_3', 'Circle', 25),
            ],
            'rounds': [
                [  # 1
                    # (행동, 대상, 위치, 시간)
                    ('move', 'actor_1', Pos(200, 200), 0),
                    ('move', 'actor_2', Pos(100, 200), 0),
                    ('move', 'actor_3', Pos(100, 100), 0),
                ],
                [  # 2
                    ('move', 'actor_1', Pos(100, 200), 0),
                    ('move', 'actor_2', Pos(100, 100), 0),
                    ('move', 'actor_3', Pos(200, 100), 0),
                ],
                [
                    ('move', 'actor_1', Pos(150, 150), 0),
                    ('move', 'actor_2', Pos(150, 150), 0),
                    ('move', 'actor_3', Pos(150, 150), 0),
                ]
            ],
        }

    def play(self):
        pass