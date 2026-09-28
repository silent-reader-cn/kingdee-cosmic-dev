# 历史外汇报价-md_forexquote_h

## 报价输出-子表 t_md_forexquote_output_h

- **表名称：** 报价输出-子表
- **表名：** t_md_forexquote_output_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterm | 期限 | varchar | 30 |  | √ | ' ' | 期限 |
| 3 | fmidprice | 中间价 | numeric | 23 | 10 | √ | 0.0000000000 | 中间价 |
| 4 | fsellprice | 卖出价 | numeric | 23 | 10 | √ | 0.0000000000 | 卖出价 |
| 5 | fbuyprice | 买入价 | numeric | 23 | 10 | √ | 0.0000000000 | 买入价 |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fquotetype | 货币对报价方式 | varchar | 30 |  | √ | ' ' | 货币对报价方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_md_forexquote_output_h |  | fentryid |
| 2 | idx_md_forexquote_output_h |  | fid |

---

## 日历-多选基础资料表 t_md_quote_wc_h

- **表名称：** 日历-多选基础资料表
- **表名：** t_md_quote_wc_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [工作日历 tbd_workcalendar](../fbd_files/tbd_workcalendar.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_quote_wc_h |  | fentryid |
| 2 | pk_t_md_quote_wc_h |  | fpkid |

---

## 历史外汇报价-多语言表 t_md_forexquote_h_l

- **表名称：** 历史外汇报价-多语言表
- **表名：** t_md_forexquote_h_l

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
| 1 | pk_t_md_forexquote_h_l |  | fpkid |
| 2 | idx_md_forexquote_l_h |  | fid,flocaleid |

---

## 历史外汇报价-主表 t_md_forexquote_h

- **表名称：** 历史外汇报价-主表
- **表名：** t_md_forexquote_h

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
| 8 | fviewdateaxisid | 远期日期轴 | int8 | 64 |  | √ | 0 | [日期轴 tbd_dateaxis](../fbd_files/tbd_dateaxis.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fissuezoneid | 发布时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 14 | fissuetime | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 15 | fbizdate | 报价日期 | timestamp | 0 |  |  | null | 报价日期 |
| 16 | fsourcebillid | 源报价id不要修改 | int8 | 64 |  | √ | 0 | 源报价id不要修改 |
| 17 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 18 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 19 | fbillno | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型,枚举: yield :收益率曲线 bond volatility :债券波动率曲面 rate quote :外汇报价 rate ceil volatility :利率上限波动率曲面 forex volatility :外汇波动率曲面 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_forexquote_h_b |  | fbillno |
| 2 | pk_t_md_forexquote_h |  | fid |

---

## 报价录入-子表 t_md_forexquote_input_h

- **表名称：** 报价录入-子表
- **表名：** t_md_forexquote_input_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterm | 期限 | varchar | 30 |  | √ | ' ' | 期限 |
| 3 | fmidprice | 中间价 | numeric | 23 | 10 | √ | 0.0000000000 | 中间价 |
| 4 | fsellprice | 卖出价 | numeric | 23 | 10 | √ | 0.0000000000 | 卖出价 |
| 5 | fsellpoints | 卖出价远期点数（BP） | numeric | 23 | 10 | √ | 0.0000000000 | 卖出价远期点数（BP） |
| 6 | fbuyprice | 买入价 | numeric | 23 | 10 | √ | 0.0000000000 | 买入价 |
| 7 | fmidpoints | 中间价远期点数（BP） | numeric | 23 | 10 | √ | 0.0000000000 | 中间价远期点数（BP） |
| 8 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fquotetype | 货币对报价方式 | varchar | 30 |  | √ | ' ' | 货币对报价方式 |
| 12 | fbuypoints | 买入价远期点数（BP） | numeric | 23 | 10 | √ | 0.0000000000 | 买入价远期点数（BP） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_forexquote_input_h |  | fid |
| 2 | pk_t_md_forexquote_input_h |  | fentryid |

---

## 定义-子表 t_md_forexquote_define_h

- **表名称：** 定义-子表
- **表名：** t_md_forexquote_define_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspotdelay | 即期偏移（d） | int4 | 32 |  | √ | 2 | 即期偏移（d） |
| 3 | fspotmethod | 即期汇率 | varchar | 30 |  | √ | ' ' | 即期汇率,枚举: specify :指定 crossExRate :交叉汇率计算 |
| 4 | frcuryieldcurveid | 标价币种收益率曲线 | int8 | 64 |  | √ | 0 | [收益率曲线 md_yieldcurve_f7](../md_files/md_yieldcurve_f7.md) |
| 5 | fmidcurrencyid | 中间币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | ffowardquotation | 远期汇率录入方式 | varchar | 30 |  | √ | ' ' | 远期汇率录入方式,枚举: exRate :汇率 point :点数 |
| 7 | fcurrency | 买方币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 8 | fautoupdate | 自动更新 | bpchar | 1 |  | √ | '0' | 自动更新 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fsellcurrency | 卖方币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | frateaccuracy | 报价输出精度 | int4 | 32 |  | √ | 10 | 报价输出精度 |
| 12 | fdateadjustmethod | 日期调整方式 | varchar | 30 |  | √ | ' ' | 日期调整方式,枚举: forward :延后 ad_forward :调整延后 backward :提前 ad_backward :调整提前 no_adjust :不调整 |
| 13 | finputcount | 报价录入行数 | int4 | 32 |  | √ | 0 | 报价录入行数 |
| 14 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fquotetype | 货币对报价方式 | varchar | 30 |  | √ | ' ' | 货币对报价方式 |
| 17 | fdateaxisid | 远期汇率日期轴 | int8 | 64 |  | √ | 0 | [日期轴 tbd_dateaxis](../fbd_files/tbd_dateaxis.md) |
| 18 | fdaterule | 日期 | varchar | 30 |  | √ | ' ' | 日期,枚举: sys :系统生成 specify :指定 |
| 19 | ffowardmethod | 远期汇率 | varchar | 30 |  | √ | ' ' | 远期汇率,枚举: specify :指定 crossExRate :交叉汇率计算 ycDeduction :收益率曲线推导 none :无 |
| 20 | flcuryieldcurveid | 基准币种收益率曲线 | int8 | 64 |  | √ | 0 | [收益率曲线 md_yieldcurve_f7](../md_files/md_yieldcurve_f7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_md_forexquote_define_h |  | fid |
| 2 | pk_t_md_forexquote_define_h |  | fentryid |
