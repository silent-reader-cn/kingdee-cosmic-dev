# 取样出库单-im_sampoutbill

## 取样出库单-主表 t_im_sampoutbill

- **表名称：** 取样出库单-主表
- **表名：** t_im_sampoutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbizoperatorid | 取样员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 8 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbizorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 12 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 17 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbillstatus | 单据状态 | varchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcomment | 备注 | varchar | 1536 |  | √ | ' ' | 备注 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 25 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 26 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fisvoucher | 已生成凭证 | varchar | 1 |  | √ | '0' | 已生成凭证 |
| 29 | fbizdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sampoutbill_fbillno |  | fbillno |
| 2 | pk_t_im_sampoutbill |  | fid |

---

## 取样出库单-多语言表 t_im_sampoutbill_l

- **表名称：** 取样出库单-多语言表
- **表名：** t_im_sampoutbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 1536 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sampoutbill_l_fid |  | flocaleid,fid |
| 2 | pk_t_im_sampoutbill_l |  | fpkid |

---

## 物料明细-子表 t_im_sampoutbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_sampoutbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 3 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 10 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 11 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fcostcurrency | 成本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fqty | 来源单据下推数量 | numeric | 23 | 10 | √ | 0 | 来源单据下推数量 |
| 17 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | funitid | 取样单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fsettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 24 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 25 | fcostaccount | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 26 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 27 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 29 | fproductionorg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 33 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 34 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 35 | fsamplingqty | 取样数量 | numeric | 23 | 10 | √ | 0 | 取样数量 |
| 36 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 37 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 38 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 39 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 40 | foutkeepertype | 出库保管者类型 | varchar | 50 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 41 | fbonded | 保税 | varchar | 1 |  | √ | ' ' | 保税 |
| 42 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 43 | fsamplingbaseqty | 取样基本数量 | numeric | 23 | 10 | √ | 0 | 取样基本数量 |
| 44 | foutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 45 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 46 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 47 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 48 | fentrycomment | 备注 | varchar | 1536 |  | √ | ' ' | 备注 |
| 49 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 50 | fbaseqty | 来源单据下推基本数量 | numeric | 23 | 10 | √ | 0 | 来源单据下推基本数量 |
| 51 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sampoutbillentry_fseq |  | fseq |
| 2 | idx_im_sampoutbill_fmaterialid |  | fmaterialid |
| 3 | idx_im_sampoutbillentry_fid |  | fid |
| 4 | pk_t_im_sampoutbillentry |  | fentryid |

---

## 关联子实体-子表 t_im_sampoutbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_sampoutbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 来源单据下推基本数量_原始携带值 | numeric | 23 | 10 |  | null | 来源单据下推基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 来源单据下推基本数量_确认携带值 | numeric | 23 | 10 |  | null | 来源单据下推基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sampoutbillentry_lk_fk |  | fentryid |
| 2 | pk_im_sampoutbillentry_lk |  | fpkid |

---

## 物料明细-分表 t_im_sampoutbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_sampoutbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | varchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fmainbillentryseq | 核心单据分录序号 | int4 | 32 |  | √ | 0 | 核心单据分录序号 |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 8 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 9 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 13 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 15 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sampoutentry_r_fid |  | fid |
| 2 | pk_t_im_sampoutbillentry_r |  | fentryid |

---

## 物料明细-分表 t_im_sampoutbillentry_s

- **表名称：** 物料明细-分表
- **表名：** t_im_sampoutbillentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsamplingplan | 取样方案 | int8 | 64 |  | √ | 0 | [取样方案 bd_samplingplan](../basedata_files/bd_samplingplan.md) |
| 3 | fsamplingplanrowid | 取样方案分录id | int8 | 64 |  | √ | 0 | 取样方案分录id |
| 4 | fsamplingloc | 取样位置 | varchar | 50 |  | √ | ' ' | 取样位置 |
| 5 | fsamplenum | 样本份数 | int4 | 32 |  | √ | 0 | 样本份数 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_sampoutentry_s_fid |  | fid |
| 2 | pk_t_im_sampoutbillentry_s |  | fentryid |

---

## 样品信息-多语言表 t_im_subentryentity_l

- **表名称：** 样品信息-多语言表
- **表名：** t_im_subentryentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsampleno | 样品编号 | varchar | 150 |  | √ | ' ' | 样品编号 |
| 2 | fsamplename | 样品名称 | varchar | 150 |  | √ | ' ' | 样品名称 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |
| 6 | fsamplcomment | 备注 | varchar | 765 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_subentryentity_l |  | fpkid |
| 2 | idx_im_subentryl_fdetailid |  | fdetailid,flocaleid |

---

## 关联子实体-子表 t_im_sampoutbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_sampoutbill_lk

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
| 1 | pk_im_sampoutbill_lk |  | fpkid |
| 2 | idx_im_sampoutbill_lk_fk |  | fid |

---

## 取样出库单-关联追踪表 t_im_sampoutbill_tc

- **表名称：** 取样出库单-关联追踪表
- **表名：** t_im_sampoutbill_tc

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
| 1 | idx_im_sampoutbill_tc_tbill |  | ftbillid |
| 2 | idx_im_sampoutbill_tc_tid |  | ftid |
| 3 | pk_im_sampoutbill_tc |  | fid |

---

## 取样出库单-反写记录表 t_im_sampoutbill_wb

- **表名称：** 取样出库单-反写记录表
- **表名：** t_im_sampoutbill_wb

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
| 1 | idx_im_sampoutbill_wb_fk |  | fid |
| 2 | pk_im_sampoutbill_wb |  | fentryid |

---

## 样品信息-子表 t_im_subentryentity

- **表名称：** 样品信息-子表
- **表名：** t_im_subentryentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fretentionperiod | 留存期限 | int4 | 32 |  | √ | 0 | 留存期限 |
| 2 | fsamplerecjoinqty | 关联样品记录数量 | numeric | 23 | 10 | √ | 0 | 关联样品记录数量 |
| 3 | fsamplestorageloc | 留样位置 | varchar | 50 |  | √ | ' ' | 留样位置 |
| 4 | fsamplename | 样品名称 | varchar | 50 |  | √ | ' ' | 样品名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsamplerecqty | 样品记录数量 | numeric | 23 | 10 | √ | 0 | 样品记录数量 |
| 7 | fsamplestartdate | 留样开始计算日期 | varchar | 1 |  | √ | ' ' | 留样开始计算日期,枚举: A :生产日期 B :样品生成日期 |
| 8 | fsampleusage | 样品用途 | varchar | 50 |  | √ | ' ' | 样品用途 |
| 9 | fsamplcomment | 备注 | varchar | 765 |  | √ | ' ' | 备注 |
| 10 | fsamrecbaseqty | 样品记录基本数量 | numeric | 23 | 10 | √ | 0 | 样品记录基本数量 |
| 11 | fsampleno | 样品编号 | varchar | 50 |  | √ | ' ' | 样品编号 |
| 12 | fsamrecjoinbaseqty | 关联样品记录基本数量 | numeric | 23 | 10 | √ | 0 | 关联样品记录基本数量 |
| 13 | fsamplbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fsamplebaseqty | 样品基本数量 | numeric | 23 | 10 | √ | 0 | 样品基本数量 |
| 15 | fsamplunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fobscount | 预计观察次数 | int4 | 32 |  | √ | 0 | 预计观察次数 |
| 17 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 18 | fsampleform | 样品形态 | varchar | 50 |  | √ | ' ' | 样品形态 |
| 19 | fsubmaterial | 样品物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 20 | fsampleqty | 样品数量 | numeric | 23 | 10 | √ | 0 | 样品数量 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fperiodunit | 留存期限单位 | varchar | 50 |  | √ | ' ' | 留存期限单位,枚举: YEAR :年 MONTH :月 DAY :日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_subentryentity |  | fdetailid |
| 2 | idx_im_subentry_fseq |  | fseq |
| 3 | idx_im_subentry_fentryid |  | fentryid |
