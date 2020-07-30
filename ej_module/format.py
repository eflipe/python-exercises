def my_print(txt):
    print(txt)


msg_template = '''
Lalala {name}, dolor lorem ipsum {item} lalala.            

'''


def format_msg(name_ej='pepe', item_ej='lorem ipsum'):
    msg_template_print = msg_template.format(name=name_ej, item=item_ej)
    return print(msg_template_print)

