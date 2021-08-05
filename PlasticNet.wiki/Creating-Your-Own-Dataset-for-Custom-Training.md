There are many ways to label a dataset for machine learning object detection, but the one we used, and recommend is Cloud Annotations. Cloud Annotations allows you to work collaboratively with other team members in a cloud environment, so that no progress is overwritten when multiple people are working at the same time, which is very helpful for larger datasets! Additionally, Cloud Annotations allows you to export the labeled dataset in many different formats, which is helpful for the formats we're using in this project. 

## Cloud Annotations

To get started with Cloud Annotations, go to the following site: https://cloud.annotations.ai

If you don't already have an IBM Cloud account, you can make one and create a free instance of Cloud Object Storage (up to 25 GB), which should be large enough to contain all of your cloud annotations project. 

When you have a created an account, click "Start a New Project" in the top right of Cloud Annotations. It will ask you to create a bucket, which you can name whatever you want. This is just the name of the folder that contains your project and will be the name of the file that is exported when you export your project as well.

When you've opened your project, you will be greeted with this screen. Make sure you select localization so that you are able to draw bounding boxes for objects within your images.

![Localization](https://i.imgur.com/UP6G33n.png)

You can then click File in the top left and upload your images into Cloud Annotations. After they have all uploaded, they will appear and you can scroll through them at the bottom of the screen. 

Under the File button, there's a button that says "Untitled Label." You can double click on it to change the name of the label. When you have added multiple labels, you can use this as a list to change between labels.

As you label images, they will be grouped by labels at the bottom of the screen, which allows you to easily keep track of how many instances of each type of object you have. 

## Exporting your Dataset

When you have finished labeling your dataset, you can export it by pressing File. If you are going to train with YOLO, you will want to "Export as YOLO." If you're training with TensorFlow, you will want to "Export as Pascal VOC." Then, once all of the images are downloaded, you can use the scripts provided to partition your dataset, and in the case of tensorflow, generate the necessary .record files so you can begin training. 

## Cloud Annotations Common Errors and Fixes

ISSUE: When exporting my project, cloud annotations appears stuck while zipping the files! It gets to a certain number and stops without completing.
FIX: This is likely due to one of your images being broken after deleting it. Open the console (F12) and export your model again. You should see an error that includes the image name. Go into cloud.ibm.com and find your bucket. Search for the image - if it doesn't exist, upload an image with the same name, and then delete it in cloud annotations to remove the issue. 

ISSUE: When exporting my project, many of the files appear to be missing! 
FIX: This often happens when you have a decently large dataset (> 1600 images). If you can get a stronger internet connection, it will likely download, so try a few times. If this doesn't help, our best recommendation is to create a separate bucket when you need to add more images to your dataset, and then download both of the smaller datasets, and then combine them. Just make sure the labels in each of your datasets are created in the same order and everything should work fine. 

## Other Labeling Methods

Another good option is LabelImg. You can find installation instructions and how to use it here: https://github.com/tzutalin/labelImg

Everything on LabelImg is done locally, so you're unable to work with a team on it very easily. If you're maintaining the dataset just as one person, this is likely a better option, as you won't have to upload images or download your exports at all. 

For any other annotation softwares, all that is important is that you know that if you will be using YOLO, you will either want to export as YOLO or use the option that exports with `.txt` files. If you will be using TensorFlow, you will want to export as XML due to how our pipeline was built to create `.record` files.  