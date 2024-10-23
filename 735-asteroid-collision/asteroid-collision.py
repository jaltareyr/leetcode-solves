class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                # Collision: compare the top of the stack (a positive asteroid) with the current one (a negative asteroid)
                if stack[-1] < -ast:
                    stack.pop()  # The positive asteroid explodes, continue checking for further collisions
                    continue
                elif stack[-1] == -ast:
                    stack.pop()  # Both asteroids explode
                break
            else:
                # No collision or the current asteroid moves to the right
                stack.append(ast)
        
        return stack