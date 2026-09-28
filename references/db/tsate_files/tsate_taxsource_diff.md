# 税源比对记录表-tsate_taxsource_diff

## 税源比对记录表-主表 t_tsate_taxsource_diff

- **表名称：** 税源比对记录表-主表
- **表名：** t_tsate_taxsource_diff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | ftaxsourcenumber | 税源编码 | varchar | 50 |  | √ | ' ' | 税源编码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdiffcontent_tag | 比对信息_详情 | text | 0 |  |  | null | 比对信息_详情 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | ftaxsourceid | 税源管理记录id | varchar | 50 |  | √ | ' ' | 税源管理记录id |
| 11 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 12 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdiffcontent | 比对信息 | varchar | 255 |  | √ | ' ' | 比对信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_taxsourcediff1 |  | ftaxsourcenumber |
| 2 | pk_tsate_taxsource_diff |  | fid |
