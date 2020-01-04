from graphics import *
from tetris_midori import *
 
game = Game(12,20)
game.drop_random_shapes()

game.win.mainloop()
