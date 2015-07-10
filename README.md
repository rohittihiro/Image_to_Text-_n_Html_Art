# Image_to_Text-_n_Html_Art
You can convert images to beautiful looking text and html arts to send them as greetings.

###Usage
Go to the parent directory, i.e. the directory in which **text_n_html_art.py** resides.

Open command prompt/terminal in this directory.

And issue the command **python text_n_html_art.py [path_to_image] _[basewidth]_ _[pixel]_**

**Example : 1** python text_n_html_art.py "C:\Users\MyName\Desktop\myImage.jpg"

**Example : 2** If the image is in the same parent directory, you can simply use:

python text_n_html_art.py "myImage.jpg"

####Note
Arguments/Parameters _basewidth_ and _pixel_ are optional.

__basewidth__ : It resizes your input image, to a new image of the specified basewidth, it automatically sets the 
height to be proportional to the new basewidth. Its default value is 300 pixels if your image's width is less than 300 pixels it will not change your image size and convert as it is to the text and html art.

__pixel__ : It is for defining the size of pixel in text art, it has no affect on html art. Its default value is set to 7 pixels. You can change it and optimise for your image as per your wish.

###Samples

####Sample 1
**Input image:**
![harry.jpg in static_images folder](/static_images/harry.jpg)

**harry_html.html** will look like this:

![harry_html.png in static_images folder](/static_images/harry_html.png)

**harry_txt.html** will look like this:

![harry_text.png in static_images folder](/static_images/harry_text.png)
