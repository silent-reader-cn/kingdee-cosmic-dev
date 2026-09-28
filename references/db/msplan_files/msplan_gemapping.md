# 实体对照数据源-msplan_gemapping

## 实体对照数据源-主表 t_msplan_gemapping

- **表名称：** 实体对照数据源-主表
- **表名：** t_msplan_gemapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 5 | fdatasourceid | fdatasourceid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fmodelentityid | fmodelentityid | varchar | 255 |  | √ | 0 |  |
| 8 | fstatus | fstatus | varchar | 1 |  | √ | ' ' |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fenable | fenable | varchar | 1 |  | √ | ' ' |  |
| 12 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 13 | fversionfield | fversionfield | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msplan_gemang_fnumber |  | fnumber |
| 2 | pk_msplan_gemapping |  | fid |
| 3 | idx_msplan_gemang_fcreatetime |  | fcreatetime |

---

## 实体对照数据源-多语言表 t_msplan_gemapping_l

- **表名称：** 实体对照数据源-多语言表
- **表名：** t_msplan_gemapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' |  |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msplan_gemapping_l |  | fpkid |
| 2 | idx_msplan_gemangl_fname |  | fname |
| 3 | idx_msplan_gemangl_fid |  | fid,flocaleid |
