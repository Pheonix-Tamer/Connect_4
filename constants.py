SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

GAME_FPS = 60

# Grid needs to be 7×6
GRID_DIMENSIONS = (6, 7)
board_ratio = GRID_DIMENSIONS[0]/GRID_DIMENSIONS[1]
BOARD_WIDTH = 600
BOARD_HEIGHT = board_ratio * BOARD_WIDTH
BOARD_GRID_WIDTH = BOARD_WIDTH/7
BOARD_CIRCLE_RADIUS = (BOARD_GRID_WIDTH/2) - (0.1 * BOARD_GRID_WIDTH)

CHIP_RADIUS = (BOARD_GRID_WIDTH/2) - (0.1 * BOARD_GRID_WIDTH/2)