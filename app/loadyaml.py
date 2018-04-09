# -*- coding:utf-8 -*-
#    __author__ = 'afantishui'
#    __date__ = '2018/4/9'
#    __Desc__ = 读取yaml
import yaml

def getYaml(path):
	with open(path,encoding='utf-8') as f:
		x = yaml.load(f)
		print(x)

# yaml里有中文时不能打印
getYaml('login.yaml')
