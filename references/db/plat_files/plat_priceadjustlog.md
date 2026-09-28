# 批量调整日志-plat_priceadjustlog

## 批量调整日志-主表 t_plat_priceadjustlog

- **表名称：** 批量调整日志-主表
- **表名：** t_plat_priceadjustlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjustbillinfo | 批量调整单信息 | varchar | 512 |  | √ | ' ' | 批量调整单信息 |
| 3 | fbatchadjnumber | 批量调整单号 | varchar | 80 |  | √ | ' ' | 批量调整单号 |
| 4 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | forgid | 调价组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | ffiltercondition_tag | 详情 | text | 0 |  |  | null | 详情 |
| 8 | fbatchadjustment |  | varchar | 512 |  |  | null |  |
| 9 | fbatchadjustment_tag | 详情 | text | 0 |  |  | null | 详情 |
| 10 | flogtype | 日志类型 | varchar | 10 |  | √ | ' ' | 日志类型,枚举: SALE :销售 PUR :采购 |
| 11 | ffiltercondition |  | varchar | 512 |  |  | null |  |
| 12 | fadjustbillinfo_tag | 批量调整单信息_详情 | text | 0 |  |  | null | 批量调整单信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plat_priceadjustlog_num |  | fbatchadjnumber |
| 2 | pk_t_plat_priceadjustlog |  | fid |
