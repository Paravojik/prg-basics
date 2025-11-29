import queue


def addCustomer(que,name,curC):
    que.put((name,curC))
    print(f'Customer {name} added to the queue with ticket number {curC}.')

def serveCustomer(que):
    if not que.empty():
        customer=que.get()
        print(f'Customer {customer[0]} with ticket number {customer[1]} is being served.')
    else:
        print('No customers in the queue.')

curC=0
q=queue.Queue()

while True:
    print('1. Add customer to the queue')
    print('2. Serve customer')
    print('0. Quit')
    menu = input('Select an option: ')
    
    if menu == '1':
        name = input('Enter customer name: ')
        curC+=1
        addCustomer(q,name,curC)

    elif menu=='2':
        serveCustomer(q)

    elif menu == '0':
        break