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
import os, sys

# Install required dependencies
os.system("pip install -r requirements.txt")

# Clone the tensorflow/models respository
current_dir = os.path.dirname(os.path.abspath(__file__))


# Clone the PlasticNet YOLOv4 Darknet Forked Repository
if not os.path.isdir(os.path.join(current_dir, "darknet")): 
    os.system("git clone https://github.com/mattokc35/darknet.git")

# Set up the darknet directory by running make
os.chdir('darknet')
os.system('make')
os.chdir('../')

# Clone the TensorFlow Model Garden
if not os.path.isdir(os.path.join(current_dir, "models")): 
    os.system("git clone https://github.com/tensorflow/models.git")


# Change to research directory and complete TensorFlow Setup
os.chdir('models/research')
print(str(os.getcwd()))
os.system("protoc -I=./ --python_out=./ ./object_detection/protos/*.proto")
sys.path.append(str(current_dir) + '/sli')
sys.path.append(str(current_dir) + "/models")
print(str(current_dir) + "/models")
os.chdir("../../")


# Convert command line client file into an executable
current_path = os.getcwd()
print(current_path)
os.system("cp PlasticNet.py PlasticNetCopy.py")
os.system("chmod +x PlasticNetCopy.py")
os.system("mv PlasticNetCopy.py PlasticNet")

#permanently add PlasticNet to your bin $PATH
os.system('mkdir -p ~/bin')
os.system('cp PlasticNet ~/bin')

### WORKING FOR MACOS
file_read = open(os.path.expanduser("~") + '/.zshrc', 'r+')
readfile = file_read.read()
if not 'PATH=$PATH":$HOME/bin"' in readfile:
    file = open(os.path.expanduser("~") + '/.zshrc', 'a')
    file.write('\nexport PATH=$PATH\":$HOME/bin\"')

print("********************************")
print("SUCCESS!!!!!")
print("Dependencies installed. Please restart your terminal session and type PlasticNet from any location to run")
print("********************************")

