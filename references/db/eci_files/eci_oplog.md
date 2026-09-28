# 企业征信_操作记录-eci_oplog

## 企业征信_操作记录-主表 t_eci_oplog

- **表名称：** 企业征信_操作记录-主表
- **表名：** t_eci_oplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | freportstatus | 报告状态 | varchar | 100 |  |  | ' ' | 报告状态,枚举: new :最新 |
| 5 | ftype | 操作类型 | varchar | 100 |  |  | ' ' | 操作类型,枚举: view_report :查看报告 |
| 6 | fcompname | 企业名 | varchar | 100 |  |  | ' ' | 企业名 |
| 7 | freportno | 报告编号 | varchar | 100 |  |  | ' ' | 报告编号 |
| 8 | fisfee | 是否付费 | bpchar | 1 |  | √ | '0' | 是否付费 |
| 9 | fcreditcode | 社会统一信用代码 | varchar | 100 |  |  | ' ' | 社会统一信用代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eci_oplog_creator |  | fcreator,fcreatedate,ftype |
| 2 | pk_eci_oplog |  | fid |
