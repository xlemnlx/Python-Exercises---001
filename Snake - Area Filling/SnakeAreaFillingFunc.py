def SnakeAreaFilling(testVariable):
    totalArea = testVariable * testVariable
    
    snakeLength = 1
    count = 0
    
    while True:
        if snakeLength > totalArea:
            snakeLength /= 2
            count -= 1
            break
        else:
            snakeLength *= 2
            count += 1
    
    return count