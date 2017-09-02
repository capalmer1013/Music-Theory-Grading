from PIL import Image
import random

size = 256, 256
maxDelta = 5
currentPos = startPos = random.randint(0, size[0]-1), random.randint(0, size[1]-1)
listOfPositions = [(x, y) for y in range(size[1]) for x in range(size[0])]


def initializeImageMatrix(size):
    # type: (Tuple[int, int]) -> List[List[int]]
    return [[-1 for _ in range(size[0])] for _ in range(size[1])]


def getSurroundingValues(pos, matrix):
    # TODO: this needs some work
    result = []  # type: List[int]
    try:
        result.append(matrix[pos[0]-1][pos[1]] if matrix[pos[0]-1][pos[1]] >= 0 else -1)       # left
    except IndexError: pass

    try:
        result.append(matrix[pos[0]+1][pos[1]] if matrix[pos[0]+1][pos[1]] < size[0] else -1)  # right
    except IndexError: pass

    try:
        result.append(matrix[pos[0]][pos[1]-1] if matrix[pos[0]][pos[1]-1] >= 0 else -1)       # top
    except IndexError: pass

    try:
        result.append(matrix[pos[0]][pos[1]+1] if matrix[pos[0]][pos[1]+1] < size[1] else -1)  # bottom
    except IndexError: pass

    return result


def changePoint(pos, matrix, maxDelta):
    # type: (Tuple[int, int], List[List[int]], int) -> None
    surroundingValues = getSurroundingValues(pos, matrix)
    while -1 in surroundingValues:
        surroundingValues.remove(-1)

    if not surroundingValues:
        matrix[pos[0]][pos[1]] = random.randint(0, 255)
        return

    tmpMin = min(surroundingValues)
    tmpMax = max(surroundingValues)

    if tmpMax - tmpMin > maxDelta:
        matrix[pos[0]][pos[1]] = int((tmpMax-tmpMin)/2)
        return
    val = random.randint(tmpMin-maxDelta, tmpMax+maxDelta)
    matrix[pos[0]][pos[1]] = val
    return


def imageCopy(toImg, fromImg):
    # type: (Image, List[List[int]]) -> None
    xCounter = 0
    for x in fromImg:
        yCounter = 0
        for y in x:
            toImg[xCounter, yCounter] = (fromImg[xCounter][yCounter],) * 3
            yCounter += 1

        xCounter += 1

    return


def main():
    # type: () -> None
    memImg = initializeImageMatrix(size)
    while len(listOfPositions) > 0:
        nextPoint = random.choice(listOfPositions)
        listOfPositions.remove(nextPoint)
        changePoint(nextPoint, memImg, maxDelta)

    img = Image.new("RGB", size)
    imageCopy(img.load(), memImg)
    img.save("test.png", "PNG")
    return

if __name__ == "__main__":
    main()
