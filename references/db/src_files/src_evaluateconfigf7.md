# 专家考评设置F7-src_evaluateconfigf7

## 专家考评设置F7-主表 t_src_evaluateconfig

- **表名称：** 专家考评设置F7-主表
- **表名：** t_src_evaluateconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fgradeschemeid | 分级方案 | int8 | 64 |  | √ | 0 | 考评分级方案 src_expertgrade |
| 4 | fdateto | 评分结束时间 | timestamp | 0 |  |  | null | 评分结束时间 |
| 5 | fqfilter | fqfilter | varchar | 255 |  | √ | ' ' |  |
| 6 | fproschemeid | fproschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fentrystatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :未下达 B :已下达 C :部分评标 E :已评标 |
| 8 | fschemeid | 考评方案 | int8 | 64 |  | √ | 0 | 方案配置 src_scheme |
| 9 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 10 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 11 | fexpertcount | 评委人数要求 | int4 | 32 |  | √ | 0 | 评委人数要求 |
| 12 | fentryparentid | 父单据ID | int8 | 64 |  | √ | 0 | 父单据ID |
| 13 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 14 | fqfilter_tag | fqfilter_tag | text | 0 |  |  | null |  |
| 15 | fweight | 权重(%) | numeric | 19 | 6 | √ | 0 | 权重(%) |
| 16 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | 标段名称 src_packagef7 |
| 17 | fdatefrom | 评分开始时间 | timestamp | 0 |  |  | null | 评分开始时间 |
| 18 | ftplname | ftplname | varchar | 100 |  | √ | ' ' |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateconfig_pid |  | fentryparentid |
| 2 | pk_src_evaluateconfig |  | fentryid |
| 3 | idx_src_evaluateconfig_fid |  | fid |

---

## 评委-多选基础资料表 t_src_evaluateuser

- **表名称：** 评委-多选基础资料表
- **表名：** t_src_evaluateuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_evaluateuser_fbid |  | fbasedataid |
| 2 | pk_src_evaluateuser |  | fpkid |
| 3 | idx_src_evaluateuser_fentryid |  | fentryid |
