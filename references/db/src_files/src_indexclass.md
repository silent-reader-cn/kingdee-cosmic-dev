# 指标类型-src_indexclass

## 指标类型-多语言表 t_src_indexclass_l

- **表名称：** 指标类型-多语言表
- **表名：** t_src_indexclass_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | ffullname | 长名称 | varchar | 300 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_indexclass_l_fid |  | fid,flocaleid |
| 2 | idx_src_indexclass_l_fname |  | fname |
| 3 | pk_src_indexclass_l |  | fpkid |

---

## 指标类型-主表 t_src_indexclass

- **表名称：** 指标类型-主表
- **表名：** t_src_indexclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 600 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 5 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 6 | fparentid | 上级指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 300 |  | √ | ' ' |  |
| 9 | fbasetype | 基本类型 | bpchar | 1 |  | √ | ' ' | 基本类型,枚举: 1 :技术类 2 :商务类 3 :商务综合类 4 :资质审查类 5 :供应商分析类 6 :综合评标类 7 :资质后审类 8 :专家考评 |
| 10 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 11 | fpartialpur | 分采评标人员最低数量 | int4 | 32 |  | √ | 0 | 分采评标人员最低数量 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | ffocuspur | 集采评标人员最低数量 | int4 | 32 |  | √ | 0 | 集采评标人员最低数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_indexclass |  | fid |
| 2 | idx_src_indexclass_fnumber |  | fnumber |
| 3 | idx_src_indexclass_fmasterid |  | fmasterid |
| 4 | idx_src_indexclass_fcreatetime |  | fcreatetime |
| 5 | idx_src_indexclass_fparentid |  | fparentid |
