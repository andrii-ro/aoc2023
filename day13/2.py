import itertools

import copy

lines = []
# removing the new line characters
with open('input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

puzzles = []
temp = []
for i in lines:
    if len(i) == 0:
        puzzles.append(temp.copy())
        temp = []
        continue
    temp.append(i)
puzzles.append(temp)

for puzzle in puzzles:
    print(i)


res = 0
for puzzle in puzzles:
    height = len(puzzle)
    width = len(puzzle[0])

    ###########################
    index = 0
    lRow = index
    rRow = index + 1

    isMirror = True
    mirrorPow = 0
    error = 0
    puzzleCopy = copy.deepcopy(puzzle)
    while index < height - 1:
        for j in range(width):
            left = puzzle[lRow][j]
            right = puzzle[rRow][j]

            if left != right:
                error += 1
                puzzle[lRow][j] = puzzle[rRow][j]
                # print("Error occured: " + str(index))
                # print(lRow, rRow)
                # for p in puzzle:
                #     print(p)

            if error > 1:
                isMirror = False
                error = 0
                # print("before: ")
                # for p in puzzle:
                #     print(p)
                puzzle = copy.deepcopy(puzzleCopy)

                # print("after: ")
                # for p in puzzle:
                #     print(p)
                break

        if isMirror:
            mirrorPow += 1
            lRow -= 1
            rRow += 1
            if lRow < 0 or rRow >= height:
                print("row is mirror:")
                print("index: " + str(index))
                print("mirrorPow: " + str(mirrorPow))
                print(lRow, rRow)

                res += (index + 1) * 100

                for p in puzzle:
                    print(p)
                break
        else:
            isMirror = True
            mirrorPow = 0
            index += 1
            lRow = index
            rRow = index + 1

    # #########
    #
    # print('Go to col check')
    # for p in puzzle:
    #     print(p)
    #
    # index = 0
    # lCol = index
    # rCol = index + 1
    #
    # isMirror = True
    # mirrorPow = 0
    # prevError = error
    # # error = 0
    # while index < width - 1:
    #     for i in range(height):
    #         left = puzzle[i][lCol]
    #         right = puzzle[i][rCol]
    #
    #         if left != right:
    #             error += 1
    #
    #         if error > 1:
    #             isMirror = False
    #             error = prevError
    #             break
    #
    #     if isMirror:
    #         mirrorPow += 1
    #         lCol -= 1
    #         rCol += 1
    #         if lCol < 0 or rCol >= width:
    #             print("col 1is mirror:")
    #             print("index: " + str(index))
    #             print("mirrorPow: " + str(mirrorPow))
    #             print(lCol, rCol)
    #
    #             res += index + 1
    #
    #             for p in puzzle:
    #                 print(p)
    #             break
    #     else:
    #         isMirror = True
    #         mirrorPow = 0
    #         index += 1
    #         lCol = index
    #         rCol = index + 1
    #
    #
    # ###########################

print(res)
