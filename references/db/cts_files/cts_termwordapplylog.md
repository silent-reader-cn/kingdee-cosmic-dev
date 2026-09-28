# 术语明细日志-cts_termwordapplylog

## 术语明细日志-主表 t_cts_termwordapplylog

- **表名称：** 术语明细日志-主表
- **表名：** t_cts_termwordapplylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftermwordlogid | 汇总日志id | int8 | 64 |  | √ | 0 | 汇总日志id |
| 3 | fsourcenumber | 表单编码 | varchar | 36 |  | √ | ' ' | 表单编码 |
| 4 | flanid | 语言id | int8 | 64 |  | √ | 0 | [语言种类 inte_language](../base_files/inte_language.md) |
| 5 | fcloudid | 所属云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 6 | foldname | 原名称 | varchar | 1024 |  | √ | ' ' | 原名称 |
| 7 | fsourceid | 表单id | varchar | 36 |  | √ | ' ' | 表单id |
| 8 | fnewname | 新名称 | varchar | 1024 |  | √ | ' ' | 新名称 |
| 9 | ftermwordcompid | 词条 | int8 | 64 |  | √ | 0 | [术语词条表 cts_termwordcomp](../cts_files/cts_termwordcomp.md) |
| 10 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_termwordapplylog |  | fid |
| 2 | idx_cts_termapplylog_flogid |  | ftermwordlogid |
