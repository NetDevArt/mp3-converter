# README

This README document whatever steps are necessary to get your application up and running on a Windows environment (x64).

## mp3_converter

Its name speak for itself. This little piece of code aims to make mp3 conversion easier, faster and Lightweight...  
Indeed, i was looking for a simple massive audio converter, and it was hard to get one which fit with my special needs.  
So I decided to code my own converter, and then I publish it in open source ;)

## How do I set up ?

I consider that you have a perfect working python environment for the steps below.
* MediaInfo
* ffmpeg

To set my python environment, I'm using pycharm, within python 3.8 

### MediaInfo library

First of all, you will have to install the MediaInfo library to get some informations about a file.  
In fact, this library allows you to know if a file is an Audio/Video type. Then, you could enhance the code in order to play with metadata information or modify the media quality etc.

I put the MediaInfo programm with its dll under "*modules/pymediainfo/pymediainfo/*". This program is a wrapper containing python methods to control the lib

**Links** 
> *These links are normally not needed because I had added MediaInfo to my modules sources...*    
[Here is the documentation](https://pymediainfo.readthedocs.io/en/stable/)  
[Download the MediaInfo programm](https://mediaarea.net/en/MediaInfo)  
[Download your own MediaInfo.dll](https://mediaarea.net/fr/MediaInfo/Download/Windows)

By downloading the MediaInfo program, you should have access to the dll. If it is not working, try to download a most recent dll (choose x32 or x64 to fit with your windows architecture).

### ffmpeg program

In the other hand, you will need the ffmpeg programm to allow you converting a file to the expected media format.  
I am using the subprocess package to use the ffmpeg command.

However, in order to use the command by the subprocess, you must register the ffmpeg binary location to your environment Path, then restart your computer.
The relative path is : ${project_location}/modules/ffmpeg/bin  
> Where **${project_location}** is the folder where you cloned my repository.

**Link**  
> *As I did it with MediaInfo, I had added the ffmpeg sources to my modules folder...*  
[Download ffmpeg for windows](https://ffmpeg.org/download.html)

**MP3 Codecs**  
After restarting your computer, try to call ffmpeg in a command line terminal (like in your pycharm IDE, or else...).  
You should see *--enable-libmp3lame*  
If so, it's all good, the programm should be perfectly working. 

### Use the program

Type the command bellow, and follow the two steps.
- python mp3_converter.py
  - The program ask you to tell him where is your MediaInfo.dll
  - Then it ask you to tell him which folder you want to process recursivly
  - Then, grab a coffee and wait until finish
  
  
## It is not working ?

Please, let me know the stacktrace you get, I could help you ;) 