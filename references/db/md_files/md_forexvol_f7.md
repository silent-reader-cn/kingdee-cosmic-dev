# 外汇波动率曲面-md_forexvol_f7

## 外汇波动率曲面-多语言表 t_md_forexvol_l

- **表名称：** 外汇波动率曲面-多语言表
- **表名：** t_md_forexvol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_forexvol_l |  | fpkid |
| 2 | idx_md_forexvol_l_id |  | fid,flocaleid |

---

## 外汇波动率曲面-主表 t_md_forexvol

- **表名称：** 外汇波动率曲面-主表
- **表名：** t_md_forexvol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcallvolfreeze | fcallvolfreeze | varchar | 30 |  | √ | ' ' |  |
| 3 | fpriceruleid | fpriceruleid | int8 | 64 |  | √ | 0 |  |
| 4 | fcurrpairs | fcurrpairs | varchar | 2000 |  | √ | ' ' |  |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | flockdelta | flockdelta | bpchar | 1 |  | √ | ' ' |  |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fatmlayer | fatmlayer | int8 | 64 |  | √ | 0 |  |
| 11 | freferdate | freferdate | timestamp | 0 |  |  | null |  |
| 12 | fupdateoption | fupdateoption | varchar | 30 |  | √ | ' ' |  |
| 13 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fstrikenum | fstrikenum | int8 | 64 |  | √ | 0 |  |
| 16 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 17 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flockstrike | flockstrike | bpchar | 1 |  | √ | ' ' |  |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fputvolfreeze | fputvolfreeze | varchar | 30 |  | √ | ' ' |  |
| 22 | fcallstrikefreeze | fcallstrikefreeze | varchar | 30 |  | √ | ' ' |  |
| 23 | fsmilecurrpairs | fsmilecurrpairs | varchar | 2000 |  | √ | ' ' |  |
| 24 | fsmilematurityterm | fsmilematurityterm | varchar | 255 |  | √ | ' ' |  |
| 25 | fputstrikefreeze | fputstrikefreeze | varchar | 30 |  | √ | ' ' |  |
| 26 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 27 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 28 | fdateaxisid | fdateaxisid | int8 | 64 |  | √ | 0 |  |
| 29 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 30 | fdatatype | fdatatype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_forexvol |  | fid |
| 2 | idx_md_forexvol_bb |  | fbillno |
