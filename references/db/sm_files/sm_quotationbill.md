# 销售报价单-sm_quotationbill

## 销售报价单-主表 t_sm_quotationbill

- **表名称：** 销售报价单-主表
- **表名：** t_sm_quotationbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 512 |  |  | null | 联系地址 |
| 3 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 10 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 11 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 14 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 15 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 16 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 23 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 26 | fdeliverpatternid | 交货方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 27 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 32 | fbizdate | 报价日期 | timestamp | 0 |  |  | null | 报价日期 |
| 33 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 34 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 35 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 36 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 37 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 40 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 43 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_uniq_quotion_billnoorg |  | fbillno,forgid |
| 2 | pk_t_sm_quotationbill |  | fid |

---

## 关联子实体-子表 t_sm_quotationentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_quotationentry_lk

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
| 1 | pk_sm_quotationentry_lk |  | fpkid |
| 2 | idx_sm_quotationentry_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_sm_quotationbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_quotationbill_lk

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
| 1 | pk_sm_quotationbill_lk |  | fpkid |
| 2 | idx_sm_quotationbill_lk_fk |  | fid |

---

## 销售报价单-关联追踪表 t_sm_quotationbill_tc

- **表名称：** 销售报价单-关联追踪表
- **表名：** t_sm_quotationbill_tc

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
| 1 | pk_sm_quotationbill_tc |  | fid |
| 2 | idx_sm_quotationbill_tc_tbill |  | ftbillid |
| 3 | idx_sm_quotationbill_tc_tid |  | ftid |

---

## 销售报价单-反写记录表 t_sm_quotationbill_wb

- **表名称：** 销售报价单-反写记录表
- **表名：** t_sm_quotationbill_wb

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
| 1 | idx_sm_quotationbill_wb_fk |  | fid |
| 2 | pk_sm_quotationbill_wb |  | fentryid |

---

## 物料明细-子表 t_sm_quotationentry

- **表名称：** 物料明细-子表
- **表名：** t_sm_quotationentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料销售信息 bd_materialsalinfo |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmatchpricelistid | 行价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 11 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 12 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 16 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 17 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 21 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 23 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 24 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 25 | fdelivdays | 交货天数 | int8 | 64 |  | √ | 0 | 交货天数 |
| 26 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 27 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_quotionentry_fid |  | fid |
| 2 | pk_t_sm_quotationentry |  | fentryid |
