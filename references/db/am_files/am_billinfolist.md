# 单据信息-am_billinfolist

## 单据信息-主表 t_am_associatebill

- **表名称：** 单据信息-主表
- **表名：** t_am_associatebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpropname | 业务属性名称 | varchar | 500 |  | √ | ' ' | 业务属性名称 |
| 3 | fcreatorid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fpropnum | 业务属性编号 | varchar | 500 |  | √ | ' ' | 业务属性编号 |
| 5 | fbillid | 所选单据主键 | varchar | 50 |  | √ | '0' | 所选单据主键 |
| 6 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 7 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_am_associatebill_no |  | fbillno |
| 2 | pk_t_am_associatebill |  | fid |
| 3 | idx_am_associatebill |  | fbilltype,fcreatorid |
