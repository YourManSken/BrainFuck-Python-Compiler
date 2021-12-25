FILE_IMPORT = True
LIVE_DISPLAY = False

BRAINFUCK_POINTER = 0
BRAINFUCK_CODE = ''
MEMORY = [0]
MEMORY_POINTER = 0
LOOP_START_POINTERS = []

def import_script():
    code = ''
    with open("script.bf") as script:
        for c in script.read():
            if (c=='>' or c=='<' or c=='+' or c=='-' or c=='[' or c==']' or c==',' or c=='.'):
                code += c
    return code

def move_right():
    global MEMORY_POINTER
    if (len(MEMORY)-1 == MEMORY_POINTER):
        MEMORY.append(0)
    MEMORY_POINTER += 1

def move_left():
    global MEMORY_POINTER
    if (MEMORY_POINTER > 0):
        MEMORY_POINTER -= 1

def increase():
    MEMORY[MEMORY_POINTER] += 1

def decrease():
    if MEMORY[MEMORY_POINTER]>=1:
        MEMORY[MEMORY_POINTER] -= 1

def loop_start():
    global LOOP_START_POINTERS
    LOOP_START_POINTERS.append(BRAINFUCK_POINTER)

def loop_end():
    global BRAINFUCK_POINTER, LOOP_START_POINTERS
    if (MEMORY[MEMORY_POINTER] > 0):
        BRAINFUCK_POINTER = LOOP_START_POINTERS[-1]
    else:
        LOOP_START_POINTERS.pop(-1)

def memory_input():
    global MEMORY, MEMORY_POINTER
    MEMORY[MEMORY_POINTER] = input()

def memory_output():
    print(MEMORY[MEMORY_POINTER])


def convert():
    if BRAINFUCK_CODE[BRAINFUCK_POINTER] == '>':
        move_right()
    elif BRAINFUCK_CODE[BRAINFUCK_POINTER] == '<':
        move_left()
    elif BRAINFUCK_CODE[BRAINFUCK_POINTER] == '+':
        increase()
    elif BRAINFUCK_CODE[BRAINFUCK_POINTER] == '-':
        decrease()
    elif BRAINFUCK_CODE[BRAINFUCK_POINTER] == '[':
        loop_start()
    elif BRAINFUCK_CODE[BRAINFUCK_POINTER] == ']':
        loop_end()
    elif BRAINFUCK_CODE[BRAINFUCK_POINTER] == ',':
        memory_input()
    elif BRAINFUCK_CODE[BRAINFUCK_POINTER] == '.':
        memory_output()

def execute():
    global BRAINFUCK_CODE, BRAINFUCK_POINTER
    if FILE_IMPORT:
        BRAINFUCK_CODE = import_script()
        print(BRAINFUCK_CODE)

    while BRAINFUCK_POINTER < len(BRAINFUCK_CODE):
        convert()
        BRAINFUCK_POINTER += 1
        if LIVE_DISPLAY:
            display()

def display():
    print(MEMORY)
    for _ in range(MEMORY_POINTER*3+1):
        print(' ', end='')
    print('^', end='\n')

execute()