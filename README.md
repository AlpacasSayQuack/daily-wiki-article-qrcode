# daily-wiki-article-qrcode
I'm a beginner at Github and a semi-beginner at python so bare with me. Any comments are welcome.

Do you want a quick and easy way to read the wikipedia article each day?
Required python libraries:
datetime
qrcode
PIL
PIL Image

This short script works as follows:
It uses datetime to get today's date.
This date is inserted into the wikipedia URL
The qrcode then generates a QRcode for that URL and the code is saved as a PNG.

The QRcode's properties (size etc) is modifable. See comments in daily-wiki.py

There are bash shell scripts included. 
They work in the linux terminal and will run the python script without
having to type "python3 daily-wiki.py".

The bash scripts: 

Dependancies / install-dependancies.sh:
  The following dependancies are required:
    Python3 or newer
    The following libraries:
    qrcode
    datetime
    PIL
    Image from PIL
  You can automatically install all the dependancies by running
  install-dependancies.sh. It will install/verify the above libraries
  and python3 install.

  start-program.sh 
    This script is best used when you don't need to view the QRcode after creation.
    Some examples:
      You make a bot to tweet out the code each day;
      You are going to display it on a Raspberry piHAT screen;
      You are going to schedule the script to run once a day.
  Imageviewing scripts:
  PiOS-start-program.sh
    This script is for Raspberry Pis running PiOS or Raspbian, maybe NOOBS.
    It will launch the default imageviewer on PiOS, GPicView. 
  start-program-xviewer
    This script is to launch xviewer, my default image viewer program right after creation.
    You can always modify the code to have it launch your favorite or needed program. 
