import time
x = 'This is Halloween'

def words():
    i = 100
    while i > 0:
        time.sleep(1)
        print(x)
        i = i-1
words()
