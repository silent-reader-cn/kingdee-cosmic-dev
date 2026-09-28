# 合并方案变更备份-xkcr_stchange_backup

## 合并方案变更备份-主表 t_xkcr_stchange_backup

- **表名称：** 合并方案变更备份-主表
- **表名：** t_xkcr_stchange_backup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fvalueid | 单据内码 | varchar | 50 |  | √ | ' ' | 单据内码 |
| 4 | fyear | 年度 | int4 | 32 |  | √ | 0 | 年度 |
| 5 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fcontent | 备份数据 | text | 0 |  |  | null | 备份数据 |
| 9 | fformid | 单据标示 | varchar | 50 |  | √ | ' ' | 单据标示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_stchange_backup |  | fid |
| 2 | idx_xkcr_stc_backup_formid |  | fformid |
