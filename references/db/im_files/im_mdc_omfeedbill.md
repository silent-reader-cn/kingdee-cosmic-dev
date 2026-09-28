# 委外补料单-im_mdc_omfeedbill

## 关联子实体-子表 t_im_mdc_omoutbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mdc_omoutbillentry_lk

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
| 1 | pk_im_mdc_omoutbillentry_lk |  | fpkid |
| 2 | idx_im_mdc_omoutbillentry_lk_fk |  | fentryid |

---

## 委外补料单-多语言表 t_im_mdc_omoutbill_l

- **表名称：** 委外补料单-多语言表
- **表名：** t_im_mdc_omoutbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 521 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omoutbill_l |  | fpkid |
| 2 | idx_im_mdc_omoutbill_l |  | fid,flocaleid |

---

## 委外补料单-分表 t_im_mdc_omoutbill_m

- **表名称：** 委外补料单-分表
- **表名：** t_im_mdc_omoutbill_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fneedtime | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 3 | fworkshopid | 车间ID | int8 | 64 |  | √ | 0 | 车间ID |
| 4 | fdoctype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: A :委外领料 |
| 5 | fworkshop | 车间 | varchar | 50 |  | √ | ' ' | 车间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omoutbill_m |  | fid |
| 2 | idx_im_mdc_omoutbill_m |  | fdoctype |

---

## 委外补料单-关联追踪表 t_im_mdc_omoutbill_tc

- **表名称：** 委外补料单-关联追踪表
- **表名：** t_im_mdc_omoutbill_tc

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
| 1 | idx_im_mdc_omoutbill_tc_tbill |  | ftbillid |
| 2 | pk_im_mdc_omoutbill_tc |  | fid |
| 3 | idx_im_mdc_omoutbill_tc_tid |  | ftid |

---

## 委外补料单-反写记录表 t_im_mdc_omoutbill_wb

- **表名称：** 委外补料单-反写记录表
- **表名：** t_im_mdc_omoutbill_wb

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
| 1 | pk_im_mdc_omoutbill_wb |  | fentryid |
| 2 | idx_im_mdc_omoutbill_wb_fk |  | fid |

---

## 委外补料单-主表 t_im_mdc_omoutbill

- **表名称：** 委外补料单-主表
- **表名：** t_im_mdc_omoutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequserid | 领用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsupplyowner | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 7 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fischargeoff | 冲销 | bpchar | 1 |  | √ | ' ' | 冲销 |
| 12 | finnerbilltype | 内部交易单据类别 | varchar | 50 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 13 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 14 | fsupplier | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbizorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fasyncstatus | 异步状态 | varchar | 50 |  | √ | ' ' | 异步状态,枚举: A :处理中 B :已完成 |
| 18 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | ' ' | 内部交易单据 |
| 19 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 20 | fcostcenterorg | 成本中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fsupplyownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | ' ' | 已被冲销 |
| 26 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 30 | fsettlecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 33 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fisbackflush | 倒冲 | bpchar | 1 |  | √ | '0' | 倒冲 |
| 35 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 36 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 37 | fsettleorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 39 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 40 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 41 | fbizdeptid | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_omoutbill_bizorg |  | fbizorgid |
| 2 | pk_t_im_mdc_omoutbill |  | fid |
| 3 | idx_im_mdc_omoutbil |  | fbillno,forgid |

---

## 物料明细-分表 t_im_mdc_omoutbillentry_m

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_omoutbillentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscrappedbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 3 | fmanubillid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 4 | fmanuentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 5 | fiscannegative | fiscannegative | bpchar | 1 |  | √ | '0' |  |
| 6 | fproductmasterid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | favbinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 8 | fprodunitqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 9 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 10 | fprodunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | fnotupdateunclaimed | fnotupdateunclaimed | bpchar | 1 |  | √ | '0' |  |
| 13 | fisadd | 是否新增行 | bpchar | 1 |  | √ | '0' | 是否新增行 |
| 14 | fmanubill | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 15 | fcansendqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 16 | favbinvqty | 可用库存数量 | numeric | 23 | 10 | √ | 0 | 可用库存数量 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fmanuentry | 委外工单行编号 | varchar | 50 |  | √ | ' ' | 委外工单行编号 |
| 19 | fscrappedqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 20 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_omoutbillentry_m |  | fid |
| 2 | pk_t_im_mdc_omoutbillentry_m |  | fentryid |
| 3 | idx_omoutbillentry_m_meid |  | fmanuentryid |

---

## 物料明细-分表 t_im_mdc_omoutbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_omoutbillentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
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
| 1 | idx_im_mdc_omoutentry_c_fid |  | fid |
| 2 | pk_im_mdc_omoutentry_c |  | fentryid |

---

## 物料明细-分表 t_im_mdc_omoutbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_omoutbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 3 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | ' ' | 跨组织业务 |
| 4 | fmainbillentryseq | 核心单据分录序号 | int4 | 32 |  | √ | 0 | 核心单据分录序号 |
| 5 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 6 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0 | 已退库基本数量 |
| 7 | fvmisettleqty | VMI已结算数量 | numeric | 23 | 10 | √ | 0 | VMI已结算数量 |
| 8 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 9 | fremainpurqty | 未转固数量 | numeric | 23 | 10 | √ | 0 | 未转固数量 |
| 10 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 11 | fremainreturnbaseqty | 未退库基本数量 | numeric | 23 | 10 | √ | 0 | 未退库基本数量 |
| 12 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 13 | fvmiremainsettleqty | VMI剩余结算数量 | numeric | 23 | 10 | √ | 0 | VMI剩余结算数量 |
| 14 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 15 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 16 | fvmisettlebaseqty | VMI已结算基本数量 | numeric | 23 | 10 | √ | 0 | VMI已结算基本数量 |
| 17 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 18 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0 | 已退库数量 |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fpurchasedqty | 已转固数量 | numeric | 23 | 10 | √ | 0 | 已转固数量 |
| 21 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 22 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 23 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 24 | fvmiremainsettlebaseqty | VMI剩余结算基本数量 | numeric | 23 | 10 | √ | 0 | VMI剩余结算基本数量 |
| 25 | fpurchasedamount | 已转固金额 | numeric | 23 | 10 | √ | 0 | 已转固金额 |
| 26 | fremainpuramount | 未转固金额 | numeric | 23 | 10 | √ | 0 | 未转固金额 |
| 27 | fremainreturnqty | 未退库数量 | numeric | 23 | 10 | √ | 0 | 未退库数量 |
| 28 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omoutbillentry_r |  | fentryid |
| 2 | idx_im_mdc_omoutbillentry_r |  | fid |

---

## 物料明细-子表 t_im_mdc_omoutbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_mdc_omoutbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 1 :是 0 :否 |
| 3 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 4 | fbasequantity | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 255 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fisrework | 返工 | bpchar | 1 |  | √ | ' ' | 返工 |
| 10 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 11 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 12 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 17 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 23 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 24 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 25 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 26 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 27 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 29 | foperationdesc | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 30 | freturnmaterialtype | freturnmaterialtype | bpchar | 1 |  | √ | 'A' |  |
| 31 | fproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | ffeereasonid | 补料原因 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 33 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 36 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 37 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 38 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 39 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 40 | fprdownerid | 产品货主（废弃） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 42 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 43 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 44 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 45 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 46 | foutkeepertype | 出库保管者类型 | varchar | 50 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 47 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 48 | fworkprocedureid | 工序名称 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 49 | fsettlerouteid | 结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 50 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 51 | fquantity | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 52 | foutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 53 | fprdownertype | 产品货主类型（废弃） | varchar | 30 |  | √ | ' ' | 产品货主类型（废弃）,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 54 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 55 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 56 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 57 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 58 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 59 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 60 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 61 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 62 | fisfreegift | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omoutbillentry |  | fentryid |
| 2 | idx_im_mdc_omoutbillentry |  | fid,fseq |

---

## 关联子实体-子表 t_im_mdc_omoutbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mdc_omoutbill_lk

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
| 1 | idx_im_mdc_omoutbill_lk_fk |  | fid |
| 2 | pk_im_mdc_omoutbill_lk |  | fpkid |
