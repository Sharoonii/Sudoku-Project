import pygame
# Cell (Recommended)
# This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

# Constructor for the Cell class

    def set_cell_value(self, value):
        self.value = value
# Setter for this cell’s value

    def set_sketched_value(self, value):
        self.value = value

# Setter for this cell’s sketched value

    def draw(self):
        size = 60
        bg_color = (255, 255, 255)  # white
        selected = False

        x = self.col * size
        y = self.row * size
        rect = pygame.Rect(x,y,size,size)

        pygame.draw.rect(self.screen, bg_color, rect)

        if selected:
            outline_color = (255,0,0)
        else:
            outline_color = (0,0,0)

        pygame.draw.rect(self.screen, outline_color, rect,2)

        if self.value != 0:
            num_font = pygame.font.Font(None, 400)
            num_text = num_font.render(self.value, 0, (0,0,0))
            num_text_rect = num_text.get_rect(center = (x + size/2, y + size/2))
            self.screen.blit(num_text, num_text_rect)

            # chip_x_rect = chip_x_surf.get_rect(
            #     center=(self.col * SQUARE_SIZE + SQUARE_SIZE / 2, self.row * SQUARE_SIZE + SQUARE_SIZE / 2))
            # screen.blit(chip_x_surf, chip_x_rect)
            #
            # chip_font = pygame.font.Font(None, CHIP_FONT)
            # chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
            # chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)


# Draws this cell, along with the value inside it.
# If this cell has a nonzero value, that value is displayed.
# Otherwise, no value is displayed in the cell.
# The cell is outlined red if it is currently selected.

#I almost accidentally deleted the cell class so just a backup for rn