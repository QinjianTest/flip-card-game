import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 设置游戏窗口的尺寸
screen_width, screen_height = 1200, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("翻牌记忆")

# 定义颜色
EYE_CARE_COLOR = (199, 237, 204)  # 护眼色背景
BLACK = (0, 0, 0)  # 黑色，用于字体
GRAY = (169, 169, 169)  # 灰色，用于按钮背景
WHITE = (255, 255, 255)  # 白色
DARK_GRAY = (105, 105, 105)  # 深灰色，用于阴影


# 定义卡片类
class Card():
    def __init__(self, x, y, size, image, value):
        # 初始化卡片属性
        self.rect = pygame.Rect(x, y, size, size)
        self.image = pygame.transform.scale(image, (size, size))
        self.value = value
        self.is_flipped = False

    def draw(self, screen):
        # 绘制卡片
        if self.is_flipped:
            screen.blit(self.image, self.rect.topleft)  # 翻转时显示图片
        else:
            pygame.draw.rect(screen, BLACK, self.rect)  # 未翻转时显示黑色

    def flip(self):
        # 翻转卡片的状态
        self.is_flipped = not self.is_flipped


def initialize_game():
    # 加载图片
    images = [pygame.image.load(f'image{i}.png') for i in range(1, 6)]

    # 定义卡片的初始数据，5对卡片，每对具有相同的图片和值
    card_data = [(images[i], f"Value{i}") for i in range(5)] * 2  # 每种图片有两张

    # 随机打乱卡片数据
    random.shuffle(card_data)

    # 定义卡片位置（5x2的网格），包括间距
    card_size = 200
    margin = 20
    # 计算起始位置以居中显示
    start_x = (screen_width - (5 * card_size + 4 * margin)) // 2
    start_y = (screen_height - (2 * card_size + margin)) // 2
    positions = [(start_x + (i % 5) * (card_size + margin), start_y + (i // 5) * (card_size + margin)) for i in
                 range(10)]

    # 创建卡片列表
    cards = []
    for i in range(10):
        x, y = positions[i]
        image, value = card_data[i]
        card = Card(x, y, card_size, image, value)
        cards.append(card)

    return cards


# 初始化游戏状态
cards = initialize_game()
first_card = None
second_card = None
show_delay = False
game_won = False

# 主游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_won:
                # 检查Success和Retry按钮是否被点击
                if success_rect.collidepoint(event.pos):
                    running = False  # 点击成功提示后关闭窗口
                elif retry_rect.collidepoint(event.pos):
                    # 重新开始游戏
                    cards = initialize_game()
                    first_card = None
                    second_card = None
                    show_delay = False
                    game_won = False
            elif not show_delay:
                for card in cards:
                    if card.rect.collidepoint(event.pos) and not card.is_flipped:
                        card.flip()
                        if first_card is None:
                            first_card = card
                        elif second_card is None:
                            second_card = card
                            show_delay = True

    # 用护眼色填充整个屏幕背景
    screen.fill(EYE_CARE_COLOR)

    # 绘制所有卡片
    for card in cards:
        card.draw(screen)

    # 如果需要展示延迟
    if show_delay and second_card:
        pygame.display.flip()
        pygame.time.wait(1000)
        if first_card.value != second_card.value:
            # 如果不匹配，翻回去
            first_card.flip()
            second_card.flip()
        # 重置状态
        first_card = None
        second_card = None
        show_delay = False

    # 检查所有卡片是否都已翻开
    if all(card.is_flipped for card in cards):
        game_won = True
        font = pygame.font.SysFont(None, 74)
        success_text = font.render('Success', True, BLACK)
        success_rect = success_text.get_rect(center=(screen_width / 2, screen_height / 2 - 50))

        # 绘制按钮阴影
        shadow_rect = success_rect.inflate(40, 40)
        shadow_rect.topleft = (shadow_rect.x + 5, shadow_rect.y + 5)
        pygame.draw.rect(screen, DARK_GRAY, shadow_rect, border_radius=10)

        # 绘制灰色按钮背景
        pygame.draw.rect(screen, GRAY, success_rect.inflate(40, 40), border_radius=10)
        screen.blit(success_text, success_rect)

        # 绘制Retry按钮
        retry_text = font.render('Retry', True, BLACK)
        retry_rect = retry_text.get_rect(center=(screen_width / 2, screen_height / 2 + 50))
        pygame.draw.rect(screen, GRAY, retry_rect.inflate(40, 40), border_radius=10)
        screen.blit(retry_text, retry_rect)

    # 更新显示
    pygame.display.flip()

# 退出Pygame
pygame.quit()
sys.exit()
