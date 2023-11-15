
from object import Actor
from itertools import chain

class ActorManager():
    ''' 액터 관리 클래스 ( 현재는 모든 루프를 관리 )
    '''
    def __init__(self):
        self.actor_list = []
        self.actor_dict = {}

    def add_actor(self, actor, tag=None):
        if tag: 
            if tag in self.actor_dict:
                print('Tag already exists')
            else:
                self.actor_dict[tag] = actor
        else:
            self.actor_list.append(actor)

    def remove_actor(self, tag):
        del self.actor_dict[tag]

    def action(self, elapsed_time):
        for actor in chain(self.actor_list, self.actor_dict.values()):
            actor.action(elapsed_time)

    def draw(self, screen):
        for actor in chain(self.actor_list, self.actor_dict.values()):
            actor.draw(screen)


if __name__ == '__main__':
    am = ActorManager()
    from object import Pos
    from action import MoveLinearByPosition

    am.print_actors = lambda: print(am.actor_list, am.actor_dict)

    actor = Actor(x=0, y=0)
    act = MoveLinearByPosition(actor = actor, target_pos=Pos(100, 100), duration=10)
    actor.add_action(act)
    am.add_actor(actor, 'actor')

    am.action(1)
    am.action(1)
