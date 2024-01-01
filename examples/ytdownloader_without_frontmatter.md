## About this :

YTdownloader is a python tkinter application which can help you to download any youtube video as a video or audio. In this post we will discuss how to create it.

> **Assuming that you know the basics of tkinter, I am not going into the detail of tkinter. If you don't you can add this post to your reading list and go read some tkinter documentation.**

## Required modules :

To make this application I am going to use to mainly 2 modules - tkinter and pytube. I also use tkinter's filedialog and messagebox module.

In case of **tkinter**, it will come with the python installer. So no need to install it separately but **pytube** does not come with the python so we need to install it.

Type `pip install pytube` in your terminal to then `enter` to install pytube.

Once to pytube is installed we have to import it into our python file ( in my case its main.py ).

```python

from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror, showinfo
from pytube import YouTube


```

Initially I don't know how many thing do I need from the tkinter so I import everything from it using \*.

## Initializing tkinter :

After importing the modules let initialize the tkinter and create a gui window. Then give it a name and dimensions i.e. size of the gui window and an icon. We will do all this in few steps -

- Firstly create an instance of tkinter Tk() and store it in a variable named 'root', like this `root = Tk()`. Since I am importing everything from the tkinter I can write **Tk()** instead of **tkinter.Tk()**.

- Now give it a size using `root.geometry()`. I am going to give it a fixed size of 350px width and 250px height. So I am also going to do this `root.resizable(0, 0)` so that it can't be resizeable.

- Then giving it a name using `root.title()`. For this app, I am naming it **YTdownloader**.

- I also download an icon of '.ico' extension from the web and add that to this app using `root.iconbitmap("./icon.ico")`

- Now give this app a background color by writing `root.configure(bg=bgColor)`. I already store the color code in a variable to use it multiple times.

- At last `root.mainloop()` at the very bottom of the file.

Our application should look something like this.

![look of applocation after the initialinzing procss](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/d64toocvre4gynlyjk16.png)

## Widget implementation :

Let add some widget like labels, button, entry widget to make this interactive.

- Adding a label at the very top just as a heading and pack it to the root.

```py

Label(root, text="Youtube Downloader",
   bg=bgColor,font="sarif 15 bold").pack(pady=7)


```

I am also using the same background as the root to remove the it white background.

- Now add a frame where I am going to place the entry widget and optionmenu.

```python

frame = Frame(root, padx=10, pady=20,
        bg=bgColor, height=150)
frame.pack(fill="both")


```

In this app I am add a entry and to optionmenu widget. The entry widget is for the url input and one optionmenu widget for type download type 'video' or 'audio' and another is for the resolution or quality of the video in case of video download. I also create three tkinter variable to store their data.

- Creating the entry widget and placing it and storing it value to **link** variable.

```python

link = StringVar()
Entry(frame, textvariable=link).place(in_=frame, anchor="c",
      relx=.5, rely=0.0, relheight=0.3, relwidth=0.9)


```

- Creating the both optionmenu and storing it value to two variable. I also set a default value to both variables. I also add a label on top of each optionmenu to denote which one is for what. You can skip this.

```python

Label(text="filetype", bg=bgColor).place(
    in_=frame, anchor="c", relx=.25, rely=.325)
fileType = StringVar()
fileType.set("video")
OptionMenu(frame, fileType, *["video", "audio"]
           ).place(in_=frame, anchor="c", relx=.25, rely=.575)

Label(text="resolution", bg=bgColor).place(
    in_=frame, anchor="c", relx=.75, rely=.325)

res = StringVar()
resList = ["144p", "240p", "360p", "480p", "720p", "1080p"]
res.set(resList[2])
OptionMenu(frame, res, *resList
           ).place(in_=frame, anchor="c", relx=.75, rely=.575)


```

- Add a button to start the download process. I add command to a function named 'download' where I will write all its logics. If you don't know what does this command attribute do - it run the provide function every time the button is clicked.

```python

Button(root, command=download, text="download").place(
    in_=frame, anchor="c", relx=.5, rely=.9, relheight=0.3)


```

You have define the 'download' function before the button widget otherwise you will get an error.

Now our application is looking something like this

![gui after all widgets are added](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1k54uutksw00wcj46oph.png)

## Logic behind the download :

> Firstly I will say, "I did not knew that there is python module called **pytube** which can download youtube videos". I read a post about this youtube video download using python by one of our **dev.to** friend and use his code after doing some modification on it. If you want to know more about this I suggest you to read his post. The link of his post is given at the bottom.

- Instead of fixing the download location, I give the user a option to select the folder every time when the **download** button is clicked using tkinter's **askdirectory** widget. It will return the path of selected folder which I stored in the path variable.

```python

    path = askdirectory(title='Select Folder')


```

- After getting the path I store url, file type and resolution of the video in 3 different variables.

```python

    videoLink = link.get()
    downloadType = fileType.get()
    resolution = res.get()


```

- At last seting up the **YouTube** class. Wrap up this section in a **try** block so that error can be handled easily. And I use **if...else** to handle audio or video download.

```python

    video = YouTube(videoLink)

    try:
        if downloadType == "audio":
            file = video.streams.filter(only_audio=True).first()
        else:
            file = video.streams.filter(resolution=resolution).first()

        file.download(path)

    except:
        showerror("error", "Unable to download video at this time!")
    else:
        showinfo("download complete", f"{format} downloaded!")


```

As you can see in the code above, if there is any problem to download the video it will go to the **except** block where an error pop up message will be shown using the **showerror** widget of tkinter.

## Wrap up :

You can get the code at my github following this [link](https://github.com/dshaw0004/youtube-video-downloader).

Here the link of the post by 'Shittu Olumide' whose code I use.
[click here](https://dev.to/shittu_olumide_/how-to-download-youtube-music-and-videos-with-python-37k5)
