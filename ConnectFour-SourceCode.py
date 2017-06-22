

# for use as a starting point for
# the Player class (and AI)
#
import random
def index_function(e,L):
    ''' this function finds the index of the element e in the list'''

    if L[0]==e:
        return 0
    else:
        return index_function(e,L[1:])+1

class Board:
    """ a datatype representing a C4 board
        with an arbitrary number of rows and cols
    """

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]
        
        # do not need to return inside a constructor!


    def __repr2__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '-'*(self.width*2) + '-\n'
        for col in range(self.width):
            s += ' ' + str(col%10)
        

        return s


        
        

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'

        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        
        for col in range( self.width ):
            s += ' ' + str(col%10)

        s += '\n'
        return s       # the board is complete, return it

    def set_board(self, LoS):
        """ this method returns a string representation
            for an object of type Board
        """
        for row in range( self.height ):
            for col in range( self.width ):
                self.data[row][col] = LoS[row][col]

    def setBoard( self, moves, show=True ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            if show: print(self)    

    def set( self, moves, show=True ):
        """ sets the board according to a string
            of turns (moves), starting with 'X'
            if show==True, it prints each one
        """
        nextCh = 'X'
        for move in moves:
            col = int(move)
            if self.allowsMove(col):
                self.addMove( col, nextCh )
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            if show: print(self)

    def clear( self ):
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def addMove( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        row = self.height - 1
        while row >= 0:
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return
            row -= 1


    def winsFor( self, ox ):
        for row in range(self.height - 3 ):
            for col in range(self.width - 3 ):
                if self.data[row][col] == ox and\
                   self.data[row+1][col+1] == ox and\
                   self.data[row+2][col+2] == ox and\
                   self.data[row+3][col+3] == ox:
                    return True

        return False
                
        

    def addMove2( self, col, ox ):
        """ adds checker ox into column col
            does not need to check for validity...
            allowsMove will do that.
        """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox

    def delMove( self, col ):
        """ removes the checker from column col """
        for row in range( self.height ):
            # look for the first nonempty row
            if self.data[row][col] != ' ':
                # put in the checker
                self.data[row][col] = ' '
                return
        # it's empty, just return
        return
        

    def allowsMove( self, col ):
        """ returns True if a move to col is allowed
            in the board represented by self
            returns False otherwise
        """
        if col < 0 or col >= self.width:
            return False
        return self.data[0][col] == ' '

    def isFull( self ):
        """ returns True if the board is completely full """
        for col in range( self.width ):
            if self.allowsMove( col ):
                return False
        return True

    def gameOver( self ):
        """ returns True if the game is over... """
        if self.isFull() or self.winsFor('X') or self.winsFor('O'):
            return True
        return False

    def isOX( self, row, col, ox ):
        """ checks if the spot at row, col is legal and ox """
        if 0 <= row < self.height:
            if 0 <= col < self.width: # legal...
                if self.data[row][col] == ox:
                    return True
        return False

    def winsFor( self, ox ):
        """ checks if the board self is a win for ox """
        for row in range( self.height ):
            for col in range( self.width ):
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col, ox ) and \
                   self.isOX( row+2, col, ox ) and \
                   self.isOX( row+3, col, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row, col+1, ox ) and \
                   self.isOX( row, col+2, ox ) and \
                   self.isOX( row, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col+1, ox ) and \
                   self.isOX( row+2, col+2, ox ) and \
                   self.isOX( row+3, col+3, ox ):
                    return True
                if self.isOX( row, col, ox ) and \
                   self.isOX( row+1, col-1, ox ) and \
                   self.isOX( row+2, col-2, ox ) and \
                   self.isOX( row+3, col-3, ox ):
                    return True
        return False

# Here is a version of hostGame for use in your Board class
#
# it simply alternates moves in the game and checks if
# the game is over at each move


    def hostGame( self ):
        """ hosts a game of Connect Four """

        nextCheckerToMove = 'X'
        
        while True:
            # print the board
            print(self)

            # get the next move from the human player...
            col = -1
            while not self.allowsMove( col ):
                col = eval(input('Next col for ' + nextCheckerToMove + ': '))
            self.addMove( col, nextCheckerToMove )

            # check if the game is over
            if self.winsFor( nextCheckerToMove ):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
            else:
                nextCheckerToMove = 'X'

        print('Come back soon 4 more!')

    def playGame( self, pForX, pForO, ss=False ):
        """ plays a game of Connect Four
            p1 and p2 are objects of type Player OR
            the string 'human'
            ss will "show scores" each time...
        """

        nextCheckerToMove = 'X'
        nextPlayerToMove = pForX
        
        while True:
            
            # print the current board
            print(self)

            # choose the next move
            if nextPlayerToMove == 'human':
                col = -1
                while not self.allowsMove( col ):
                    col = eval(input('Next col for ' + nextCheckerToMove + ': '))
            else: # it's a computer player
                if ss:
                    scores = nextPlayerToMove.scoresFor(self)
                    print((nextCheckerToMove + "'s"), 'Scores: ', [ int(sc) for sc in scores ])
                    print()
                    col = nextPlayerToMove.tiebreakMove( scores )
                else:
                    col = nextPlayerToMove.nextMove( self )

            # add the checker to the board
            self.addMove( col, nextCheckerToMove )

            # check if game is over
            if self.winsFor( nextCheckerToMove ):
                print(self)
                print('\n' + nextCheckerToMove + ' wins! Congratulations!\n\n')
                break
            if self.isFull():
                print(self)
                print('\nThe game is a draw.\n\n')
                break

            # swap players
            if nextCheckerToMove == 'X':
                nextCheckerToMove = 'O'
                nextPlayerToMove = pForO
            else:
                nextCheckerToMove = 'X'
                nextPlayerToMove = pForX

        print('Come back 4 more!')

    
class Player:
    """ an AI player for Connect Four """

    def __init__( self, ox, tbt, ply ):
        """ the constructor """
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and ply == " + str(self.ply) + "\n\n"
        return s

    def oppCh(self):
        ''' this method return the other kind of checker or playing piece'''

        if self.ox== "X":
            return 'O'

        else:
            return 'X'

    def scoreBoard(self,b):
        ''' this method return a float representing the score of the board for a given checker'''

        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppCh()):
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self,scores):
        ''' this method takes in a list of scores and returns the column number depending on what
        self.tbt is
        '''
        L=[]

        for i in range(0,len(scores)):
            if scores[i]== max(scores):
                L= L+[i]
                

        if self.tbt=="LEFT":
            return min(L)
        elif self.tbt== "RIGHT":
            return max(L)
        else:
            return random.choice(L)

    def scoresFor(self,b):
        ''' this method returns the list of scores representing the goodness of the input board
        after the plaves to the column c 
        '''
        scores= [50.0,50.0,50.0,50.0,50.0,50.0,50.0]

        for col in range(0,7):

            if b.allowsMove(col)== False:
                scores[col]=-1
            elif b.winsFor(self.ox)== True:
                scores[col]=100.0
            elif b.winsFor(self.oppCh())== True:
                scores[col]=0.0
            elif self.ply==0:
                scores[col]=50.0

            else:
                b.addMove(col,self.ox)
                OPP=Player(self.oppCh(),self.tbt,self.ply-1)
                S=OPP.scoresFor(b)
                scores[col]=  100- max(S)
                b.delMove(col)

        return scores

    def nextMove(self,b):
        ''' this method returns a column that the player must move the checker to'''
        c= self.tiebreakMove(self.scoresFor(b))
        return c


