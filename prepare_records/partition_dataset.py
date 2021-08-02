# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import glob, os, shutil

### NOTE: IF YOU HAVE MULTIPLE FILE TYPES, YOU WILL HAVE TO RUN THIS SCRIPT ONCE FOR EACH FILE TYPE AND CHANGE THE EXTENSION

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Percentage of images to be used for the test set
percentage_test = 20
counter=1
current_dir = os.path.join(current_dir, "images/")
if not os.path.isdir(os.path.join(current_dir, "train")): 
    os.mkdir(os.path.join(current_dir, "train"))
    os.mkdir(os.path.join(current_dir, "test"))
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        shutil.move(str(pathAndFilename), current_dir + "test/" + str(title) + str(ext))
        shutil.move(str(pathAndFilename)[:-3] + "xml", current_dir + "test/" + str(title) + ".xml")
    else:
        shutil.move(str(pathAndFilename), current_dir + "train/" + str(title) + str(ext))
        shutil.move(str(pathAndFilename)[:-3] + "xml", current_dir + "train/" + str(title) + ".xml")
        counter = counter + 1

