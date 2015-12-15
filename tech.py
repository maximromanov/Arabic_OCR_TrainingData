# generate MONK labels for Arabic
import re

def deNoise(text):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return(text)

def dictReplace(text, dic):
    for k, v in dic.items():
        text = text.replace(k, v)
    return(text)

def dictReplaceRev(text, dic):
    for k, v in dic.items():
        text = text.replace(v, k)
    return(text)

monktionary = {
    '،'   : ',',
# letters
    'ء'  : 'c',
    'ؤ'  : 'u',
    'ئ'  : 'i',
    'ا'  : 'A',
    'إ'  : 'i',
    'أ'  : 'a',
    'آ'  : 'O',
    'ب'  : 'b',
    'ة'  : 'o',
    'ت'  : 't',
    'ث'  : 'v',
    'ج'  : 'j',
    'ح'  : 'H',
    'خ'  : 'x',
    'د'  : 'd',
    'ذ'  : 'V',
    'ر'  : 'r',
    'ز'  : 'z',
    'س'  : 's',
    'ش'  : 'E',
    'ص'  : 'S',
    'ض'  : 'D',
    'ط'  : 'T',
    'ظ'  : 'Z',
    'ع'  : 'C',
    'غ'  : 'g',
    'ف'  : 'f',
    'ق'  : 'q',
    'ك'  : 'k',
    'ل'  : 'l',
    'م'  : 'm',
    'ن'  : 'n',
    'ه'  : 'h',
    'و'  : 'w',
    'ى'  : 'Y',
    'ي'  : 'y',
}




        
