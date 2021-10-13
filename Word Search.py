from collections import defaultdict
class Solution:
    #Recursive solution, recursion depth will only ever be the length of the word.
    def checkSurround(self,x,y,word,board, seen):
        positions = ([1,0],[0,1],[-1,0],[0,-1])
        # check if coordinate hass been seen before, or if 
        # the character matches the current character in `word`
        if board[y][x] == word[0] and (x,y) not in seen:
            seen.add((x,y))
            if len(word) == 1:
                return True
            for pos in positions:
                # Look around at the surrounding 4 options, checking for the next character
                newx = x + pos[0]
                newy = y + pos[1]
                if self.checkSurround(newx, newy, word[1:], board, seen):
                    return True
            seen.discard((x,y)) # If we need to backtrack, need to drop
        return False
    
    def checkSet(self,word,board):
        '''
        If board is [[A,A,A,A],[A,A,A,A]] and word is 'AAAH', there is no H.
        This is a performance edge case where the algorithm will recurse everything
        and only realize its not possible at the very end.
        This just prevents part of that edge case
        '''
        boardcounts = defaultdict(int)
        wordcounts = defaultdict(int)
        for row in board:
            for c in row:
                boardcounts[c] += 1
        for c in word:
            wordcounts[c] += 1
        for c in wordcounts.keys():
            if c not in boardcounts:
                return False
            if wordcounts[c] > boardcounts[c]:
                return False
        return True
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenY = len(board)
        lenX = len(board[0])
        pad =  ['']*(lenX + 2)
        board = [pad] + [[''] + row + [''] for row in board] + [pad]
        # Premature optimization: Easy fast check if its worth trying
        if not self.checkSet(word,board):
            return False
        # REAL ALGORITHM: Iterate through the starting characters
        for x in range(1,lenX+1):
            for y in range(1, lenY+1):
                if self.checkSurround(x, y, word, board, seen=set()):
                    return True
        return False

Normally people don't like premature optimizations, but given the high computational complexity here, the gains are HUGE. I took care of one case below in checkSet but others exist that are less easy to catch, like the scenario below. My checkSet function would be like "yep all the characters exist, go ahead", and the DFS solution would then spend 3^25 (847 BILLION) iterations verifying it isn't possible.

grid =[
['A','A','A','A','A','A'],
['A','A','A','A','A','A'],
['A','A','A','A','A','A'],
['A','A','A','A','A','A'],
['A','A','A','A','B','B'],
['A','A','A','A','B','C']
]
word = 'AAAAAAAAAAAAAAAAAAAAAAAAC'
