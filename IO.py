#文件的读写，open、read、write
#r-读标记，w-写模式，a-追加模式，b-二进制模式，+读写模式
# try:
#     f=open(r'c:\text\qiye.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# #上面的try....finally...可以使用with语句代替
# with open(r'c:\text\qiye.text','r') as fileReader:
#     print(fileReader.read())

#序列化：将内存中的数据转成序列化数据，方便存储到存储介质中去，以便反序列化读取后使用
#pickle模块
# d=dict(url='index.html',title='首页',content='首页')
# try:
#     import cPickle as pickle
# except ImportError:
#     import pickle
# #pickle.dump(d)
# import os
#
# with open(r'c:\text\dump.txt','wb') as fileDump:
#     pickle.dump(d,fileDump)
# fileDump.close()

#进程
#同一个运行程序中父进程创建多个子进程进行程序的处理，进程间不会相互影响，占用资源多，数据不共享需要编程互相通信
#使用os模块的fork方法,仅适用于linux/unix;multiprocessing模块创建process类,pool类，两种方法创建，适用于windows
################fork方法，在windows下会报AttributeError: module 'os' has no attribute 'fork'错误###############
# import os
# if __name__=='__main__':
#     print(r'current Process (%s) start ...'%(os.getpid()))
#     pid = os.fork()
#     if pid < 0:
#         print(r'error in fork')
#     if pid == 0:
#         print(r'I am child Process (%s) and my parent process is (%s)'%(os.getpid(),os.getppid()))
#     else:
#         print(r'I(%s) created a child process(%s)'%(os.getpid(),pid))
###############multiprocessing模块########################
import os
from multiprocessing import Process
#子程序执行的代码
def run_proc(name):
    print('Child process %s(%s) Running...'%(name,os.getpid()))
if __name__=='__main__':
    print(r'Parent process %s.'%os.getpid())
    for i in range(5):
        p = Process(target=run_proc,args=(str(i),))
        print(r'Process will start.')
        p.start()
    p.join()
    print(r'process end.')