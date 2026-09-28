# 需求移交-src_apply_translog

## 需求移交-主表 t_src_demandtranslog

- **表名称：** 需求移交-主表
- **表名：** t_src_demandtranslog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | freason | 移交原因 | varchar | 50 |  | √ | ' ' | 移交原因 |
| 7 | fdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 8 | ftargetuser | 接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | foperationdate | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | forigncreator | forigncreator | int8 | 64 |  | √ | 0 |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcurrentuser | 移交人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fapplybillno | 需求申请单号 | varchar | 50 |  | √ | ' ' | 需求申请单号 |
| 15 | fbillno | 需求申请单号 | varchar | 30 |  | √ | ' ' | 需求申请单号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_demandtranslog_fbillno |  | fbillno |
| 2 | pk_src_demandtranslog |  | fid |
