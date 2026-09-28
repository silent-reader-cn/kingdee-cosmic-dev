# 采购退料申请单-pm_purrefundapplybill

## 采购退料申请单-主表 t_pm_purrefundapplybill

- **表名称：** 采购退料申请单-主表
- **表名：** t_pm_purrefundapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 512 |  | √ | ' ' | 联系地址 |
| 3 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 10 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 17 | frefundtype | 退货类型 | varchar | 5 |  | √ | ' ' | 退货类型,枚举: A :库存退货 B :检验退货 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 20 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 22 | fmanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 23 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 24 | fsettleorgid | 结算组织(封存) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 26 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 30 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 31 | fconfirmstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :自动确认 |
| 32 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 33 | fprovideraddress | 供货联系地址 | varchar | 512 |  |  | ' ' | 供货联系地址 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 36 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |
| 37 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 40 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fprovidersupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 44 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 45 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 46 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 47 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 48 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 49 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 50 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 51 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purrefund_billno_org |  | fbillno,forgid |
| 2 | t_pm_purrefundapplybill_pkey |  | fid |
| 3 | idx_pm_purrefundapply_time |  | fbiztime |
| 4 | idx_pm_purrefundapply_org |  | forgid,fbiztime,fbillno |
| 5 | idx_pm_purra_supplier |  | fsupplierid |

---

## 采购退料申请单-反写记录表 t_pm_purrefundapplybill_wb

- **表名称：** 采购退料申请单-反写记录表
- **表名：** t_pm_purrefundapplybill_wb

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
| 1 | t_pm_purrefundapplybill_wb_pkey |  | fentryid |
| 2 | idx_pm_purrefundapplybill_wb_fk |  | fid |

---

## 采购退料申请单-多语言表 t_pm_purrefundapplybill_l

- **表名称：** 采购退料申请单-多语言表
- **表名：** t_pm_purrefundapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purrefundapplybill_l_pkey |  | fpkid |
| 2 | idx_pm_purrefundapply_l |  | fid |

---

## 关联子实体-子表 t_pm_purrefundappentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purrefundappentry_lk

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
| 1 | t_pm_purrefundappentry_lk_pkey |  | fpkid |
| 2 | idx_pm_purrefundappentry_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_pm_purrefundapplybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purrefundapplybill_lk

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
| 1 | idx_pm_purrefundapplybill_lk_fk |  | fid |
| 2 | t_pm_purrefundapplybill_lk_pkey |  | fpkid |

---

## 采购退料申请单-关联追踪表 t_pm_purrefundapplybill_tc

- **表名称：** 采购退料申请单-关联追踪表
- **表名：** t_pm_purrefundapplybill_tc

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
| 1 | t_pm_purrefundapplybill_tc_pkey |  | fid |
| 2 | idx_pm_purrefundapplybill_tc_tbill |  | ftbillid |
| 3 | idx_pm_purrefundapplybill_tc_tid |  | ftid |

---

## 物料明细-子表 t_pm_purrefundapplyentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_purrefundapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 9 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 17 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 23 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 24 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 25 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 26 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 27 | fentrymanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 28 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 29 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 30 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 31 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 32 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 33 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 36 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 37 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 38 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 40 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 42 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 43 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 44 | freturnmaterialtype | 退料类型 | bpchar | 1 |  | √ | '0' | 退料类型,枚举: 0 : 1 :退料 2 :退补料 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | fentrypayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 48 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 49 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 50 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 51 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 52 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 53 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 54 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 55 | fsupplierlot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 56 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 57 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 58 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 59 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 60 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 61 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 62 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 63 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 64 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 65 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 66 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 67 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 68 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 69 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 70 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 71 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 72 | ffloatingconversion | 浮动换算 | bpchar | 1 |  | √ | '0' | 浮动换算 |
| 73 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 74 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 75 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 76 | fentryinvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 77 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 78 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 79 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 80 | fentrypurorgid | 分录采购组织(封存) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 81 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 82 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 83 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purrefundapplyentry |  | fid |
| 2 | t_pm_purrefundapplyentry_pkey |  | fentryid |
