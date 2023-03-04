import sys
from pydub import AudioSegment

# Take every command line argument from index 1 onwards
args = sys.argv[1:] 


## Formula = x * 1000, where x is desired seconds to clip and * 1000 is accounting for millisecond format ##
clip_time = 2 * 1000 


def main():
    validCheck(args)
    audioClip(args)


# Clip off last <seconds> of audio
def audioClip(*args):
    lst = []

    for arg in args:
        lst.extend(arg)


    for i in lst:
        song = AudioSegment.from_mp3(i)
        desired_clip = song[:clip_time]
        desired_clip.export("clipped" + i, format="mp3")


# Check for valid arg entry
def validCheck(*args):
    if len(args) == 0:
        exit()
    

main()
