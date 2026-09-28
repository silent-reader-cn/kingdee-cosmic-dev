# 清理单-ap_liquidation

## 关联子实体-子表 t_ap_liquidationbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_liquidationbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_liquidationbillentry_lk_pkey |  | fpkid |

---

## 清理单-反写记录表 t_ap_liquidationbill_wb

- **表名称：** 清理单-反写记录表
- **表名：** t_ap_liquidationbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_liquidationbill_wb_pkey |  | fentryid |

---

## 单据体-子表 t_ap_liquidationentry

- **表名称：** 单据体-子表
- **表名：** t_ap_liquidationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | flqdlocalamt | 清理金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 清理金额(本位币) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsourceentryid | 源分录ID | int8 | 64 |  | √ | 0 | 源分录ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | funsettleamt | 清理金额 | numeric | 19 | 6 | √ | 0.000000 | 清理金额 |
| 9 | famount | 应付金额 | numeric | 19 | 6 | √ | 0.000000 | 应付金额 |
| 10 | fsourcebilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fitemid | 费用项目/物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fitemtype | 项目类型 | varchar | 30 |  | √ | ' ' | 项目类型,枚举: bd_material :物料 er_expenseitemedit :费用项目 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fpaypropertyid | 款项性质 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 16 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fsourcebillno | 源单编号 | varchar | 30 |  | √ | ' ' | 源单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_liqe_id |  | fid |
| 2 | t_ap_liquidationentry_pkey |  | fentryid |

---

## 清理单-主表 t_ap_liquidation

- **表名称：** 清理单-主表
- **表名：** t_ap_liquidation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 4 | fasstact | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpurdepartmentid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fasstacttype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :人员 cas_othercontactunit :其他往来单位 |
| 8 | fpurdeptid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fliquidaterid | 清理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 15 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已作废 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fliquidationlocalamt | 清理金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 清理金额(本位币) |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fdescription | 备注 | varchar | 255 |  |  | null | 备注 |
| 24 | fdepartmentid | fdepartmentid | int8 | 64 |  | √ | 0 |  |
| 25 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fliquidationamt | 清理金额 | numeric | 19 | 6 | √ | 0.000000 | 清理金额 |
| 27 | fissettled | 是否已核销 | bpchar | 1 |  | √ | ' ' | 是否已核销 |
| 28 | fliquidationdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 29 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | ' ' | 已生成凭证 |
| 31 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_liq_org |  | forgid |
| 2 | t_ap_liquidation_pkey |  | fid |

---

## 清理单-关联追踪表 t_ap_liquidationbill_tc

- **表名称：** 清理单-关联追踪表
- **表名：** t_ap_liquidationbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_liquidationbill_tc_tid |  | ftid |
| 2 | t_ap_liquidationbill_tc_pkey |  | fid |
| 3 | idx_ap_liquidationbill_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_ap_liquidationbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ap_liquidationbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_liquidationbill_lk_pkey |  | fpkid |
