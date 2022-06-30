import math

def test_square_root(a):
    x=1

    print('a\tmysqrt(a)\tmath.sqrt(a)\tdiff')
    print('-\t---------\t------------\t----')
    
    while a<=9:
        print(float(a),'\t',end="")

        while True:
            y=(x+a/x)/2
            if y==x:
                print(y,'\t',end="")
                break
            else:
                x=y

        print(math.sqrt(a),'\t',end="")
        
        y=(x+a/x)/2
        print (abs(y-x),'\n')
        
        a+=1


test_square_root(1)
