# 销售退货申请单-sm_returnapply

## 销售退货申请单-多语言表 t_sm_returnapply_l

- **表名称：** 销售退货申请单-多语言表
- **表名：** t_sm_returnapply_l

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
| 1 | t_sm_returnapply_l_pkey |  | fpkid |
| 2 | idx_t_sm_returnapply_l_fid |  | fid,flocaleid |

---

## 销售退货申请单-分表 t_sm_returnapply_m

- **表名称：** 销售退货申请单-分表
- **表名：** t_sm_returnapply_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fccmexcessamount | 预估信用超标额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标额度 |
| 3 | fccmexcessdays | 预估信用超标天数 | numeric | 23 | 10 | √ | 0 | 预估信用超标天数 |
| 4 | fccmexcessoveramount | 预估信用超标逾期额度 | numeric | 23 | 10 | √ | 0 | 预估信用超标逾期额度 |
| 5 | fccmexcessbillamount | 预估信用超标单笔限额 | numeric | 23 | 10 | √ | 0 | 预估信用超标单笔限额 |
| 6 | fccmupdatetime | 预估信用超标时点 | timestamp | 0 |  |  | null | 预估信用超标时点 |
| 7 | fccmunsettlecount | 信用未结批数 | int4 | 32 |  | √ | 0 | 信用未结批数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_returnapply_m_t |  | fccmupdatetime |
| 2 | pk_sm_returnapply_m |  | fid |

---

## 销售退货申请单-主表 t_sm_returnapply

- **表名称：** 销售退货申请单-主表
- **表名：** t_sm_returnapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 客户联系地址 | varchar | 512 |  |  | null | 客户联系地址 |
| 3 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 9 | fcurtotalamount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | freccustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 13 | fdeliveraddressf7 | 收货地点 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 19 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 20 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 21 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | flinkaddressf7 | 客户联系地址f7 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 23 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fcustomerid | 退货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 28 | foperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 29 | freclinkmanid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 30 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 31 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fpayingcustomerid | 付款客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 33 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 34 | frecconditionid | 收款条件 | int8 | 64 |  | √ | 0 | [收款条件 bd_reccondition](../sbd_files/bd_reccondition.md) |
| 35 | freceiveaddress_bak | 发货明细执行地址(后台用) | varchar | 512 |  | √ | ' ' | 发货明细执行地址(后台用) |
| 36 | funitsrctype | 销售单位来源 | varchar | 30 |  | √ | ' ' | 销售单位来源,枚举: BIZUNIT :默认业务单位 MAINBILLUNIT :核心单据计量单位 |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 39 | foperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fcurtotalallamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 42 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 44 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 45 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 46 | fclosemanual | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 47 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CREDIT :赊销 CASH :现销 |
| 48 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 49 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 50 | fsettlecustomerid | 结算客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 51 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 52 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 53 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 54 | freceiveaddress | 收货地址 | varchar | 512 |  |  | null | 收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_returnapply_pkey |  | fid |
| 2 | idx_sm_returnapply_customer |  | fcustomerid |
| 3 | idx_uniq_returnapply_billnoorg |  | fbillno,forgid |

---

## 销售退货申请单-反写记录表 t_sm_returnnotice_wb

- **表名称：** 销售退货申请单-反写记录表
- **表名：** t_sm_returnnotice_wb

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
| 1 | t_sm_returnnotice_wb_pkey |  | fentryid |
| 2 | idx_sm_returnnotice_wb_fk |  | fid |

---

## 关联子实体-子表 t_sm_returnnoticeentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sm_returnnoticeentry_lk

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
| 1 | t_sm_returnnoticeentry_lk_pkey |  | fpkid |
| 2 | idx_sm_returnnoticeentry_lk_fk |  | fentryid |

---

## 物料明细-子表 t_sm_returnapplyentry

- **表名称：** 物料明细-子表
- **表名：** t_sm_returnapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassociatedbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 3 | ftaildiffstatus | 尾差调整标识 | bpchar | 1 |  | √ | '0' | 尾差调整标识 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 10 | fconfirmqty | 已确认数量(封存) | numeric | 23 | 10 | √ | 0.0000000000 | 已确认数量(封存) |
| 11 | fmatchpricelistid | 行价目表 | int8 | 64 |  | √ | 0 | [销售价目表 sm_salepricelist](../sm_files/sm_salepricelist.md) |
| 12 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 13 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 14 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 15 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 16 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 17 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 20 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 21 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 22 | fqcorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 26 | ftaildifflog | 尾差调整日志 | varchar | 2000 |  | √ | ' ' | 尾差调整日志 |
| 27 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 28 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 29 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 30 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 31 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 32 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 33 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 34 | funitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 35 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 36 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 37 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 38 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | freturntype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 3 :仅退款不退货 |
| 41 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 42 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 43 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 44 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 45 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 46 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 47 | fmaterialinvid | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 48 | fsalesorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 50 | fbaseunitdenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分母 |
| 51 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 52 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 53 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 54 | fmaterialname | 物料名称(历史) | varchar | 800 |  | √ | ' ' | 物料名称(历史) |
| 55 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 56 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 57 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 58 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 59 | fbaseunitnumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 1 | 基本单位用量：分子 |
| 60 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 61 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 62 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 63 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 64 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 65 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 66 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 67 | fconfiguredcodeid | 配置号（废弃） | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 68 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 69 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 70 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 71 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 72 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 73 | freturninspect | 退货检验 | bpchar | 1 |  | √ | '0' | 退货检验 |
| 74 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 75 | fauxunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 76 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 77 | fconbillentryseq | 合同分录序号 | int8 | 64 |  | √ | 0 | 合同分录序号 |
| 78 | fremark | 备注 | varchar | 512 |  |  | null | 备注 |
| 79 | fsuitepricepercent | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 80 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 81 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 82 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 83 | fproducttype | 产品类别 | varchar | 50 |  | √ | 'standard' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 84 | fassociatedqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 85 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 86 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 87 | fconfirmbaseqty | 已确认基本数量(封存) | numeric | 23 | 10 | √ | 0.0000000000 | 已确认基本数量(封存) |
| 88 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 89 | fentryinvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 90 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 91 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 92 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 93 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 94 | fsuitedeliverytype | 套件退货方式 | varchar | 50 |  | √ | ' ' | 套件退货方式,枚举: kitreturn :成套退货 nonkitreturn :非成套退货 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sm_returnapplyentry_pkey |  | fentryid |
| 2 | idx_t_sm_returnapplyentry_id |  | fid |

---

## 销售退货申请单-关联追踪表 t_sm_returnnotice_tc

- **表名称：** 销售退货申请单-关联追踪表
- **表名：** t_sm_returnnotice_tc

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
| 1 | t_sm_returnnotice_tc_pkey |  | fid |
| 2 | idx_sm_returnnotice_tc_tbill |  | ftbillid |
| 3 | idx_sm_returnnotice_tc_tid |  | ftid |

---

## 物料明细-分表 t_sm_returnapplyentry_r

- **表名称：** 物料明细-分表
- **表名：** t_sm_returnapplyentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freturnpassbaseqty | 关联合格退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联合格退货基本数量 |
| 3 | fscrapqty | 报废退货数量 | numeric | 23 | 10 | √ | 0 | 报废退货数量 |
| 4 | ffailqty | 不合格退货数量 | numeric | 23 | 10 | √ | 0 | 不合格退货数量 |
| 5 | freturnfailbaseqty | 关联不合格退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联不合格退货基本数量 |
| 6 | freturnscrapbaseqty | 关联报废退货基本数量 | numeric | 23 | 10 | √ | 0 | 关联报废退货基本数量 |
| 7 | freturnpassqty | 关联合格退货数量 | numeric | 23 | 10 | √ | 0 | 关联合格退货数量 |
| 8 | fassoinvinspectbaseqty | 关联检验基本数量 | numeric | 23 | 10 | √ | 0 | 关联检验基本数量 |
| 9 | freturnfailqty | 关联不合格退货数量 | numeric | 23 | 10 | √ | 0 | 关联不合格退货数量 |
| 10 | fpassbaseqty | 合格退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格退货基本数量 |
| 11 | finspectedbaseqty | 已检验基本数量 | numeric | 23 | 10 | √ | 0 | 已检验基本数量 |
| 12 | fassoinvinspectqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 13 | ffailbaseqty | 不合格退货基本数量 | numeric | 23 | 10 | √ | 0 | 不合格退货基本数量 |
| 14 | fscrapbaseqty | 报废退货基本数量 | numeric | 23 | 10 | √ | 0 | 报废退货基本数量 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | finspectedqty | 已检验数量 | numeric | 23 | 10 | √ | 0 | 已检验数量 |
| 17 | fpassqty | 合格退货数量 | numeric | 23 | 10 | √ | 0 | 合格退货数量 |
| 18 | freturnscrapqty | 关联报废退货数量 | numeric | 23 | 10 | √ | 0 | 关联报废退货数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sm_returnapplyentry_r |  | fentryid |
| 2 | idx_sm_returnapply_e_r_fid |  | fid |
