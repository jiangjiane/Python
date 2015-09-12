#与全局共享状态
def tester(start):
    global state
    state=start
    def nested(label):
        global state
        print(label,state)
        state+=1
    return nested

F=tester(0)
F('spam')
F('eggs')
print('\n')

G=tester(42)
G('toast')
G('bacon')
F('ham')
