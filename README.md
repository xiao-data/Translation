# 调用百度翻译api的python划词翻译脚本
- 需求python3，安装库pyperclip和pyautogui
- 去[百度翻译api](https://fanyi-api.baidu.com/api/trans/product/index)注册appid
- 在translate.py中输入appid和secretkey
- 下载[Hotkey Helper](https://dl-sh-ctc-2.pchome.net/03/pz/HotkeyHelper_setup.zip?key=92750dbee844c133cbefdffd7e62c072&tmp=1552221453534)
- 配置如下图所示，其中Hotkey选择想要的快捷键，File选择pythonw.exe的绝对位置，Parameter选择translate.py的绝对位置

![image](https://raw.githubusercontent.com/xiao-data/Images/master/hotkeyhelper.PNG)

- 通过鼠标选择文本后，按下快捷键可以快速英汉互译，通过弹窗显示结果，其中汉译英需要满足第一个字是汉字
- 脚本也会自动复制翻译结果到剪切板中，按ctrl+v也可以显示文本
![image](https://bbs.pku.edu.cn/attach/f1/ad/f1ad6ed762e83fcf/chopper.jpg)
