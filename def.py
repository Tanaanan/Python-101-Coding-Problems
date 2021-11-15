def get_input(num):
    data = []
    for i in range(num):
    value = int(input('Enter number #{}: '.format(i)))
    data.append(value)
    return data