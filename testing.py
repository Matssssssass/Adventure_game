import sys
from time import sleep


def fin_utprint(sträng):
    string = sträng
    string = str(string)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(.03)
    sleep(1)

min_sträng = '''
Hej CHONK CHARLES FATNESS

suck my dick

'''
fin_utprint(min_sträng)

        