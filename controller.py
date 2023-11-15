from object import Object, Pos


class Controller(Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_remove = False
        
        