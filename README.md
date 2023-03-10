# audioclip
This program is written in Python using Pydub's library to clip audio files.

___

## Dependencies

Make sure you have Python 3 installed on your system.

Install the Pydub library by running the following command in your terminal:

> pip install pydub

You will also need ffmpeg: https://ffmpeg.org/download.html

Follow instructions for download and install. 
___

## Usage

Open a terminal or command prompt and navigate to the directory where you saved the program files.

Run the following command to launch the program:

> python clipper.py (action) (args)
  
(action) = "merge" or "clip", depending on desired function.

(args) = the mp3 files you wish to manipulate.

    NOTE: you can instead use "all" to merge / clip every mp3 file in the directory. 

The new audio file will be outputted to and /output dir which will be generated for you if not already made.

