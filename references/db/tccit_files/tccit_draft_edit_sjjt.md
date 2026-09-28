# 底稿调整记录单据-tccit_draft_edit_sjjt

## 底稿调整记录单据-主表 t_tccit_draft_edit_sjjt

- **表名称：** 底稿调整记录单据-主表
- **表名：** t_tccit_draft_edit_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxorg | 取数组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpreadjust | 调整数值前 | numeric | 23 | 10 | √ | 0 | 调整数值前 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | fadjustexplain | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 7 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fadjusttype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: 1 :数据源调整 2 :手工录入调整 |
| 10 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 11 | fpostadjust | 调整数值后 | numeric | 23 | 10 | √ | 0 | 调整数值后 |
| 12 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 13 | fentrytype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型 |
| 14 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 15 | fitemname | 业务名称 | varchar | 200 |  | √ | ' ' | 业务名称 |
| 16 | ftitlename | 调整项目 | varchar | 200 |  | √ | ' ' | 调整项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_draft_sjjt_org_date |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_draft_edit_sjjt |  | fid |
