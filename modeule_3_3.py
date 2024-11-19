def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [ False, 'Block', 999]
values_dict = { 'a' : 1, 'b' : 'строка', 'c' : True }

#print_params(*values_list, **values_dict) как я понимаю это не должно было сработать так как параметров только 3)

values_list_2 = True, 'Bob'
print_params(*values_list_2, 42)