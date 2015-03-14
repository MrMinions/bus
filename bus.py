dict_and={"375":["345","123","432"],"345":["23","32"],"123":["1","2"],"23":["3","4"],"3":["5","6"]}
findit = 0
changeno = ""
def find(n,end):
        global findit,changeno
        if dict_and.has_key(n):
                l_n = dict_and[n]
        else:
                return
        for n1 in l_n:
                if n1 == end :
                        print n1
                        findit = 1
                        changeno = n
                        return
                else:
                        find(n1,end)
                        if changeno == n1:
                                print n1
                                changeno = n
findit = 0
find("375","5")
changeno = ""
findit = 0
find("375","6")
changeno = ""
findit = 0
find("375","3")