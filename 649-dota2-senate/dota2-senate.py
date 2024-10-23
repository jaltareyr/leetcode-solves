from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        R = deque()
        D = deque()
        n = len(senate)

        # Store the indices of Radiant and Dire senators
        for i, s in enumerate(senate):
            if s == "R":
                R.append(i)
            else:
                D.append(i)

        # Simulate the rounds
        while R and D:
            R_item = R.popleft()
            D_item = D.popleft()

            # The senator with the lower index bans the other
            if R_item < D_item:
                # Radiant bans Dire, Radiant senator gets back in the queue
                R.append(R_item + n)
            else:
                # Dire bans Radiant, Dire senator gets back in the queue
                D.append(D_item + n)

        # Determine the winner
        return "Radiant" if R else "Dire"
