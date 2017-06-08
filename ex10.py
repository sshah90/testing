tabline = "\tI'm tabbed in."
splitline = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"
fat_cat = """
I'll do a list:
\t* Cat food
\t* fishes
\t* catnip\n\t* Grass
"""
print tabline
print splitline
print backslash_cat
print fat_cat

while True:
 for i in ["/","-", "|", "\\", "|"]:
 print %s\r %i,