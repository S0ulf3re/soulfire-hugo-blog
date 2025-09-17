---
title: "3D Printing"
date: 2025-03-20
tags: 
  - "technology"
---

So these past couple of months have really been the prime time for me to finally get ahold of a lot of the things that I have always wanted. I managed to get a robotic vaccum, a nice set of speakers, and, of todays topic, a 3D printer.

The specific model I got isn't particuarly exciting. It's a random Chinese brand called Flashforge, and the model is the Flashforge Adventurer 5M. I got it at the beginning of February, and it arrived while I was sick. But I immediately pulled the strength that I had to haul it downstairs and set it up.

During the process, however, I accidentally managed to break the hinge on the display. So, after a few weeks of waiting for a replacement and fiddling with the display ribbon more to get a minimal amount of picture to set up a few things, the printer had been fully completed.

3D printers are interesting because they're not exactly like regular printers. Unlike a regular printer, a 3D printer isn't always successful, and it's pretty rare that you would need to print out something again with a regular printer (barring running out of ink, paper jams, etc.)

  
But the entire 3D printing process is a very intricate one, one that involves precision and is codependent on everything being exactly right. Of course, if you maintain your printer well, you don't have to worry as much about it messing up. But even then, not everything is going to come out exactly the way you want it. From what I know, a 3D printer prints by following the instructions it is given. These instructions simply command the printer to extrude filament that is hot enough to bend into shape, but cool enough that it quickly hardens so that another layer can be placed on top of it. Repeat this process hundreds of times, and eventually, you end up with a finished product.

As you might guess, just like building a house by laying all the bricks together, this is a delicate process, and a desired result isn't always garunteed to happen on the first try. Problems I've already ran into include:

- The filament gets jammed. Leading to nothing being printed as the nozzle moves around

- The build is knocked over, causing the printer to try and lay filament on air (that falls to the plate, creating a mess

- The printer extrudes too much filament at once. Resulting in a giant mess of filament stuck together at the nozzle

- The build gets stuck to the nozzle. Leaving an unfinished build with a giant goopy substance attached to it.

Many of these problems can be fixed with some common troubleshooting I picked up in my A+ certification, and often just involve running some functions from the printer itself. But it definately doesn't detract from the dissappointment of a failed model and all it's wasted filament.

## Why I wanted a 3D Printer

In addition to thinking that they were cool, I wanted to be able to print a lot of the things that I had been considering ordering off of Amazon, but didn't really want to because it just didn't seem worth it to spend 10-30$ over and over again on random things made out of plastic. Especially compared to making a one time purchase, plus multiple purchases of filament that could could make a lot of those things. Coupled with a little DIY, I could probably save a lot of money and make something that looks just as good, and more customized as well.

At least right now, I can do that, provided there's an STL file available. In terms of creating models, I'm only a little bit good with Blender, and FreeCAD feels like it's way out of my territory for something I could learn. A lot of the stuff behind it feels like something that an engineer would do (I wanted to be a software engineer at one point, but only because I thought that the title "engineer" sounded really nice and important).

Instead of going off that though. I think I would rather just infodump a lot of different information about the 3D printing pipeline so you can get an idea of it and how interesting it can be.

## How the 3D printing process works

The printing process starts with the model you want to use. This would probably be in the format of a Stereolithography (STL ) file. There's a few other formats as well, but this one is the most common and compatible out there.

Whether you made this model, or downloaded it off the internet, it's first stop is the Slicer. For me, this one is OrcaSlicer, an open source application based on PrusaSlicer and BambuStudio.

The slicer is where the model is inspected, adjusted, checked if it's physically possible to print as shown (and make adjustments, such as adding supports, if needed) and converted into instructions that the printer can use to adjust it's settings and know what paths it should take for extruding filament. It converts the model into a programming language called G-code (which was first made in 1963, according to Wikipedia). It kind of looks like Assembly with code that looks like this:

```
;WIPE_START
G1 F3000
G1 X-21.395 Y-9.05
;WIPE_END
G1 X-14.638 Y-5.5 Z.6 F30000
G1 X.099 Y2.242 Z.6
G1 Z.2
G1 E.8 F2100
```

Basically, a lot of function names and commands that instruct specific adjustments the printer should make to it positioning and settings. The `G1` command specifically tells the printer it should move the print head in a straight line.

There are other commands as well, each of which look something like the ones shown but with a different number and letter. And tell the printer a variety of things from:

- Adjusting the fan speed, plate level, and extruder temperature

- Starting and stopping certain components

- Turning and moving the print head in different directions

Overall though, it's not particuarly important to know this if all you want to do is print. But it's good to know so you can understand whats happening, especially if you want to start playing with more advanced, open source firmware like Klipper that rely more on you setting up different macros and having much more fine grain control of your printer.

The point is, the slicer converts the model into G-code, and gives you a preview of what the model might look like when it's printed. From there, you can either export the G-code file, place it onto a flash drive, insert it into the printer, and print it from the on screen menu. Or in my case, directly send the gcode file to the internal storage of the printer and automatically start printing.

If it helps any, you can think of the slicer as essentially being the Print Dialog Box you get whenever you press `Control/Command + P`. It has a ton of options, but chances are, depending on what you are doing, you may only need to press a single option, or none at all. It just so happens that printing a 3D model to a 3D printer isn't something that one does everyday to justify including a slicer in every app.

## What can I Print?

The thing that I have printed the most, with 3 of them. Is [#3DBenchy](https://www.3dbenchy.com), which is a popular little tugboat model that serves a calibration model of sorts. It's symmetrical design with lots of overhangs and caves, coupled with it's ability to be printed in place (sliced without changing any settings), it's quick print time (a little over half an hour for me) as well as how cute it looks, makes it a popular model for testing if your printer is working correctly. In fact, as of right now, it's actually one of the most downloaded models on [Thingiverse](https://thingiverse.com), and recently entered the public domain as well.

## Conclusion

These printers, while a little cumbersome to work with, and involving some things that are a little bit beyond my scope of knowledge. Are ultimately very interesting to work with. As long as you make sure to adjust your expectations, and know what it is that they can and cannot do. I would recommend getting one if you have the ability to.
