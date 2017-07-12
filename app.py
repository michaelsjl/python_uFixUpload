#coding:utf-8
from bottle import Bottle,route,template,request

app=Bottle()

@app.route('/upload')
def upload():
    return template('templates/upload')

upload_path=r"C:\Users\michael_shu.SOUTHBAYTECH\Desktop\python\uFixUpload\upload"
@app.route('/upload', method='POST')
def do_upload():
    filename=request.forms.get('filename')
    upload_file=request.files.get('filedata')
    upload_file.save(upload_path, overwrite=True)
    return {'status':'ok'}

app.run(host='localhost',port=8081,debug=True)
