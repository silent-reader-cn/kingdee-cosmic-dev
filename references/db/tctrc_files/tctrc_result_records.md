# 风险运行记录表-tctrc_result_records

## 单据体-子表 t_tctrc_records_entry

- **表名称：** 单据体-子表
- **表名：** t_tctrc_records_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 值 | varchar | 500 |  | √ | ' ' | 值 |
| 3 | findex | 行号 | varchar | 100 |  | √ | ' ' | 行号 |
| 4 | fkey | key | varchar | 100 |  | √ | ' ' | key |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_records_entry_fk |  | fid |
| 2 | t_tctrc_records_entry_pkey |  | fentryid |

---

## 风险运行记录表-主表 t_tctrc_records

- **表名称：** 风险运行记录表-主表
- **表名：** t_tctrc_records

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ftext | 过滤条件 | varchar | 1000 |  | √ | ' ' | 过滤条件 |
| 4 | fjson | 过滤条件JSON | varchar | 510 |  | √ | ' ' | 过滤条件JSON |
| 5 | fexist | 存在 | varchar | 30 |  | √ | ' ' | 存在,枚举: 1 :存在 0 :不存在 |
| 6 | ftableid | 取数表配置 | int8 | 64 |  | √ | 0 | [数据源配置 tctb_custom_datasource](../tctb_files/tctb_custom_datasource.md) |
| 7 | fjson_tag | 过滤条件JSON_详情 | text | 0 |  |  | null | 过滤条件JSON_详情 |
| 8 | fisrisk | 是否为风险 | bpchar | 1 |  | √ | ' ' | 是否为风险 |
| 9 | ffieldid | 字段ID | varchar | 1000 |  | √ | ' ' | 字段ID |
| 10 | fresultid | 运行结果ID | int8 | 64 |  | √ | 0 | 运行结果ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_records |  | ftableid |
| 2 | t_tctrc_records_pkey |  | fid |
