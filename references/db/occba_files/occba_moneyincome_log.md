# 资金收入单同步失败日志-occba_moneyincome_log

## 资金收入单同步失败日志-主表 t_occba_moneyincome_log

- **表名称：** 资金收入单同步失败日志-主表
- **表名：** t_occba_moneyincome_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 3 | fopobjectentityid | 操作实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fopuserid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fopdesc | 操作描述 | varchar | 2000 |  | √ | ' ' | 操作描述 |
| 7 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_occba_moneyincome_log |  | fid |
| 2 | idx_occba_mincome_log_bno |  | fbillno |
