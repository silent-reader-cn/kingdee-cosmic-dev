# 行类型-bd_linetype

## 行类型-主表 t_bd_linetype

- **表名称：** 行类型-主表
- **表名：** t_bd_linetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcontrolcriterion | 控制基准 | varchar | 50 |  | √ | ' ' | 控制基准,枚举: 0 :数量 1 :金额 |
| 5 | fshipments | 是否发货 | bpchar | 1 |  | √ | '0' | 是否发货 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | freceiving | 是否收货 | bpchar | 1 |  | √ | '0' | 是否收货 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstorageout | 是否出库 | bpchar | 1 |  | √ | '0' | 是否出库 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fserviceattribute | 业务属性 | int8 | 64 |  | √ | 0 | [业务属性 bd_serviceattribute](../sbd_files/bd_serviceattribute.md) |
| 16 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 18 | fstorage | 是否入库 | bpchar | 1 |  | √ | '0' | 是否入库 |
| 19 | facceptance | 是否验收 | bpchar | 1 |  | √ | '0' | 是否验收 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_linetype |  | fid |
| 2 | index_bd_linetype_fnumber |  | fnumber |

---

## 行类型-多语言表 t_bd_linetype_l

- **表名称：** 行类型-多语言表
- **表名：** t_bd_linetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_linetype_l |  | fpkid |
| 2 | idx_bd_linetype_l_fid |  | fid,flocaleid |
