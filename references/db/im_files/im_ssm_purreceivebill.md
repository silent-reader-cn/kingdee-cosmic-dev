# 滚动采购收料通知单-im_ssm_purreceivebill

## 滚动采购收料通知单-反写记录表 t_im_ssm_purreceivebill_wb

- **表名称：** 滚动采购收料通知单-反写记录表
- **表名：** t_im_ssm_purreceivebill_wb

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
| 1 | pk_im_ssm_purreceivebill_wb |  | fentryid |
| 2 | idx_im_ssm_purreceivebill_wb_fk |  | fid |

---

## 滚动采购收料通知单-关联追踪表 t_im_ssm_purreceivebill_tc

- **表名称：** 滚动采购收料通知单-关联追踪表
- **表名：** t_im_ssm_purreceivebill_tc

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
| 1 | idx_im_ssm_purreceivebill_tc_tid |  | ftid |
| 2 | pk_im_ssm_purreceivebill_tc |  | fid |
| 3 | idx_im_ssm_purreceivebill_tc_tbill |  | ftbillid |

---

## 物料明细-多语言表 t_im_ssm_purrecbillentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_im_ssm_purrecbillentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprovideraddress | 供货地址 | varchar | 455 |  | √ | ' ' | 供货地址 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_ssm_purrecbillentry_l_0 |  | fentryid,flocaleid |
| 2 | pk_im_ssm_purrecbillentry_l |  | fpkid |

---

## 物料明细-分表 t_im_ssm_purrecbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_ssm_purrecbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconcessionqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fjoinrejectdiscountamount | 关联不良品折让金额 | numeric | 23 | 10 | √ | 0 | 关联不良品折让金额 |
| 6 | ftotalreturnqty | 合格已退货数量 | numeric | 23 | 10 | √ | 0 | 合格已退货数量 |
| 7 | fconcessionbaseqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 8 | fdamagebaseqty | 采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 采购损耗基本数量 |
| 9 | ftotalreturnbaseqty | 合格已退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格已退货基本数量 |
| 10 | fremaininvqty | 未入库数量 | numeric | 23 | 10 | √ | 0 | 未入库数量 |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fleftinspqty | 未送检数量 | numeric | 23 | 10 | √ | 0 | 未送检数量 |
| 13 | fremainreturnbaseqty | 合格未退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格未退货基本数量 |
| 14 | frejectdiscountamount | 不良品折让金额 | numeric | 23 | 10 | √ | 0 | 不良品折让金额 |
| 15 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 17 | fleftinspbaseqty | 未送检基本数量 | numeric | 23 | 10 | √ | 0 | 未送检基本数量 |
| 18 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 19 | funqualifiedqty | 不合格数量 | numeric | 23 | 10 | √ | 0 | 不合格数量 |
| 20 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 21 | fleftunqualreturnbaseqty | 不合格未退货基本数量 | numeric | 23 | 10 | √ | 0 | 不合格未退货基本数量 |
| 22 | fleftunqualreturnqty | 不合格未退货数量 | numeric | 23 | 10 | √ | 0 | 不合格未退货数量 |
| 23 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 24 | fqualifiedbaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 25 | ftotalunqualreturnqty | 不合格已退货数量 | numeric | 23 | 10 | √ | 0 | 不合格已退货数量 |
| 26 | funqualifiedbaseqty | 不合格基本数量 | numeric | 23 | 10 | √ | 0 | 不合格基本数量 |
| 27 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 28 | fremaininvbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0 | 未入库基本数量 |
| 29 | ftotalinspbaseqty | 已送检基本数量 | numeric | 23 | 10 | √ | 0 | 已送检基本数量 |
| 30 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 31 | ftotalunqualreturnbaseqty | 不合格已退货基本数量 | numeric | 23 | 10 | √ | 0 | 不合格已退货基本数量 |
| 32 | fremainreturnqty | 合格未退货数量 | numeric | 23 | 10 | √ | 0 | 合格未退货数量 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 34 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_ssm_purrecbillentry_r |  | fentryid |
| 2 | idx_im_ssm_purentry_r_fk |  | fid |

---

## 滚动采购收料通知单-主表 t_im_ssm_purreceivebill

- **表名称：** 滚动采购收料通知单-主表
- **表名：** t_im_ssm_purreceivebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 6 | fexchangemethod | fexchangemethod | varchar | 50 |  | √ | ' ' |  |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fbizoperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 12 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 13 | fquotation | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 17 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fsupplierouttime | 供应商出库日期 | timestamp | 0 |  |  | null | 供应商出库日期 |
| 22 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 28 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 30 | fbizoperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 33 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 34 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 35 | fclosestatus | 关闭状态 | varchar | 50 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 36 | fpaymode | 付款方式 | varchar | 50 |  | √ | ' ' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 37 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 38 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 39 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 40 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 41 | fplanreceipttime | 预计收货日期 | timestamp | 0 |  |  | null | 预计收货日期 |
| 42 | fbizdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_ssm_purreceivebill |  | fid |
| 2 | idx_im_ssm_purreceivebill_m0 |  | fbillno |

---

## 滚动采购收料通知单-多语言表 t_im_ssm_purreceivebill_l

- **表名称：** 滚动采购收料通知单-多语言表
- **表名：** t_im_ssm_purreceivebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 770 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_ssm_purreceivebill_l_0 |  | fid,flocaleid |
| 2 | pk_im_ssm_purreceivebill_l |  | fpkid |

---

## 关联子实体-子表 t_im_ssm_purrecbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_ssm_purrecbillentry_lk

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
| 1 | idx_im_ssm_purrecbillentry_lk_fk |  | fentryid |
| 2 | pk_im_ssm_purrecbillentry_lk |  | fpkid |

---

## 物料明细-子表 t_im_ssm_purrecbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_ssm_purrecbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 单位折扣(率) | numeric | 23 | 6 | √ | 0 | 单位折扣(率) |
| 3 | ftaxrate | 税率% | numeric | 23 | 2 | √ | 0 | 税率% |
| 4 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 7 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fjoinstockdamageqty | 关联入库采购损耗数量 | numeric | 23 | 10 | √ | 0 | 关联入库采购损耗数量 |
| 11 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 13 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 14 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 15 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 16 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 17 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 19 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 24 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fbaseprice | 基本单价 | numeric | 23 | 10 | √ | 0 | 基本单价 |
| 26 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 28 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 30 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 31 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 32 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fjoinstockdamagebaseqty | 关联入库采购损耗基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库采购损耗基本数量 |
| 34 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 35 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 36 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 37 | fisinspect | 来料检验 | bpchar | 1 |  | √ | '0' | 来料检验 |
| 38 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 39 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 40 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 41 | fmaterialmaster | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 42 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 43 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fqtyunit2nd | 收货数量(辅助) | numeric | 23 | 10 | √ | 0 | 收货数量(辅助) |
| 45 | freturntype | 退货类型 | varchar | 50 |  | √ | ' ' | 退货类型,枚举: A :合格退货 B :不合格退货 |
| 46 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 47 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 48 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 49 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 50 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 51 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 52 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 53 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 54 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 55 | frowclosestatus | 行关闭状态 | varchar | 50 |  |  | null | 行关闭状态,枚举: A :正常 B :已关闭 |
| 56 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 57 | fconbillentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 58 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 59 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 60 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 61 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 62 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 63 | famount | 暂估金额 | numeric | 23 | 10 | √ | 0 | 暂估金额 |
| 64 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 65 | foutkeepertype | 出库保管者类型 | varchar | 50 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 66 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 67 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 68 | fprovideraddress | 供货地址 | varchar | 300 |  | √ | ' ' | 供货地址 |
| 69 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 70 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 71 | fjoininvqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 72 | foutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 73 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 74 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 75 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 76 | fprovidersupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 77 | ftotalinspqty | 已送检数量 | numeric | 23 | 10 | √ | 0 | 已送检数量 |
| 78 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 79 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 80 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 81 | fjoininvbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 82 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 83 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 84 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 85 | fdamageqty | 采购损耗数量 | numeric | 23 | 10 | √ | 0 | 采购损耗数量 |
| 86 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 87 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 88 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_ssm_purrecbillentry |  | fentryid |
| 2 | idx_im_ssm_purrecbillentry_fk |  | fid |
