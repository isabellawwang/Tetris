from graphics import *
from tetris import *
 
game = Game(12,20)
game.drop_random_shapes()

game.win.mainloop()
