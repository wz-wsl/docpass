import base64
import docx

shellcode=b""
sc=base64.b64encode(shellcode)

doc=docx.Document()
doc.add_paragraph(str(sc))
doc.save("shec.docx")