
from object import Object, Pos, Actor

from object import Circle


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

        scinario = [
            ('make', 'Circle', ), )
        ]
        