# 生产改制日志M表-pom_restructlogm

## 生产改制日志M表-主表 t_pom_restructlogm

- **表名称：** 生产改制日志M表-主表
- **表名：** t_pom_restructlogm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftbillno | 目标单据编码 | varchar | 50 |  | √ | ' ' | 目标单据编码 |
| 6 | freslogid | 改制日志id | int8 | 64 |  | √ | 0 | 改制日志id |
| 7 | fentitytype | 单据类型 | varchar | 50 |  | √ | ' ' | [业务对象 bos_entity](../mdl_files/bos_entity.md) |
| 8 | freslogentryid | 改制日志分录id | int8 | 64 |  | √ | 0 | 改制日志分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_restructlogm_logid |  | freslogid |
| 2 | pk_pom_restructlogm |  | fid |
