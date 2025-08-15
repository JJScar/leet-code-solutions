# Intuition
All I could think was sliding through the array (string in this case) while saving the number that is good and compare it to another one if there is one in the big num.

# Approach
I decided to iterate through the string while making sure we are not going out of bounds.
Next I wanted to get the 3 digits we are looking at, the three neighbours.
Now, if they are all equal to each other we add them up to create the sum of them. The bigger the number the bigger will be their sum.
If the sum is bigger than the previous one, or 0 in case of the first one, we save it.

We then return the max number if there is one, or empty string if not.

# Complexity
- **Time complexity:**
The time complexity is `O(n)` where `n` is the length of the input string num.

- **Space complexity:**
The space complexity is `O(1)` - constant space, as the algorithm only uses a fixed amount of extra variables regardless of input size.

# Code
```python
class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_num = 0
        count = 0
    
        for c in num:
            if (count == len(num) -2 ):
                break

            first = num[count]
            second = num[count+1]
            third = num[count+2]

            if first == second and second == third:
                is_max = first + second + third
                if is_max > max_num:
                    max_num = is_max
                    is_max = 0 

            count += 1

        if max_num:
            return str(max_num)
        return ""
```