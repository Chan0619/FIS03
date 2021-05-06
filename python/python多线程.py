import _thread
import logging
from time import ctime, sleep

# 初始化    level，日志的输出等级 设置为INFO级别，所有的INFO日志会打印输出
logging.basicConfig(level=logging.INFO)

loops = [2, 4]


# nloop标识当前loop处于第几个，nsec 时间，lock 锁
def loop(nloop, nsec, lock):
    # 添加日志信息，Python自带的库，需导入logging模块
    logging.info('start loop ' + str(nloop) + ' at ' + ctime())
    sleep(nsec)
    logging.info('end loop ' + str(nloop) + ' at ' + ctime())
    lock.release()


# def loop1():
#     logging.info('start loop1 at ' + ctime())
#     sleep(2)
#     logging.info('end loop1 at ' + ctime())
def main():
    logging.info('start all at ' + ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = _thread.allocate_lock()  # 声明锁
        lock.acquire()  # 加锁
        locks.append(lock)
    for i in nloops:  # 启动线程用
        # (i, loops[i],locks[i]) --nloop, nsec, lock
        # 执行子线程
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        # locked() 加锁时返回True，进入死循环，没有锁住返回False，退出循环
        while locks[i].locked(): pass  # 锁上的状态时，什么都不做
    # 使用_thread时，后面要加sleep(),
    # 因为当主线程退出时，子线程会强行退出
    # _thread.start_new_thread(loop0, ())
    # _thread.start_new_thread(loop1, ())
    # sleep(6)
    logging.info('end all at ' + ctime())


if __name__ == '__main__':
    main()
