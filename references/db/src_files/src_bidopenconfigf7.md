# 评标设置F7(工具)-src_bidopenconfigf7

## 评标设置F7(工具)-主表 t_src_assessconfig

- **表名称：** 评标设置F7(工具)-主表
- **表名：** t_src_assessconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 2 | fagentid | 代理评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 4 | fqfilter | fqfilter | varchar | 255 |  | √ | ' ' |  |
| 5 | fproschemeid | fproschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fentrystatus | 评标状态 | bpchar | 1 |  | √ | ' ' | 评标状态,枚举: A :未下达 B :已下达 C :部分评标 E :已评标 |
| 7 | fschemeid | 评标方案 | int8 | 64 |  | √ | 0 | [方案配置 src_scheme](../src_files/src_scheme.md) |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 10 | fexpertcount | 评委人数要求 | int4 | 32 |  | √ | 0 | 评委人数要求 |
| 11 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 12 | fqfilter_tag | fqfilter_tag | text | 0 |  |  | null |  |
| 13 | fweight | 权重(%) | numeric | 19 | 6 | √ | 0 | 权重(%) |
| 14 | fpackageid | 标段名称 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
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

---

## 评委-多选基础资料表 t_src_assessscorer

- **表名称：** 评委-多选基础资料表
- **表名：** t_src_assessscorer

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
| 1 | idx_src_assessscorer_fbid |  | fbasedataid |
| 2 | pk_src_assessscorer |  | fpkid |
| 3 | idx_src_assessscorer_fentryid |  | fentryid |
