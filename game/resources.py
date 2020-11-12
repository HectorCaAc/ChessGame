import pyglet

pyglet.resource.path=['./resources']
pyglet.resource.reindex()

white_pawns = pyglet.resource.image('Chess_plt60.png')
black_pawns = pyglet.resource.image('Chess_pdt60.png')