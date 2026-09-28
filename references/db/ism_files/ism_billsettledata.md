# 单据结算路径匹配-ism_billsettledata

## 单据结算路径匹配-主表 t_ism_billsettledata

- **表名称：** 单据结算路径匹配-主表
- **表名：** t_ism_billsettledata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 3 | fsettlerelationid | 结算路径 | int8 | 64 |  | √ | 0 | 结算路径 |
| 4 | fbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 5 | fbillentityid | 业务对象 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 6 | fentrykey | 分录实体名 | varchar | 50 |  | √ | ' ' | 分录实体名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_billsettledata |  | fbillentityid,fbillentryid |
| 2 | idx_ism_billsettledata_billid |  | fbillid |
| 3 | pk_ism_billsettledata |  | fid |
