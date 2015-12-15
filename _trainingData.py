# Draw (Bitmap Font) Text to Image
import re
# need to install PIL on Homer
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper # http://mpcabd.xyz/python-arabic-text-reshaper/
from bidi.algorithm import get_display
import tech

### split freqList - too long for gitHub
##def splitter(fileName):
##    lcoll = []
##    limit = 500000
##    count = 0
##    suf =   0
##    with open(fileName, "r", encoding="utf8") as f1:
##        f1 = f1.read().split("\n")
##        for l in f1:
##            if count <= limit:
##                suf += 1
##                print(suf)
##                with open("wfreqs_"+str(suf)+".txt", "w", encoding="utf8") as f9:
##                    f9.write("\n".join(lcoll))
##                lcoll = []
##            lcoll.append(l)
##            count += 1
##    suf += 1
##    with open("wfreqs_"+str(suf)+".txt", "w", encoding="utf8") as f9:
##        f9.write("\n".join(lcoll))                           
##    print(len(f1))
##
##splitter("corpus_WordFrequencies.txt")

fList = [
    #"Arial.ttf", # some glitches, actually none of the book use it...
    #"ArialBold.ttf", # ditto
    #"CourierNew.ttf",
    #"CourierNewBold.ttf",
    "MAJALLA.TTF", # some issues with ha', but otherwise quite good
    #"MAJALLAB.TTF",
    "TRADBDO.TTF", # Allah is typeset wrong (Alif is missing)
    "TRADO.TTF",
    #"TimesNR.ttf",
    #"TimesNRBold.ttf",
    ]

fFolder = "fonts/"
iFolder = "images/"
fntSize = 150

def renderImage(word, label):
    reshaped = arabic_reshaper.reshape(u"%s" % word)
    bidi = get_display(reshaped)

    for f in fList:
        #print(f)
        font = ImageFont.truetype(fFolder+f, fntSize)
        width, height = font.getsize(reshaped)
        img = Image.new('RGB', (width, height), "white")
        d = ImageDraw.Draw(img)
        d.text((0, 0), bidi, fill="black", font=font)
        img.save(iFolder+"%s_%s_%s.png" % (label, str(fntSize), f[:-4]))

def monkLabel(w):
    l = tech.dictReplace(w, tech.monktionary)    
    l = "@ArP@%s" % l
    return(l)

def cleanFreqList(freqList):
    fixed = []
    with open(freqList, "r", encoding="utf8") as f1:
        f1 = f1.read().split("\n")
        print(len(f1))
        for f in f1:
            ft = f.split("\t")[1]
            if not re.search("[A-Za-z0-9]", ft):
                ft = monkLabel(ft)
                if len(ft[5:]) == 1:
                    print(ft)
                if re.search("^[A-Za-z]+$", ft[5:]):
                    f += "\t%s" % ft
                    fixed.append(f)
    print(len(fixed))
    with open(freqList.replace(".txt", "_clean.txt"), "w", encoding="utf-8") as f9:
        f9.write("\n".join(fixed))
    print("%s has been cleaned..." % freqList)
              

def main(freqListFile,  counter):
    ImageList = []
    with open(freqListFile, "r", encoding="utf8") as f1:
        f1 = f1.read().split("\n")
        for l in f1:
            counter += 1
            l = l.split("\t")
            lab = "@ArP@%010d" % counter
            l.append(lab)
            renderImage(l[1], lab)
            ImageList.append("\t".join(l))
            #if counter % 100 == 0:
            #    break
    with open("List_%s.txt" % freqListFile, "w", encoding="utf8") as f9:
        f9.write("\n".join(ImageList))
    print("Image generation complete...")
    return(counter)

#cleanFreqList("corpus_Auto_WordFrequencies.txt")
#main("corpus_Auto_WordFrequencies_clean.txt")

counter = 0
counter = main("wfreq_aa", counter)
counter = main("wfreq_ab", counter)
counter = main("wfreq_ac", counter)
counter = main("wfreq_ad", counter)

