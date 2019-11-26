import os
import time
from os import listdir
from os.path import join


def list_files1(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))


def fuc(mypath,wcfilter):
    solution = []
    take = []
    print(wcfilter)
    if wcfilter:
        extesion_filter = (list_files1(mypath, wcfilter))
        for f in extesion_filter:
            take.append(f)
    else:
        take = listdir(mypath)

    for f in take:
        newp = (join(mypath, f))
        if os.path.isdir(newp):
            type = '<DIR>'
        elif os.path.isfile(newp):
            type = ' <FILE>'
        tup = (f,  'Modified time:', time.ctime(os.path.getmtime(newp)), 'Size:', os.path.getsize(newp), type)
        solution.append(tup)
    return solution
