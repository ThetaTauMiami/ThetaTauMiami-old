'''
Created on Dec 19, 2013

@author: kyle
'''

def convert_array_to_YxZ(val, z):
    out_list_list = []
    for i in xrange(len(val)/z + 1):
        out_list_list.append([])
        for j in xrange(z):
            if i*z+j < len(val):
                out_list_list[i].append( val[i*z+j] )
    return out_list_list
    