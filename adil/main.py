# myList = [0, 1, 20, 40, 55, 12, 78]

# print(myList.sort())   
# print(myList)   

# myList = [10, 1, 2, 8, 20, 43, 15]
# print(sorted(myList))
# print(myList)

# import sup

# import time

# sup.hello()

# time.sleep(5)

# sup.sum(10, 20)

# class Adil:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 

#     def hello(self):
#         print(f"привет Меня зовут {self.name}!")


# one_person = Adil("adil", 20)
# print(one_person.age)
# print(one_person.name)
# one_person.hello()

# two_person = Adil("el", 33)
# print(two_person.age)
# print(two_person.name)



from tkinter import *

def get_entry():
    value = entry.get()
    txt["text"] = value


root = Tk()
root.title("My first app")
root.geometry("400x300")


entry = Entry()
entry.pack()


txt = Label(text="New text...")
txt.pack()

btn = Button(text="Click me!", command=get_entry)
btn.pack()





root.mainloop()






