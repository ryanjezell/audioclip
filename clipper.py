import sys
from pydub import AudioSegment
import os


## Check to see if output folder exists, creates one if not
current_dir = os.getcwd()
output_dir = os.path.join(current_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


## Take every command line argument from index 1 onwards, and quit if there isn't any input. 
args = []
args = sys.argv[1:]
if len(args) == 0:
    print("Input 'clip' or 'merge and then the file name(s)")
    sys.exit()

## Formula = x * 1000, where x is desired seconds to clip off the end and * 1000 is accounting for millisecond format ##
back_clip_time = 2 * 1000 

## Export path determination
clipped_path =  "output/clipped_" if os.name == 'nt' else "output\clipped_"
merged_path = "output/merged_"if os.name == 'nt' else "output\merged_"

def main():
    keyWord(args)

## recognize first word command
def keyWord(args):
    
    if len(args) < 2:
        print("Error: Input 'merge' or 'clip and then the file name(s) you wish to execute the action on.")
        return

    if args[0] == "merge":
        args.remove("merge")
        mergeClips(args)

    elif args[0] == "clip": 
        args.remove("clip")
        backClip(args)

    else:
        print("Error: Input 'merge' or clip' before file name(s).")
    

# Clip off last <seconds> of audio
def backClip(args):

    for i in args:
        whole_clip = AudioSegment.from_mp3(i)
        desired_clip = whole_clip[:len(whole_clip) - back_clip_time]
        desired_clip.export(clipped_path + i, format="mp3")

def mergeClips(args):

    length = len(args)

    firstClip = AudioSegment.from_mp3(args[0])

    for index in range(1, length):
        i = args[index]
        mergeClip = AudioSegment.from_mp3(i)
        combined = firstClip + mergeClip
        firstClip = combined
    combined.export(merged_path + i, format="mp3")

            
main()