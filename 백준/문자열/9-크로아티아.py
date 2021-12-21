a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()

for k in a:
    b = b.replace(k, '_')

print(len(b))
