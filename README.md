# Bachelor's thesis

Based on the growing number of diseases caused by thyroid disorders, the topic of my thesis was to create a web application to support medical decision making with the help deep convolutional neaural networks. 

The thyroid nodule detection is performed by a pre-trained convolutional neural network, which is able to determine the position of nodules based on an input ultrasound image, and to classify the malignancy category according to the unified TI-RADS scoring system. The user interface is a web application, where doctors beside running the object detection itself, they can perform statistical analysis of the prevalence of the disease, either in different age groups or gender distribution.
Based on the results of research in medical object detection, I chose the Faster R-CNN neural network model. This model has been used to achieve higher node localization results on a small dataset, which has similar composition to mine, than other state-of-the-art neural model architectures.

After several transformation process on the dataset, I was able to achieve 73% accuracy in binary classification of thyroid nodes.

# EXPLONATION

The "APPLICATION" directory opens up several other directories, which contain codes of the training itself, raw data processing, python web application with the frozen model and the main web application which performs as an UI. The main web application was written in C# (ASP.NET Core), on the frontend side using VUE.js framework and it has a cloud hosted database on Microsoft Azure Cloud. 
