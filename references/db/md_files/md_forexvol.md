# 外汇波动率曲面-md_forexvol

## 单据体-子表 t_md_forexvol_entrys

- **表名称：** 单据体-子表
- **表名：** t_md_forexvol_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterm | 到期期限 | varchar | 30 |  | √ | ' ' | 到期期限 |
| 3 | fcallvol | 看涨波动率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 看涨波动率(%) |
| 4 | fcurrpair | 币种对 | varchar | 30 |  | √ | ' ' | 币种对 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fputvol | 看跌波动率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 看跌波动率(%) |
| 7 | fputdelta | 看跌Delta | numeric | 23 | 10 | √ | 0.0000000000 | 看跌Delta |
| 8 | ftputstrikertfsource | 看跌执行价格数据源 | varchar | 30 |  | √ | ' ' | 看跌执行价格数据源 |
| 9 | fputstrikespread | 看跌执行价差 | numeric | 23 | 10 | √ | 0.0000000000 | 看跌执行价差 |
| 10 | fcallstrikertfsource | 看涨执行价格数据源 | varchar | 30 |  | √ | ' ' | 看涨执行价格数据源 |
| 11 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 12 | frtfon | 实时更新 | bpchar | 1 |  | √ | ' ' | 实时更新 |
| 13 | fcallvolrtfsource | 看涨波动率数据源 | varchar | 30 |  | √ | ' ' | 看涨波动率数据源 |
| 14 | fputvolspread | 看跌波动率差 | numeric | 23 | 10 | √ | 0.0000000000 | 看跌波动率差 |
| 15 | fstrikeno | 执行价格次数 | int8 | 64 |  | √ | 0 | 执行价格次数 |
| 16 | fputpremium | 看跌期权费 | numeric | 23 | 10 | √ | 0.0000000000 | 看跌期权费 |
| 17 | fputvolrtfsource | 看跌波动率数据源 | varchar | 30 |  | √ | ' ' | 看跌波动率数据源 |
| 18 | fcallpremium | 看涨期权费 | numeric | 23 | 10 | √ | 0.0000000000 | 看涨期权费 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fcalldelta | 看涨Delta | numeric | 23 | 10 | √ | 0.0000000000 | 看涨Delta |
| 21 | fputstrike | 看跌执行价格 | numeric | 23 | 10 | √ | 0.0000000000 | 看跌执行价格 |
| 22 | fcallvolspread | 看涨波动率差 | numeric | 23 | 10 | √ | 0.0000000000 | 看涨波动率差 |
| 23 | fcallstrike | 看涨执行价格 | numeric | 23 | 10 | √ | 0.0000000000 | 看涨执行价格 |
| 24 | fcallstrikespread | 看涨执行价差 | numeric | 23 | 10 | √ | 0.0000000000 | 看涨执行价差 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_forexvol_entrys |  | fentryid |
| 2 | idx_md_forexvol_entrys_id |  | fid |

---

## 外汇波动率曲面-多语言表 t_md_forexvol_l

- **表名称：** 外汇波动率曲面-多语言表
- **表名：** t_md_forexvol_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 80 |  | √ | ' ' |  |
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
| 2 | fcallvolfreeze | 固定看涨波动率 | varchar | 30 |  | √ | ' ' | 固定看涨波动率,枚举: unset :不固定 pricepoint :按价差基点调整 pricepercentage :按价差百分比调整 |
| 3 | fpriceruleid | 定价规则 | int8 | 64 |  | √ | 0 | [定价规则 md_pricerule](../fbd_files/md_pricerule.md) |
| 4 | fcurrpairs | 货币对 | varchar | 2000 |  | √ | ' ' | 货币对 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | flockdelta | 固定Delta | bpchar | 1 |  | √ | ' ' | 固定Delta |
| 9 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 10 | fatmlayer | ATM层 | int8 | 64 |  | √ | 0 | ATM层 |
| 11 | freferdate | 参考日期 | timestamp | 0 |  |  | null | 参考日期 |
| 12 | fupdateoption | 更新选项 | varchar | 30 |  | √ | ' ' | 更新选项,枚举: calVolatility :计算波动率 calPremium :计算期权费 |
| 13 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fstrikenum | 执行价格数量 | int8 | 64 |  | √ | 0 | 执行价格数量 |
| 16 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 17 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flockstrike | 固定执行价格 | bpchar | 1 |  | √ | ' ' | 固定执行价格 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fputvolfreeze | 固定看跌波动率 | varchar | 30 |  | √ | ' ' | 固定看跌波动率,枚举: unset :不固定 pricepoint :按价差基点调整 pricepercentage :按价差百分比调整 |
| 22 | fcallstrikefreeze | 固定看涨执行价格 | varchar | 30 |  | √ | ' ' | 固定看涨执行价格,枚举: unset :不固定 pricepoint :按价差基点调整 pricepercentage :按价差百分比调整 |
| 23 | fsmilecurrpairs | 币种对 | varchar | 2000 |  | √ | ' ' | 币种对,枚举: |
| 24 | fsmilematurityterm | 到期期限 | varchar | 255 |  | √ | ' ' | 到期期限,枚举: |
| 25 | fputstrikefreeze | 固定看跌执行价格 | varchar | 30 |  | √ | ' ' | 固定看跌执行价格,枚举: unset :不固定 pricepoint :按价差基点调整 pricepercentage :按价差百分比调整 |
| 26 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 27 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 28 | fdateaxisid | 到期期限 | int8 | 64 |  | √ | 0 | [日期轴 tbd_dateaxis](../fbd_files/tbd_dateaxis.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: yield :收益率曲线 bond volatility :债券波动率曲面 rate quote :汇率报价 rate ceil volatility :汇率上限波动率曲面 forex volatility :外汇波动率曲面 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_forexvol |  | fid |
| 2 | idx_md_forexvol_bb |  | fbillno |
