# Program to solve the `container that contains most water`


def findMaxArea(heights):

    maxPairs = []
    maxValue = 0

    length = len(heights)
    for index in range(length):
        # Update `length`
        length -= index
        for back in range(length - index):
            index_pos = (length - back) - 1

            # Find max value and pair
            temp = heights[index] + heights[index_pos]
            if temp > maxValue:
                maxValue = temp

                # Update the max pairs
                maxPairs.append((index, index_pos))

    return maxPairs


def processPairs(pairs, height):

    maxPair = 0

    for value in pairs:
        begin, end = value
        temp = sum(height[begin:end + 1]) + len(height[begin:end]) - 2
        if maxPair < temp:
            maxPair = temp

    return maxPair


heights = [1, 8, 6, 2, 5, 4, 8, 3, 8]
values = findMaxArea(heights)
print(processPairs(values, heights))















