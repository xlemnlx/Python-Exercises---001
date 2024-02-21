def snake_area_filling(test_variable):
    total_area = test_variable * test_variable
    
    snake_length = 1
    count = 0
    
    while True:
        if snake_length > total_area:
            snake_length /= 2
            count -= 1
            break
        else:
            snake_length *= 2
            count += 1
    
    return count