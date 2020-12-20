import pyglet
from pyglet import shapes

from game import board, controller, load, pawn, resources

pyglet.options['debug_gl'] = False

# something to do is smaller is way to big right now
game_window = pyglet.window.Window(800,700, resizable=True)

main_batch = pyglet.graphics.Batch()

# View
board_view = board.Board(main_batch)

# Controller
board_control = controller.Controller(board_view, main_batch)
board_control.draw_pawns()
board_control.draw_rooks()
board_control.draw_bishops()
board_control.draw_queens()
board_control.draw_kings()
board_control.draw_knigths()

# Lets assume that the player selected white for now
# black_paws = load.paws("black", 225,925, 100, main_batch)

game_window.push_handlers(board_control)

@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    # vertex_list.draw()


if __name__ == '__main__':
    # I am not sure that this timer is required for this project
    # pyglet.clock.schedule_interval(on_draw, 1/120.0)

    pyglet.app.run()