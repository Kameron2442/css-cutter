read_file = "YOUR_FILE.css"  # The path of the file which will be cut
to_keep = ".navbar-"  # The class name or prefix of class names that you want to keep

file = open(read_file, "r")
new_file = ""  # String to hold the style rules that are kept
get_styles = 0  # Flag for if to_keep in found in a line
get_media = 0  # Flag for if a media rule is present
flag = 0  # Flag gets activated if a "}" has already been claimed by a previous if-statment for belonging to a style rule. In short, it checks if the "}" belongs to a media rule.

for line in file:
    flag = 0
    if get_styles == 1 and "}" not in line:
        new_file += line
    if to_keep in line:
        new_file += line
        get_styles = 1
    if get_styles == 1 and "}" in line:
        new_file += line
        get_styles = 0
        flag = 1

    if to_keep not in line and "{" in line:
        get_styles = -1
    if get_styles == -1 and "}" in line:
        get_styles = 0
        flag = 1

    if "media" in line:
        new_file += line
        get_media = 1

    if get_media == 1 and "}" in line and get_styles == 0 and flag == 0:
        new_file += line
        get_media = 0


print(new_file)

file = open("output.css", "w")
file.write(new_file)
file.close()
