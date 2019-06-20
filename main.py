#coding:utf-8
import sys,os

vp=sys.version_info
if vp[0]==2:
    os.system("cd cube_py2 && python cube.py")
elif vp[0]==3:
    os.system("cd cube_py3 && python cube.py")


