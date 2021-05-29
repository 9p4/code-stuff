import os

info = dict(version="1.0", madeby="xxxxxx Saggi", datemade="August 10, 2016")

global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe       #html cpde
global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv       #css code
kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = ""
vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv = ""

def title(text):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<title>" + text + "</title>"

def picture(location, alternative, width, height):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<img>src=" + location + " alt=" + alternative + " width=" + width + " height=" + height

def run():
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    f = open("file.html", "w")
    x = open("style.css", "w")
    f.write(kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe)
    x.write(vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv)
    f.close()
    x.close()
    os.startfile("file.html")

def text(text):
    #if color == None:
    #    color = None
    #else: pass
    #print(color)
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<p>" + text + "</p>"

def title1(text):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<h1>" + text + "</h1>"

def title2(text):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<h2>" + text + "</h2>"

def title3(text):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<h3>" + text + "</h3>"

def title4(text):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<h4>" + text + "</h4>"

def title5(text):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<h5>" + text + "</h5>"

def title6(text):
    global kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe
    global vcxmnbvcxnmxcvbmncvxmncvxbxmcvbmxcbvxmcvbv
    kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe = kjhrekjghkjdgkjfkfkffjfjfjhekjhckjdhkjarhe + "<h6>" + text + "</h6>"

