# 物料版本（作废）-bd_materialversion

## 物料版本（作废）-主表 t_bd_bomversion

- **表名称：** 物料版本（作废）-主表
- **表名：** t_bd_bomversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fecnbillno | fecnbillno | varchar | 60 |  | √ | ' ' |  |
| 6 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 7 | faudittime | faudittime | timestamp | 0 |  |  | null |  |
| 8 | feffectdate | feffectdate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fdisabletime | fdisabletime | timestamp | 0 |  |  | null |  |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fecodate | fecodate | timestamp | 0 |  |  | null |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 15 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 16 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 17 | fversionname | fversionname | int8 | 64 |  | √ | 0 |  |
| 18 | fbomversionrule | fbomversionrule | int8 | 64 |  | √ | 0 |  |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fremark | fremark | varchar | 60 |  | √ | ' ' |  |
| 21 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 22 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 23 | fenableorid | fenableorid | int8 | 64 |  | √ | 0 |  |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 26 | fenabletime | fenabletime | timestamp | 0 |  |  | null |  |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 128 |  |  | ' ' | 编码 |
| 29 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fdisableorid | fdisableorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_bomversion_createorg |  | fcreateorgid |
| 2 | idx_bd_bomversion |  | fnumber,fcreateorgid |
| 3 | idx_t_bd_bomversion_master |  | fmasterid |
| 4 | t_bd_bomversion_pkey |  | fid |
| 5 | idx_bd_bomversion_material |  | fmaterialid |

---

## 物料版本（作废）-多语言表 t_bd_bomversion_l

- **表名称：** 物料版本（作废）-多语言表
- **表名：** t_bd_bomversion_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_bomversion_l_pkey |  | fpkid |
| 2 | idx_bd_bomversion_l |  | fid,flocaleid |
