# 净改变转移记录-msplan_netchange_trans

## 净改变转移记录-主表 t_msplan_nchangetrans

- **表名称：** 净改变转移记录-主表
- **表名：** t_msplan_nchangetrans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fafrecordid | 转移后净改变记录ID | int8 | 64 |  | √ | 0 | 转移后净改变记录ID |
| 4 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 5 | ftranstype | 转移类型 | varchar | 50 |  | √ | ' ' | 转移类型,枚举: trans :净改变转移 replace :净改变替换 |
| 6 | ftransbill | 单据实体 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 9 | fbfrecordid | 转移前净改变记录ID | int8 | 64 |  | √ | 0 | 转移前净改变记录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_nchangetrans |  | fid |
