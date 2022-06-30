from getkey import getkey, keys
import os
import time


def menu(index,legend=""):
    """
    Create a menu : Need a list as argument.

    Exemple of index : ['menu1','menu2']
    """
    def selector(index):

        def print_menu(index,selector,lengend):
            selector %= len(index)
            u=os.system('clear')
            print(" ")
            print(legend)
            for i in range(len(index)):
                
                if selector == i:
                    print("   > - "+str(index[i]))
                else:
                    print("     - "+str(index[i]))
            print(" ")

        selector = 0
        running = True
        print_menu(index,selector,legend)
        while running:  # making a loop
            key = getkey()
            if key == keys.UP:
                selector-=1
                print_menu(index,selector,legend)
            elif key == keys.DOWN:
                selector+=1
                print_menu(index,selector,legend)
            elif key == keys.ENTER:
                return selector % len(index)

    return selector(index)
    

def loading_bar(percent,legend="",pas=10,char1 = '#',char2=' '):
    """
    Create a loading bar fill with percent
    """
    u=os.system('clear')
    percinit=percent
    res="["
    for i in range(pas):
        if percent>=100/pas:
            res+=char1
            percent-=100/pas
        else:
            res+= char2
    res+="]"
    print(legend)
    print(str(res)+" - "+str(percinit)+" %")



def slider(lenght=10,init=-1,legend=""):
    """
    Generate a slider 
    """
    if init == -1:
        init = lenght // 2
    
    u=os.system('clear')
    res = "["
    for i in range (lenght):
        if i<init:
            res+='#'
        else:
            res+=' '
    print(legend)
    print(str(res)+"]  - "+str(init))

    while True:
        key = getkey()
        if key == keys.RIGHT:
            if init != lenght:
                init+=1
            u=os.system('clear')
            res = "["
            for i in range (lenght):
                if i<init:
                    res+='#'
                else:
                    res+=' '
            print(legend)
            print(str(res)+"]  - "+str(init))
        elif key == keys.LEFT:
            if init !=0:
                init-=1
            u=os.system('clear')
            res = "["
            for i in range (lenght):
                if i<init:
                    res+='#'
                else:
                    res+=' '
            print(legend)
            print(str(res)+"]  - "+str(init))
        elif key == keys.ENTER:
            return init





    
      