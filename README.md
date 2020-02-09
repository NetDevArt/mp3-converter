# README

This README would normally document whatever steps are necessary to get your application up and running.

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

I put the MediaInfo.dll under "*modules/pymediainfo/pymediainfo/*" which is also a wrapper containing python methods to control the lib.

### ffmpeg program

In the other hand, you will need the ffmpeg programm to allow you converting a file to the expected media format.  
I am using the subprocess package to use the ffmpeg command.

However, in order to use the command by the subprocess, you must register the ffmpeg binary location to your environment Path, then restart your computer.
The relative path is : ${project_location}/modules/ffmpeg/bin  
> Where **${project_location}** is the folder where you cloned my repository.