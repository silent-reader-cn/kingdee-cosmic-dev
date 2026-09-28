# 收益率曲线-md_yieldcurve_f7

## 日历-多选基础资料表 t_md_yieldline_wc

- **表名称：** 日历-多选基础资料表
- **表名：** t_md_yieldline_wc

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
| 1 | pk_t_md_yieldline_wc |  | fpkid |
| 2 | idx_md_yieldline_wc_fid |  | fid |

---

## 单据体-子表 t_md_yieldline_fintool

- **表名称：** 单据体-子表
- **表名：** t_md_yieldline_fintool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffra | FRA(num-num) | varchar | 50 |  | √ | ' ' | FRA(num-num) |
| 3 | fmidrate | 中间利率 | numeric | 23 | 10 | √ | 0.0000000000 | 中间利率 |
| 4 | ffuturecontract | 期货合约 | varchar | 50 |  | √ | ' ' | 期货合约 |
| 5 | fterm | 期限 | varchar | 50 |  | √ | ' ' | 期限 |
| 6 | fadjmethod | 日期调整方式 | varchar | 50 |  | √ | ' ' | 日期调整方式,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fsellrate | 卖出利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 卖出利率(%) |
| 9 | fissuedate | 债券发行日期 | timestamp | 0 |  |  | null | 债券发行日期 |
| 10 | fisforcurve | 用于构建曲线 | bpchar | 1 |  | √ | '1' | 用于构建曲线 |
| 11 | fprice | 价格 | numeric | 23 | 10 | √ | 0.0000000000 | 价格 |
| 12 | fcouponrate | 债券息票率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 债券息票率（%） |
| 13 | frateoffset | 利率确定偏移(d) | int4 | 32 |  | √ | 0 | 利率确定偏移(d) |
| 14 | fenddate | 债券到期日 | timestamp | 0 |  |  | null | 债券到期日 |
| 15 | ffreq | 计息频率 | varchar | 50 |  | √ | ' ' | 计息频率,枚举: month :1m season :3m hyear :6m year :1y |
| 16 | ffintool | 金融工具名称 | varchar | 50 |  | √ | ' ' | 金融工具名称,枚举: Cash :现金 FRA :远期利率协议 Bond :债券 Swap :互换 Future :期货 |
| 17 | fbasis | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: Actual_365 :Actual/365 Actual_360 :Actual/360 ISDA_30_360 :30/360(ISDA) SIA_30_360 :30/360(SIA) BMA_30_360 :30/360(BMA) European_30_360 :30/360(European) Actual_actual :Actual/Actual(ISDA) Japanese_Actual_365 :Actual/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Actual/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fismidrate | fismidrate | bpchar | 1 |  | √ | '1' |  |
| 20 | fbuyrate | 买入利率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 买入利率(%) |
| 21 | ffutureenddate | 期货到期日方式 | varchar | 50 |  | √ | ' ' | 期货到期日方式,枚举: thirdWednesday :第三个星期三 secondFriday :第二个星期五 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_yieldline_fintool |  | fentryid |
| 2 | idx_md_yieldline_finid |  | fid |

---

## 收益率曲线-多语言表 t_md_yieldline_l

- **表名称：** 收益率曲线-多语言表
- **表名：** t_md_yieldline_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
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
| 1 | idx_md_yieldline_l_id |  | fid,flocaleid |
| 2 | pk_t_md_yieldline_l |  | fpkid |

---

## 收益率曲线-主表 t_md_yieldline

- **表名称：** 收益率曲线-主表
- **表名：** t_md_yieldline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbondendroll | fbondendroll | bpchar | 1 |  | √ | '0' |  |
| 3 | fpriceruleid | fpriceruleid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | finterptype | 插值方法 | varchar | 30 |  | √ | ' ' | 插值方法,枚举: perFwdRateCon :每日远期利率常数 lineZeroRate :线性零息率 tripleSamp :三次样条 |
| 9 | fbillno | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 10 | fadjustmethod | fadjustmethod | varchar | 30 |  | √ | ' ' |  |
| 11 | ffrequency | ffrequency | varchar | 30 |  | √ | ' ' |  |
| 12 | fbootstrap | 息票剥离法 | varchar | 30 |  | √ | ' ' | 息票剥离法,枚举: OnZeroRate :输入零息利率 OnForward :远期 OnYield :即期 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | fname | varchar | 100 |  |  | ' ' |  |
| 15 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fzerorate | fzerorate | bpchar | 1 |  | √ | '0' |  |
| 19 | fbonddealtype | 债券处理方法 | varchar | 30 |  | √ | ' ' | 债券处理方法,枚举: swap :互换法 bond :债券法 |
| 20 | fbasis | 计息基准 | varchar | 30 |  | √ | ' ' | 计息基准,枚举: Actual_365 :Actual/365 Actual_360 :Actual/360 ISDA_30_360 :30/360(ISDA) SIA_30_360 :30/360(SIA) BMA_30_360 :30/360(BMA) European_30_360 :30/360(European) Actual_actual :Actual/Actual(ISDA) Japanese_Actual_365 :Actual/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Actual/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 21 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 22 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 23 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fdateaxisid | fdateaxisid | int8 | 64 |  | √ | 0 |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | fdatatype | fdatatype | varchar | 30 |  | √ | ' ' |  |
| 27 | frefdate | frefdate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_yieldline_bn |  | fbillno |
| 2 | pk_t_md_yieldline |  | fid |
