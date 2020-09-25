#reference_number = 9
text = ' is a prime number '
print('................................')
#print('This are numbers which can be divided into ' + str(reference_number))
for i in range(1, 100):
    first = i / i
    second = i/1
    # print('Residual value of dividing ' + str(i) + ' / ' + str(reference_number) + ' = ' + str(residual))
    if first == 1:
        if second == i:
            print(str(i) + text) #+ str(reference_number))