## 简介
此项目只是以flask框架做出了一个基础模版，日后方便在次编写开发。

#### 目录结构
```
./
├── README.md
├── app                                 # APP中心
│   ├── API_1_0                         # API代码中心
│   │   ├── Begins.py                   # Views文件
│   │   └── __init__.py                 
│   ├── __init__.py                     # 蓝图、路由编写
│   ├── models                          # 数据库表编写
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py
│       └── response_code.py            # 错误码
├── config.py                           # 配置文件
├── logs                                # 日志目录
│   └── app_2019_8_2.log
├── manager.py                          # 启动文件
└── requirements.txt
```
