import pygame
import sys

from actor_manager import ActorManager

from object import Circle
# Pygame 초기화

pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 창 제목 설정
pygame.display.set_caption("Pygame Tutorial")

# 색깔 정의
COLOR_RED = (255, 0, 0)

clock = pygame.time.Clock()
fps = 60

#객체 리스트
objects = []


am = ActorManager()

# 게임 루프
running = True

prev_dt = clock.tick(fps)

while running:
    # 시간 갱신 및 소요시간 계산
    dt = clock.tick(fps)
    elapsed_time = (dt - prev_dt) / 1000
    prev_dt = dt


    # 이벤트 컨트롤
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos

                # 기존 객체 클릭여부 확인
                for obj in objects:
                    if obj.is_pick(x, y):
                        objects.remove(obj)
                        break
                else:
                    objects.append(Circle(x=x, y=y, radius=50, color=COLOR_RED))

        
    
    # 오브젝트 업데이트
    am.action(dt / 1000)

    # 화면 업데이트
    screen.fill((0, 0, 0))  # 검은색 배경 채우기
    am.draw(screen)

    # 화면 갱신
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
