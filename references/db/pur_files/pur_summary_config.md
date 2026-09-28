# 明细汇总方案-pur_summary_config

## 明细汇总方案-主表 t_pur_summary_config

- **表名称：** 明细汇总方案-主表
- **表名：** t_pur_summary_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fecommerce | 电商 | bpchar | 1 |  | √ | '0' | 电商 |
| 3 | fsummarybillentrykey | 单据分录 | varchar | 80 |  | √ | ' ' | 单据分录 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsummarydimension | 汇总维度 | varchar | 255 |  | √ | ' ' | 汇总维度,枚举: |
| 8 | fsummaryfield | 汇总值 | varchar | 255 |  | √ | ' ' | 汇总值,枚举: |
| 9 | fglobal | 全局 | bpchar | 1 |  | √ | '0' | 全局 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 12 | fisenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsummaryplan | 汇总方案 | int8 | 64 |  | √ | 0 | [明细汇总维度 pur_summary_dimension](../pur_files/pur_summary_dimension.md) |
| 15 | fisperset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_summary_config_fsplan |  | fsummaryplan |
| 2 | pk_pur_summary_config |  | fid |
| 3 | idx_pur_summary_config |  | fnumber |

---

## 明细汇总方案-多语言表 t_pur_summary_config_l

- **表名称：** 明细汇总方案-多语言表
- **表名：** t_pur_summary_config_l

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
| 1 | pk_pur_summary_config_l |  | fpkid |
| 2 | idx_pur_summary_config_l |  | fid,flocaleid |
