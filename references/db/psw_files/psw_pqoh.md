# 预计可用库存-psw_pqoh

## 预计可用库存-主表 t_psw_pqoh

- **表名称：** 预计可用库存-主表
- **表名：** t_psw_pqoh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_pqoh |  | fid |
| 2 | idx_t_psw_pqoh |  | fmodifytime,fid |

---

## -子表 t_psw_pqohdetail

- **表名称：** -子表
- **表名：** t_psw_pqohdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectedqty25 |  | numeric | 23 | 10 | √ | 0 |  |
| 3 | fprojectedqty24 |  | numeric | 23 | 10 | √ | 0 |  |
| 4 | fprojectedqty23 |  | numeric | 23 | 10 | √ | 0 |  |
| 5 | fprojectedqty22 |  | numeric | 23 | 10 | √ | 0 |  |
| 6 | fprojectedqty21 |  | numeric | 23 | 10 | √ | 0 |  |
| 7 | fprojectedqty20 |  | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fprojectedqty29 |  | numeric | 23 | 10 | √ | 0 |  |
| 10 | fprojectedqty28 |  | numeric | 23 | 10 | √ | 0 |  |
| 11 | fprojectedqty27 |  | numeric | 23 | 10 | √ | 0 |  |
| 12 | fprojectedqty26 |  | numeric | 23 | 10 | √ | 0 |  |
| 13 | fsafetystock | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 14 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fprojectedqty14 |  | numeric | 23 | 10 | √ | 0 |  |
| 18 | fprojectedqty58 |  | numeric | 23 | 10 | √ | 0 |  |
| 19 | fprojectedqty13 |  | numeric | 23 | 10 | √ | 0 |  |
| 20 | fprojectedqty57 |  | numeric | 23 | 10 | √ | 0 |  |
| 21 | fprojectedqty12 |  | numeric | 23 | 10 | √ | 0 |  |
| 22 | fprojectedqty56 |  | numeric | 23 | 10 | √ | 0 |  |
| 23 | fprojectedqty11 |  | numeric | 23 | 10 | √ | 0 |  |
| 24 | fprojectedqty55 |  | numeric | 23 | 10 | √ | 0 |  |
| 25 | fprojectedqty10 |  | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprojectedqty54 |  | numeric | 23 | 10 | √ | 0 |  |
| 27 | fprojectedqty53 |  | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprojectedqty52 |  | numeric | 23 | 10 | √ | 0 |  |
| 29 | fprojectedqty51 |  | numeric | 23 | 10 | √ | 0 |  |
| 30 | fprojectedqty19 |  | numeric | 23 | 10 | √ | 0 |  |
| 31 | fprojectedqty18 |  | numeric | 23 | 10 | √ | 0 |  |
| 32 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 33 | fprojectedqty17 |  | numeric | 23 | 10 | √ | 0 |  |
| 34 | fprojectedqty16 |  | numeric | 23 | 10 | √ | 0 |  |
| 35 | fprojectedqty15 |  | numeric | 23 | 10 | √ | 0 |  |
| 36 | fprojectedqty59 |  | numeric | 23 | 10 | √ | 0 |  |
| 37 | fmaterialcodeid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 38 | fprojectedqty60 |  | numeric | 23 | 10 | √ | 0 |  |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fprojectedqty9 |  | numeric | 23 | 10 | √ | 0 |  |
| 41 | fprojectedqty47 |  | numeric | 23 | 10 | √ | 0 |  |
| 42 | fprojectedqty8 |  | numeric | 23 | 10 | √ | 0 |  |
| 43 | fprojectedqty46 |  | numeric | 23 | 10 | √ | 0 |  |
| 44 | fprojectedqty45 |  | numeric | 23 | 10 | √ | 0 |  |
| 45 | fprojectedqty44 |  | numeric | 23 | 10 | √ | 0 |  |
| 46 | fprojectedqty5 |  | numeric | 23 | 10 | √ | 0 |  |
| 47 | fprojectedqty43 |  | numeric | 23 | 10 | √ | 0 |  |
| 48 | fprojectedqty4 |  | numeric | 23 | 10 | √ | 0 |  |
| 49 | fprojectedqty42 |  | numeric | 23 | 10 | √ | 0 |  |
| 50 | fprojectedqty7 |  | numeric | 23 | 10 | √ | 0 |  |
| 51 | fprojectedqty41 |  | numeric | 23 | 10 | √ | 0 |  |
| 52 | fprojectedqty6 |  | numeric | 23 | 10 | √ | 0 |  |
| 53 | fprojectedqty40 |  | numeric | 23 | 10 | √ | 0 |  |
| 54 | fprojectedqty49 |  | numeric | 23 | 10 | √ | 0 |  |
| 55 | fprojectedqty48 |  | numeric | 23 | 10 | √ | 0 |  |
| 56 | fprojectedqty1 |  | numeric | 23 | 10 | √ | 0 |  |
| 57 | fprojectedqty50 |  | numeric | 23 | 10 | √ | 0 |  |
| 58 | fprojectedqty0 |  | numeric | 23 | 10 | √ | 0 |  |
| 59 | fprojectedqty3 |  | numeric | 23 | 10 | √ | 0 |  |
| 60 | fprojectedqty2 |  | numeric | 23 | 10 | √ | 0 |  |
| 61 | fprojectedqty36 |  | numeric | 23 | 10 | √ | 0 |  |
| 62 | fprojectedqty35 |  | numeric | 23 | 10 | √ | 0 |  |
| 63 | fprojectedqty34 |  | numeric | 23 | 10 | √ | 0 |  |
| 64 | fqtytype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 0 :/ 1 :需求 2 :供应 |
| 65 | fprojectedqty33 |  | numeric | 23 | 10 | √ | 0 |  |
| 66 | fprojectedqty32 |  | numeric | 23 | 10 | √ | 0 |  |
| 67 | fprojectedqty31 |  | numeric | 23 | 10 | √ | 0 |  |
| 68 | fprojectedqty30 |  | numeric | 23 | 10 | √ | 0 |  |
| 69 | fauxiliaryproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 70 | fprojectedqty39 |  | numeric | 23 | 10 | √ | 0 |  |
| 71 | fprojectedqty38 |  | numeric | 23 | 10 | √ | 0 |  |
| 72 | fprojectedqty37 |  | numeric | 23 | 10 | √ | 0 |  |
| 73 | finvqtyonhand | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |
| 74 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_psw_pqohdetail |  | fentryid |
| 2 | idx_t_psw_pqohdetail |  | fparententryid,fentryid |
