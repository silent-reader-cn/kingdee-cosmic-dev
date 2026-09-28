# 明细汇总维度-pur_summary_dimension

## 明细汇总维度-多语言表 t_pur_summary_dimension_l

- **表名称：** 明细汇总维度-多语言表
- **表名：** t_pur_summary_dimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_summary_dimension_l |  | fid,flocaleid |
| 2 | pk_pur_summary_dimension_l |  | fpkid |

---

## 明细汇总维度-主表 t_pur_summary_dimension

- **表名称：** 明细汇总维度-主表
- **表名：** t_pur_summary_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsummarydimension | 汇总维度 | varchar | 255 |  | √ | ' ' | 汇总维度,枚举: |
| 7 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 8 | fsummaryfield | 汇总值 | varchar | 255 |  | √ | ' ' | 汇总值,枚举: |
| 9 | fsourcebill | 汇总单据 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsourceentrykey | 汇总分录标识 | varchar | 80 |  | √ | ' ' | 汇总分录标识,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_sum_di_sourcebill |  | fsourcebill |
| 2 | idx_pur_sum_di_number |  | fnumber |
| 3 | pk_pur_summary_dimension |  | fid |
