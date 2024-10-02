from typing import Tuple

data_structure = [
  [1, 2, 3],                                #0
  {'a': 4, 'b': 5},                         #1
  (6, {'cube': 7, 'drum': 8}),              #2
  "Hello",                                  #3
  ((), [{(2, 'Urban', ('Urban2', 35))}])    #4
]
def tele2(data_structure):
    glob = []
    mgb = []
    for i in data_structure:
        if type(i) == str:
            glob.append(len(i))

        if type(i) == list:
            glob.append(sum(i))

        if type(i) == dict:
            d = list(i)
            for o in d:
                fr = len(o)
                glob.append(fr)
            e = sum(list(i.values()))
            glob.append(e)

        if type(i) == tuple:
            for p in i:
                if isinstance(p, dict) == True:
                    d = list(p)
                    for o in d:
                        fr1 = len(o)
                        glob.append(fr1)
                    e1 = sum(list(p.values()))
                    glob.append(e1)
                if isinstance(p, int) == True:
                    glob.append(p)


        if type(i) == tuple:
            if isinstance(i, int) == False:
                for wew in i:
                    if type(wew) == list:
                        if len(wew) == 1:

                            if type(wew) == list and len(wew) == 1:
                                gta = (wew[0])
                                if type(gta) == set:
                                    if len(gta) == 1:
                                        for uf in gta:
                                            if type(uf) == tuple:

                                                for rur in uf:
                                                    if type(rur) == int:
                                                        mgb.append(rur)
                                                    if type(rur) == str:
                                                        btr = len(rur)
                                                        mgb.append(btr)
                                                    if type(rur) == tuple:

                                                        for error in rur:
                                                            if type(error) == str:
                                                                pdf = len(error)
                                                                mgb.append(pdf)
                                                            if type(error) == int:
                                                                mgb.append(error)
    print(sum(mgb) + sum(glob))




tele2(data_structure)
#    if isinstance(p, int) == True:
#            print(fof, p)
#            print(g)
#            glob.append(g)


  #      if len(ellem) == 1:isinstance
    #        dlin_ellem = 0
   #     else:
    #        if len(ellem) >= 2:
    #            dlin_ellem = len(ellem) - 1

# if isinstance(list_1, dict) == True:     if isinstance(ellem, int) == True:


#if isinstance(list_1, dict) == True:   если в картедже бибд.


#result = tele2(data_structure)
#print(result)
#
#ggg = data_structure[4]
#print(len(ggg[0]))