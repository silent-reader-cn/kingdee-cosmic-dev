# 信用等级-task_creditlevel

## 信用等级-多语言表 t_tk_creditlevel_l

- **表名称：** 信用等级-多语言表
- **表名：** t_tk_creditlevel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 信用等级名称 | varchar | 50 |  | √ | ' ' | 信用等级名称 |
| 3 | fdescribe | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_creditlevel_l_pkey |  | fpkid |
| 2 | index_t_tk_creditlevel_l |  | fid,flocaleid |

---

## 信用等级-主表 t_tk_creditlevel

- **表名称：** 信用等级-主表
- **表名：** t_tk_creditlevel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 组织（弃用） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaxvalue | 分数范围至 | numeric | 19 | 6 | √ | 0.000000 | 分数范围至 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fdefaultlevel | 默认等级 | bpchar | 1 |  | √ | 'A' | 默认等级 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 D :废弃 |
| 11 | fminvalue | 分数范围从（含） | numeric | 19 | 6 | √ | 0.000000 | 分数范围从（含） |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 15 | fdefaultvalue | 默认分数 | numeric | 19 | 6 | √ | 0.000000 | 默认分数 |
| 16 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_creditlevel_num |  | fnumber |
| 2 | idx_t_tk_creditlevel_createorg |  | fcreateorgid |
| 3 | t_tk_creditlevel_pkey |  | fid |
| 4 | idx_t_tk_creditlevel_master |  | fmasterid |
