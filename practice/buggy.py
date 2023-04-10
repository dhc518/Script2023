import traceback
def bacon():
    try:
        raise Exception('My Error')
    except:
        with open('error_story.txt', 'a') as ef:
            for line in traceback.format_stack():
                ef.write(line)
def spam():
    bacon()

def ham():
    spam()

ham()
