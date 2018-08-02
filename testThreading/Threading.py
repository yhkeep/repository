import threading
import time
from queue import Queue
# 此处flag必须设置在类上面
exitFlag = 0
class ThreadingDemo(threading.Thread):

    # def __init__(self,threadingName,count):
    #     """Constructor for ThreadingDemo"""
    #     threading.Thread.__init__(self)
    #     self.threadingName = threadingName
    #     self.count = count
    def __init__(self,threadingName,queue):
        """Constructor for ThreadingDemo"""
        threading.Thread.__init__(self)
        self.threadingName = threadingName
        self.queue = queue
    # 线程开启
    def run(self):
        print("开始线程：{}".format(self.threadingName))

        self.print_time(self.threadingName,self.queue)

        print("结束线程：{}".format(self.threadingName))
    # 执行操作

    def print_time(self,threadingName,q):
        while not exitFlag:
            # 获取锁，用于线程同步
            threading_lock.acquire()
            if not queue.empty():
                q_get = q.get()
                # 此处必须将线程锁释放，否则会一直执行
                threading_lock.release()
                print("%s processing %s" % (threadingName, q_get))
            else:
                # 释放锁，开启下一个线程
                threading_lock.release()
            time.sleep(1)

if __name__ == '__main__':
    queue = Queue(10)
    threading_lock = threading.Lock()
    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["One", "Two", "Three", "Four", "Five"]
    threads = []
    # 创建线程放入列表中
    for threadName in threadList:
        thread = ThreadingDemo(threadName,queue)
        # 启动线程
        thread.start()
        threads.append(thread)
    # 放入数据到队列中
    threading_lock.acquire()
    for name in nameList:
        queue.put(name)
    threading_lock.release()
    # 清空队列，才会将方法print_time循环中的判断继续执行
    while not queue.empty():
        pass
    exitFlag = 1
    # thread0 = ThreadingDemo("线程1",3)
    # thread1 = ThreadingDemo("线程2",4)
    # threads.append(thread0)
    # threads.append(thread1)
    # thread0.start()
    # thread1.start()
    for t in threads:
        t.join()

    print("退出主线程")