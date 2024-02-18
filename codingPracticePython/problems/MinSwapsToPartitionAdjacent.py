class MinSwapsToPartitionAdjacent:
    def run(self):
        input = [1, 0, 0, 1, 0, 1, 1, 0, 0, 1]

        count = 0

        leftP = 0
        rightP = len(input) - 1

        while leftP < rightP:
            left = input[leftP]
            right = input[rightP]
            if left == right:
                if left == 1:
                    rightP -= 1
                else:
                    leftP += 1
            elif left > right:
                count += rightP - leftP
                leftP += 1
                rightP -= 1
            else:
                leftP += 1
                rightP -= 1

        print(count)
        return count
