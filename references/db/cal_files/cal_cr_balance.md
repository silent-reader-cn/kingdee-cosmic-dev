# 追溯期初余额表-cal_cr_balance

## 追溯期初余额表-分表 t_cal_cr_balance_a

- **表名称：** 追溯期初余额表-分表
- **表名：** t_cal_cr_balance_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcaldimensionvalue | 核算维度值 | varchar | 50 |  | √ | ' ' | 核算维度值 |
| 3 | faccounttype | 计价方法 | varchar | 50 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 C :实时移动加权平均法 D :标准成本法 E :先进先出计价法 G :先进先出法（月末） |
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
| 1 | pk_cal_cr_balance_a |  | fid |

---

## 追溯期初余额表-主表 t_cal_cr_balance

- **表名称：** 追溯期初余额表-主表
- **表名：** t_cal_cr_balance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyearissuecostdiff | 本年累计发出成本差异 | numeric | 23 | 10 | √ | 0 | 本年累计发出成本差异 |
| 3 | fperiodissuecostdiff | 本期发出成本差异 | numeric | 23 | 10 | √ | 0 | 本期发出成本差异 |
| 4 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 5 | fyearinactualcost | 本年累计收入实际成本 | numeric | 23 | 10 | √ | 0 | 本年累计收入实际成本 |
| 6 | fyearissueactualcost | 本年累计发出实际成本 | numeric | 23 | 10 | √ | 0 | 本年累计发出实际成本 |
| 7 | fyearincostdiff | 本年累计收入成本差异 | numeric | 23 | 10 | √ | 0 | 本年累计收入成本差异 |
| 8 | fseqnum | 顺序号 | int8 | 64 |  | √ | 0 | 顺序号 |
| 9 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 10 | fdevcost | 研发费用 | varchar | 50 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 11 | fperiodissueactualcost | 本期发出实际成本 | numeric | 23 | 10 | √ | 0 | 本期发出实际成本 |
| 12 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 14 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 15 | fmonth | 月 | int8 | 64 |  | √ | 0 | 月 |
| 16 | flot | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 17 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fyearinqty | 本年累计收入数量 | numeric | 23 | 10 | √ | 0 | 本年累计收入数量 |
| 19 | fyearinstandradcost | 本年累计收入标准成本 | numeric | 23 | 10 | √ | 0 | 本年累计收入标准成本 |
| 20 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fperiodid | 记账期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 23 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 24 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fperiodissueqty | 本期发出数量 | numeric | 23 | 10 | √ | 0 | 本期发出数量 |
| 26 | faccsysid | 核算体系 | int8 | 64 |  | √ | 0 | [核算体系（已作废） bd_accountingsys](../fibd_files/bd_accountingsys.md) |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fperiodinqty | 本期收入数量 | numeric | 23 | 10 | √ | 0 | 本期收入数量 |
| 29 | fperiod | 导入期间 | int8 | 64 |  | √ | 0 | 导入期间 |
| 30 | fyearissueqty | 本年累计发出数量 | numeric | 23 | 10 | √ | 0 | 本年累计发出数量 |
| 31 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0 | 期末成本差异 |
| 32 | fperiodinactualcost | 本期收入实际成本 | numeric | 23 | 10 | √ | 0 | 本期收入实际成本 |
| 33 | fyearissuestandradcost | 本年累计发出标准成本 | numeric | 23 | 10 | √ | 0 | 本年累计发出标准成本 |
| 34 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 35 | fperiodissuestandardcost | 本期发出标准成本 | numeric | 23 | 10 | √ | 0 | 本期发出标准成本 |
| 36 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 37 | fperiodendactualcost | 期末实际成本 | numeric | 23 | 10 | √ | 0 | 期末实际成本 |
| 38 | fisstandardcost | 是否标准成本法 | bpchar | 1 |  | √ | '0' | 是否标准成本法 |
| 39 | fperiodbeginactualcost | 期初实际成本 | numeric | 23 | 10 | √ | 0 | 期初实际成本 |
| 40 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 41 | fdividebasisvalue | fdividebasisvalue | varchar | 500 |  | √ | ' ' |  |
| 42 | fbeginstandardcost | 期初标准成本 | numeric | 23 | 10 | √ | 0 | 期初标准成本 |
| 43 | fperiodendstandardcost | 期末标准成本 | numeric | 23 | 10 | √ | 0 | 期末标准成本 |
| 44 | fendperiod | 结束期间 | int8 | 64 |  | √ | 0 | 结束期间 |
| 45 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 46 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0 | 期初成本差异 |
| 48 | frtpplanid | 还原方案 | int8 | 64 |  | √ | 0 | [还原方案 cal_cr_retrospectplan](../cal_files/cal_cr_retrospectplan.md) |
| 49 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 cal_bd_calpolicy](../cal_files/cal_bd_calpolicy.md) |
| 50 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0 | 本期收入成本差异 |
| 51 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 52 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 53 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 54 | fperiodendqty | 期末结存数量 | numeric | 23 | 10 | √ | 0 | 期末结存数量 |
| 55 | fperiodbeginqty | 期初结存数量 | numeric | 23 | 10 | √ | 0 | 期初结存数量 |
| 56 | fperiodinstandardcost | 本期收入标准成本 | numeric | 23 | 10 | √ | 0 | 本期收入标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_cr_balance |  | fid |
| 2 | idx_cal_cr_balance_m0 |  | frtpplanid |

---

## 单据体-子表 t_cal_cr_balance_detail

- **表名称：** 单据体-子表
- **表名：** t_cal_cr_balance_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyearissuestandradcost | 本年累计发出标准成本 | numeric | 23 | 10 | √ | 0 | 本年累计发出标准成本 |
| 3 | fyearissuecostdiff | 本年累计发出成本差异 | numeric | 23 | 10 | √ | 0 | 本年累计发出成本差异 |
| 4 | fperiodissuecostdiff | 本期发出成本差异 | numeric | 23 | 10 | √ | 0 | 本期发出成本差异 |
| 5 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fperiodissuestandardcost | 本期发出标准成本 | numeric | 23 | 10 | √ | 0 | 本期发出标准成本 |
| 8 | fyearinactualcost | 本年累计收入实际成本 | numeric | 23 | 10 | √ | 0 | 本年累计收入实际成本 |
| 9 | fyearissueactualcost | 本年累计发出实际成本 | numeric | 23 | 10 | √ | 0 | 本年累计发出实际成本 |
| 10 | fperiodendactualcost | 期末实际成本 | numeric | 23 | 10 | √ | 0 | 期末实际成本 |
| 11 | fyearincostdiff | 本年累计收入成本差异 | numeric | 23 | 10 | √ | 0 | 本年累计收入成本差异 |
| 12 | fperiodbeginactualcost | 期初实际成本 | numeric | 23 | 10 | √ | 0 | 期初实际成本 |
| 13 | fperiodissueactualcost | 本期发出实际成本 | numeric | 23 | 10 | √ | 0 | 本期发出实际成本 |
| 14 | fbeginstandardcost | 期初标准成本 | numeric | 23 | 10 | √ | 0 | 期初标准成本 |
| 15 | fperiodendstandardcost | 期末标准成本 | numeric | 23 | 10 | √ | 0 | 期末标准成本 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fyearinqty | 本年累计收入数量 | numeric | 23 | 10 | √ | 0 | 本年累计收入数量 |
| 18 | fyearinstandradcost | 本年累计收入标准成本 | numeric | 23 | 10 | √ | 0 | 本年累计收入标准成本 |
| 19 | fperiodbegincostdiff | 期初成本差异 | numeric | 23 | 10 | √ | 0 | 期初成本差异 |
| 20 | fperiodissueqty | 本期发出数量 | numeric | 23 | 10 | √ | 0 | 本期发出数量 |
| 21 | fcostelementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 22 | fperiodinqty | 本期收入数量 | numeric | 23 | 10 | √ | 0 | 本期收入数量 |
| 23 | fperiodincostdiff | 本期收入成本差异 | numeric | 23 | 10 | √ | 0 | 本期收入成本差异 |
| 24 | fperiodendqty | 期末结存数量 | numeric | 23 | 10 | √ | 0 | 期末结存数量 |
| 25 | fyearissueqty | 本年累计发出数量 | numeric | 23 | 10 | √ | 0 | 本年累计发出数量 |
| 26 | fperiodendcostdiff | 期末成本差异 | numeric | 23 | 10 | √ | 0 | 期末成本差异 |
| 27 | fperiodinactualcost | 本期收入实际成本 | numeric | 23 | 10 | √ | 0 | 本期收入实际成本 |
| 28 | fperiodbeginqty | 期初结存数量 | numeric | 23 | 10 | √ | 0 | 期初结存数量 |
| 29 | fperiodinstandardcost | 本期收入标准成本 | numeric | 23 | 10 | √ | 0 | 本期收入标准成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_cr_balance_detail |  | fdetailid |
| 2 | idx_cal_cr_balance_detail_fk |  | fid |
