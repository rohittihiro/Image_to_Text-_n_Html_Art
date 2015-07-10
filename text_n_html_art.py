from PIL import Image
from PIL.Image import ANTIALIAS
import os
import sys

def draw_html(x,filename):
    f=open(filename,"w")
    f.write('<html><head></head><body><p><pre class="white" style="font: 10px/5px monospace; text-align: center;">')
    img_size=x.size
    for i in range(int(img_size[1])):
        for j in range(int(img_size[0])):
            temp_str='<span style="color:rgba({0},{1},{2},1)">#</span>'.format(*x.getpixel((j,i)))
            f.write(temp_str)
        f.write("<br>")
    f.write('</pre></p></body></html>')
    f.close()
    return

def draw_text(x,filename,pixel):
    x=x.convert("L")
    f=open(filename,"w")
    f.write('<!DOCTYPE html><html><head></head><body><p><pre class="white" style="font:monospace;font-size:{0}px;text-align:center;">'.format(pixel))
    img_size=x.size
    for i in range(int(img_size[1])):
        for j in range(int(img_size[0])):
            curr_pixel=x.getpixel((j,i))
            if 0<=curr_pixel<15:
                f.write("$")
            elif 15<=curr_pixel<30:
                f.write("#")
            elif 30<=curr_pixel<45:
                f.write("%")
            elif 45<=curr_pixel<60:
                f.write("&")
            elif 60<=curr_pixel<75:
                f.write("@")
            elif 75<=curr_pixel<90:
                f.write("5")
            elif 90<=curr_pixel<105:
                f.write("0")
            elif 105<=curr_pixel<120:
                f.write(">")
            elif 120<=curr_pixel<135:
                f.write("=")
            elif 135<=curr_pixel<150:
                f.write("+")
            elif 150<=curr_pixel<165:
                f.write("?")
            elif 165<=curr_pixel<180:
                f.write("|")
            elif 180<=curr_pixel<195:
                f.write("!")
            elif 195<=curr_pixel<210:
                f.write(";")
            elif 210<=curr_pixel<225:
                f.write(":")
            elif 225<=curr_pixel<240:
                f.write(".")
            elif 240<=curr_pixel<=255:
                f.write("&nbsp;")
        f.write("<br>")
    f.write('</pre></p></body></html>')
    f.close()
    return

def main(img_path,basewidth=300,pixel=7):
    basewidth=int(basewidth)
    pixel=int(pixel)
    img_src=r"%s"%img_path
    img_name=os.path.basename(img_src)
    dir_name=os.path.dirname(img_src)
    text_name=img_name.split(".")[0]+"_txt.html"
    html_name=img_name.split(".")[0]+"_html.html"
    img=Image.open(img_src)
    if img.size[0]>basewidth:
        wpercent=basewidth/float(img.size[0])
        hsize=int(float(img.size[1])*wpercent)
        img=img.resize((basewidth,hsize),ANTIALIAS)
    draw_html(img,os.path.join(dir_name,html_name))
    draw_text(img,os.path.join(dir_name,text_name),pixel)
    return

if __name__=="__main__":
    main(*sys.argv[1:])