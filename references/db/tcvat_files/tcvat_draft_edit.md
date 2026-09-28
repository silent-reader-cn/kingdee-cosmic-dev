# 底稿调整记录单据-tcvat_draft_edit

## 底稿调整记录单据-主表 t_tcvat_draft_edit

- **表名称：** 底稿调整记录单据-主表
- **表名：** t_tcvat_draft_edit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdraftid | 底稿ID | int8 | 64 |  | √ | 0 | 底稿ID |
| 3 | frowcode | 单元格编码 | varchar | 50 |  | √ | ' ' | 单元格编码 |
| 4 | ftaxorg | 取数组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdraftnumber | 底稿编码 | varchar | 50 |  | √ | ' ' | 底稿编码 |
| 7 | fmodifier | fmodifier | varchar | 50 |  | √ | ' ' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ftzszq | 调整数值前 | numeric | 23 | 10 | √ | 0 | 调整数值前 |
| 11 | fadjusttype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: 1 :数据源调整 2 :手工录入调整 |
| 12 | ftzsm | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 13 | foriginamount | 原数值 | numeric | 23 | 10 | √ | 0 | 原数值 |
| 14 | fitemname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 15 | fdrafttype | 底稿类型 | varchar | 50 |  | √ | ' ' | 底稿类型 |
| 16 | fisrefreshmodify | 是否已刷新变更 | varchar | 1 |  | √ | ' ' | 是否已刷新变更 |
| 17 | ftzszh | 调整数值后 | numeric | 23 | 10 | √ | 0 | 调整数值后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_draft_edit |  | fid |
| 2 | idx_t_tcvat_draft_edit_fdraft |  | fdraftid |
