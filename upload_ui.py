#coding:utf-8
from PySide.QtCore import *
from PySide.QtGui import *
import sys
import os
import requests

file_info={'ProjectName':'Bear_2EXRV1_Test',
           'Reel':'R1',
           'ShotNum':'23',
           'LastVersion':'1',
           'FixVersion':'1',
           'Fixer':'michael_shu',
           'filesPath':r'C:\Bear_2EXRV1_Test-S23\Material'
          }

def tc(strings):
    return strings.decode('utf-8')

class FixerApp(QLabel):
    def __init__(self):
        QLabel.__init__(self)
        self.setMinimumSize(QSize(500,300))
        self.setAlignment(Qt.AlignCenter)
        self.setWindowTitle(tc('修图人员模块'))

        self.upload_button=QPushButton(tc('上传素材'),self)
        self.upload_button.clicked.connect(self.upload_slot)
    
    @Slot()
    def upload_slot(self):    
        print(os.listdir(file_info['filesPath']))

class TraverseDir(object):
    def __init__(self,path_name):
        self._files_list=[]
        self._list_files(path_name.replace('\\','/'))
    
    def _list_files(self,dir):
        files=os.listdir(dir)
        for file in files:
            file=dir+'/'+file
            if not os.path.isdir(file):
                
                self._files_list.append(file)
            else:
                self._list_files(file)
    
    def get_file_list(self):
        return self._files_list

if __name__=='__main__':
    t=TraverseDir(file_info['filesPath'])
    files = t.get_file_list()
    print len(files)
    print(files)
    """qtapp=QApplication(sys.argv)
    upload_app=FixerApp()
    upload_app.show()
    qtapp.exec_()
    sys.exit()"""