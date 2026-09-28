# 数据确认日志-occba_checkconfirmlog

## 数据确认日志-主表 t_occba_checkconfirmlog

- **表名称：** 数据确认日志-主表
- **表名：** t_occba_checkconfirmlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 3 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 4 | fcheckerid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fsrcbilltype | 单据类型 | varchar | 80 |  | √ | ' ' | 单据类型 |
| 6 | fchecktime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fcheckstatus | 确认事务 | bpchar | 1 |  | √ | 'A' | 确认事务,枚举: A :数据确认 B :取消确认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_checkconfirmlog_bid |  | fsrcbillid |
| 2 | idx_occba_checkconfirmlog_bno |  | fsrcbillno |
| 3 | pk_occba_checkconfirmlog |  | fid |
