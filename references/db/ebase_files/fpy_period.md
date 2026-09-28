# 会计期间-fpy_period

## 会计期间-多语言表 tk_fpy_period_l

- **表名称：** 会计期间-多语言表
- **表名：** tk_fpy_period_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_period_l |  | fpkid |

---

## 会计期间-主表 tk_fpy_period

- **表名称：** 会计期间-主表
- **表名：** tk_fpy_period

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fperiodnumber | 会计期间 | int4 | 32 |  | √ | 0 | 会计期间 |
| 6 | fperiodoutlineid | 会计期间 | int8 | 64 |  |  | null | [会计期间 fpy_periodoutline_tree](../ebase_files/fpy_periodoutline_tree.md) |
| 7 | ftypeid | 会计期间类型 | int8 | 64 |  |  | null | [会计期间类型 fpy_period_type](../ebase_files/fpy_period_type.md) |
| 8 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fisadjustperiod | 调整期 | bpchar | 1 |  | √ | '0' | 调整期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fperiodquarter | 会计季度 | int4 | 32 |  | √ | 0 | 会计季度 |
| 12 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 13 | fperiodyear | 会计年度 | int4 | 32 |  | √ | 0 | 会计年度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_period |  | fid |
