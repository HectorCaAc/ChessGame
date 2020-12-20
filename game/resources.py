import pyglet

pyglet.resource.path=['./resources']
pyglet.resource.reindex()

white_pawns = pyglet.resource.image('Chess_plt60.png')
black_pawns = pyglet.resource.image('Chess_pdt60.png')

black_rook = pyglet.resource.image('Chess_rdt60.png')
white_rook = pyglet.resource.image('Chess_rlt60.png')

black_bishop = pyglet.resource.image('Chess_bdt60.png')
white_bishop = pyglet.resource.image('Chess_blt60.png')
                                    