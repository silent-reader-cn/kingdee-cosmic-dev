# 引入核销-ar_settleimport

## 引入核销-主表 t_ar_settleimport

- **表名称：** 引入核销-主表
- **表名：** t_ar_settleimport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchnumber | 引入核销批号 | varchar | 80 |  | √ | ' ' | 引入核销批号 |
| 3 | fexratetable | fexratetable | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmainbillentity | 主方实体标识 | varchar | 50 |  | √ | ' ' | 主方实体标识 |
| 6 | fasstacttype | 主方往来类型 | varchar | 30 |  | √ | ' ' | 主方往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 7 | ftotalunsettledamt | 主方可核销金额 | numeric | 23 | 10 | √ | 0 | 主方可核销金额 |
| 8 | flocaltotalsettleamt | 主方本次核销折本位币 | numeric | 23 | 10 | √ | 0 | 主方本次核销折本位币 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fexchangerate | 主方单据汇率 | numeric | 23 | 10 | √ | 0 | 主方单据汇率 |
| 11 | fmainbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 12 | fquotation | fquotation | varchar | 30 |  | √ | '0' |  |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fpayableamt | 主方应收金额 | numeric | 23 | 10 | √ | 0 | 主方应收金额 |
| 15 | fbillno | 引入核销编码 | varchar | 80 |  | √ | ' ' | 引入核销编码 |
| 16 | fbillsrctype | fbillsrctype | varchar | 5 |  | √ | ' ' |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmainbillnum | 主方单据编号 | varchar | 80 |  | √ | ' ' | 主方单据编号 |
| 19 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: appaysettle :应付付款核销 liqsettle :未清项核销 paytrans :应付转付 payself :付款红蓝对冲 apself :应付红蓝对冲 aparsettle :应付冲应收 apwriteoff :应付红蓝冲销 payrecsettle :付款冲退款 aprecsettle :应付退款核销 transwar :转出质保金 appaidsettle :采购期初预付 recsettle :应收收款核销 arself :应收红蓝对冲 artransfer :债权转移 arapsettle :应收冲应付 recself :收款红蓝对冲 arwriteoff :应收红蓝冲销 baddebtloss :坏账损失 baddebtrecovery :坏账收回 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arliqsettle :未清项核销 |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 引入时间 | timestamp | 0 |  |  | null | 引入时间 |
| 22 | fsettleresult | 核销结果 | varchar | 30 |  | √ | '0' | 核销结果,枚举: 0 :未核销 1 :成功 2 :失败 |
| 23 | ftotalsettleamt | 主方本次核销金额 | numeric | 23 | 10 | √ | 0 | 主方本次核销金额 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fasstactname | fasstactname | varchar | 255 |  | √ | ' ' |  |
| 26 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | fbizdate | 主方业务日期 | timestamp | 0 |  |  | null | 主方业务日期 |
| 28 | fmainasstactid | 主方往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 30 | fcurrencyid | 主方单据币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_settleimport |  | fid |
| 2 | idx_ar_si_billno |  | fbillno |
| 3 | idx_ar_si_billnum |  | fmainbillnum |
| 4 | idx_ar_si_mainbillid |  | fmainbillid |
| 5 | idx_ar_si_dateorg |  | fbizdate,forgid |

---

## 单据体-子表 t_ar_settleimportentry

- **表名称：** 单据体-子表
- **表名：** t_ar_settleimportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funsettledamt | 辅方可核销金额 | numeric | 23 | 10 | √ | 0 | 辅方可核销金额 |
| 3 | fasstact | fasstact | varchar | 255 |  | √ | ' ' |  |
| 4 | fasstactid | 辅方往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | fsettlelocalamt | 辅方本次核销折本位币 | numeric | 23 | 10 | √ | 0 | 辅方本次核销折本位币 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fasstacttype | 辅方往来类型 | varchar | 50 |  | √ | ' ' | 辅方往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 bos_org :业务单元 cas_othercontactunit :其他往来单位 |
| 8 | fbilldate | 辅方业务日期 | timestamp | 0 |  |  | null | 辅方业务日期 |
| 9 | fsettleamt | 辅方本次核销金额 | numeric | 23 | 10 | √ | 0 | 辅方本次核销金额 |
| 10 | fexchangerate | 辅方单据汇率 | numeric | 23 | 10 | √ | 0 | 辅方单据汇率 |
| 11 | fquotation | fquotation | varchar | 30 |  | √ | '0' |  |
| 12 | fbillnum | 辅方单据编号 | varchar | 80 |  | √ | ' ' | 辅方单据编号 |
| 13 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 14 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 15 | fpayableamt | 辅方金额 | numeric | 23 | 10 | √ | 0 | 辅方金额 |
| 16 | fexratetableid | fexratetableid | int8 | 64 |  | √ | 0 |  |
| 17 | fbillentity | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fcurrencyid | 辅方单据币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_sie_billnum |  | fbillnum |
| 2 | idx_ar_sie_pid |  | fid |
| 3 | pk_t_ar_settleimportentry |  | fentryid |
| 4 | idx_ar_sie_billid |  | fbillid |
