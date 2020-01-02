# css-cutter
Removes unwanted CSS rules from large CSS files. This repository has two files.

cutter_with_UI.py: Useful if you want to use this with a UI <br>
cutter_without_UI.py: Useful if you just want the cutting algorithm

## My use case
I run a website through Webflow which allows me to build pages with a visual editor and export code. A small part of my website is hosted on a separate hosting provider and only needs 30ish classes out of the hundreds on the main website, but webflow puts the entire website's style rules into one file. I made this script so that I don't have to repeatedly delete the style rules I don't need and cut down from having .4mb of style rules to 10kb.

## Instructions - cutter_with_UI.py
![Example](https://github.com/Kameron2442/css-cutter/blob/master/UI.png)
1. Download and open cutter_with_UI.py
2. UI uses Tkinter
3. Select your file to edit and enter class names, IDs, prefixes...
4. Hit Cut File

## Instructions - cutter_without_UI.py
1. Download and open cutter_without_UI.py 
2. In the first line, rename the "read_file" string to the path of your file to cut
3. Rename all the styles you want to keep to have the same unique first few letters if you want
4. In the second line, rename the "to_keep" String to the first few letters of the styles you want to keep
5. Run cutter_without_UI.py
