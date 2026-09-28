# 支付链路日志-fcs_paytracelog

## 支付链路日志-主表 t_fcs_paytracelog

- **表名称：** 支付链路日志-主表
- **表名：** t_fcs_paytracelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmethodname | 方法名 | varchar | 200 |  | √ | ' ' | 方法名 |
| 4 | fdetailinfo | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 5 | ftraceid | traceid | varchar | 60 |  | √ | ' ' | traceid |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdetailinfo_tag | 详细信息_详情 | text | 0 |  |  | ' ' | 详细信息_详情 |
| 9 | fclassname | 类名 | varchar | 200 |  | √ | ' ' | 类名 |
| 10 | fexception_tag | 异常堆栈_详情 | text | 0 |  |  | ' ' | 异常堆栈_详情 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fsource | 日志来源 | varchar | 30 |  | √ | ' ' | 日志来源,枚举: biz :准入业务单据 pay :付款类单据 bank :银行单据 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ftaginfo | 摘要信息 | varchar | 100 |  | √ | ' ' | 摘要信息 |
| 15 | flinenum | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 16 | fbillnumber | 单据编码 | varchar | 60 |  | √ | ' ' | 单据编码 |
| 17 | flevel | 日志级别 | varchar | 30 |  | √ | ' ' | 日志级别,枚举: INFO :INFO ERROR :ERROR |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 20 | fpaystep | 支付环节 | varchar | 30 |  | √ | ' ' | 支付环节,枚举: BIZ :业务单据流转 CREATE :生成银行单据 SIGN :跨单据签名 PAY :支付 QUERY :同步付款状态 REPAY :失败重付 BITBACK :打回 SYNC :付款单据同步 |
| 21 | fexception | 异常堆栈 | varchar | 255 |  | √ | ' ' | 异常堆栈 |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbilltype | 单据类型 | varchar | 60 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_paytracelog |  | fid |
| 2 | idx_t_fcs_paytracelog_billnum |  | fbillnumber |
