import time
import threading

def song(a,b,c):
    print(a, b, c)
    for i in range(5):
        print("song")
        time.sleep(1)
if __name__ == "__main__":
    # 使用元组传递 threading.Thread(target=方法名，args=（参数1,参数2, ...）)
    threading.Thread(target=song,args=(1,2,3)).start()
    # 使用字典传递 threading.Thread(target=方法名, kwargs={"参数名": 参数1, "参数名": 参数2, ...})
    threading.Thread(target=song, kwargs={"a": 1, "c": 3, "b": 2}).start()  # 参数顺序可以变
    # 混合使用元组和字典 threading.Thread(target=方法名，args=（参数1, 参数2, ...）, kwargs={"参数名": 参数1,"参数名": 参数2, ...})
    threading.Thread(target=song, args=(1,), kwargs={"c": 3, "b": 2}).start()