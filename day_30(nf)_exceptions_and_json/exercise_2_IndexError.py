fruits = ["Apple", "Pear", "Orange"]

## Without try-exception
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + "pie")

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(f"{fruit} pie")
        
fruit_index = int(input("Fruit index: "))
make_pie(fruit_index)