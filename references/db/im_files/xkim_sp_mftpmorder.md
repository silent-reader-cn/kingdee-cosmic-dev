# 简单生产领料单-xkim_sp_mftpmorder

## 关联子实体-子表 t_im_mreqoutbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mreqoutbill_lk

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
| 1 | t_im_mreqoutbill_lk_pkey |  | fpkid |
| 2 | idx_im_mreqoutbill_lk_fk |  | fid |

---

## 物料明细-子表 t_xkim_sp_mftpmentry

- **表名称：** 物料明细-子表
- **表名：** t_xkim_sp_mftpmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 3 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 8 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 9 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 10 | funitrate | funitrate | numeric | 23 | 10 | √ | 0 |  |
| 11 | fownertype | 入库货主类型 | varchar | 30 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 16 | fmftunitqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 17 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 18 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 19 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fkeepertype | 入库保管者类型 | varchar | 30 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 22 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 23 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 24 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 25 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 27 | fproductid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 28 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 31 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 32 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 33 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 34 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0 |  |
| 36 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0 |  |
| 37 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 38 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 39 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 40 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 41 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 42 | fbomentryid | bom分录编号 | int8 | 64 |  | √ | 0 | bom分录编号 |
| 43 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 44 | fmftunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 45 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 46 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 47 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 48 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 49 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 50 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 51 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 52 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 53 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 54 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkim_sp_mftpmentry |  | fentryid |
| 2 | idx_xkim_sp_mre_wh |  | fwarehouseid |
| 3 | idx_xkim_sp_mre_foowid |  | foutownerid |
| 4 | idx_xkim_sp_mre_fid_seq |  | fid,fseq |
| 5 | idx_xkim_sp_mre_fmid |  | fmaterialid |
| 6 | idx_xkim_sp_mre_fmmid |  | fmaterialmasterid |

---

## 简单生产领料单-关联追踪表 t_im_mreqoutbill_tc

- **表名称：** 简单生产领料单-关联追踪表
- **表名：** t_im_mreqoutbill_tc

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
| 1 | idx_im_mreqoutbill_tc_tbill |  | ftbillid |
| 2 | idx_im_mreqoutbill_tc_tid |  | ftid |
| 3 | t_im_mreqoutbill_tc_pkey |  | fid |
| 4 | idx_im_mreqout_tc_ftbidtid |  | ftbillid,ftid |

---

## 简单生产领料单-多语言表 t_xkim_sp_mftpmorder_l

- **表名称：** 简单生产领料单-多语言表
- **表名：** t_xkim_sp_mftpmorder_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkim_sp_mb_l_flid |  | fid,flocaleid |
| 2 | pk_t_xkim_sp_mftpmorder_l |  | fpkid |

---

## 简单生产领料单-主表 t_xkim_sp_mftpmorder

- **表名称：** 简单生产领料单-主表
- **表名：** t_xkim_sp_mftpmorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequserid | 领用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  |  | null | 物料生产信息 bd_materialmftinfo |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fsupplyowner | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fmftqty | 生产数量 | numeric | 23 | 10 |  | 0 | 生产数量 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 12 | fmatversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 13 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 14 | fbomid | BOM编码 | int8 | 64 |  |  | null | BOM维护 pdm_mftbom |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbizorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 18 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 19 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 20 | fcostcenterorg | 成本中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fsupplyownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 26 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fmftunitid | 生产单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 28 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fsettlecurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 33 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 35 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 36 | fsettleorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 38 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 39 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 40 | fbizdeptid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkim_sp_mr_bizorg |  | fbiztime,forgid,fbillno |
| 2 | pk_t_xkim_sp_mftpmorder |  | fid |
| 3 | idx_xkim_sp_m_bktorgno |  | fbookdate,forgid,fbillno |
| 4 | idx_xkim_sp_mr_invs |  | finvschemeid |
| 5 | idx_xkim_sp_mr_bo |  | fbillno |
| 6 | idx_xkim_sp_mrob_bizorg |  | fbizorgid |
| 7 | idx_xkim_sp_mrb_idtn |  | forgid,fbiztime,fbillno |

---

## 物料明细-分表 t_xkim_sp_mftpmentry_c

- **表名称：** 物料明细-分表
- **表名：** t_xkim_sp_mftpmentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostcurrencyid | 成本币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 4 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 5 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkim_sp_mftpmentry_c |  | fentryid |
| 2 | idx_xkim_sp_mftpmentry_c |  | fid |

---

## 物料明细-分表 t_xkim_sp_mftpmentry_r

- **表名称：** 物料明细-分表
- **表名：** t_xkim_sp_mftpmentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 3 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 4 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 5 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 6 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0 | 已退库基本数量 |
| 7 | fvmisettleqty | VMI已结算数量 | numeric | 23 | 10 | √ | 0 | VMI已结算数量 |
| 8 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
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
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 20 | fpurchasedqty | 已转固数量 | numeric | 23 | 10 | √ | 0 | 已转固数量 |
| 21 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 22 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 23 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 24 | fvmiremainsettlebaseqty | VMI剩余结算基本数量 | numeric | 23 | 10 | √ | 0 | VMI剩余结算基本数量 |
| 25 | fpurchasedamount | 已转固金额 | numeric | 23 | 10 | √ | 0 | 已转固金额 |
| 26 | fremainpuramount | 未转固金额 | numeric | 23 | 10 | √ | 0 | 未转固金额 |
| 27 | fremainreturnqty | 未退库数量 | numeric | 23 | 10 | √ | 0 | 未退库数量 |
| 28 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkim_sp_mftpmentry_r |  | fentryid |
| 2 | idx_xkim_sp_mo_e_fid |  | fid |
| 3 | idx_xkim_sp_mr_fseid |  | fsrcbillentryid |
| 4 | idx_xkim_sp_mr_fmeid |  | fmainbillentryid |

---

## 简单生产领料单-反写记录表 t_im_mreqoutbill_wb

- **表名称：** 简单生产领料单-反写记录表
- **表名：** t_im_mreqoutbill_wb

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
| 1 | idx_im_mreqoutbill_wb_fk |  | fid |
| 2 | t_im_mreqoutbill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_im_mreqoutbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mreqoutbillentry_lk

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
| 1 | t_im_mreqoutbillentry_lk_pkey |  | fpkid |
| 2 | idx_im_mreqoutbillentry_lk_fk |  | fentryid |
