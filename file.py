import math as m

def click(entry, to_print):
    old = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, old + to_print)

def sc(entry, key):
    text = key['text']
    no = entry.get()
    result = ''
    try:
        if text == 'deg':
            result = str(m.degrees(float(no)))
        elif text == 'sin':
            result = str(m.sin(m.radians(float(no))))
        elif text == 'cos':
            result = str(m.cos(m.radians(float(no))))
        elif text == 'tan':
            result = str(m.tan(m.radians(float(no))))
        elif text == 'lg':
            result = str(m.log10(float(no)))
        elif text == 'ln':
            result = str(m.log(float(no)))
        elif text == 'Sqrt':
            result = str(m.sqrt(float(no)))
        elif text == 'x!':
            result = str(m.factorial(int(no)))
        elif text == '1/x':
            result = str(1 / float(no))
        elif text == 'pi':
            result = str(float(no) * m.pi) if no else str(m.pi)
        elif text == 'e':
            result = str(m.e ** float(no)) if no else str(m.e)
    except Exception:
        result = "Error"
    entry.delete(0, 'end')
    entry.insert(0, result)

def clear(entry):
    entry.delete(0, 'end')

def bksps(entry):
    current = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, current[:-1])

def evaluate(entry):
    try:
        ans = eval(entry.get().replace("^", "**"))
        entry.delete(0, 'end')
        entry.insert(0, ans)
    except Exception:
        entry.delete(0, 'end')
        entry.insert(0, "Error")
