# Name : Isabella Wang

# This file helps you start making tetris pieces, or tetronimoes.

from graphics import *
import time
import random

corners = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
# a list of grid points for 4 corner blocks (clockwise)
edges = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# a list of grid points for 4 edge blocks (clockwise)
long_boi = [(2, 0), (0, 2)]
# two extra coordinates for I shapes

    
class Block(Rectangle):

    def __init__(self, p, color):
        Rectangle.__init__(self, Point(p.getX()*30, p.getY()*30), Point(p.getX()*30+30, p.getY()*30+30))
        # initialize the block as a rectangle
        self.x = p.getX()
        self.y = p.getY()
        # store x and y coordinates as attributes
        self.setFill(color)

    def move(self, dx, dy):
        Rectangle.move(self, 30*dx, 30*dy)
        # move the block with actual (pixel system) dx and dy 
        self.x += dx
        self.y += dy
        # increment x and y coordinates after each movement

    def can_move(self, dx, dy, r, c, blocks):
        if self.x + dx >= c or self.y + dy >= r or self.x + dx < 0:
            return False
        for b in blocks:
            if self.x +dx == b.x and self.y + dy == b.y:
                # check for stacking
                return False
        return True

class Shape(object):
    def __init__(self, coords, color):
        self.blocks = []
        for i in coords:
            self.blocks.append(Block(i, color))
        # make a list of blocks from the list of coordinates
        self.rotated = False
        self.center_block = self.blocks[2]

    def move(self, dx, dy):
        for b in self.blocks:
            b.move(dx, dy)
            # move each block 

    def draw(self, win):
        for b in self.blocks:
            b.draw(win)
            # draw each block

    def can_move(self, dx, dy, r, c, blocks):
        for b in self.blocks:
            if not b.can_move(dx, dy, r, c, blocks):
                # check if one block is off the grid
                return False
        return True
        # After the for loop ensures all 4 blocks are movable, the shape is movable
    
    def rotate(self):
        x0, y0 = self.center_block.x, self.center_block.y
        for b in self.blocks:
            x = b.x - x0
            y = b.y - y0
            if x == y == 0:
                continue
            # calculate the relative grid point with the center block being the origin
            if (x, y) in corners:
                # corner blocks 
                i = corners.index((x,y))
                x_new, y_new = corners[(i+1)%len(corners)]
            elif (x, y) in edges:
                # edge blocks
                i = edges.index((x,y))
                x_new, y_new = edges[(i+1)%len(corners)]
            else:
                i = long_boi.index((x,y))
                # the left most block in the I_Shape tetrominoes
                x_new, y_new = long_boi[(i+1)%len(long_boi)]
            b.move(x_new - x, y_new - y)

    def undraw(self):
        for b in self.blocks:
            b.undraw()
    
    def can_rotate(self, r, c, blocks):
        x0, y0 = self.center_block.x, self.center_block.y
        for b in self.blocks:
            x = b.x - x0
            y = b.y - y0
            if x == y == 0:
                continue
                # skip the center block
            # calculate the relative grid point with the center block being the origin
            if (x, y) in corners:
                # corner blocks 
                i = corners.index((x,y))
                x_new, y_new = corners[(i+1)%len(corners)]
            elif (x, y) in edges:
                # edge blocks
                i = edges.index((x,y))
                x_new, y_new = edges[(i+1)%len(corners)]
            else:
                # the rightmost block in the I_Shape tetrominoes
                i = long_boi.index((x,y))
                x_new, y_new = long_boi[(i+1)%len(long_boi)]
            if not b.can_move(x_new - x, y_new - y, r, c, blocks):
                return False
        return True


class I_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x + 2, center.y),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "blue")

class J_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x + 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "orange")
        
class L_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "cyan")
        
class O_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x , center.y + 1)]
        Shape.__init__(self, coords, "red")

    def rotate(self):
        pass
        # ensures that O_shape does not rotate

        
class S_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x, center.y + 1),
                  Point(center.x - 1, center.y + 1),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "green")
    
        
class T_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x + 1, center.y)]
        Shape.__init__(self, coords, "yellow")
        
class Z_shape(Shape):
    def __init__(self, center):
        coords = [Point(center.x + 1, center.y + 1),
                  Point(center.x - 1, center.y),
                  Point(center.x    , center.y),
                  Point(center.x, center.y + 1)]
        Shape.__init__(self, coords, "purple")



shape_dict = {'I': I_shape,
              'J': J_shape,
              'L': L_shape,
              'O': O_shape,
              'S': S_shape,
              'T': T_shape,
              'Z': Z_shape,
              }



class Game(object):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.win =  GraphWin("Tetronimoes", cols*50, rows*30)
        # initialize a game window with given cols and rows
        border = Line(Point(cols*30, 0), Point(cols*30, rows*30))
        border.setWidth(5)
        border.draw(self.win)
        # draw a border that divides the game and the preview 
        self.current_shape = None
        self.stationary_blocks = []
        self.key=None
        self.win.bind_all('<Key>',self.key_pressed)
        # initialize the keypress variable
        self.score = 0
        self.score_text = Text(Point(self.cols*25,10), "Score: " + str(self.score))
        self.score_text.draw(self.win)
        # initialize the score and the text that displays the score on the top right corner
        self.level = 1
        self.level_text = Text(Point(self.cols*5,10), "Level: " + str(self.level))
        self.level_text.draw(self.win)
        # initialize the level and the text that displays the score on the top left corner
        self.preview_list = [self.get_random_shape(), self.get_random_shape(), self.get_random_shape()]
        # initialize a queue of three random shapes
        next_text = Text(Point(cols*35, 20), "NEXT")
        next_text.setSize(28)
        next_text.draw(self.win)
        # initialize the title for the preview
        y = 2
        self.drawn_shapes = []
        # initialize a queue of shape objects
        for s in self.preview_list:
            shape = shape_dict[s](Point(cols + 2,y))
            self.drawn_shapes.append(shape)
            shape.draw(self.win)
            y += 3
        # draw all the shapes in the queue

            
    def add_drop_shape(self, shape):
        s = shape_dict[shape](Point(self.cols/2, 0))
        self.current_shape = s
        s.draw(self.win)
        while s.can_move(0, 1, self.rows, self.cols, self.stationary_blocks):
            s.move(0,1)
            for i in range(3):
                self.handle_keypress(self.key)
                self.key = None
                # reset the key
                time.sleep(0.1/self.level)
                # shapes move faster when the level gets higher
            self.score_text.setText("Score: " + str(self.score))
            if self.score  == self.level*100:
                # the level goes up after evey 100 points
                level_up = Text(Point(self.cols*15, self.rows*15), "LEVEL UP!")
                level_up.setSize(30)
                level_up.draw(self.win)
                # display a message "LEVEL UP"
                self.level += 1
                time.sleep(1)
                level_up.undraw()
                self.level_text.setText("Level: " + str(self.level))
                # update the level text displayed on the top left corner
        self.stationary_blocks.extend(s.blocks)

    def key_pressed(self,event):
        self.key=event.keysym

    def handle_keypress(self, key):
        '''
        Helper function: handle keypress and move current_shape accordingly
        '''
        s = self.current_shape
        if key == 'Right':
            if self.current_shape.can_move(1,0, self.rows, self.cols,self.stationary_blocks):
                s.move(1,0)
        elif key == 'Left':
            if self.current_shape.can_move(-1, 0, self.rows, self.cols, self.stationary_blocks):
                s.move(-1, 0)
        elif key == 'Down':
            while s.can_move(0, 1, self.rows, self.cols, self.stationary_blocks):
                s.move(0,1)
        elif key == 'Up':
            if s.can_rotate(self.rows, self.cols, self.stationary_blocks):
                s.rotate()
        self.key = None
                

    def check_full(self):
        '''
        Helper function: check all the rows for full rows and return a list of row numbers
        '''
        result = []
        status = [0]*self.rows
        # initialize the number of blocks in each row as 0 (a bin with no blocks)
        for b in self.stationary_blocks:
            status[int(b.y)] += 1
            # increment the bin (the number at index y) accordingly
        for i in range(self.rows):
            if status[i] == self.cols:
                result.append(i)
                # add the row number to the result list
                self.score += 10
                # update the score
        return result

    def eliminate_row(self, r):
        '''
        Helper funcion: undraws all the blocks in a specific row and delete them from stationary_blocks
        '''
        deleted = []
        # initialize a to-be-deleted list of blocks
        for b in self.stationary_blocks:
            if b.y == r:
                # check the row number of the block
                b.undraw()
                # undraw the block in the row
                deleted.append(b)
        for d in deleted:
            self.stationary_blocks.remove(d)
            # remove the blocks from stationary_blocks
                
    def move_down(self, r):
        '''
        Helper function: move every block above the cleared row down 
        '''
        for b in self.stationary_blocks:
            if b.y < r and b.y > 0:
                # check if the block is above the clear row and in the game window
                b.move(0,1)

    def get_random_shape(self):
        '''
        Helper function: return a random shape letter
        '''
        shapes = list(shape_dict.keys())
        # get a list of shape letters
        return shapes[random.randint(0,len(shapes)-1)]

    def drop_random_shapes(self):
        while not self.end_game():
            current_shape = self.preview_list[-1]
            self.drawn_shapes[-1].undraw()
            # undraw the last shape in the queue
            self.drawn_shapes[0].move(0,3)
            self.drawn_shapes[1].move(0,3)
            # move the next two down 
            self.preview_list = [self.get_random_shape()] + self.preview_list[:2]
            # update preview_list with a new shape letter
            self.drawn_shapes = [shape_dict[self.preview_list[0]](Point(self.cols+2, 2))]+ self.drawn_shapes[:2]
            # update drawn_shapes with a new shape object
            self.drawn_shapes[0].draw(self.win)
            # draw the new shape
            self.add_drop_shape(current_shape)
            # drop the new_shape
            for r in self.check_full():
                # check full rows
                self.eliminate_row(r)
                # clear full rows
                self.move_down(r)
                # move everything else down
        game_over_text = Text(Point(self.cols*15, self.rows*15), "GAME OVER")
        game_over_text.setSize(30)
        game_over_text.draw(self.win)
        # draw the text 'GAME OVER'

    def end_game(self):
        '''
        Helper function: determines if the game is over or not by checking if the last shape in the queue is touching the ceiling
        '''
        to_be_dropped = shape_dict[self.preview_list[-1]](Point(self.cols/2, 0))
        return not to_be_dropped.can_move(0, 0, self.rows, self.cols, self.stationary_blocks)




