# 资质后审设置F7-src_aptitudeconfig2f7

## 资质后审设置F7-主表 t_src_aptitudeconfig2

- **表名称：** 资质后审设置F7-主表
- **表名：** t_src_aptitudeconfig2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdateto | 资审结束时间 | timestamp | 0 |  |  | null | 资审结束时间 |
| 4 | fqfilter | fqfilter | varchar | 255 |  | √ | ' ' |  |
| 5 | fischanged | 最低分修改否 | bpchar | 1 |  | √ | '0' | 最低分修改否 |
| 6 | fproschemeid | fproschemeid | int8 | 64 |  | √ | 0 |  |
| 7 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | 'A' | 评标状态,枚举: A :未下达 B :已下达 C :部分评标 E :已评标 |
| 8 | fschemeid | 评标方案 | int8 | 64 |  | √ | 0 | [方案配置 src_scheme](../src_files/src_scheme.md) |
| 9 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 10 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 11 | fexpertcount | 评委人数要求 | int4 | 32 |  | √ | 0 | 评委人数要求 |
| 12 | fsumscore | 合格最低分 | numeric | 19 | 2 | √ | 0 | 合格最低分 |
| 13 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 14 | fqfilter_tag | fqfilter_tag | text | 0 |  |  | null |  |
| 15 | fweight | 权重(%) | numeric | 23 | 10 | √ | 0 | 权重(%) |
| 16 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 17 | fdatefrom | 资审开始时间 | timestamp | 0 |  |  | null | 资审开始时间 |
| 18 | ftplname | ftplname | varchar | 100 |  | √ | ' ' |  |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_aptitudeconfig2_fid |  | fid |
| 2 | pk_src_aptitudeconfig2 |  | fentryid |

---

## 评标人-多选基础资料表 t_src_aptitudeuser

- **表名称：** 评标人-多选基础资料表
- **表名：** t_src_aptitudeuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_aptitudeuser |  | fpkid |
| 2 | idx_src_aptitudeuser_bid |  | fbasedataid |
| 3 | idx_src_aptitudeuser_eid |  | fentryid |
