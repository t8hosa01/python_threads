import threading

# Assign global variable
g = 0
lock = threading.Lock()


# Method which handles locks and printing
def increment():
    global g

    # try, except, finally to acquire and then release lock
    try:
        lock.acquire()
        print("Lock acquired")
        g += 1 # Add 1 to the global variable
        print("Hello World: {}".format(g)) # Pass the global variable to the print

    except Exception as e:
        print(str(e))

    finally:
        lock.release() # Release the lock


# Task for threads
def hello_world():
    print("Inside hello_world")
    while g < 3: # Loop to print and run threads 4 times
        increment()


# Method for threads
def main():
    global g
    g = 0

    # Creating threads
    th1 = threading.Thread(target=hello_world)
    th2 = threading.Thread(target=hello_world)

    # Start threads
    th1.start()
    th2.start()

    # Wait until threads finish their job
    th1.join()
    th2.join()

# Run threads
main()
