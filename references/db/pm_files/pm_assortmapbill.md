# 配套映射单据-pm_assortmapbill

## 配套映射单据-主表 t_pm_assortmapbill

- **表名称：** 配套映射单据-主表
- **表名：** t_pm_assortmapbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fsourcebillid | 源单单据id | int8 | 64 |  | √ | 0 | 源单单据id |
| 5 | ftargetbillno | 目标单单据编号 | varchar | 50 |  | √ | ' ' | 目标单单据编号 |
| 6 | fsourcebillrowid | 源单单据行id | int8 | 64 |  | √ | 0 | 源单单据行id |
| 7 | fsourcebillno | 源单单据编号 | varchar | 50 |  | √ | ' ' | 源单单据编号 |
| 8 | fbilltype | 选单单据类型 | varchar | 30 |  | √ | ' ' | 选单单据类型,枚举: |
| 9 | fsourcebillrow | 源单单据行号 | int2 | 16 |  | √ | 0 | 源单单据行号 |
| 10 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_assort_sourcebillid |  | fsourcebillid |
| 2 | pk_t_pm_assortmapbill |  | fid |
| 3 | idx_pm_assort_sourcebillrowid |  | fsourcebillrowid |
