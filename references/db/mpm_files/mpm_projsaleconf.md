# 项目销售服务确认单-mpm_projsaleconf

## 项目销售服务确认单-反写记录表 t_mpm_saleconf_wb

- **表名称：** 项目销售服务确认单-反写记录表
- **表名：** t_mpm_saleconf_wb

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
| 1 | pk_mpm_saleconf_wb |  | fentryid |
| 2 | idx_mpm_saleconf_wb_fk |  | fid |

---

## 交付确认信息单据体-子表 t_mpm_pscentry

- **表名称：** 交付确认信息单据体-子表
- **表名：** t_mpm_pscentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 3 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 7 | fcontractentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fcontractid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 10 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 12 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 13 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 15 | fsrcentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 16 | fcontractseq | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 17 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 18 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fcurincrelamt | 关联收入金额(本位币) | numeric | 23 | 10 | √ | 0 | 关联收入金额(本位币) |
| 20 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 21 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 22 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 23 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 25 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 26 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 28 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 29 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 32 | fcontractentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 33 | fincrelamt | 关联收入金额 | numeric | 23 | 10 | √ | 0 | 关联收入金额 |
| 34 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 35 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 36 | fmainentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 37 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 38 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 39 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 40 | fmainbillno | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 41 | fcontractnum | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 42 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 43 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 46 | fmainentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_pscentry |  | fentryid |
| 2 | idx_mpm_pscentry_fid |  | fid |

---

## 关联子实体-子表 t_mpm_pscdeliver_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_pscdeliver_lk

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
| 1 | idx_mpm_pscdeliver_lk_fk |  | fentryid |
| 2 | pk_mpm_pscdeliver_lk |  | fpkid |

---

## 项目销售服务确认单-主表 t_mpm_saleconf

- **表名称：** 项目销售服务确认单-主表
- **表名：** t_mpm_saleconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 经办人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcurtaxsettlamt | 含税结算额(本位币) | numeric | 23 | 10 | √ | 0 | 含税结算额(本位币) |
| 4 | forgid | 立项组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsettleamt | 结算额 | numeric | 23 | 10 | √ | 0 | 结算额 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fischargeoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 8 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 10 | frevconrate | 收入确认比例(%) | numeric | 23 | 10 | √ | 0 | 收入确认比例(%) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fischargedoff | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 13 | fcurincrelamt | 关联收入金额(本位币) | numeric | 23 | 10 | √ | 0 | 关联收入金额(本位币) |
| 14 | foperatordeptid | 经办部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | frevconway | 收入确认方式 | bpchar | 1 |  | √ | ' ' | 收入确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 16 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 17 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 18 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fisprojectbegin | 项目期初 | bpchar | 1 |  | √ | '0' | 项目期初 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fcursettamt | 结算额(本位币) | numeric | 23 | 10 | √ | 0 | 结算额(本位币) |
| 29 | fincrelamt | 关联收入金额 | numeric | 23 | 10 | √ | 0 | 关联收入金额 |
| 30 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 31 | fpaymode | 付款方式 | varchar | 10 |  | √ | 'CREDIT' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 32 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 33 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 34 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 35 | fexchangetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 36 | ftaxsettleamt | 含税结算额 | numeric | 23 | 10 | √ | 0 | 含税结算额 |
| 37 | ftaskid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 38 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 42 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_saleconf_billno |  | fbillno |
| 2 | pk_mpm_saleconf |  | fid |

---

## 项目销售服务确认单-多语言表 t_mpm_saleconf_l

- **表名称：** 项目销售服务确认单-多语言表
- **表名：** t_mpm_saleconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_saleconf_l |  | fpkid |
| 2 | idx_mpm_saleconfl_fidflid |  | fid,flocaleid |

---

## 项目销售服务确认单-分表 t_mpm_saleconf_s

- **表名称：** 项目销售服务确认单-分表
- **表名：** t_mpm_saleconf_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 3 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 4 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 5 | fcontractentity | 合同实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fsalegroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 7 | fcontractid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 8 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | fcontractentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 10 | fsaledeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fsrcentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 13 | fmainentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 14 | fcontractseq | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 15 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 16 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | fmainbillno | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 18 | fsaleuserid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 19 | fcontractnum | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 20 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 22 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 23 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 24 | fmainentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_saleconf_s |  | fid |

---

## 关联子实体-子表 t_mpm_saleconf_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_saleconf_lk

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
| 1 | idx_mpm_saleconf_lk_fk |  | fid |
| 2 | pk_mpm_saleconf_lk |  | fpkid |

---

## 项目销售服务确认单-关联追踪表 t_mpm_saleconf_tc

- **表名称：** 项目销售服务确认单-关联追踪表
- **表名：** t_mpm_saleconf_tc

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
| 1 | idx_mpm_saleconf_tc_tbill |  | ftbillid |
| 2 | pk_mpm_saleconf_tc |  | fid |
| 3 | idx_mpm_saleconf_tc_tid |  | ftid |
