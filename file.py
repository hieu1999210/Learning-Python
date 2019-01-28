# nameHandle = open("kids", 'w')
# for i in range(2):
#     name = input("Enter name: ")
#     nameHandle.write(name + '\n')
# nameHandle.close()

nameHandle = open("kids", 'r')
for l in nameHandle:
    print(l)
nameHandle.close()