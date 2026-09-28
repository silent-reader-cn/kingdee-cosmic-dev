# 许可证业务单据关联记录-gtm_licence_bill_record

## 许可证业务单据关联记录-主表 t_gtm_licence_bill_record

- **表名称：** 许可证业务单据关联记录-主表
- **表名：** t_gtm_licence_bill_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmaterialid | 物料id | int8 | 64 |  | √ | 0 | 物料id |
| 4 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 5 | flicencematentryid | 许可证物料分录主键id | int8 | 64 |  | √ | 0 | 许可证物料分录主键id |
| 6 | flicenceno | 许可证编号 | varchar | 50 |  | √ | ' ' | 许可证编号 |
| 7 | fentityname | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 8 | fisfinal | 是否存档 | bpchar | 1 |  | √ | '0' | 是否存档 |
| 9 | fbillentryid | 单据分录主键id | int8 | 64 |  | √ | 0 | 单据分录主键id |
| 10 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 11 | flicenceid | 许可证主键id | int8 | 64 |  | √ | 0 | 许可证主键id |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | frecordtime | 关联时间 | timestamp | 0 |  |  | null | 关联时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_licence_bill_record |  | fid |
| 2 | idx_gtm_licence_bill_record_m0 |  | fbillno |
