# Face Recognition using Convolution Neural Networks

  ![Python](https://img.shields.io/badge/Python-3.6-green.svg)
  ![Stars](https://img.shields.io/github/stars/syamkakarla98/Face_Recognition_Using_Convolutional_Neural_Networks?color=tomato)
  ![Forks](https://img.shields.io/github/forks/syamkakarla98/Face_Recognition_Using_Convolutional_Neural_Networks)
  ![issues](https://img.shields.io/github/issues/syamkakarla98/Face_Recognition_Using_Convolutional_Neural_Networks)
  ![License](https://img.shields.io/github/license/syamkakarla98/Face_Recognition_Using_Convolutional_Neural_Networks)
  

## Team Members
* Syam Kakrala
* M. Sai Rahul 
* G. Priyaranjan Reddy
* C. Sai Charan Singh 
* Dr. T. Hiterndra Sarma

### Abstract
Convolutional Neural Networks has been playing a significant role in many applications including surveillance, object detection, object tracking, etc. Extensive research is recorded for face recognition using CNNs, which is a key aspect of surveillance applications. In most recent times, the Face Recognition technique is widely used in University automation systems, Smart Entry management systems, etc. In this paper, a novel CNN architecture for face recognition system is proposed including the process of collecting face data of students. Experimentally it is shown that the proposed CNN architecture provides 99% accuracy. Further, the proposed CNN framework is used to develop a “Smart Attendance Management System (SAMS)“, which is a web-based application, to provide attendance of students using face recognition, in realtime. The proposed application is easy to deploy and maintain.

### Project Description
The application gives a complete description  regarding dataset creation i.e, collection of images and creating of **CSV** files as well as exploratory analysis of the generated data including development of a custom **CNN model** using convolutional layers, maxpooling, dropout and dense layers by hyperparameter tuning resulting the increase in accuracy.

Firstly, coming to the dataset creation, the current repository contains a folder namely:
* **Dataset_Creation** consisting of two python scripts **Create_Dataset.py**  used to capture images, **convert_to_csv.py** used to generate the dataset i.e, a csv file.

By executing the **Create_Dataset.py** file, it prompts the user for his/her desired label, number of images to be captured and then starts capturing the required number of images and stores them into a folder with the name previously prompted for. Then by executing the **convert_to_csv.py** file those collected images can be converted into a CSV file.



### The Research paper "Smart Attendance Management System Based on Face Recognition Using CNN" is published in [IEEE](https://ieeexplore.ieee.org/abstract/document/9242847). DOI: 10.1109/HYDCON48903.2020.9242847
