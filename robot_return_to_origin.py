""""
657. Robot Return to Origin

There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move. Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.

Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once, 'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
"""

class Solution:
    # There isn't much to explain here, the script will just keep track of how much the robot has
    # moved both horizontally and vertically, if in the end all the movements sums to 0, return True
    def judgeCircle1(self, moves: str) -> bool:
        pos = [0, 0]
        for move in moves:
            if move == "L":
                pos[0] += -1
            elif move == "R":
                pos[0] += 1
            elif move == "U":
                pos[1] += 1
            elif move == "D":
                pos[1] += -1
        
        if pos[0] == 0 and pos[1] == 0:
            return True
        
        return False
    
    # This method uses the built in count() function for arrays and see if the amount of Ls and Us
    # matches the amount of Rs and Ds, respectively. It is more efficient than the previous one
    def judgeCircle2(self, moves: str) -> bool:
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")

test_case = "UDLR"

solution = Solution()
answer = solution.judgeCircle2(test_case)

print(answer)