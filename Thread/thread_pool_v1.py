from concurrent.futures import ThreadPoolExecutor
import time

def return_fu(msg):
    time.sleep(2)
    print(msg)
    return 'end'

#新建一个线程池
pool = ThreadPoolExecutor(max_workers=4)

#给线程池添加任务
w1 = pool.submit(return_fu, 'hello')
w2 = pool.submit(return_fu, 'world')
w3 = pool.submit(return_fu, 'my dear')
w4 = pool.submit(return_fu, 'friend')
#利用map实现,可以替代submit
#msg = ['hello','world','my dear','friend']
#for i in pool.map(return_fu,msg)
#   print(i)
print(w1.done())
time.sleep(4)
print(w2.done())
time.sleep(4)
print(w3.done())
time.sleep(4)
print(w4.done())
#为什么会随机失败？

print(w1.result())
print(w2.result())
print(w3.result())
print(w4.result())