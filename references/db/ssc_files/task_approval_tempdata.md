# 智能审批训练数据上传临时表-task_approval_tempdata

## 智能审批训练数据上传临时表-主表 t_tk_smartapproval_data

- **表名称：** 智能审批训练数据上传临时表-主表
- **表名：** t_tk_smartapproval_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | varchar | 50 |  | √ | ' ' | 组织 |
| 3 | forgpatternid | 组织形态 | varchar | 20 |  | √ | ' ' | 组织形态 |
| 4 | fisbizorg | 业务组织 | varchar | 10 |  | √ | ' ' | 业务组织 |
| 5 | ffeetype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 6 | frecordtype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 7 | fyzjimported | 是否云之家同步 | varchar | 10 |  | √ | ' ' | 是否云之家同步 |
| 8 | fisaccounting | 是否核算组织 | varchar | 10 |  | √ | ' ' | 是否核算组织 |
| 9 | fstatus | 数据上传状态 | varchar | 4 |  | √ | ' ' | 数据上传状态,枚举: 0 :未上传 1 :已上传 2 :失败重试 3 :数据异常 |
| 10 | fcreatorid | 创建人 | varchar | 50 |  | √ | ' ' | 创建人 |
| 11 | fcreatetime_user | 人员创建时间 | timestamp | 0 |  |  | null | 人员创建时间 |
| 12 | fcreatetime_org | 组织创建时间 | timestamp | 0 |  |  | null | 组织创建时间 |
| 13 | fmoney | 报销金额 | numeric | 19 | 6 | √ | 0 | 报销金额 |
| 14 | fusertype | 人员类型 | varchar | 20 |  | √ | ' ' | 人员类型 |
| 15 | foperation | 不通过的操作类型 | varchar | 200 |  | √ | ' ' | 不通过的操作类型 |
| 16 | fcount | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 17 | fcreditvalue | 信用分数 | numeric | 19 | 6 | √ | 0 | 信用分数 |
| 18 | fsscid | 共享中心 | varchar | 50 |  | √ | ' ' | 共享中心 |
| 19 | ferrinfo | 异常信息 | varchar | 1000 |  | √ | ' ' | 异常信息 |
| 20 | fcreditlevel | 信用等级 | varchar | 50 |  | √ | ' ' | 信用等级 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fuser | 用户 | varchar | 50 |  | √ | ' ' | 用户 |
| 23 | fissale | 是否销售组织 | varchar | 10 |  | √ | ' ' | 是否销售组织 |
| 24 | fbreakrule | 通过但有问题项 | varchar | 200 |  | √ | ' ' | 通过但有问题项 |
| 25 | fgender | 性别 | varchar | 10 |  | √ | ' ' | 性别 |
| 26 | fwithdrawal | 批退原因 | varchar | 200 |  | √ | ' ' | 批退原因 |
| 27 | fisinventory | 是否库存组织 | varchar | 10 |  | √ | ' ' | 是否库存组织 |
| 28 | fstate | 最终状态 | varchar | 10 |  | √ | ' ' | 最终状态 |
| 29 | fisneedimage | 是否需要影像上传 | varchar | 10 |  | √ | ' ' | 是否需要影像上传 |
| 30 | fispurchase | 是否采购组织 | varchar | 10 |  | √ | ' ' | 是否采购组织 |
| 31 | ftaskid | 任务id | varchar | 50 |  | √ | ' ' | 任务id |
| 32 | fimageok | 影像是否OK | varchar | 50 |  | √ | ' ' | 影像是否OK |
| 33 | funqualifiedtotalnum | 总不合格次数 | int8 | 64 |  | √ | 0 | 总不合格次数 |
| 34 | fbilltypeid | 业务单据 | varchar | 50 |  | √ | ' ' | 业务单据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_smartapproval_data |  | fid |
| 2 | idx_ssc_approval_data_taskid |  | ftaskid |
| 3 | idx_ssc_approval_data_status |  | fstatus |
