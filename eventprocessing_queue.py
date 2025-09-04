queue = []

def add(e):
    queue.append(e)
    print(f"Added '{e}'")

def process():
    if queue:
        print(f"Processed '{queue.pop(0)}'")
    else:
        print("No events")

def show():
    if queue:
        for i, e in enumerate(queue, 1):
            print(f"{i}. {e}")
    else:
        print("No events")

def cancel(e):
    if e in queue:
        queue.remove(e)
        print(f"Canceled '{e}'")
    else:
        print(f"'{e}' not found")

def menu():
    while True:
        print("\n1.Add 2.Process 3.Show 4.Cancel 5.Exit")
        c = input("Choice: ")
        if c == '1':
            add(input("Event: "))
        elif c == '2':
            process()
        elif c == '3':
            show()
        elif c == '4':
            cancel(input("Event to cancel: "))
        elif c == '5':
            break
        else:
            print("Invalid")

menu()
