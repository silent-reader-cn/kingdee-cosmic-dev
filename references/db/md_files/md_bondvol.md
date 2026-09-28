# 债券波动率曲面-md_bondvol

## 债券波动率曲面-主表 t_md_bondvol

- **表名称：** 债券波动率曲面-主表
- **表名：** t_md_bondvol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fpriceruleid | 定价规则 | int8 | 64 |  | √ | 0 | [定价规则 md_pricerule](../fbd_files/md_pricerule.md) |
| 8 | finterpolate | finterpolate | varchar | 30 |  | √ | ' ' |  |
| 9 | fdateorperiod | 日期或期限 | varchar | 30 |  | √ | ' ' | 日期或期限,枚举: date :日期 period :期限 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 14 | fsurfacetype | 曲面类型 | varchar | 30 |  | √ | ' ' | 曲面类型,枚举: bond :债券 |
| 15 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 16 | fdesc | 曲面描述 | varchar | 255 |  | √ | ' ' | 曲面描述 |
| 17 | fdateaxisid | 期权行权日期轴 | int8 | 64 |  | √ | 0 | [日期轴 tbd_dateaxis](../fbd_files/tbd_dateaxis.md) |
| 18 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fsmilepoints | 行权价格点数 | int8 | 64 |  | √ | 0 | 行权价格点数 |
| 21 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: yield :收益率曲线 bond volatility :债券波动率曲面 rate quote :汇率报价 rate ceil volatility :汇率上限波动率曲面 forex volatility :外汇波动率曲面 |

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

## 金融工具单据体-子表 t_md_bondvol_entrys

- **表名称：** 金融工具单据体-子表
- **表名：** t_md_bondvol_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstrikefp | 行权价格(全价) | numeric | 23 | 10 | √ | 0.0000000000 | 行权价格(全价) |
| 3 | fexercisedate | 期权行权日期 | timestamp | 0 |  |  | null | 期权行权日期 |
| 4 | fprepricevol | 预估价格波动率 | numeric | 23 | 10 | √ | 0.0000000000 | 预估价格波动率 |
| 5 | fstrikecp | 行权价格(净价) | numeric | 23 | 10 | √ | 0.0000000000 | 行权价格(净价) |
| 6 | fatmfp | ATM价格（全价） | numeric | 23 | 10 | √ | 0.0000000000 | ATM价格（全价） |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | frtfsource | 实时更新数据源 | varchar | 30 |  | √ | ' ' | 实时更新数据源 |
| 9 | fbondissueid | 债券发行代码 | int8 | 64 |  | √ | 0 | 债券发行F7 tm_bondissuef7 |
| 10 | fstrikepricespread | 行权价差 | numeric | 23 | 10 | √ | 0.0000000000 | 行权价差 |
| 11 | fpremium | 期权费 | numeric | 23 | 10 | √ | 0.0000000000 | 期权费 |
| 12 | fpricevol | 隐含价格波动率 | numeric | 23 | 10 | √ | 0.0000000000 | 隐含价格波动率 |
| 13 | fexperiod | 期权行权期限 | varchar | 30 |  | √ | ' ' | 期权行权期限 |
| 14 | fbienddate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 15 | fyieldvol | fyieldvol | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | foptiontype | 期权类型 | varchar | 30 |  | √ | ' ' | 期权类型,枚举: call :看涨 put :看跌 |
| 17 | fsmilepoint | 行权价格点数 | int4 | 32 |  | √ | 0 | 行权价格点数 |
| 18 | fatmcp | ATM价格（净价） | numeric | 23 | 10 | √ | 0.0000000000 | ATM价格（净价） |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fisrtf | 是否实时更新 | bpchar | 1 |  | √ | ' ' | 是否实时更新 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_bondvol_entrys |  | fentryid |
| 2 | idx_md_bondvol_entrys_fid |  | fid |

---

## 债券波动率曲面-多语言表 t_md_bondvol_l

- **表名称：** 债券波动率曲面-多语言表
- **表名：** t_md_bondvol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdesc | 曲面描述 | varchar | 255 |  | √ | ' ' | 曲面描述 |
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

---

## 债券发行-多选基础资料表 t_md_bondvol_bi

- **表名称：** 债券发行-多选基础资料表
- **表名：** t_md_bondvol_bi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 债券发行F7 tm_bondissuef7 |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_bondvol_bi |  | fpkid |
| 2 | idx_t_md_bondvol |  | fid,fbasedataid |
