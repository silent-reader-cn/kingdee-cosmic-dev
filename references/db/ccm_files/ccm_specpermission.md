# 信用单笔特批权限-ccm_specpermission

## 信用单笔特批权限-主表 t_ccm_specpermission

- **表名称：** 信用单笔特批权限-主表
- **表名：** t_ccm_specpermission

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | flimitamount | 允许特批超标额度 | numeric | 23 | 10 | √ | 0 | 允许特批超标额度 |
| 4 | flimitbillamount | 允许特批超标单笔限额 | numeric | 23 | 10 | √ | 0 | 允许特批超标单笔限额 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 授信组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | flimitpressctrl | 允许特批超标压批批数 | int4 | 32 |  | √ | 0 | 允许特批超标压批批数 |
| 9 | flimitday | 允许特批超标天数 | int4 | 32 |  | √ | 0 | 允许特批超标天数 |
| 10 | flimitoveramount | 允许特批超标逾期额度 | numeric | 23 | 10 | √ | 0 | 允许特批超标逾期额度 |
| 11 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 13 | fuserid | 特批人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_specpermuser |  | fuserid |
| 2 | pk_ccm_specpermission |  | fid |
