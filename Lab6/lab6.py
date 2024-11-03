from threading import Semaphore, Thread, Lock 
from queue import Queue, Empty 
from random import randint 
from time import sleep 

max_customers_in_bank = 10  # maximum number of customers that can be in the bank at one time 
max_customers = 30 # number of customers that will go to the bank today 
max_tellers = 3 # number of tellers working today             
teller_timeout = 10 # longest time that a teller will wait for new customers 

class Customer():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self): 
        return f"{self.name}"
    
class Teller():
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self): 
        return f"{self.name}"
    
def bankprint(lock, msg):
    with lock as l:
        print(msg)

def getNames(file) -> list[str]:
    with open(file, 'r') as f:
        names = [line.strip() for line in f.readlines() if line.strip() != '']
    return names

def wait_outside_bank(customer: Customer, guard: Semaphore, teller_line: Queue, printlock: Lock): 
    bankprint(printlock, f"(C) Customer {customer} is waiting outside bank")
    guard.acquire()
    bankprint(printlock, f"<G> Security guard letting Customer {customer} into the bank")
    bankprint(printlock, f"(C) Customer {customer} getting into line")
    teller_line.put(customer)
    return

def teller_job(teller: Teller, guard: Semaphore, teller_line: Queue, printlock: Lock): 
    bankprint(printlock, f"[T] Teller {teller} has started work")
    while True:
        try:
            customer = teller_line.get(timeout= teller_timeout)
            bankprint(printlock, f"[T] Teller {teller} is now helping Customer {customer}")
            sleep(randint(1, 4))
            bankprint(printlock, f"[T] Teller {teller} is finished helping Customer {customer}")
            bankprint(printlock, f"<G> Security guard letting Customer {customer} out of the bank")
            guard.release()

        except Empty:
            bankprint(printlock, f"[T] Teller {teller} is going on break")
            break
    return

if __name__ == '__main__':
    printlock = Lock()
    teller_line = Queue(maxsize=max_customers_in_bank) 
    guard = Semaphore(max_customers_in_bank) 

    bankprint(printlock, "<G> Security guard starting their shift") 
    bankprint(printlock, "*B* Bank open")  

    # Get names from a list and make a customer list that is max_customers long 
    # names: list[str] = getNames('Lab6/names.txt')
    # customers = [Customer(name) for count, name in enumerate(names, start = 1) if count <= max_customers]
    customers = [Customer(i) for i in range(max_customers)]

    # wait_outside_bank(customers[0], guard, teller_line, printlock)
    customer_threads = []
    for i, customer in enumerate(customers):
        customer_threads.append(Thread(target=wait_outside_bank, args=(customer, guard, teller_line, printlock)))
        customer_threads[i].start()

    sleep(5)
    
    bankprint(printlock, f"*B* Tellers are beginning work")
    tellers = [Teller(i) for i in range(max_tellers)]
    teller_threads = []
    for i, teller in enumerate(tellers):
        teller_threads.append(Thread(target = teller_job, args = (teller, guard, teller_line, printlock)))
        teller_threads[i].start()
    
    [thread.join() for thread in customer_threads]
    [thread.join() for thread in teller_threads]

    bankprint(printlock, f"*B* Bank is closed")
