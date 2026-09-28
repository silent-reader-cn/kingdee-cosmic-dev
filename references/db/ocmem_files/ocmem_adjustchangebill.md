# 预算调整清单-ocmem_adjustchangebill

## 预算调整清单-主表 t_ocmem_adjustchangebill

- **表名称：** 预算调整清单-主表
- **表名：** t_ocmem_adjustchangebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 5 | fbudgetorgid | 预算编制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | forgid | 预算公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbudgetmonthid | 预算月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 8 | frulechangebillid | 费率规则变更单ID | int8 | 64 |  | √ | 0 | 费率规则变更单ID |
| 9 | fdimension | 预算周期维度 | bpchar | 1 |  | √ | ' ' | 预算周期维度,枚举: A :按年 B :按月 |
| 10 | fadjustbillid | 原关联预算调整单id | int8 | 64 |  | √ | 0 | 原关联预算调整单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_adchangebill_ajid |  | fadjustbillid |
| 2 | pk_t_ocmem_adjustchangebill |  | fid |

---

## 清单明细-子表 t_ocmem_adchangeentry

- **表名称：** 清单明细-子表
- **表名：** t_ocmem_adchangeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpoolitemclassid | 关联数据源计算商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 3 | fnewtotalsalerate | 新费率值 | numeric | 23 | 10 | √ | 0 | 新费率值 |
| 4 | foldtotalsalerate | 原费率值 | numeric | 23 | 10 | √ | 0 | 原费率值 |
| 5 | fadjustbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 6 | fruletype | 费率规则 | bpchar | 1 |  | √ | ' ' | 费率规则,枚举: A :金额比例 B :单位费用金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foldcalallocationrate | 原分配比例% | numeric | 23 | 10 | √ | 0 | 原分配比例% |
| 9 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 10 | fstatus | 完成状态 | bpchar | 1 |  | √ | 'A' | 完成状态,枚举: A :未完成 B :已完成 |
| 11 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fcalunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 14 | fversion | 版本 | int4 | 32 |  | √ | 0 | 版本 |
| 15 | fpoolitemid | 关联数据源商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 16 | fbudgetbalanceid | 预算编码 | int8 | 64 |  | √ | 0 | 预算余额表 ocdbd_budgetbalance |
| 17 | fpoolchannelid | 关联数据源渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 18 | foldadjustamount | 原费用金额 | numeric | 23 | 10 | √ | 0 | 原费用金额 |
| 19 | fitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 20 | fcalamount | 计算金额 | numeric | 23 | 10 | √ | 0 | 计算金额 |
| 21 | fentryorgid | 预算承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fitemid | 预算产品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 24 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 25 | fpoolentryid | 关联数据源分录id | int8 | 64 |  | √ | 0 | 关联数据源分录id |
| 26 | frollruleid | 费率规则编码 | int8 | 64 |  | √ | 0 | 变动费率规则 ocmem_rollraterule |
| 27 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 28 | frollruleentryid | 关联规则分录id | int8 | 64 |  | √ | 0 | 关联规则分录id |
| 29 | fnewadjustamount | 新费用金额 | numeric | 23 | 10 | √ | 0 | 新费用金额 |
| 30 | fcalqty | 计算数量 | numeric | 23 | 10 | √ | 0 | 计算数量 |
| 31 | fnewcalallocationrate | 新分配比例% | numeric | 23 | 10 | √ | 0 | 新分配比例% |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_adchangeentry_fid |  | fid |
| 2 | pk_ocmem_adchangeentry |  | fentryid |
