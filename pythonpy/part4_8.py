#第四部分习题
#part4_8 质数
def prime(y):
    if y<=1:
        print(y,'not prime')
    else:
        x=y//2
        while x>1:
            if y%x==0:
                print(y,'has factor',x)
                break
            x-=1
        else:
            print(y,'is pime')

prime(13);prime(13.0)
prime(15);prime(15.0)
prime(3);prime(2)
prime(1);prime(-3)
