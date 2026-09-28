# 生产入库单模板-im_productinbilltpl

## 生产入库单模板-关联追踪表 t_im_productinbill_tc

- **表名称：** 生产入库单模板-关联追踪表
- **表名：** t_im_productinbill_tc

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
| 1 | t_im_productinbill_tc_pkey |  | fid |
| 2 | idx_im_productin_tc_ftbidtid |  | ftbillid,ftid |
| 3 | idx_im_productinbill_tc_tbill |  | ftbillid |
| 4 | idx_im_productinbill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_im_productinbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_productinbillentry_lk

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
| 1 | t_im_productinbillentry_lk_pkey |  | fpkid |
| 2 | idx_im_productinbillentry_lk_fk |  | fentryid |

---

## 生产入库单模板-反写记录表 t_im_productinbill_wb

- **表名称：** 生产入库单模板-反写记录表
- **表名：** t_im_productinbill_wb

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
| 1 | t_im_productinbill_wb_pkey |  | fentryid |
| 2 | idx_im_productinbill_wb_fk |  | fid |

---

## 生产入库单模板-主表 t_im_productinbill

- **表名称：** 生产入库单模板-主表
- **表名：** t_im_productinbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 7 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 8 | fbiztimes | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 14 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 15 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 18 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 26 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fbiztypeids | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 29 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 30 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fsettlecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_productinbill_pkey |  | fid |
| 2 | idx_im_prbl_forgbillno |  | fbillno,forgid |
| 3 | idx_im_prbl_idtn |  | forgid,fbiztimes,fbillno |
| 4 | idx_im_pibill_bktorgno |  | fbookdate,forgid,fbillno |
| 5 | idx_im_prbl_biztorgno |  | fbiztimes,forgid,fbillno |
| 6 | idx_im_prbl_finvsc |  | finvschemeid |
| 7 | idx_im_prbl_org |  | forgid |

---

## 物料明细-子表 t_im_productinbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_productinbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 3 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 8 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 9 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | freturnsqty | freturnsqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 21 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 22 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 23 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 24 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 26 | famounts | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 27 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 30 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 31 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 32 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 33 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 37 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 38 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 39 | freturnsbaseqty | freturnsbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 41 | fprices | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 42 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 43 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 44 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 45 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 46 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 47 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 48 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 49 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 50 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 51 | fmaindeptid | 主制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_productinbillentry_pkey |  | fentryid |
| 2 | idx_im_prbl_e_fokid |  | foutkeeperid |
| 3 | idx_im_prbl_e_mmt |  | fmaterialmasterid |
| 4 | idx_im_prbl_e_fkid |  | fkeeperid |
| 5 | idx_im_prbl_e_fid |  | fid |
| 6 | idx_im_prbl_e_foowid |  | foutownerid |
| 7 | idx_im_prbl_e_wh |  | fwarehouseid |
| 8 | idx_im_prbl_e_fowid |  | fownerid |

---

## 物料明细-分表 t_im_productinbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_productinbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | freturnqty | freturnqty | int8 | 64 |  | √ | 0 |  |
| 7 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | freturnbaseqty | freturnbaseqty | int8 | 64 |  | √ | 0 |  |
| 9 | fremainreturnbaseqtys | 剩余退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余退库基本数量 |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 13 | freturnqtys | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 14 | fremainreturnqtys | 剩余退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余退库数量 |
| 15 | fremainreturnbaseqty | fremainreturnbaseqty | int8 | 64 |  | √ | 0 |  |
| 16 | freturnbaseqtys | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 17 | fremainreturnqty | fremainreturnqty | int8 | 64 |  | √ | 0 |  |
| 18 | fsrcbillentity | 来源单据实体 | varchar | 100 |  | √ | ' ' | 来源单据实体 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_productinbillentry_r_pkey |  | fentryid |
| 2 | idx_im_prbe_r_fid |  | fid |

---

## 生产入库单模板-多语言表 t_im_productinbill_l

- **表名称：** 生产入库单模板-多语言表
- **表名：** t_im_productinbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_productinbill_l_pkey |  | fpkid |
| 2 | idx_im_prbl_l_flid |  | fid,flocaleid |

---

## 关联子实体-子表 t_im_productinbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_productinbill_lk

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
| 1 | idx_im_productinbill_lk_fk |  | fid |
| 2 | t_im_productinbill_lk_pkey |  | fpkid |
