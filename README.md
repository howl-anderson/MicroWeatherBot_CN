## 安装
### 安装 rasa x
```pip
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```
### 安装 rasa_nlu_addons
```pip
pip install -r requestments.txt
```

## 启动
### 启动 action server
```bash
SENIVERSE_KEY=xxxx rasa run actions
```

`xxxx` 部分应该替换成从 [心知天气](https://www.seniverse.com/) 申请获得的 API key 。用户可以免费注册，注册后可以在后台找到 `我的API密钥`。

### 启动 rasa x
```bash
rasa x
```

启动后会自动打开浏览器窗口

## 使用
### 训练模型
在 rasa x 左侧菜单栏，点击 `训练` 按钮，训练模型

### 设定为 production model
在 rasa x 左侧菜单栏，点击 `models` 菜单进入模型管理，鼠标放到模型上，在其右边会出现 `...` 按钮，点击后，将之选择为 `production`。

### 人机对话
在 rasa x 左侧菜单栏，点击 `Talk to your bot` 菜单进入 人机对话界面
 