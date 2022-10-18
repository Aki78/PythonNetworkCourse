import threading

#Treading allows us to speed up pgorgrams by executing multiple tasks at the same time.
#Each task will run on its own thread
#Each thread can run simultaneously and share data with eachother.

#Every thread when you start it must do something, which we can define with a function.
#Our threads will then target these functions.
#When we start the threads, the target functions will be run.


def function1():
    for i in range(10):
        print("One ")


def function2():
    for i in range(10):
        print("Two ")


def function3():
    for i in range(10):
        print("Three ")

#If we call these functions, we see the first function call MUST complete before the next
#They are executed linearly.

# function1()
# function2()
# function3()

#We Must
t1 = threading.Thread(target = function1)
t2 = threading.Thread(target = function2)
t3 = threading.Thread(target = function3)
t1.start()
t2.start()
t3.start()

#Need join to pause before running next
t1.join()
t2.join()
t3.join()

#Thread can only run once
t1 = threading.Thread(target = function1)
t1.start()

print("Threading rules!")

