# 会计日历-bd_periodoutline_tree

## 会计日历-多语言表 t_bd_periodoutline_l

- **表名称：** 会计日历-多语言表
- **表名：** t_bd_periodoutline_l

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
| 1 | t_bd_periodoutline_l_pkey |  | fpkid |
| 2 | idx_bd_periodoutline_l_fid |  | fid,flocaleid |

---

## 会计日历-主表 t_bd_periodoutline

- **表名称：** 会计日历-主表
- **表名：** t_bd_periodoutline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjuststrategy | 调整期策略 | varchar | 50 |  | √ | '1' | 调整期策略,枚举: 1 :无 2 :按年 3 :按季 |
| 3 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fgroupid | 会计日历类型 | int8 | 64 |  | √ | 0 | [会计日历类型 bd_period_type](../fibd_files/bd_period_type.md) |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifyorgid | fmodifyorgid | int8 | 64 |  | √ | 0 |  |
| 7 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 8 | fgeneratetype | 生成方式 | varchar | 50 |  | √ | ' ' | 生成方式,枚举: 1 :自然月 2 :月（屏蔽） 3 :周 4 :月 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fbegindate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 11 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fperiodquarter | 会计季度 | int8 | 64 |  | √ | 0 | 会计季度 |
| 18 | fperiod | 会计期间 | int8 | 64 |  | √ | 0 | 会计期间 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fperiodyear | 会计年度 | int4 | 32 |  | √ | 0 | 会计年度 |
| 22 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_periodoutline_pkey |  | fid |
