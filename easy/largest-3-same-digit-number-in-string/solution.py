# This solution has been written by me with no help with outside sources (other solutions, LLMs etc)
# This solution passes on the LeetCode platform, therefore no tests have been added here!

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        # Initializing variables to use in the for loop
        max_num = 0
        count = 0
    
        # Iterating through the string and looking for a 3 digit number with the same digit and storing it into max but comparing with other maxes in the digits
        for c in num:
            # Checking we are not at the end of the string 
            if (count == len(num) -2 ):
                break
            
            # Storing the 3 digits we are looking at
            first = num[count]
            second = num[count+1]
            third = num[count+2]

            # If this is a 3 digit with same digit number 
            if first == second and second == third:
                # Making the digit sum
                is_max = first + second + third
                # If the sum is bigger than the previous sum we store it
                if is_max > max_num:
                    max_num = is_max
                    # Resetting checked sum 
                    is_max = 0 
                    
            # Moving count up so we can move down the string
            count += 1

        # If there is a number here we return it as a string otherwise empty string
        if max_num:
            return str(max_num)
        return ""
    
# -----------------------------------------------------------------------
# This is after looking at other solutions and LLMs to make my solution better for learning purposes