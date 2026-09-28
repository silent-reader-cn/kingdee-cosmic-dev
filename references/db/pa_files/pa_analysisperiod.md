# 分析期间-pa_analysisperiod

## 分析期间-多语言表 t_pa_analysisperiod_l

- **表名称：** 分析期间-多语言表
- **表名：** t_pa_analysisperiod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 100 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_analysisperiod_l |  | fpkid |
| 2 | pa_analysisperiod_l_fid |  | fid,flocaleid |

---

## 分析期间-主表 t_pa_analysisperiod

- **表名称：** 分析期间-主表
- **表名：** t_pa_analysisperiod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsemiannual | 半年度 | int4 | 32 |  | √ | 0 | 半年度 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [分析期间 pa_analysisperiod](../pa_files/pa_analysisperiod.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fymonth | 年月 | int4 | 32 |  | √ | 0 | 年月 |
| 9 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 10 | fquarter | 季度 | int4 | 32 |  | √ | 0 | 季度 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 18 | fyear | 年份 | int4 | 32 |  | √ | 0 | 年份 |
| 19 | fmonth | 月份 | int4 | 32 |  | √ | 0 | 月份 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fisadjust | 调整期 | bpchar | 1 |  | √ | ' ' | 调整期 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fhierarchical | 层级 | bpchar | 1 |  | √ | ' ' | 层级,枚举: 1 :年 2 :半年 3 :季度 4 :月 |
| 24 | fyquarter | 年季 | int4 | 32 |  | √ | 0 | 年季 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_analysisperiod_y |  | fyear |
| 2 | idx_pa_analysisperiod_ym |  | fymonth |
| 3 | idx_pa_analysisperiod_parent |  | fparentid |
| 4 | pk_pa_analysisperiod |  | fid |
| 5 | idx_pa_analysisperiod_longn |  | flongnumber |
| 6 | idx_pa_analysisperiod_yq |  | fyquarter |
