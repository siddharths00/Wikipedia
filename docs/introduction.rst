
Introduction
^^^^^^^^^^^^^

This report is made in reference to the 1st Programming Assignment for the course 
COP 701 - Software Systems Laboratory.

Our team built a Local markdown editor with wiki like functionality using Python
and a library which aids in GUI development for desktop applications called 
Custom Tkinter. Each of the articles being dealt with in this application has 
been written in a markdown format. These articles exist in an 'articles' folder 
in the root directory. The desktop application allows for the following 
functionalities:

* Viewing articles
* Creating articles
* Editing articles
* Removing articles

Tools & Technologies Used:
===============
The team chose to develop the application in Python since it is a very user 
friendly language with a gentle learning curve. Python is famous for being open 
source and there are many libraries and modules available at our disposal.

* ``Visual Studio``:  Visual Studio is an Integrated Development Environment developed by microsoft. The application was developed in this IDE. This IDE comes with very powerful functionalities out of the box. It's extensions and add ons make it even easier to develop applications in Visual Studio.


* ``Tkinter and Custom Tkinter``:  Tkinter(TK Interface) is a GUI library based on the TK GUI toolkit. It is one of the most common libraries when it comes to creating desktop applications in Python. Custom Tkinter is an advanced version of the same TKinter library which makes it much easier to assign themes and other GUI features to the application widgets. 


* ``tkhtmlview``:  The articles that are visible in the application are all written in markdown. There is a need for some kind of processing before the article becomes viewable. We need to first parse the input and then render the HTML as explained before. Parsing of the markdown is done in the myMarkdown module, however the rendering of the articles is managed by this library.


* ``os Library``:  Python's OS library is one of the most powerful since it can directly interact with the operating system of our machine. This OS library was used to read the file data from the articles stored on the local system.


* ``Sphinx``:  It is a very powerful document generator used by developers of Python. It works automatically by reading comments in our local files to make inferences. In the end an HTML file is generated with all the required documentation.

Authors:
========
Tarun Kumar Sharma
Ruptirumal Sai Bodavula
Siddharth S