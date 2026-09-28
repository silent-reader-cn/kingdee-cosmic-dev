# 采购验收单-pm_puracceptbill

## 物料明细-子表 t_pm_puraccbillentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_puraccbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 5 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | freturnbaseqty | 已退验基本数量 | numeric | 23 | 10 | √ | 0 | 已退验基本数量 |
| 9 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 |
| 17 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 19 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 24 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 25 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 26 | fedliveraddress | 交货地址 | varchar | 512 |  |  | null | 交货地址 |
| 27 | fecostcenterid | 验收成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 28 | fjoinpayablepriceamount | 关联应付金额 | numeric | 23 | 10 | √ | 0 | 关联应付金额 |
| 29 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 31 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 32 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 33 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 36 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 37 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 38 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 40 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 41 | freturnmaterialtype | 退料类型 | bpchar | 1 |  | √ | '0' | 退料类型,枚举: 0 : 1 :退料 2 :退补料 |
| 42 | frecretqty | 验收可退数量 | numeric | 23 | 10 | √ | 0 | 验收可退数量 |
| 43 | fhasgenapbusbill | 已生成暂估应付单 | bpchar | 1 |  | √ | '0' | 已生成暂估应付单 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 46 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | null | 物料名称(历史) |
| 47 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | frecretamount | 验收可退金额 | numeric | 23 | 10 | √ | 0 | 验收可退金额 |
| 49 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 50 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 51 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 52 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 53 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 54 | frecretbaseqty | 验收可退基本数量 | numeric | 23 | 10 | √ | 0 | 验收可退基本数量 |
| 55 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 56 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 57 | fjoinpayablebaseqty | 关联应付基本数量 | numeric | 23 | 10 | √ | 0 | 关联应付基本数量 |
| 58 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 59 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 60 | fpayablebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0 | 应付基本数量 |
| 61 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 62 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 63 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 64 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 65 | freturnqty | 已退验数量 | numeric | 23 | 10 | √ | 0 | 已退验数量 |
| 66 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 67 | freturnamount | 已退验金额 | numeric | 23 | 10 | √ | 0 | 已退验金额 |
| 68 | fordersupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 69 | fpayablepriceqty | 应付数量 | numeric | 23 | 10 | √ | 0 | 应付数量 |
| 70 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 71 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 72 | fjoinpayablepriceqty | 关联应付数量 | numeric | 23 | 10 | √ | 0 | 关联应付数量 |
| 73 | fentrycomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 74 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_puraccbillentry_fid |  | fid |
| 2 | idx_pm_puraccbillentry_mat |  | fmaterialid,fid |
| 3 | pk_t_pm_puraccbillentry |  | fentryid |

---

## 关联子实体-子表 t_pm_puracceptbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_puracceptbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_puracceptbill_lk |  | fpkid |
| 2 | idx_pm_puracceptbill_lk_fk |  | fid |

---

## 采购验收单-主表 t_pm_puracceptbill

- **表名称：** 采购验收单-主表
- **表名：** t_pm_puracceptbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisallocbyper | 按比例分配 | bpchar | 1 |  | √ | '1' | 按比例分配 |
| 3 | forgid | 验收组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fhasapbusbill | 是否生成暂估应付单 | bpchar | 1 |  | √ | '0' | 是否生成暂估应付单 |
| 6 | fiswholealloc | 按整单分摊 | bpchar | 1 |  | √ | '1' | 按整单分摊 |
| 7 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fpuroperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 9 | fbiztime | 验收日期 | timestamp | 0 |  |  | null | 验收日期 |
| 10 | frecdeptid | 验收部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 14 | fisexpensealloc | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 18 | fpuroperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 27 | frecoperatorid | 验收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 31 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 32 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 33 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 34 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 35 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 36 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 37 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 38 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 39 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 40 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 42 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 43 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_puracceptbill_fbillno |  | fbillno |
| 2 | pk_t_pm_puracceptbill |  | fid |
| 3 | idx_pm_puracceptbill_org |  | forgid,fbiztime,fbillno |
| 4 | idx_pm_puracceptbill_time |  | fbiztime |

---

## 采购验收单-关联追踪表 t_pm_puracceptbill_tc

- **表名称：** 采购验收单-关联追踪表
- **表名：** t_pm_puracceptbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_puracceptbill_tc_tbill |  | ftbillid |
| 2 | pk_pm_puracceptbill_tc |  | fid |
| 3 | idx_pm_puracceptbill_tc_tid |  | ftid |

---

## 采购验收单-多语言表 t_pm_puracceptbill_l

- **表名称：** 采购验收单-多语言表
- **表名：** t_pm_puracceptbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_puracceptbill_l |  | fid,flocaleid |
| 2 | pk_t_pm_puracceptbill_l |  | fpkid |

---

## 关联子实体-子表 t_pm_puraccbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_puraccbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_puraccbillentry_lk |  | fpkid |
| 2 | idx_pm_puraccbillentry_lk_fk |  | fentryid |

---

## 分摊明细-子表 t_pm_puraccbillfientry

- **表名称：** 分摊明细-子表
- **表名：** t_pm_puraccbillfientry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | fallocationamt | 分配金额 | numeric | 23 | 10 | √ | 0 | 分配金额 |
| 4 | fallocationper | 分配比例(%) | numeric | 23 | 10 | √ | 0 | 分配比例(%) |
| 5 | ffientrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | ffientrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | ffientrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | ffientrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fexpenseitermid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_puraccbillfientry_fid |  | fid |
| 2 | pk_t_pm_puraccbillfientry |  | fentryid |

---

## 采购验收单-反写记录表 t_pm_puracceptbill_wb

- **表名称：** 采购验收单-反写记录表
- **表名：** t_pm_puracceptbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_puracceptbill_wb |  | fentryid |
| 2 | idx_pm_puracceptbill_wb_fk |  | fid |
