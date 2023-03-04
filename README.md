# audioclip
This program is written in Python using Pydub's library to clip audio files.

Installation

Make sure you have Python 3 installed on your system.

Install the Pydub library by running the following command in your terminal:

pip install pydub

Clone the repository or download the ZIP file and extract it to your desired location.

Usage
Open a terminal or command prompt and navigate to the directory where you saved the program files.

Run the following command to launch the program:
python clipper.py

And then add the files you wish to clip, using command line arguments (subject to change), make sure to include complete file name AKA "clip1.mp3"

The new audio file will be saved in the same directory as the original file with the prefix clipped attached to the file name.

Limitations
This program only works with audio files that are supported by Pydub (see the Pydub documentation for a list of supported file types).

This program may not work correctly with audio files that have a variable bitrate or sample rate.
