# keep track of todos using a list
todo_list = []

# I need to print my todos

def print_todos():
    for todo in todo_list:
        print(todo)

# I need a way to add todos
def add_todo(todo):
    # We receive a todo, which is a string
    todo_list.append(todo)

# print the empty todo list
print_todos()
# add a todo by calling our function
add_todo("feed the cat")
# print the todo list again, making sure
print_todos()

# I need to be able to delete todos
def delete_todo(index):
    # del todo_list[index]
    try:
        todo_list.pop(index)
    except IndexError:
        print("👎👎 Sorry, we couldn't find that one.")

delete_todo(0)
print_todos()
delete_todo(0)
print_todos()


# Show user main menu

# (Bottom-Up Approach)