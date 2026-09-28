# 选择的报表-tcvvt_check_report

## 选择的报表-主表 t_tcvvt_check_report

- **表名称：** 选择的报表-主表
- **表名：** t_tcvvt_check_report

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fintroname | 介绍名 | varchar | 300 |  | √ | ' ' | 介绍名 |
| 3 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 4 | fmainname | 大名字 | varchar | 200 |  | √ | ' ' | 大名字 |
| 5 | fentitytable | 实体表名 | varchar | 50 |  | √ | ' ' | 实体表名 |
| 6 | ffitid | 适合的模板id | int8 | 64 |  | √ | 0 | 适合的模板id |
| 7 | ficonsurl | 图片地址 | varchar | 100 |  | √ | ' ' | 图片地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_check_report |  | ffitid |
| 2 | pk_tcvvt_check_report |  | fid |
| 3 | idx_tcvvt_check_report_1 |  | ftype |
