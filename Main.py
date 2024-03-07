import mochi


my_list = []
print("---start---")
while True:
  user_input = input("Enter item\n")
  my_list.append(user_input)
  mochi.show_list(my_list)
print("---end---")
