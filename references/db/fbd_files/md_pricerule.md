# 定价规则-md_pricerule

## 选择市场-多选基础资料表 t_tbd_pricerule_mk

- **表名称：** 选择市场-多选基础资料表
- **表名：** t_tbd_pricerule_mk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [市场信息 tbd_marketinfo](../fbd_files/tbd_marketinfo.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tbd_pricerule_mk |  | fpkid |
| 2 | idx_tbd_pricerule_mk_fk |  | fid |

---

## 单据体-子表 t_tbd_pricerule_yield

- **表名称：** 单据体-子表
- **表名：** t_tbd_pricerule_yield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbootstrap | 息票剥离法 | varchar | 30 |  | √ | ' ' | 息票剥离法,枚举: OnZeroRate :零息利率 OnForward :远期 OnYield :即期 |
| 3 | fmarketid | 市场 | int8 | 64 |  | √ | 0 | [市场信息 tbd_marketinfo](../fbd_files/tbd_marketinfo.md) |
| 4 | fbondfutures | 债券 | bpchar | 1 |  | √ | ' ' | 债券 |
| 5 | fswpbndmethod | 债券处理方法 | varchar | 30 |  | √ | ' ' | 债券处理方法,枚举: swap :互换法 bond :债券法 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdf | 折现因子 | varchar | 30 |  | √ | ' ' | 折现因子,枚举: impledDF :隐含因子 specifyDF :指定因子 |
| 8 | ffras | 远期利率协议 | bpchar | 1 |  | √ | ' ' | 远期利率协议 |
| 9 | finterpolation | 插值方法 | varchar | 30 |  | √ | ' ' | 插值方法,枚举: perFwdRateCon :每日远期利率常数 lineZeroRate :线性零息率 tripleSamp :三次样条 |
| 10 | frates | 利率 | varchar | 30 |  | √ | ' ' | 利率,枚举: buyingRates :买入/中间利率 sellingRates :卖出利率 |
| 11 | fcash | 现金 | bpchar | 1 |  | √ | ' ' | 现金 |
| 12 | fswapbond | 互换 | bpchar | 1 |  | √ | ' ' | 互换 |
| 13 | ftype | 用途 | varchar | 30 |  | √ | ' ' | 用途,枚举: disc :折现 ref :参考 |
| 14 | fyieldsid | 收益率曲线 | int8 | 64 |  | √ | 0 | [收益率曲线 md_yieldcurve_f7](../md_files/md_yieldcurve_f7.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ffutures | 期货 | bpchar | 1 |  | √ | ' ' | 期货 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_pricerule_yield_fk |  | fyieldsid,fmarketid |
| 2 | pk_t_tbd_pricerule_yield |  | fentryid |

---

## 定价规则-多语言表 t_tbd_pricerule_l

- **表名称：** 定价规则-多语言表
- **表名：** t_tbd_pricerule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tbd_pricerule_l |  | fpkid |
| 2 | idx_tbd_pricerule_l_id |  | fid,flocaleid |

---

## 定价规则-主表 t_tbd_pricerule

- **表名称：** 定价规则-主表
- **表名：** t_tbd_pricerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fforexquoteid | 外汇报价 | int8 | 64 |  | √ | 0 | [外汇报价 md_forexquote_f7](../md_files/md_forexquote_f7.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fintratevolid | 利率上限波动率曲面 | int8 | 64 |  | √ | 0 | [利率上限波动率曲面 md_intratevol_f7](../md_files/md_intratevol_f7.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | finsertmethod | 插值方法 | varchar | 30 |  | √ | ' ' | 插值方法,枚举: linear :线性插值 cubicspline :三次样条 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fbondvolid | 债券波动率曲面 | int8 | 64 |  | √ | 0 | [债券波动率曲面 md_bondvol_f7](../md_files/md_bondvol_f7.md) |
| 13 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 14 | fisspecific | 允许特定的汇率和波动率 | bpchar | 1 |  | √ | ' ' | 允许特定的汇率和波动率 |
| 15 | fforexvolid | 外汇波动率曲面 | int8 | 64 |  | √ | 0 | [外汇波动率曲面 md_forexvol_f7](../md_files/md_forexvol_f7.md) |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 17 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 18 | fdefaultrule | 默认定价规则 | bpchar | 1 |  | √ | '0' | 默认定价规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tbd_pricerule |  | fid |
| 2 | idx_tbd_pricerule_id |  | fmasterid |
