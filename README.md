# Mood sensing

This repository has been created to store snippets about mood sensing app excersice for Tiempo Development.

# Snippets available in this repository

  - Take a pic: Use the regular laptop camera to take a picture and get the location (latitude & longitude) where it was taken.
  - Face recognition: Check a photograph stored on your system and recognize the faces on it
  - Check the mood of that picture


You can also:
  - You can find an Flask REST API instalation where could be added the mentioned snippets above.
  NOTE: the snippets work apart of the API behaviour, it was added just to show an idea about how the data will be stored.


> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

All the code in this repository has been created on python 3.6:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

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
