# 销售签收单-im_salreceiptbill

## 销售签收单-多语言表 t_im_salreceiptbill_l

- **表名称：** 销售签收单-多语言表
- **表名：** t_im_salreceiptbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 770 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | freceiveaddress | 客户收货地址 | varchar | 455 |  | √ | ' ' | 客户收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_salreceiptbill_l |  | fpkid |
| 2 | idx_im_salreceiptbill_l_0 |  | fid,flocaleid |

---

## 物料明细-分表 t_im_salreceiptbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_salreceiptbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 4 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |
| 12 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_receiptentry_r_fk |  | fid |
| 2 | pk_im_salreceiptbillentry_r |  | fentryid |

---

## 物料明细-分表 t_im_salreceiptbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_salreceiptbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_salreceiptbillentry_c |  | fentryid |
| 2 | idx_im_salreceiptentry_c_fk |  | fid |

---

## 关联子实体-子表 t_im_receiptentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_receiptentry_lk

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
| 1 | idx_im_receiptentry_lk_fk |  | fentryid |
| 2 | pk_im_receiptentry_lk |  | fpkid |

---

## 销售签收单-主表 t_im_salreceiptbill

- **表名称：** 销售签收单-主表
- **表名：** t_im_salreceiptbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freceipttype | 签收类型 | varchar | 50 |  | √ | ' ' | 签收类型,枚举: fullorder :整单签收 details :明细签收 |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbiztime | 签收日期 | timestamp | 0 |  |  | null | 签收日期 |
| 6 | fbizoperatorid | 销售员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbizorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 12 | fdeliveraddressf7 | 客户收货地点 | int8 | 64 |  | √ | 0 | [地址 bd_address](../basedata_files/bd_address.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 20 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 24 | fbizoperatorgroupid | 销售组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | freceivecontactphone | 收货联系人电话 | varchar | 50 |  | √ | ' ' | 收货联系人电话 |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | freceivecontactid | 收货联系人 | int8 | 64 |  | √ | 0 | [客户联系人 bd_customerlinkman](../sbd_files/bd_customerlinkman.md) |
| 29 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 30 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 31 | fbizdeptid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fcustomerid | 收货客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 34 | freceiveaddress | 客户收货地址 | varchar | 300 |  | √ | ' ' | 客户收货地址 |
| 35 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_salreceiptbill_m0 |  | fbillno |
| 2 | pk_im_salreceiptbill |  | fid |

---

## 关联子实体-子表 t_im_receipt_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_receipt_lk

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
| 1 | pk_im_receipt_lk |  | fpkid |
| 2 | idx_im_receipt_lk_fk |  | fid |

---

## 销售签收单-关联追踪表 t_im_receipt_tc

- **表名称：** 销售签收单-关联追踪表
- **表名：** t_im_receipt_tc

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
| 1 | idx_im_receipt_tc_tid |  | ftid |
| 2 | idx_im_receipt_tc_tbill |  | ftbillid |
| 3 | pk_im_receipt_tc |  | fid |

---

## 销售签收单-反写记录表 t_im_receipt_wb

- **表名称：** 销售签收单-反写记录表
- **表名：** t_im_receipt_wb

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
| 1 | idx_im_receipt_wb_fk |  | fid |
| 2 | pk_im_receipt_wb |  | fentryid |

---

## 物料明细-子表 t_im_salreceiptbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_salreceiptbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flossexecbaseqty | 途损已执行数量(基本) | numeric | 23 | 10 | √ | 0 | 途损已执行数量(基本) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | finternalparty | 内部责任方 | varchar | 50 |  | √ | ' ' | 内部责任方,枚举: entrysettleorg :结算组织 outowner :出库货主 |
| 4 | flossexecqty | 途损已执行数量 | numeric | 23 | 10 | √ | 0 | 途损已执行数量 |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | freturnbaseqty | 已退货数量(基本) | numeric | 23 | 10 | √ | 0 | 已退货数量(基本) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcarrier | 承运商 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 12 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | foverqty | 多签数量 | numeric | 23 | 10 | √ | 0 | 多签数量 |
| 14 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 15 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 16 | fgroupseq | 成组行号 | varchar | 50 |  | √ | ' ' | 成组行号 |
| 17 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 18 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | foverqtyunit2nd | 多签辅助数量 | numeric | 23 | 10 | √ | 0 | 多签辅助数量 |
| 20 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fdeliveryqtyunit2nd | 交货辅助数量 | numeric | 23 | 10 | √ | 0 | 交货辅助数量 |
| 23 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fqty | 签收数量 | numeric | 23 | 10 | √ | 0 | 签收数量 |
| 26 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 27 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 29 | funitid | 签收单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 31 | flossreturntype | 途损退货类型 | varchar | 50 |  | √ | ' ' | 途损退货类型,枚举: 1 :退货 2 :退补货 |
| 32 | flossqtyunit2nd | 途损辅助数量 | numeric | 23 | 10 | √ | 0 | 途损辅助数量 |
| 33 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 34 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 35 | flosshandle | 途损处理方式 | varchar | 50 |  | √ | ' ' | 途损处理方式,枚举: transferoutother :转其他出库 resell3rdparty :转售第三方 |
| 36 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 37 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 38 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 39 | flossbaseqty | 途损数量(基本) | numeric | 23 | 10 | √ | 0 | 途损数量(基本) |
| 40 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fqtyunit2nd | 签收辅助数量 | numeric | 23 | 10 | √ | 0 | 签收辅助数量 |
| 42 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 43 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 44 | flossparty | 途损责任方 | varchar | 50 |  | √ | ' ' | 途损责任方,枚举: seller :卖方承担 buyer :买方承担 carrier :承运方承担 |
| 45 | fisnotupdate | 不更新库存 | bpchar | 1 |  | √ | '0' | 不更新库存 |
| 46 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 47 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 48 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 49 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 50 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 51 | flossqty | 途损数量 | numeric | 23 | 10 | √ | 0 | 途损数量 |
| 52 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 53 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 54 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 55 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 56 | fgroupnumber | 成组号 | varchar | 50 |  | √ | ' ' | 成组号 |
| 57 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 58 | foutkeepertype | 出库保管者类型 | varchar | 50 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 59 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 60 | foverqtyunit3rd | 多签辅助数量(2) | numeric | 23 | 10 | √ | 0 | 多签辅助数量(2) |
| 61 | fdeliveryqty | 交货数量 | numeric | 23 | 10 | √ | 0 | 交货数量 |
| 62 | fdeliveryqtyunit3rd | 交货辅助数量(2) | numeric | 23 | 10 | √ | 0 | 交货辅助数量(2) |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 64 | fdeliverybaseqty | 交货数量(基本) | numeric | 23 | 10 | √ | 0 | 交货数量(基本) |
| 65 | foutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 66 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 67 | freturnqty | 已退货数量 | numeric | 23 | 10 | √ | 0 | 已退货数量 |
| 68 | flossqtyunit3rd | 途损辅助数量(2) | numeric | 23 | 10 | √ | 0 | 途损辅助数量(2) |
| 69 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 70 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 71 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 72 | fqtyunit3rd | 签收辅助数量(2) | numeric | 23 | 10 | √ | 0 | 签收辅助数量(2) |
| 73 | foverbaseqty | 多签数量(基本) | numeric | 23 | 10 | √ | 0 | 多签数量(基本) |
| 74 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 75 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 76 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 77 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 78 | fbaseqty | 签收数量(基本) | numeric | 23 | 10 | √ | 0 | 签收数量(基本) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_receiptentry_fk |  | fid |
| 2 | pk_im_salreceiptbillentry |  | fentryid |
