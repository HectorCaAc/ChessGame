import pyglet

pyglet.resource.path=['./resources']
pyglet.resource.reindex()

white_pawns = pyglet.resource.image('Chess_plt60.png')
black_pawns = pyglet.resource.image('Chess_pdt60.png')

white_rook = pyglet.resource.image('Chess_rlt60.png')
black_rook = pyglet.resource.image('Chess_rdt60.png')

white_bishop = pyglet.resource.image('Chess_blt60.png')
black_bishop = pyglet.resource.image('Chess_bdt60.png')

white_queen = pyglet.resource.image('Chess_qlt60.png')
black_queen = pyglet.resource.image('Chess_qdt60.png')

white_king = pyglet.resource.image('Chess_klt60.png')
black_king = pyglet.resource.image('Chess_kdt60.png')
                                    