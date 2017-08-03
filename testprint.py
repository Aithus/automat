from printer import Printing

test_print = Printing()
filename = test_print.create_ticket()
test_print.do(filename)
