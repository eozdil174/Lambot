# Lambot
A simple bot for posting images from imgur using image id s

-----------------------

## How it works ?

It basically has a local dictionary which has the image names (can be anything) and unique imgur image ids to store the images.
When you type a command, like ```-post bear``` it will search that dictionary and try to find and post the relevant image.

--------------

## How to set it up ?

It's already ready to go you just have to download necessary files and applications to your computer. These are :

  * [Python 3.6.7](https://www.python.org/ftp/python/3.6.7/python-3.6.7-amd64.exe)
  !! **Be sure to select "Add to PATH" option when installing python** !!
  * Discord.py library, to download this you first need to install python. Then open a command line and type the following command:
  
  ```
     python -m pip install -U discord.py
  ```
  
  * After downloading and installing discord.py you are good to go. Run main.py file and the bot will turn on in few seconds.
    
    * **NOTE :** If you can't run the script by clicking on main.py file. Then open a command line in that directory (You can simply do that by clicking the adress bar on the file explorer and typing "cmd" and hitting enter) and then type the following command :
      ```
        python main.py
      ```

--------------------

## How to use it ?

The boot has a simple commmand style. For now it only has one or two commands. The usage is:
  * ```-post [the name of the image]```
  * ``` -help ```
            
           
  
