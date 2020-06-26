# 留言板系统
## 注意事项
- 此项目有单独的git仓库，其中有提交记录，是完成开发后方便老师下载放在了平时作业仓库。如果需要看提交记录麻烦查看仓库链接<https://github.com/B5DX/bbs-demo>。
- 本项目开发过程使用Pycharm运行一切正常。请以bbs-demo\目录作为项目根目录，创建好项目后直接运行bbs-demo\app\routes.py即可。  
- 如果使用cmd运行出现了import错误，解决方法是在app\routes.py文件的**最开头**（要在其他import语句之前）加上如下代码：
```python
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
```
- 数据库的转储文件为message_board_db.sql，可以方便测试。如果需要修改数据库的配置（如数据库引擎或密码）请前往app\config.py。
## 题目描述

题目2：开发设计一个留言板系统；用户登陆后，能发布留言，能对自己发布的留言进行管理；能查看留言列表，分页显示，能根据留言的发布者，和留言内容，做模糊查询；基于flask框架。

## 成品大致功能

- 用户注册（用户名用于登录和唯一标识发布留言的用户，对用户名和密码数据类型和长度做了限制）
- 用户登录
- 修改密码
- 发布留言（对留言长度和分行做了限制）
- 个人留言管理（修改留言、删除留言）
- 留言展示与分页（展示页内容按时间降序排列）
- 分页跳转
- 留言作者与内容的模糊查询

## 代码文件结构

> bbs-demo\  请在Pycharm中以此目录作为项目根目录，直接运行app\routes.py即可
> 
> > app\
> > 
> > > \_\_init\_\_.py
> > > - 创建FLASK对象(flask服务，提供给app\routes.py)
> > > - 创建LoginManager对象(用于用户登录，提供给module\model.py) 
> > > - 创建SQLAlchemy对象(数据库相关，提供给module\model.py和module\SQL.py)
> > > 
> > > config.py  配置flask app、数据库、用户登录秘钥、分页展示等
> > > 
> > > routes.py  程序运行入口
> > > 
> > module\
> > 
> > > \_\_init\_\_.py  创建SQL对象，用于app\routes.py中的部分数据库操作  
> > > 
> > > model.py  创建Message和User类，对应数据库中的留言和用户
> > > 
> > > SQL.py  创建SQL类，提供经过异常处理后的部分数据库操作(如用户注册、插入留言等)
> > > 
> > static\
> > 
> > > js\
> > > 
> > > > index.js  提供index.html的搜索、跳转页面、基本登录数据校验操作
> > > > 
> > > > register.js  提供register.html的注册表单数据校验函数
> > > > 
> > > > util.js  提供常用的空字符串校验等函数
> > > >
> > > search.png  用于美化界面的搜索框图标
> > >
> > templates\
> >
> > > change_password.html  修改密码页
> > >
> > > index.html  主页面
> > > 
> > > profile.html  个人信息页面（包含该用户发布的留言和一些功能按钮）
> > > 
> > > register.html  用户注册页面
> > > 
> > > release.html  留言发布页面
> > > 
> > > search.html  搜索结果展示页面
> > > 
> > util\
> >
> > > \_\_init\_\_.py  对原始密码进行加密的函数

## 更多

更多内容详见“软件系统开发设计说明文档.pdf”。
