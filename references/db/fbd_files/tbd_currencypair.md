# 货币对-tbd_currencypair

## 货币对-多语言表 t_tbd_currencypair_l

- **表名称：** 货币对-多语言表
- **表名：** t_tbd_currencypair_l

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
| 1 | pk_t_tbd_currencypair_l |  | fpkid |
| 2 | idx_tbd_currencypair_l_id |  | fid |

---

## 日历-多选基础资料表 t_tbd_currency_wc

- **表名称：** 日历-多选基础资料表
- **表名：** t_tbd_currency_wc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工作日历 tbd_workcalendar](../fbd_files/tbd_workcalendar.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tbd_currency_wc |  | fid,fbasedataid |
| 2 | pk_t_tbd_currency_wc |  | fpkid |

---

## 货币对-主表 t_tbd_currencypair

- **表名称：** 货币对-主表
- **表名：** t_tbd_currencypair

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fforwarddateid | 远期日期 | int8 | 64 |  | √ | 0 | [日期轴 tbd_dateaxis](../fbd_files/tbd_dateaxis.md) |
| 3 | fbasismarketid | 基准币种市场 | int8 | 64 |  | √ | 0 | [市场信息 tbd_marketinfo](../fbd_files/tbd_marketinfo.md) |
| 4 | fcalendarsid | fcalendarsid | int8 | 64 |  | √ | 0 |  |
| 5 | fviacurrencyid | 中间币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fderivemethod | 汇率派生方式 | varchar | 30 |  | √ | ' ' | 汇率派生方式,枚举: forwardPoints :远期点数派生远期汇率 forwardRate :远期汇率派生远期点数 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpid | 汇率报价id | int8 | 64 |  | √ | 0 | 汇率报价id |
| 12 | fspotdays | 即期延迟 | int8 | 64 |  | √ | 0 | 即期延迟 |
| 13 | fquotemarketid | 标价币种市场 | int8 | 64 |  | √ | 0 | [市场信息 tbd_marketinfo](../fbd_files/tbd_marketinfo.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fcalculatefunction | 计算方法 | varchar | 30 |  | √ | ' ' | 计算方法,枚举: forwardrate :指定远期汇率 forexpairty :外汇平价 ratepairty :利率平价 |
| 18 | fbasisyieldcurveid | 基准币种收益率曲线 | int8 | 64 |  | √ | 0 | [收益率曲线 md_yieldcurve_f7](../md_files/md_yieldcurve_f7.md) |
| 19 | fquoteyieldcurveid | 标价币种收益率曲线 | int8 | 64 |  | √ | 0 | [收益率曲线 md_yieldcurve_f7](../md_files/md_yieldcurve_f7.md) |
| 20 | fquotecurrencyid | 标价币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fbasiscurrencyid | 基准币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fdateadjust | 日期调整方式 | varchar | 30 |  | √ | ' ' | 日期调整方式,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 23 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 24 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tbd_currencypair |  | fid |
| 2 | idx_tbd_currencypair_bb |  | fnumber |
