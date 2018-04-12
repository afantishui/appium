import os
import sys
import time
sys.path.append("..")
from Base.imgProcess import *
from Base.Init import *
from Base.monkeyBase import AndroidBaseOperation

# 读取 配置表、匹配图片路径、截图路径
f_config, queryImgPath, sceneFilePath = conf_Init('config.yml')
base = AndroidBaseOperation() # 实例化

game_start(f_config['activity']) # 启动游戏
time.sleep(5)
base.click(100,100,1)  # 跳过动画
base.click(100,100,1)
base.click(100,100,1)
time.sleep(3)
case = getYaml('login.yaml')
for item in case['testcase']:
	if item['operate_type'] == 'click':
		find_click(queryImgPath,item['query_img'],sceneFilePath,int(item['time']))
	if item['operate_type'] == 'check':
		exist_pic(queryImgPath,item['query_img'],sceneFilePath)
'''
find_click(queryImgPath,'login_button.png',sceneFilePath,3) # 进入游戏点击按钮
find_click(queryImgPath,'enter_game.png',sceneFilePath,6)	# # 进入游戏点击按钮
find_click(queryImgPath,'open_map.png',sceneFilePath,3)		# 打开左上角小地图入口
find_click(queryImgPath,'npc_tufu.png',sceneFilePath,3)		# 在地图找屠夫
exist_pic(queryImgPath,'exist_tufu.png',sceneFilePath)		# 在对话框是否匹配到
'''
print('ok')
time.sleep(3)
game_quit(f_config['packageName'])







