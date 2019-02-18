# Mood sensing

This repository has been created to store snippets about mood sensing app excersice for Tiempo Development.

# Snippets available in this repository

  - Take a pic: Use the regular laptop camera to take a picture and get the location (latitude & longitude) where it was taken.
  - Face recognition: Check a photograph stored on your system and recognize the faces on it


You can also:
  - You can find an Flask REST API instalation where could be added the mentioned snippets above.
  NOTE: the snippets work apart of the API behaviour, it was added just to show an idea about how the data will be stored.
  - The mood recognition example is available in below github repository as it request more other files like the data set for emotions and pictures.
  https://github.com/PiotrDabrowskey/facemoji


### Tech

All the code in this repository has been created on python 3.6:

* [Django] - Django 2.1.7
* [Django Rest framework] - django rest framework 3.9.1
* [numpy] - numpy 1.16.1
* [opencv] - opencv-contrib-python 4.0
* [Pillow] - Pillow 5.4.1
* [requests] - requests 2.21.0


And of course this is the API documentation for the available endpoints.
https://docs.google.com/document/d/1I9Qaw2vjnMuLshw-hFsYem_UHieamC7Q1JjxEzvCltk/edit?usp=sharing

### Installation

All the dependencies for this repository are available in the requirements.txt file.

Install the dependencies.

```
pip install -r requeriments.txt
```
### How to use the snippets

All the snippets for this repository are available in the folder "snippets".

Face recognition:
```
python face_detect.py abba.png haarcascade_frontalface_default.xml
```
Take a pic:
```
python take_picture.py
```
Mood sensity:
```
python take_picture.py
```

### Libraries

Some of the most important libreries concidered for this are displayed here.

| Librariy | README |
| ------ | ------ |
| OpenCV | [https://opencv.org/] |
| GeoDjango | [https://docs.djangoproject.com/es/2.1/ref/contrib/gis/] |