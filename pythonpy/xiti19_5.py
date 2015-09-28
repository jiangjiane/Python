#lambda中运用print和循环嵌套
import sys
showall=lambda x:list(map(sys.stdout.write,x))
print(showall(['spam\n','toast\n','eggs\n']))
print('\n')

showall=lambda x:[sys.stdout.write(line) for line in x]
print(showall(('bright\n','side\n','of\n','life\n')))
print('\n')

#嵌套lambda和作用域
def action(x):
    return (lambda y:x+y)#lambda能够获得上层函数的的变量
act=action(99)
print(act(2))

#以下代码暂不能运行
import sys
from tkinter import Buton,mainloop
x=button(
    text='Press me',
    command=(lambda:sys.stdout.write('Spam\n')))
x.pack()
mainloop()
