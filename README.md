# css-deleter
Removes unwanted CSS rules from large CSS files

## Use case
Usefull if you develop a website using a platform such as Webflow, export parts of the website on different hosts, and don't need all CSS rules to be present on each host. In my case, I have a website with a forum which only needs a few hundred styles from my main website. My website has .4mb worth of CSS rules in one file which I can cut to around 10kb for my website's forum.

## Instructions
1. Download and open cutter.py 
2. In the first line, rename the "read_file" string to the name of your file to cut
3. Rename all the styles you want to keep to have the same unique first few letters
4. In the second line, rename the "to_keep" String to the first few letters of the styles you want to keep
5. Run cutter.py in the same directory as the file which you are cutting
