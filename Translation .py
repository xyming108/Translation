from tkinter import *
from urllib import request
from urllib import parse
import json
import hashlib
import random

def translate_word1(zh_str):
    URL='http://api.fanyi.baidu.com/api/trans/vip/translate'
    From_Data={}
    From_Data['from']='auto'
    From_Data['to']='zh'
    From_Data['q']=zh_str
    From_Data['transtype']='hash'
    From_Data['appid']='20190511000296411'
    From_Data['salt']=str(random.randint(32768, 65536))
    Key="5cz9CWGLquZwuxHdMbUr"
    ans=From_Data['appid']+zh_str+From_Data['salt']+Key
    ans_MD5=hashlib.md5(ans.encode('utf8'))
    From_Data['sign']=ans_MD5.hexdigest()
    
    data=parse.urlencode(From_Data).encode('utf-8')
    response=request.urlopen(URL, data)
    html=response.read().decode('utf-8')
    translate_results=json.loads(html)

    print(translate_results)
    translate_results = translate_results['trans_result'][0]['dst']
    print("翻译的结果是：%s" % translate_results)
    
    return translate_results

def translate_word2(jp_str):
    URLx='http://api.fanyi.baidu.com/api/trans/vip/translate'
    From_Data={}
    From_Data['from']='auto'
    From_Data['to']='jp'
    From_Data['q']=jp_str
    From_Data['transtype']='hash'
    From_Data['appid']='20190511000296411'
    From_Data['salt']=str(random.randint(32768, 65536))
    Key="5cz9CWGLquZwuxHdMbUr"
    x=From_Data['appid']+jp_str+From_Data['salt']+Key
    x_MD5=hashlib.md5(x.encode('utf8'))
    From_Data['sign']=x_MD5.hexdigest()

    datax=parse.urlencode(From_Data).encode('utf-8')
    responsex=request.urlopen(URLx, datax)
    htmlx=responsex.read().decode('utf-8')
    translate_resultsx=json.loads(htmlx)

    print(translate_resultsx)
    translate_resultsx = translate_resultsx['trans_result'][0]['dst']
    print("翻译的结果是：%s" % translate_resultsx)

    return translate_resultsx

def translate_word3(ru_str):
    URLr='http://api.fanyi.baidu.com/api/trans/vip/translate'
    From_Data={}
    From_Data['from']='auto'
    From_Data['to']='ru'
    From_Data['q']=ru_str
    From_Data['transtype']='hash'
    From_Data['appid']='20190511000296411'
    From_Data['salt']=str(random.randint(32768, 65536))
    Key="5cz9CWGLquZwuxHdMbUr"
    r=From_Data['appid']+ru_str+From_Data['salt']+Key
    r_MD5=hashlib.md5(r.encode('utf8'))
    From_Data['sign']=r_MD5.hexdigest()
    
    datar=parse.urlencode(From_Data).encode('utf-8')
    responser=request.urlopen(URLr, datar)
    htmlr=responser.read().decode('utf-8')
    translate_resultsr=json.loads(htmlr)

    print(translate_resultsr)
    translate_resultsr = translate_resultsr['trans_result'][0]['dst']
    print("翻译的结果是：%s" % translate_resultsr)
    
    return translate_resultsr

def printevent1(event):
    zh_str=e0.get()
    print(zh_str)
    fye=translate_word1(zh_str)
    s.set("")
    e1.insert(0, fye)

def printevent2(event):
    jp_str=e0.get()
    print(jp_str)
    fyj=translate_word2(jp_str)
    m.set("")
    e2.insert(0, fyj)

def printevent3(event):
	ru_str=e0.get()
	print(ru_str)
	fyr=translate_word3(ru_str)
	z.set("")
	e3.insert(0, fyr)

def printevent4(event):
    s.set("")
    e1.insert(0, "")
    m.set("")
    e2.insert(0, "")
    z.set("")
    e3.insert(0, "")

if __name__ == "__main__":
    root = Tk()
    root.title("残疾单词翻译器")
    root['width']=600; root['height']=200
    
    Label(root, text="请输入要翻译的内容(auto)：", width=24).place(x=1, y=5)
    e0=Entry(root, width=35)
    e0.place(x=160, y=5)
    
    Label(root, text="(auto->中)翻译结果：", width=28).place(x=2, y=30)
    s=StringVar()
    s.set("")
    e1=Entry(root, width=35, textvariable=s)
    e1.place(x=160, y=35)

    Label(root, text="(auto->日)翻译结果：", width=28).place(x=2, y=60)
    m=StringVar()
    m.set("")
    e2=Entry(root, width=35, textvariable=m)
    e2.place(x=160, y=60)

    Label(root, text="(auto->俄)翻译结果：", width=28).place(x=2, y=90)
    z=StringVar()
    z.set("")
    e3=Entry(root, width=35, textvariable=z)
    e3.place(x=160, y=90)

    c1=Button(root, text="翻译(中)", width=10)
    c1.place(x=30, y=150)
    c2=Button(root, text="翻译(日)", width=10)
    c2.place(x=120, y=150)
    c3=Button(root, text="翻译(俄)", width=10)
    c3.place(x=210, y=150)
    c4=Button(root, text="清空", width=10)
    c4.place(x=300, y=150)

    c1.bind("<Button-1>", printevent1)
    c2.bind("<Button-1>", printevent2)
    c3.bind("<Button-1>", printevent3)
    c4.bind("<Button-1>", printevent4)

    root.mainloop()
