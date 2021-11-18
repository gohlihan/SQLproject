# SQLproject
管理信息-小组期末作业

![picture 3](/attachment/2021-1118-120723.png)  


## 文件说明
[Main.py](Main.py)主要的功能写在这里? tkinter我打算写在这边

[CreatingTables.py](CreatingTables.py)创建初始的tables
[AddingData.py](/AddingData.py)是给数据库输入初始数据

[DbFunction.py](DbFunction.py)把Query写成python的function,然后套用去Main.py

[system.db](system.db)是这次作业的主要数据库

[testing.sql](testing.sql)是写[CreatingTables.py](CreatingTables.py)时候的草稿

[Group project draft.sql](Group%20project%20draft.sql)是之前生成的MySQL, 用作参考

### 目前计划

用python + SQLite 完成数据库,
然后用tkinter制作GUI界面,

在GUI界面上可以按几个按钮就显示出老师要求的东西

### 进度
- [x] 建立Table 
- [ ] 填入数据 (正在进行)
- [ ] 完成老师要求的Query功能
- [ ] 把功能套用到tkinter界面上


### 遇到的问题
关于销售人员的销售额, 应该直接输入一个销售数据,
还是应该是直接用Query的方法来统计销售额?
