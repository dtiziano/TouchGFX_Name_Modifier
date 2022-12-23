#ask for the directory where the code is stored

from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

# get the new project name directly from the naming of the touchGFX project
x = folder_selected.split("/")
new_project_name=x[-1]


#replace the names in ./STM32CubeIDE/.project

file_to_modify=folder_selected+"/STM32CubeIDE/.project"
# Read in the file
with open(file_to_modify, 'r') as file :
  filedata = file.read()
# Replace the target string
filedata = filedata.replace('STM32F469I-DISCO', new_project_name)

# Write the file out again
with open(file_to_modify, 'w') as file:
  file.write(filedata)

  #replace the names in ./STM32CubeIDE/.cproject

file_to_modify=folder_selected+"/STM32CubeIDE/.cproject"

# Read in the file
with open(file_to_modify, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('STM32F469I-DISCO', new_project_name)

# Write the file out again
with open(file_to_modify, 'w') as file:
  file.write(filedata)

#replace the names in ./TouchGFX/ApplicationTemplate.touchgfx.part

file_to_modify=folder_selected+"/TouchGFX/ApplicationTemplate.touchgfx.part"

# Read in the file
with open(file_to_modify, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('STM32F469I-DISCO', new_project_name)

# Write the file out again
with open(file_to_modify, 'w') as file:
  file.write(filedata)

#replace the names in ./TouchGFX/new_project_name.touchgfx

file_to_modify=folder_selected+"/TouchGFX/"+new_project_name+".touchgfx"

# Read in the file
with open(file_to_modify, 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('STM32F469I-DISCO', new_project_name)

# Write the file out again
with open(file_to_modify, 'w') as file:
  file.write(filedata)

  # find the .ioc file that has to be renamed
import os
for file in os.listdir(folder_selected):
    if file.endswith(".ioc"):
        file_to_modify=os.path.join(folder_selected, file)
        #print(file_to_modify)

# rename the .ioc file

# Destination
new_file_name=folder_selected+"/"+new_project_name+".ioc"
#print(new_file_name)
# Renaming the file
os.rename(file_to_modify, new_file_name)

print("Done renaming the files")
