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

### 参考的教程
https://www.sqlitetutorial.net/

https://www.sqlitetutorial.net/sqlite-python/

https://www.pythontutorial.net/tkinter/

### 目前计划

用python + SQLite 完成数据库,
然后用tkinter制作GUI界面,

在GUI界面上可以按几个按钮就显示出老师要求的东西

### 进度
- [x] 建立Table 
- [x] 填入数据 (周末前完成数据填写以及总销售额计算方法确定)(手填100价格)
- [x] 完成老师要求的Query功能
    
**要求1**
  - [x] show warehouse inventory
  - [x] add or minus warehouse inventory
  - [x] move invoice to another warehouse(change city id)
  - [x] create invoice(making sales)
  - [x] invoice手动输入运输状态,0=未发货,1=正在途中,2=已收货


**要求2**
  - [x] 总销售额:sum worker_id search in Invoices Shopping_list-price
  - [x] 购买新手机最多：count max customs_id search Invoices Shopping_list Item(new phone)-quantity


- [ ] 把功能套用到tkinter界面上(正在进行,全力赶在这周末内完成)


### 遇到的问题
关于销售人员的销售额, 应该直接输入一个销售数据,
还是应该是直接用Query的方法来统计销售额?

总销售额:sum worker_id search in Invoices Shopping_list-price(手填)
购买新手机最多：count max customs_id search Invoices Shopping_list Item(new phone)-quantity

第一题的做后一句要求的好像是要物流状态?
manage the delivery process(手动输入运输状态,0=未发货,1=正在途中,2=已收货)


### Change Log
