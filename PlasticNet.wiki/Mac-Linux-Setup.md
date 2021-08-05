## Mac/Linux Setup

Due to the nature of TensorFlow installation, PlasticNet currently only supports UNIX environments. For more information, look at the FAQ.

To set up PlasticNet on your local mac or linux machine, you will first need to install protobufs:  https://github.com/protocolbuffers/protobuf/releases

Download the correct version for your Operating System, then extract the zip. Add this directory to your system path so that the protoc command is recognized.

Once you have completed this, clone PlasticNet in the location of your choice and create a conda environment for the project. Then, run the following command:

```
python setup.py
```

After this has completed successfully, if you are on MacOS, you can restart your terminal session and run PlasticNet to enter the CLI, or you can follow the instructions on [Using PlasticNet without the CLI](https://github.ibm.com/spacetech-interns/PlasticNet/wiki/Using-PlasticNet-Without-the-CLI) to run the Python Scripts Directly. 

If you are on Linux, you will need to run the command line interface script directly. 
Run the following command to launch the CLI.
```
python PlasticNet.py
```

You are also able to run the python scripts directly, using the same instructions as listed above: https://github.ibm.com/spacetech-interns/PlasticNet/wiki/Using-PlasticNet-Without-the-CLI