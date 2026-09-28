# 扫描记录匹配后序列号明细-barcm_scanrecordsn

## 扫描记录匹配后序列号明细-主表 t_barcm_scanrecordsn

- **表名称：** 扫描记录匹配后序列号明细-主表
- **表名：** t_barcm_scanrecordsn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsnnumbertext | 序列号文本 | varchar | 80 |  | √ | ' ' | 序列号文本 |
| 3 | fmatchentryid | 匹配分录id | int8 | 64 |  | √ | 0 | 匹配分录id |
| 4 | fsnnumberid | 序列号 | int8 | 64 |  | √ | 0 | 序列号主档 bd_snmainfile |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_srecordsn_dtl |  | fmatchentryid |
| 2 | pk_barcm_scanrecordsn |  | fid |
