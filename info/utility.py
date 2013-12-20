'''
Created on Dec 19, 2013

@author: kyle
'''

def convert_array_to_Yx3(val):
    out_list_list = []
    for i in xrange(len(val)/3 + 1):
        out_list_list.append([])
        for j in xrange(3):
            if i*3+j < len(val):
                out_list_list[i].append( val[i*3+j] )
    return out_list_list
    