import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Создание перса")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 139)

font = pygame.font.Font(None, 36)

races = {"Человек": {"hp": 100, "damage": 10}, "Гном": {"hp": 150, "damage": 15}, "Эльф": {"hp": 80, "damage": 8}}
professions = {"Воин": {"hp": 20, "damage": 15}, "Стрелок": {"hp": 10, "damage":15}, "Маг": {"hp": 5, "damage": 20}}
weapons = {"Меч": {"damage": 10}, "Арбалет": {"damage": 10}, "Заклинания": {"damage": 12}}


class Character:
    def __init__(self, race, profession, weapon):
        self.race = race
        self.profession = profession
        self.weapon = weapon
        self.hp = races[race]["hp"] + professions[profession]["hp"]
        self.damage = races[race]["damage"] + professions[profession]["damage"] + weapons[weapon]["damage"]

    def get_info(self):
        return [
            f"Раса: {self.race}",
            f"Профессия: {self.profession}",
            f"Оружие: {self.weapon}",
            f"HP: {self.hp}",
            f"Damage: {self.damage}"
        ]


def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def create_button(text, x, y, width, height):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    draw_text(text, x + 10, y + 10)
    return pygame.Rect(x, y, width, height)


selected_race = None
selected_profession = None
selected_weapon = None
character = None

running = True
while running:
    screen.fill(WHITE)

    draw_text("Раса:", 50, 50)
    race_buttons = [create_button(race, 50, 100 + i * 50, 200, 40) for i, race in enumerate(races)]

    draw_text("Профессия:", 300, 50)
    profession_buttons = [create_button(prof, 300, 100 + i * 50, 200, 40) for i, prof in enumerate(professions)]

    draw_text("Оружие:", 550, 50)
    weapon_buttons = [create_button(weapon, 550, 100 + i * 50, 200, 40) for i, weapon in enumerate(weapons)]

    if selected_race and selected_profession and selected_weapon:
        create_button("Создать", 300, 400, 200, 50)

    if character:
        y_position = 500
        for line in character.get_info():
            draw_text(line, 50, y_position, BLUE)
            y_position += 40

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, race in enumerate(races):
                if race_buttons[i].collidepoint(mouse_pos):
                    selected_race = race

            for i, prof in enumerate(professions):
                if profession_buttons[i].collidepoint(mouse_pos):
                    selected_profession = prof

            for i, weapon in enumerate(weapons):
                if weapon_buttons[i].collidepoint(mouse_pos):
                    selected_weapon = weapon

            if selected_race and selected_profession and selected_weapon:
                create_btn_rect = pygame.Rect(300, 400, 200, 50)
                if create_btn_rect.collidepoint(mouse_pos):
                    character = Character(selected_race, selected_profession, selected_weapon)

pygame.quit()
