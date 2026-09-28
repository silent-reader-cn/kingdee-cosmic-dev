# 评标设置F7(工具)-src_bidopenconfigf7

## 评标设置F7(工具)-主表 t_src_assessconfig

- **表名称：** 评标设置F7(工具)-主表
- **表名：** t_src_assessconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 2 | fagentid | fagentid | int8 | 64 |  | √ | 0 |  |
| 3 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 4 | fqfilter | fqfilter | varchar | 255 |  | √ | ' ' |  |
| 5 | fproschemeid | fproschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | ' ' | 评标状态,枚举: A :未下达 B :已下达 C :部分评标 E :已评标 |
| 7 | fschemeid | 评标方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 10 | fexpertcount | 评委人数要求 | int4 | 32 |  | √ | 0 | 评委人数要求 |
| 11 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 12 | fqfilter_tag | fqfilter_tag | text | 0 |  |  | null |  |
| 13 | fweight | 权重(%) | numeric | 19 | 6 | √ | 0 | 权重(%) |
| 14 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 15 | fdatefrom | fdatefrom | timestamp | 0 |  |  | null |  |
| 16 | ftplname | ftplname | varchar | 100 |  | √ | ' ' |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_assessconfig_fid |  | fid |
| 2 | idx_src_assessconfig_fpack |  | fpackageid |
| 3 | pk_src_assessconfig |  | fentryid |
