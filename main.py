from os import listdir, remove
from os.path import isfile, join
from re import sub

def write_txt(fname, data):
    out_folder = "output/"
    fname = fname.replace(".vtt", ".txt").replace(".srt", ".txt")
    f = open(out_folder+fname, "w")
    f.write(data)
    f.close()

def get_files(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]

def reset_output():
    out_folder = "output/"
    for f in listdir(out_folder):
        remove(out_folder+f)

def main(in_folder):
    in_files = get_files(in_folder)
    for fname in in_files:
        f = open(in_folder+fname, "r")
        output = ""
        next = False
        for line in f:
            if next:
                next = False
                line = sub("<[^>]*>", "", line) # remove tags
                output += line.replace("\n", "") + " "
                continue
            
            if "-->" in line:
                next = True
    
        write_txt(fname, output)

        
reset_output()
in_folder = "input/"
main(in_folder)
