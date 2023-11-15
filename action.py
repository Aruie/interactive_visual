#%%
from object import Object, Pos, Actor
from abc import abstractmethod



class ActionBase(Object):
    def __init__(self, actor: Actor, duration: float, **kwargs):
        super().__init__(**kwargs)
        self.actor = actor          # 액션을 가진 객체
        self.duration = duration    # 액션 지속 시간
        self.is_remove = False      # 액션 종료 여부

    @abstractmethod
    def run(self, elapsed_time):
        pass


class MoveLinearByPosition(ActionBase):
    def __init__(self, target_pos: Pos, **kwargs):
        super().__init__(**kwargs)
        self.velocity = Pos(target_pos.x / self.duration, target_pos.y / self.duration)

    def run(self, elapsed_time):
        # 이동할 시간 계산 ( 최대 duration )
        elapsed_time = min(elapsed_time, self.duration)
        # 액터 이동
        self.actor.x += self.velocity.x * elapsed_time
        self.actor.y += self.velocity.y * elapsed_time

        # 남은 시간 계산
        self.duration -= elapsed_time
        if self.duration <= 0:
            self.is_remove = True



if __name__ == '__main__':
    actor = Actor(x=0, y=0)
    act = MoveLinearByPosition(actor = actor, target_pos=Pos(100, 100), duration=10)
    for i in range(12):
        act.run(0.3)
        print(actor.pos())
        
# 이동할 거리        

    

