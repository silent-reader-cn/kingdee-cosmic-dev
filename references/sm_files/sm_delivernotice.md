# 发货通知单-sm_delivernotice

## 物料明细-分表 t_sm_delivernoticeentry_r

- **表名称：** 物料明细-分表
- **表名：** t_sm_delivernoticeentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvfailqty | 关联不合格出库数量 | numeric | 23 | 10 | √ | 0 | 关联不合格出库数量 |
| 3 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 4 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 5 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 6 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 7 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | ffailqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 9 | finvbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库基本数量 |
| 10 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 11 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 12 | fremaininvqty | fremaininvqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 14 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 15 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 16 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 17 | fassoinvinspectbaseqty | 关联请检基本数量 | numeric | 23 | 10 | √ | 0 | 关联请检基本数量 |
| 18 | ffailsaleableqty | 不合格可销售数量 | numeric | 23 | 10 | √ | 0 | 不合格可销售数量 |
| 19 | fpassbaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 20 | fsrcsysbillno | 来源系统单据编号 | varchar | 100 |  | √ | ' ' | 来源系统单据编号 |
| 21 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 22 | fpassqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 23 | fconbillentryseq | 合同分录序号 | int8 | 64 |  | √ | 0 | 合同分录序号 |
| 24 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 25 | finvpassqty | 关联合格出库数量 | numeric | 23 | 10 | √ | 0 | 关联合格出库数量 |
| 26 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | finvqty | 已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库数量 |
| 29 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 30 | fremaininvbaseqty | fremaininvbaseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 32 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 33 | finvpassbaseqty | 关联合格出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联合格出库基本数量 |
| 34 | fsrcsysbillentryid | 来源系统单据分录id | varchar | 100 |  | √ | ' ' | 来源系统单据分录id |
| 35 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 36 | fassoinvinspectqty | 关联请检数量 | numeric | 23 | 10 | √ | 0 | 关联请检数量 |
| 37 | ffailbaseqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0 | 不合格基本数量 |
| 38 | ffailsaleablebaseqty | 不合格可销售基本数量 | numeric | 23 | 10 | √ | 0 | 不合格可销售基本数量 |
| 39 | fscrapbaseqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 41 | fsrcsysbillid | 来源系统单据id | varchar | 100 |  | √ | ' ' | 来源系统单据id |
| 42 | finvfailbaseqty | 关联不合格出库基本数量 | numeric | 23 | 10 | √ | 0 | 关联不合格出库基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_delivernoticeentry_r_pkey |  | fentryid |
| 2 | idx_sm_delientry_r_fid |  | fid |

---

## 发货通知单-关联追踪表 t_sm_delivernotice_tc

- **表名称：** 发货通知单-关联追踪表
- **表名：** t_sm_delivernotice_tc

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
| 1 | idx_sm_delivernotice_tc_tid |  | ftid |
| 2 | t_sm_delivernotice_tc_pkey |  | fid |
| 3 | idx_sm_delivernotice_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_sm_delivernoticeentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_delivernoticeentry_lk

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
| 1 | idx_sm_delivernoticeentry_lk_fk |  | fentryid |
| 2 | t_sm_delivernoticeentry_lk_pkey |  | fpkid |

---

## 发货通知单-主表 t_sm_delivernotice

- **表名称：** 发货通知单-主表
- **表名：** t_sm_delivernotice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 联系地址 | varchar | 512 |  |  | ' ' | 联系地址 |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 6 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 7 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 11 | fterminatestatus | 终止状态 | varchar | 5 |  | √ | ' ' | 终止状态,枚举: A :正常 B :已终止 |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 15 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | fdeliveraddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | 地址 bd_address |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fdeliverpatternid | 交货方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 24 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 25 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 31 | fcustomerid | 订货客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 32 | finvgroupid | 库存组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 33 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 34 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 35 | freclinkmanid | 收货联系人 | int8 | 64 |  | √ | 0 | 客户联系人 bd_customerlinkman |
| 36 | fbiztime | 通知日期 | timestamp | 0 |  |  | null | 通知日期 |
| 37 | fdeliverdeptid | 发货部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fterminaterid | 终止人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fisvirtualbill | 是否虚单 | bpchar | 1 |  | √ | '0' | 是否虚单 |
| 42 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 43 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 44 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 45 | fdeliveroperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 46 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | 收款条件 bd_reccondition |
| 47 | freceiveaddress_bak | 发货明细执行地址(后台用) | varchar | 512 |  | √ | ' ' | 发货明细执行地址(后台用) |
| 48 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fispayrate | fispayrate | bpchar | 1 |  | √ | '1' |  |
| 51 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 54 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 55 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 57 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 58 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 59 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 60 | fclosemanual | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 61 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 62 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 63 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 64 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 65 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 66 | freceiveaddress | 收货地址 | varchar | 512 |  |  | ' ' | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delinotice_fbiztime |  | fbiztime |
| 2 | idx_sm_delinotice_customer |  | fcustomerid |
| 3 | t_sm_delivernotice_pkey |  | fid |
| 4 | idx_uniq_delinotice_billnoorg |  | fbillno,fdeliverorgid |
| 5 | idx_sm_delinotice_forgid |  | forgid,fbiztime,fbillno,fid |

---

## 发货通知单-反写记录表 t_sm_delivernotice_wb

- **表名称：** 发货通知单-反写记录表
- **表名：** t_sm_delivernotice_wb

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
| 1 | idx_sm_delivernotice_wb_fk |  | fid |
| 2 | t_sm_delivernotice_wb_pkey |  | fentryid |

---

## 物料明细-子表 t_sm_delivernoticeentry

- **表名称：** 物料明细-子表
- **表名：** t_sm_delivernoticeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeliverrateup | 发货超发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货超发比率(%) |
| 3 | fexpectqtydate | 获取可发量日期 | timestamp | 0 |  |  | null | 获取可发量日期 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '0' | 控制发货数量 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdeliverratedown | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货欠发比率(%) |
| 10 | fmatchpricelistid | 行价目表 | int8 | 64 |  | √ | 0 | 销售价目表 sm_salepricelist |
| 11 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 12 | fdeliverbaseqtyup | 发货上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限基本数量 |
| 13 | frowstatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 14 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 17 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 21 | fexpectqty | 预计可发量 | numeric | 23 | 10 | √ | 0 | 预计可发量 |
| 22 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 23 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 24 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 27 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 31 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 32 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fqtyunit2nd | 主辅数量 | numeric | 23 | 10 | √ | 0.0000000000 | 主辅数量 |
| 34 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 35 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 36 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 37 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 38 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 39 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 41 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 42 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 43 | fdeliverorgid | 发货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | 客户物料对应表明细信息 bd_customermaterialinfo |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 47 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 48 | frowclosemanual | 行手工关闭 | bpchar | 1 |  | √ | '0' | 行手工关闭 |
| 49 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 51 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 52 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 53 | funit2ndid | 主辅单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 54 | funit2ndrate | 换算率(主辅单位) | numeric | 23 | 10 | √ | 0.0000000000 | 换算率(主辅单位) |
| 55 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 56 | fdeliverqtyup | 发货上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货上限数量 |
| 57 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 58 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 59 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 60 | frowclosemanualever | 是否手工行关闭过 | bpchar | 1 |  | √ | '0' | 是否手工行关闭过 |
| 61 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 62 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 64 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 65 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 66 | fdeliverbaseqtydown | 发货下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限基本数量 |
| 67 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 68 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 69 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 70 | fcloseupdatesaleorder | 手工关闭更新订单 | bpchar | 1 |  | √ | '0' | 手工关闭更新订单 |
| 71 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 72 | fdeliverydate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 73 | fproducttype | 产品类别 | varchar | 50 |  | √ | 'standard' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 74 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 75 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 76 | fdeliverqtydown | 发货下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 发货下限数量 |
| 77 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 78 | fdeliverinspect | 发货检验 | bpchar | 1 |  | √ | '0' | 发货检验 |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 80 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 81 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 82 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_delientry_fownerid |  | fownerid |
| 2 | idx_sm_delientry_matid |  | fmaterialid,fid |
| 3 | t_sm_delivernoticeentry_pkey |  | fentryid |
| 4 | idx_sm_delientry_matmasterid |  | fmaterialmasterid,fid |
| 5 | idx_sm_delientry_fid |  | fid |

---

## 发货通知单-多语言表 t_sm_delivernotice_l

- **表名称：** 发货通知单-多语言表
- **表名：** t_sm_delivernotice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_delivernotice_l_pkey |  | fpkid |
| 2 | idx_sm_delinotice_l_fid |  | fid,flocaleid |
