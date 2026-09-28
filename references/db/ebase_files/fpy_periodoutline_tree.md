# 会计期间-fpy_periodoutline_tree

## 会计期间-主表 tk_fpy_periodoutline_tree

- **表名称：** 会计期间-主表
- **表名：** tk_fpy_periodoutline_tree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjuststrategy | 调整期策略 | varchar | 50 |  | √ | ' ' | 调整期策略,枚举: 1 :无 2 :按年 3 :按季 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 会计期间类型 | int8 | 64 |  |  | null | [会计期间类型 fpy_period_type](../ebase_files/fpy_period_type.md) |
| 6 | fgeneratetype | 生成方式 | varchar | 50 |  | √ | ' ' | 生成方式,枚举: 1 :自然月 2 :月 3 :周 4 :自定义 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fk_fpy_periodyear1 | 会计年度 | varchar | 50 |  | √ | ' ' | 会计年度,枚举: |
| 15 | fk_fpy_times | 调整次数 | varchar | 50 |  | √ | ' ' | 调整次数 |
| 16 | fperiodquarter | 会计季度 | int4 | 32 |  | √ | 0 | 会计季度 |
| 17 | fperiod | 会计期间 | int4 | 32 |  | √ | 0 | 会计期间 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fk_fpy_outlinebegindate1 | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 21 | fperiodyear | 会计年度 | int4 | 32 |  | √ | 0 | 会计年度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__fpy_periodoutline_tree |  | fid |

---

## 会计期间-多语言表 tk_fpy_periodoutline_tree_l

- **表名称：** 会计期间-多语言表
- **表名：** tk_fpy_periodoutline_tree_l

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
| 1 | pk__fpy_periodoutline_tree_l |  | fpkid |
