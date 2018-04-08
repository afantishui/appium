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

base.start_activity(f_config['activity']) # 启动游戏
time.sleep(3)
base.click(100,100,1)  # 跳过动画
base.click(100,100,1)
base.click(100,100,1)
time.sleep(3)

mid_cordinate_x,mid_cordinate_y = getImgCordinate(os.path.join(queryImgPath,'login_button.png'),sceneFilePath)
print(mid_cordinate_x,mid_cordinate_y)
# 点击坐标
base.click(mid_cordinate_x,mid_cordinate_y,1)
time.sleep(1)
print('ok')

'''
if f_config['loginType'] == 'WX':
    find_click(queryImgPath, f_config['loginButton'], sceneFilePath, 0.5)
'''
