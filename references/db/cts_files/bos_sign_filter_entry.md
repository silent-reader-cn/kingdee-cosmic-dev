# 签名过滤实体-bos_sign_filter_entry

## 签名过滤实体-主表 t_bd_signschemefilter

- **表名称：** 签名过滤实体-主表
- **表名：** t_bd_signschemefilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 签名方案 | int8 | 64 |  | √ | 0 | [签名方案 sign_scheme](../cts_files/sign_scheme.md) |
| 2 | ffiltername | 过滤条件 | varchar | 100 |  | √ | ' ' | 过滤条件 |
| 3 | ffiltertype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 1 :匹配 |
| 4 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffiltercondition | 条件 | text | 0 |  |  | null | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_signschemefilter_pkey |  | fentryid |
| 2 | idx_bd_signschemefilter_id |  | fid |
