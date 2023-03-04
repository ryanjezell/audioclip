import sys
from pydub import AudioSegment
import os
import shutil

current_dir = os.getcwd()
output_dir = os.path.join(current_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


## Take every command line argument from index 1 onwards
args = sys.argv[1:] 

## Formula = x * 1000, where x is desired seconds to clip off the end and * 1000 is accounting for millisecond format ##
back_clip_time = 2 * 1000 

## Export path determination
export_path =  "output/clipped_" if os.name == 'nt' else "output\clipped_"

def main():
    validCheck(args)
    backClip(args)


# Clip off last <seconds> of audio
def backClip(*args):
    lst = []

    for arg in args:
        lst.extend(arg)


    for i in lst:
        whole_video = AudioSegment.from_mp3(i)
        desired_clip = whole_video[:len(whole_video) - back_clip_time]
        desired_clip.export(export_path + i, format="mp3")
       




# Check for valid arg entry
def validCheck(*args):
    if len(args) == 0:
        exit()
    

main()
