## 2018.4.12
* 使用yaml进行用例配置
* 操作类型暂时分成两种点击（click）跟检查（check），其他后面再加入
* testcase:
*     query_img: 匹配图片名称
*     operate_type: click 操作类型 
*     time: 3 延时等待 
*     info: 查找点击登录按钮

## 2018.4.10

* 把每步操作截图放入img\qrerImg目录
* 在执行代码里调用 find_click(queryImgPath,'login_button.png',sceneFilePath,3)，修改第二个参数改成操作截图名字，第四个参数是操作后延时，单位s
* 判读图片是否存在调用 exist_pic(queryImgPath,'exist_tufu.png',sceneFilePath)，返回的是一个坐标
