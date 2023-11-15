
import pygame
import math



class Pos():
    ''' 위치 정보를 가지는 immutable 객체
    '''
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)
    
    def __repr__(self):
        return f'Pos({self.x}, {self.y})'
    
    


class Object():
    ''' 모든 객체에 대한 기본 객체'''
    def __init__(self, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        
    def draw(self, screen):
        pass

    # 범위 안에 있는지 확인
    def is_pick(self, x, y):
        pass

    def pos(self):
        return Pos(self.x, self.y)


    

class Actor(Object):
    ''' 액션을 가질 수 있는 객체
    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.action_list = []

    def add_action(self, action):
        self.action_list.append(action)

    def action(self, elapsed_time):
        if self.action_list:
            for action in self.action_list:
                action(elapsed_time)




class Circle(Actor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = kwargs.get('radius', 0)
        self.color = kwargs.get('color', (0, 0, 0))
        self.text = kwargs.get('text', 'NA')

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        font = pygame.font.SysFont('malgungothic', 20)
        text = font.render(self.text, True, (255, 255, 255))
        screen.blit(text, (self.x - 10, self.y - 10))

    def is_pick(self, x, y):
        distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        if distance < self.radius:
            return True
        else:
            return False
        