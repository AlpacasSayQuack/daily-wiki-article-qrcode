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

There are two shell scripts. They work in the linux terminal.
One automatically installs the python dependences. 
The other runs the script and then will automatically open the QRcode. 

NOTE: The bash shell scripts run in the linux terminal
