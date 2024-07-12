import sys
import os





# creating files

for alpha in range(97, 122):

    with open(f"{chr(alpha)}_blog.md", "w") as file:

        file.write(f"# This is a webhook test for file: {chr(alpha)}_blog.md");





