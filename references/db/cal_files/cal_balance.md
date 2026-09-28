# 核算余额表-cal_balance

## 核算余额表-分表 t_cal_balance_a

- **表名称：** 核算余额表-分表
- **表名：** t_cal_balance_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccounttype | 计价方法 | bpchar | 1 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 C :实时移动加权平均法 D :标准成本法 E :先进先出计价法 G :先进先出法（月末） |
| 3 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 cal_bd_caldimension |
| 4 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_balance_a_pkey |  | fid |
| 2 | idx_cal_balancea_currency |  | fcurrencyid |

---

## 核算余额表-主表 t_cal_balance

- **表名称：** 核算余额表-主表
- **表名：** t_cal_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyearreceiptcostdiff | fyearreceiptcostdiff | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fyearissuecostdiff | 本年累计发出成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出成本差异 |
| 4 | fperiodendbalance | fperiodendbalance | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 5 | fperiodissuecostdiff | 本期发出成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出成本差异 |
| 6 | fperiodreceiptamount | fperiodreceiptamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fperiodreceiptcostdiff | fperiodreceiptcostdiff | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fperiodreceiptassistqty | fperiodreceiptassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 10 | fperiodissueamount | fperiodissueamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fyearinactualcost | 本年累计收入实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入实际成本 |
| 12 | fyearissueactualcost | 本年累计发出实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出实际成本 |
| 13 | fyearincostdiff | 本年累计收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入成本差异 |
| 14 | fseqnum | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 15 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 16 | fperiodendassistqty | fperiodendassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fperiodissueactualcost | 本期发出实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出实际成本 |
| 18 | fyearreceiptamount | fyearreceiptamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 19 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 22 | fmonth | 月 | int8 | 64 |  | √ | 0 | 月 |
| 23 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 24 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fyearinqty | 本年累计收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入数量 |
| 26 | fyearinstandradcost | 本年累计收入标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入标准成本 |
| 27 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fperiodid | 记账期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 29 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fyearreceiptqty | fyearreceiptqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 32 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 33 | fperiodissueqty | 本期发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出数量 |
| 34 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | faccsysid | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系（已作废） bd_accountingsys |
| 36 | fperiodissueassistqty | fperiodissueassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fperiodinqty | 本期收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入数量 |
| 38 | fperiod | 导入期间 | int8 | 64 |  | √ | 0 | 导入期间 |
| 39 | fyearissueqty | 本年累计发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出数量 |
| 40 | fperiodadjustdiff | fperiodadjustdiff | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | fperiodbeginassistqty | fperiodbeginassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期末成本差异 |
| 43 | fperiodinactualcost | 本期收入实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入实际成本 |
| 44 | fyearissuestandradcost | 本年累计发出标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出标准成本 |
| 45 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 46 | fperiodissuestandardcost | 本期发出标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出标准成本 |
| 47 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 48 | fperiodendactualcost | 期末实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期末实际成本 |
| 49 | fcalrangeid | fcalrangeid | int8 | 64 |  | √ | 0 |  |
| 50 | fisstandardcost | 是否标准成本法 | bpchar | 1 |  | √ | '0' | 是否标准成本法 |
| 51 | fperiodbeginbalance | fperiodbeginbalance | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fperiodbeginactualcost | 期初实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期初实际成本 |
| 53 | fexp | fexp | timestamp | 0 |  |  | null |  |
| 54 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 55 | fbeginstandardcost | 期初标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期初标准成本 |
| 56 | fperiodendstandardcost | 期末标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期末标准成本 |
| 57 | fendperiod | 结束期间 | int8 | 64 |  | √ | 999999 | 结束期间 |
| 58 | fyearreceiptassistqty | fyearreceiptassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 59 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 60 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 61 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期初成本差异 |
| 62 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 cal_bd_calpolicy |
| 63 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入成本差异 |
| 64 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 65 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 66 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 67 | fperiodendqty | 期末结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期末结存数量 |
| 68 | fyearissueassistqty | fyearissueassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 69 | fyearissueamount | fyearissueamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 70 | fperiodreceiptqty | fperiodreceiptqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 71 | fperiodbeginqty | 期初结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初结存数量 |
| 72 | fperiodinstandardcost | 本期收入标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_balance_cmp |  | fcostaccountid,fmaterialid,fperiodid |
| 2 | idx_cal_balance_wh |  | fwarehouseid |
| 3 | idx_cal_balance_calorg |  | fcalorgid |
| 4 | idx_cal_balance_material |  | fmaterialid |
| 5 | idx_cal_balance_cp |  | fperiod,fcostaccountid |
| 6 | idx_cal_balance_cpi |  | fperiodid,fcostaccountid |
| 7 | t_cal_balance_pkey |  | fid |
| 8 | idx_cal_balance_lotcamat |  | flot,fcostaccountid,fmaterialid |
| 9 | idx_cal_balance_ce |  | fendperiod,fcostaccountid |
| 10 | idx_cal_balance_cpp |  | fcostaccountid,fperiod,fendperiod |
