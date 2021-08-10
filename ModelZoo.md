## PlasticNet Model Metrics 

**For pre-trained weights to train a PlasticNet model from scratch, see the bottom of this page!**

### TensorFlow Models
* [PlasticNet EfficientDET D1 **9 classes**640x640](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/efficientdet_d1_640x640_9classes_v2.tar.gz)

   Model File Name: efficientdet_d1_640x640_9classes_v2

   Transfer Learning From: TensorFlow efficientdet_d1

   Average Loss: 

                class_loss: 0.08758,

                localization_loss: 7.339e-4,

                regularization_loss: 0.08055,  

                total_loss: 0.1686

* [PlasticNet Faster-RCNN **9 classes** 640x640](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/faster_rcnn_640x640_9classes_v1.tar.gz)

   Model File Name: faster_rcnn_640x640_9classes_v1

   Transfer Learning From: PlasticNet Model: faster_rcnn_640x640_7classes_v2

   Average Loss:
                 
                localization_loss’: 0.16872177,

                localization_loss’: 0.24726836,

                objectness_loss’: 0.05993971,

                regularization_loss’: 0.0,  

                total_loss’: 0.63053286,
          

* [PlasticNet FasterRCNN 7 Classes 640x640 v2](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/faster_rcnn_640x640_7classes_v2.tar.gz)
   
   Model File Name: faster_rcnn_640x640_7classes_v2

   Transfer Learning From: PlasticNet Model: faster_rcnn_640x640_7classes_v1

   
   Average Loss: 
   
                 ‘classification_loss’: 0.1095

                 ‘localization_loss’: 0.3035

                 ‘objectness_loss’: 0.01122,

                 ‘regularization_loss’: 0.0,

                 ‘total_loss’: 0.4964
                
* [PlasticNet FasterRCNN 7 Classes 640x640 v1](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/faster_rcnn_640x640_7classes_v1.tar.gz)
   
   Model File Name: faster_rcnn_640x640_7classes_v1

   Transfer Learning From: TensorFlow Base Model: Faster R-CNN ResNet101 V1 640x640

   Average Loss: 
   
                 classification loss is 0.006, 
                 
                 localization loss is 0.0024, 
                 
                 regularization loss is 0.00, 
                 
                 total loss is 0.0224

* [PlasticNet SSD-Resnet 7 Classes 640x640](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/ssd_resnet_640x640_7classes_v1.tar.gz)

   Model File Name: ssd_resnet_640x640_7classes_v1

   Transfer Learning From: TensorFlow base model: SSD ResNet152 V1 FPN 640x640 (RetinaNet152)

   Average Loss: 

                 ‘classification_loss’: 0.06852589

                 ‘localization_loss’: 0.025546694,

                 ‘regularization_loss’: 0.35246804,

                 ‘total_loss’: 0.4465


### YOLO Models

* ***Best YOLO Model*** **PlasticNet YOLO 9 Classes 448x448 v3**

   Conv File Name (for transfer learning, click to download): [yolo9class448x448v3.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo9class448x448v3.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo9class448x448v3weights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo9class448x448v3weights.tar.gz)

   Average Loss: 2.33
   
* **PlasticNet YOLO 9 Classes 480x480 v2**

    Conv File Name (for transfer learning, click to download): [yolo9classv2iter27000.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo9classv2iter27000.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo9classv2iter27000weights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo9classv2iter27000weights.tar.gz)

   Average Loss: 2.183

* **PlasticNet YOLO 9 Classes 480x480 v1** 

    Conv File Name (for transfer learning, click to download): [yolo9class480x480.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo9class480x480.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo9class480x480weights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo9class480x480weights.tar.gz)
   
   Average Loss: 2.378

* **PlasticNet YOLO 7 Classes v3 576x576**

    Conv File Name (for transfer learning, click to download): [yolo7class576x576.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo7class576x576.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo7class576x576weights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo7class576x576weights.tar.gz)

   Average Loss: 2.45

* **PlasticNet YOLO 7 Classes v2 416x416**

  Conv File Name (for transfer learning, click to download): [7classyoloV2.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/7classyoloV2.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [7classyoloV2weights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/7classyoloV2weights.tar.gz)

   Average Loss: 2.47

* **PlasticNet YOLO 4 Classes Image Augmentation 416x416**

    Conv File Name (for transfer learning, click to download): [yolo4classesimgaug.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo4classesimgaug.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo4classesimgaugweights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo4classesimgaugweights.tar.gz)

   Average Loss: 1.48

* **PlasticNet YOLO 4 Classes v2 416x416**

   Conv File Name (for transfer learning, click to download): [yolo4classesupdated.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo4classesupdated.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo4classesupdatedweights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo4classesupdatedweights.tar.gz)

   Average Loss: N/A

* **PlasticNet YOLO 4 Classes v1 8000 iterations 416x416**

   Conv File Name (for transfer learning, click to download): [4class8000iteration.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/4class8000iteration.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [4class8000iteration](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/4class8000iteration.tar.gz)

   Average Loss: N/A

* **PlasticNet YOLO 2 Classes Image Augmentation 416x416**

   Conv File Name (for transfer learning, click to download): [yolo2classes-imguag.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo2classes-imguag.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo2classes-imguagweights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo2classes-imguagweights.tar.gz)

   Average Loss: N/A

* **PlasticNet YOLO 2 Classes v1 416x416**

   Conv File Name (for transfer learning, click to download): [yolo2classes3000iterations.conv.81](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo2classes3000iterations.conv.81.tar.gz)
   
   Weights File Name (for testing, click to download): [yolo2classes3000iterations](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolo2classes3000iterations.tar.gz)

   Average Loss: 6.67

* [Darknet YOLO 12 Classes Pre-Trained Weights](https://plasticnet-models.s3.us.cloud-object-storage.appdomain.cloud/yolov4.conv.137.tar.gz)

   ***This pre-trained weights is if you want to train a new PlasticNet model from scratch using the provided Darknet generic pretrained weights from https://github.com/mattokc35/darknet, not using a pre-trained PlasticNet model!***

   Model File Name: yolov4.conv.137

   Average Loss: N/A



