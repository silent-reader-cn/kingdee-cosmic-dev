# 业务存储表-aqap_bd_business

## 业务存储表-主表 t_aqap_bd_business

- **表名称：** 业务存储表-主表
- **表名：** t_aqap_bd_business

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fattr_value | 字段值 | varchar | 500 |  | √ | ' ' | 字段值 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftextfield | 银行版本编号 | varchar | 100 |  | √ | ' ' | 银行版本编号 |
| 9 | fattr_name | 字段中文名 | varchar | 100 |  | √ | ' ' | 字段中文名 |
| 10 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fattr_key | 字段属性 | varchar | 100 |  | √ | ' ' | 字段属性 |
| 13 | fbusiness_detail | 业务细分 | varchar | 100 |  | √ | ' ' | 业务细分 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbusiness_type | 业务类型 | varchar | 100 |  | √ | ' ' | 业务类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aqap_bd_business |  | fid |
| 2 | idx_bd_business |  | fattr_key |
| 3 | idx_aqap_bd_bus_0 |  | fbillno |
