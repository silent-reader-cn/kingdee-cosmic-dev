# 核算余额表-cal_balance

## 核算余额表-分表 t_cal_balance_a

- **表名称：** 核算余额表-分表
- **表名：** t_cal_balance_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcaldimensionvalue | 核算维度值 | varchar | 100 |  | √ | ' ' | 核算维度值 |
| 3 | faccounttype | 计价方法 | bpchar | 1 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 C :实时移动加权平均法 D :标准成本法 E :先进先出计价法 G :先进先出法（月末） |
| 4 | fcaldimensionid | 核算维度 | int8 | 64 |  | √ | 0 | [核算维度 cal_bd_caldimension](../cal_files/cal_bd_caldimension.md) |
| 5 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | [核算范围 cal_bd_calrange](../cal_files/cal_bd_calrange.md) |

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
| 9 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fperiodissueamount | fperiodissueamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 11 | fyearinactualcost | 本年累计收入实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入实际成本 |
| 12 | fyearissueactualcost | 本年累计发出实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出实际成本 |
| 13 | fyearincostdiff | 本年累计收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入成本差异 |
| 14 | fseqnum | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 15 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 16 | fperiodendassistqty | fperiodendassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 17 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 18 | fperiodissueactualcost | 本期发出实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出实际成本 |
| 19 | fyearreceiptamount | fyearreceiptamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 21 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 23 | fmonth | 月 | int8 | 64 |  | √ | 0 | 月 |
| 24 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 25 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fyearinqty | 本年累计收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入数量 |
| 27 | fyearinstandradcost | 本年累计收入标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计收入标准成本 |
| 28 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fperiodid | 记账期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 30 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 31 | fyearreceiptqty | fyearreceiptqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | funitid | funitid | int8 | 64 |  | √ | 0 |  |
| 33 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 34 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 35 | fperiodissueqty | 本期发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出数量 |
| 36 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | faccsysid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系（已作废） bd_accountingsys](../fibd_files/bd_accountingsys.md) |
| 38 | fperiodissueassistqty | fperiodissueassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fperiodinqty | 本期收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入数量 |
| 40 | fperiod | 导入期间 | int8 | 64 |  | √ | 0 | 导入期间 |
| 41 | fyearissueqty | 本年累计发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出数量 |
| 42 | fperiodadjustdiff | fperiodadjustdiff | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 43 | fperiodbeginassistqty | fperiodbeginassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期末成本差异 |
| 45 | fperiodinactualcost | 本期收入实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入实际成本 |
| 46 | fyearissuestandradcost | 本年累计发出标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本年累计发出标准成本 |
| 47 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 48 | fperiodissuestandardcost | 本期发出标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发出标准成本 |
| 49 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 50 | fperiodendactualcost | 期末实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期末实际成本 |
| 51 | fcalrangeid | fcalrangeid | int8 | 64 |  | √ | 0 |  |
| 52 | fisstandardcost | 是否标准成本法 | bpchar | 1 |  | √ | '0' | 是否标准成本法 |
| 53 | fperiodbeginbalance | fperiodbeginbalance | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | fperiodbeginactualcost | 期初实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期初实际成本 |
| 55 | fexp | fexp | timestamp | 0 |  |  | null |  |
| 56 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 57 | fbeginstandardcost | 期初标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期初标准成本 |
| 58 | fperiodendstandardcost | 期末标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 期末标准成本 |
| 59 | fendperiod | 结束期间 | int8 | 64 |  | √ | 999999 | 结束期间 |
| 60 | fyearreceiptassistqty | fyearreceiptassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 61 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 62 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 期初成本差异 |
| 64 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 cal_bd_calpolicy](../cal_files/cal_bd_calpolicy.md) |
| 65 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入成本差异 |
| 66 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 67 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 68 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 69 | fperiodendqty | 期末结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期末结存数量 |
| 70 | fyearissueassistqty | fyearissueassistqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 71 | fyearissueamount | fyearissueamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 72 | fperiodreceiptqty | fperiodreceiptqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 73 | fperiodbeginqty | 期初结存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初结存数量 |
| 74 | fperiodinstandardcost | 本期收入标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 本期收入标准成本 |

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
