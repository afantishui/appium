# appium
尝试使用Appium+OpenCV图像识别做UI自动化测试，与使用adb命令操作进行对比

### 所需环境
* Python3
* appium环境
* OpenCV

## 使用
* 把每步操作截图放入img\qrerImg目录
* 在执行代码里调用 find_click(queryImgPath,'login_button.png',sceneFilePath,3)，修改第二个参数改成操作截图名字，第四个参数是操作后延时，单位s
* 判读图片是否存在调用 exist_pic(queryImgPath,'exist_tufu.png',sceneFilePath)，返回的是一个坐标

## 目录结构
#### demo
*  -counter.py  计算器练习demo
*  -WX_xiaochengxu.py  appium启动微信小程序,更多详情(https://testerhome.com/topics/7053)

#### game
*  -Base
*     -imgProcess.py  图像识别
*     -init.py        初始化配置
*     --monkeyBase.py  封装monkey命令

*  -config
*     -config.yml    ui自动化配置

* -img 
*     -queryImg  匹配图片存放
*     -sceneImg  截图目录

* -Runtest
*     -adb_start.py  使用adb命令启动应用，进行图像识别操作（识别一个图像完整耗时约16s）
*     -appium_start.py  使用appium启动应用，进行图像识别操作（识别一个图像完整耗时约50s）
