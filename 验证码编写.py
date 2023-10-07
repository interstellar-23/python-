import random
def securitycode(n):
    all_num="0123456789abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b=len(all_num)-1
    code=""
    for _ in range(n):
        c=random.randint(0,b)
        code+=all_num[c]
    return code
def main():
    n=int(input("输入验证码长度:"))
    global d
    d=securitycode(n)
    print(d)
    

    
    
if __name__=="__main__":
    main()
    

b=str(input("请输入验证码:"))
if b==d:
    print("验证码正确")
else:
    print("您的输入有误")