import time, sys

indent = 0
indentIncreasing = True
zig_zag_counter = 3

try:
    while True:
        print(' ' * indent, end='')
        print('******')
        time.sleep(0.2)
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 15 and zig_zag_counter != 0:
                zig_zag_counter = zig_zag_counter - 1
                indentIncreasing = True

            if indent == 0:
                zig_zag_counter = 3
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()
