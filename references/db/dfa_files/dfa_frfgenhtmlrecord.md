# 报告互动网页生成记录-dfa_frfgenhtmlrecord

## 报告互动网页生成记录-主表 t_dfa_frfgenhtmlrecord

- **表名称：** 报告互动网页生成记录-主表
- **表名：** t_dfa_frfgenhtmlrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | freportid | 报告ID | int8 | 64 |  | √ | 0 | 报告ID |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ffileurl | 下载地址 | varchar | 255 |  | √ | ' ' | 下载地址 |
| 6 | fattachmentid | 附件id | varchar | 50 |  | √ | ' ' | 附件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_reporthtml |  | fid |
| 2 | idx_dfa_rpthtmlid |  | fattachmentid |
