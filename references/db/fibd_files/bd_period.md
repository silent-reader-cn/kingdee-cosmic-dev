# 会计日历-bd_period

## 会计日历-主表 t_bd_period

- **表名称：** 会计日历-主表
- **表名：** t_bd_period

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fperiodnumber | 会计期间 | int8 | 64 |  | √ | 0 | 会计期间 |
| 6 | fperiodoutlineid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_periodoutline_tree](../fibd_files/bd_periodoutline_tree.md) |
| 7 | ftypeid | 会计日历类型 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 8 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fstatus | 单据状态 | bpchar | 1 |  | √ | 'Z' | 单据状态,枚举: Z :暂存 A :创建 B :已提交 C :已审核 |
| 10 | fisadjustperiod | 调整期 | bpchar | 1 |  | √ | '0' | 调整期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fperiodquarter | 会计季度 | int8 | 64 |  | √ | 0 | 会计季度 |
| 13 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 14 | fperiodyear | 会计年度 | int4 | 32 |  | √ | 0 | 会计年度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_period_pkey |  | fid |
| 2 | idx_t_bd_period_fnumber |  | fnumber |

---

## 会计日历-多语言表 t_bd_period_l

- **表名称：** 会计日历-多语言表
- **表名：** t_bd_period_l

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
| 1 | t_bd_period_l_pkey |  | fpkid |
| 2 | idx_bd_period_l_fid |  | fid,flocaleid |
