# 债券波动率曲面-md_bondvol_f7

## 债券波动率曲面-主表 t_md_bondvol

- **表名称：** 债券波动率曲面-主表
- **表名：** t_md_bondvol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 7 | fpriceruleid | fpriceruleid | int8 | 64 |  | √ | 0 |  |
| 8 | finterpolate | finterpolate | varchar | 30 |  | √ | ' ' |  |
| 9 | fdateorperiod | fdateorperiod | varchar | 30 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsurfacetype | fsurfacetype | varchar | 30 |  | √ | ' ' |  |
| 15 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 16 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 17 | fdateaxisid | fdateaxisid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 20 | fsmilepoints | fsmilepoints | int8 | 64 |  | √ | 0 |  |
| 21 | fdatatype | fdatatype | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_bondvol_bb |  | fbillno |
| 2 | pk_t_md_bondvol |  | fid |

---

## 债券波动率曲面-多语言表 t_md_bondvol_l

- **表名称：** 债券波动率曲面-多语言表
- **表名：** t_md_bondvol_l

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
| 1 | idx_md_bondvol_l_id |  | fid,flocaleid |
| 2 | pk_t_md_bondvol_l |  | fpkid |
