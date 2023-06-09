from os import listdir, remove
from os.path import isfile, join

def write_txt(fname, data):
    out_folder = "output/"
    fname = fname.replace(".vtt", ".txt")
    f = open(out_folder+fname, "w")
    f.write(data)
    f.close()

def get_files(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]

def reset_output():
    out_folder = "output/"
    for f in listdir(out_folder):
        remove(out_folder+f)

def format1(in_folder):
    in_files = get_files(in_folder)
    for fname in in_files:
        f = open(in_folder+fname, "r")
        output = ""
        for line in f:
            if not ("Speaker" in line and ">" in line):
                continue
            current = line.split(">")
            output += current[1].replace("\n", "") + " "

        write_txt(fname, output)

def format2(in_folder):
    in_files = get_files(in_folder)
    for fname in in_files:
        f = open(in_folder+fname, "r")
        output = ""
        next = False
        for line in f:
            if next:
                next = False
                output += line.replace("\n", "") + " "
                continue
            
            if "-->" in line:
                next = True
    
        write_txt(fname, output)
        
reset_output()
in_folder = "input/"
# format1(in_folder)
format2(in_folder)