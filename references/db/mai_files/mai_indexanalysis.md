# 指标分析配置-mai_indexanalysis

## 指标分析配置-多语言表 t_mai_indexanalysis_l

- **表名称：** 指标分析配置-多语言表
- **表名：** t_mai_indexanalysis_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 3 | ffullname | ffullname | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | '0' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mai_indexanalysis_l |  | fpkid |
| 2 | idx_mai_inanalysis_l_fid_flo |  | fid,flocaleid |

---

## 指标分析配置-主表 t_mai_indexanalysis

- **表名称：** 指标分析配置-主表
- **表名：** t_mai_indexanalysis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 指标分类 | int8 | 64 |  |  | null | [指标分类 mai_indextype](../mai_files/mai_indextype.md) |
| 3 | fisleaf | fisleaf | bpchar | 1 |  | √ | '1' |  |
| 4 | fuseorg | fuseorg | int8 | 64 |  |  | null |  |
| 5 | forgid | forgid | int8 | 64 |  |  | null |  |
| 6 | fsortnum | 排序 | int4 | 32 |  |  | null | 排序 |
| 7 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  |  | null |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 单据状态 | varchar | 50 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 13 | fsourcedataid | fsourcedataid | int8 | 64 |  |  | null |  |
| 14 | fbitindex | fbitindex | int8 | 64 |  |  | null |  |
| 15 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 16 | fname | 指标名称 | varchar | 100 |  | √ | ' ' | 指标名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsourcenum | 源编码 | int8 | 64 |  |  | null | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |
| 19 | fparentid | fparentid | int8 | 64 |  |  | null |  |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | flongnumber | flongnumber | bpchar | 50 |  | √ | ' ' |  |
| 22 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 23 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 24 | fshow | 指标展示 | bpchar | 1 |  | √ | '0' | 指标展示 |
| 25 | flevel | flevel | int8 | 64 |  |  | null |  |
| 26 | fshownum | 源编码 | varchar | 50 |  |  | null | 源编码 |
| 27 | findexsource | 指标来源 | varchar | 5 |  | √ | ' ' | 指标来源,枚举: 1 :接口 2 :数智指标 |
| 28 | fenable | 可用状态 | varchar | 50 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :启用 |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | '0' | 编码 |
| 30 | fsourcebitindex | fsourcebitindex | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mai_indexanalysis |  | fid |
| 2 | idx_mai_inanalysis_sourcenum |  | fsourcenum |
| 3 | idx_mai_indexanalysis_fname |  | fname |
| 4 | idx_mai_indexanalysis_fnumber |  | fnumber |
