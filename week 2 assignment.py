a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
print('Column 1 = %d' % a[0][0], a[1][0], a[2][0])
print('Column 2 = %d' % a[0][1], a[1][1], a[2][1])
print('Column 3 = %d' % a[0][2], a[1][2], a[2][2])
