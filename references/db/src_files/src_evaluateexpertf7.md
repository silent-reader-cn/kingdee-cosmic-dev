# 待考评专家F7-src_evaluateexpertf7

## 待考评专家F7-主表 t_src_evaluateexpert

- **表名称：** 待考评专家F7-主表
- **表名：** t_src_evaluateexpert

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fsuppliertype | 专家类别 | varchar | 50 |  | √ | ' ' | 专家类别,枚举: src_expert :评标专家 |
| 3 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 6 | fisevaluatepush | 是否下达 | bpchar | 1 |  | √ | '0' | 是否下达 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsupplierid | 专家 | int8 | 64 |  | √ | 0 | 专家资料 src_expert |
| 9 | fentryparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_evaluateexpert |  | fentryid |
| 2 | idx_src_evaluateexpert_sid |  | fsupplierid |
| 3 | idx_src_evaluateexpert_pid |  | fentryparentid |
| 4 | idx_src_evaluateexpert_fid |  | fid |
