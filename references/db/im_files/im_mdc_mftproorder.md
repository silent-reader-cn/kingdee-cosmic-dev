# 生产领料单-im_mdc_mftproorder

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

## 物料明细-分表 t_im_mdc_mqbentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_mqbentry_c

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
| 1 | pk_im_mdc_mqbentry_c |  | fentryid |
| 2 | idx_im_mdc_mqbentry_c |  | fid |

---

## 物料明细-分表 t_im_mdc_mqbentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_mqbentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 3 | flogisticsbill | flogisticsbill | bpchar | 1 |  | √ | '0' |  |
| 4 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 5 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 6 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 7 | fvmisettleqty | VMI已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI已结算数量 |
| 8 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 9 | fremainpurqty | 未转固数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未转固数量 |
| 10 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 11 | fbasefeedqty | fbasefeedqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fremainreturnbaseqty | 未退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库基本数量 |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 14 | fvmiremainsettleqty | VMI剩余结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI剩余结算数量 |
| 15 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 16 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | fvmisettlebaseqty | VMI已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI已结算基本数量 |
| 18 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 19 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 20 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 21 | fpurchasedqty | 已转固数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已转固数量 |
| 22 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 23 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 24 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 25 | fvmiremainsettlebaseqty | VMI剩余结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | VMI剩余结算基本数量 |
| 26 | fpurchasedamount | 已转固金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已转固金额 |
| 27 | fremainpuramount | 未转固金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未转固金额 |
| 28 | fremainreturnqty | 未退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退库数量 |
| 29 | ffeedqty | ffeedqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdcout_fsrcbillid |  | fsrcbillid |
| 2 | idx_im_mdcout_fmainbillid |  | fmainbillid |
| 3 | pk_im_mdc_mqbentry_r |  | fentryid |
| 4 | idx_im_mdc_mtb_fmeid |  | fmainbillentryid |
| 5 | idx_im_mdc_mtb_fseid |  | fsrcbillentryid |
| 6 | idx_im_mdc_entryrfid |  | fid |

---

## 物料明细-分表 t_im_mdc_mqbentry_m

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_mqbentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | 工序序列 | int4 | 32 |  | √ | 0 | 工序序列 |
| 3 | fmanuentryid | 生产工单行ID | int8 | 64 |  | √ | 0 | 生产工单行ID |
| 4 | forderid | 生产工单F7 | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 5 | finspfinishbaseqty | 质检完成基本数量 | numeric | 23 | 10 | √ | 0 | 质检完成基本数量 |
| 6 | fiscannegative | fiscannegative | bpchar | 1 |  | √ | '0' |  |
| 7 | forderentryid | 生产工单分录F7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fmachiningtype | 加工类型 | varchar | 30 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 10 | freturninsprelbaseqty | 退料请检关联基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联基本数量 |
| 11 | foprno | 工序号（废弃） | varchar | 50 |  | √ | ' ' | 工序号（废弃） |
| 12 | fprocessplanentryf7id | 工序计划分录F7 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 13 | fprocessplan | 工序计划 | varchar | 50 |  | √ | ' ' | 工序计划 |
| 14 | finspfinishqty | 质检完成数量 | numeric | 23 | 10 | √ | 0 | 质检完成数量 |
| 15 | freturninspect | 退料检验 | bpchar | 1 |  | √ | '0' | 退料检验 |
| 16 | fisadd | fisadd | bpchar | 1 |  | √ | '0' |  |
| 17 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 18 | favbinvqty | 可用库存数量 | numeric | 23 | 10 | √ | 0 | 可用库存数量 |
| 19 | fmanuentry | 生产工单行号 | varchar | 50 |  | √ | ' ' | 生产工单行号 |
| 20 | fprocessplanf7id | 工序计划F7 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 21 | fscrappedbsqty | fscrappedbsqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 23 | finspectstatus | 质检状态 | bpchar | 1 |  | √ | ' ' | 质检状态,枚举: A :检验中 B :质检完成 |
| 24 | fproducedeptid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fproductmasterid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 26 | fstockid | 生产用料清单F7 | int8 | 64 |  | √ | 0 | [生产用料清单f7 pom_mftstockf7](../pom_files/pom_mftstockf7.md) |
| 27 | favbinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 28 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 30 | fstockentryid | 生产用料清单分录F7 | int8 | 64 |  | √ | 0 | [生产用料清单分录f7 pom_mftstockentryf7](../pom_files/pom_mftstockentryf7.md) |
| 31 | foperationdesc | 工序说明 | varchar | 255 |  | √ | ' ' | 工序说明 |
| 32 | fnotupdateunclaimed | fnotupdateunclaimed | bpchar | 1 |  | √ | '0' |  |
| 33 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 34 | freturninspqty | 退料请检数量 | numeric | 23 | 10 | √ | 0 | 退料请检数量 |
| 35 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fmanubill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 37 | fcansendqty | 未领数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未领数量 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | freturninsprelqty | 退料请检关联数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联数量 |
| 40 | freturninspbaseqty | 退料请检基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检基本数量 |
| 41 | fprocessseq | 工序序列（废弃） | varchar | 50 |  | √ | ' ' | 工序序列（废弃） |
| 42 | frepresonassistantid | frepresonassistantid | int8 | 64 |  | √ | 0 |  |
| 43 | fscrappedqty | fscrappedqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_mqbentry_m |  | fentryid |
| 2 | idx_im_mdc_entrymfid |  | fid |
| 3 | idx_im_mdc_manuentry |  | fmanuentryid |
| 4 | idx_im_mdc_rewqe_fm |  | fmanubill |

---

## 物料明细-子表 t_im_mdc_mqbentry

- **表名称：** 物料明细-子表
- **表名：** t_im_mdc_mqbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 4 | fbasequantity | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | fk_bj73_basedatafield | fk_bj73_basedatafield | int8 | 64 |  | √ | 0 |  |
| 7 | fnoupdateinvfields | 不更新库存字段 | varchar | 255 |  | √ | ' ' | 不更新库存字段 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fisrework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 12 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 13 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 14 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fownertype | 入库货主类型 | varchar | 30 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 16 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fqty | 实发数量 | numeric | 23 | 10 | √ | 0.0000000000 | 实发数量 |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fkeepertype | 入库保管者类型 | varchar | 30 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 24 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 26 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 27 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 28 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 29 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 30 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 32 | freturnmaterialtype | freturnmaterialtype | bpchar | 1 |  | √ | 'A' |  |
| 33 | fproductid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 34 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 37 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 38 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 39 | fprdownerid | 产品货主（废弃） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 41 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 42 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fk_bj73_qtyfield | 完工入库数 | numeric | 23 | 10 |  | null | 完工入库数 |
| 45 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 47 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 48 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 49 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 50 | fworkprocedureid | 工序名称 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 51 | fprdunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 52 | fsettlerouteid | 结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 53 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 54 | fquantity | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 55 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 56 | fprdownertype | 产品货主类型（废弃） | varchar | 30 |  | √ | ' ' | 产品货主类型（废弃）,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 57 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 58 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 59 | fprdqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 60 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 61 | fqtyunit3rd | fqtyunit3rd | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 62 | fentrycomment | 备注 | varchar | 512 |  | √ | '' | 备注 |
| 63 | funit3rdid | funit3rdid | int8 | 64 |  | √ | 0 |  |
| 64 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 65 | fbaseqty | 实发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 实发基本数量 |
| 66 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 67 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_mtb_e_fwarehouse |  | fwarehouseid |
| 2 | idx_mqbentry_ftracknumber |  | ftracknumberid |
| 3 | idx_im_mdc_mtb_e_fid |  | fid |
| 4 | idx_im_mdc_mtb_e_foutowner |  | foutownerid |
| 5 | idx_im_mdcmentry_fworkcenter |  | foprworkcenter |
| 6 | idx_mqbentry_fconfiguredcode |  | fconfiguredcodeid |
| 7 | pk_im_mdc_mqbentry |  | fentryid |
| 8 | idx_im_mdc_mtb_e_fmid |  | fmaterialid |
| 9 | idx_im_mdc_mtb_e_fmmid |  | fmaterialmasterid |

---

## 生产领料单-关联追踪表 t_im_mreqoutbill_tc

- **表名称：** 生产领料单-关联追踪表
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

## 生产领料单-反写记录表 t_im_mreqoutbill_wb

- **表名称：** 生产领料单-反写记录表
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
| 1 | idx_im_mreqoutbillentry_lk_fk |  | fentryid |
| 2 | t_im_mreqoutbillentry_lk_pkey |  | fpkid |

---

## 生产领料单-主表 t_im_mdc_mreqoutbill

- **表名称：** 生产领料单-主表
- **表名：** t_im_mdc_mreqoutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequserid | 领用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsupplyowner | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 10 | finnerbilltype | 内部交易单据类别 | varchar | 50 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 11 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbizorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 15 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 17 | fcostcenterorg | 成本中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fsupplyownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 23 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcomment | 备注 | varchar | 512 |  | √ | '' | 备注 |
| 26 | fsettlecurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 29 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fisbackflush | 倒冲 | bpchar | 1 |  | √ | '0' | 倒冲 |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 33 | fsrcreqid | 来源申请单ID | int8 | 64 |  | √ | 0 | 来源申请单ID |
| 34 | fsettleorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 36 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 37 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 38 | fbizdeptid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdcmrb_fbiztime |  | fbiztime |
| 2 | pk_im_mdc_mreqoutbill |  | fid |
| 3 | idx_im_mdc_mrb_fno |  | fbillno |
| 4 | idx_im_mdc_mreqoutbill_bizorg |  | fbizorgid |
| 5 | idx_im_mrb_fbizo |  | fbilltypeid |
| 6 | idx_im_mdcmrb_forgid |  | forgid |

---

## 生产领料单-分表 t_im_mdc_mreqoutbill_m

- **表名称：** 生产领料单-分表
- **表名：** t_im_mdc_mreqoutbill_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fneedtime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 3 | fworkshopid | 车间ID | int8 | 64 |  | √ | 0 | 车间ID |
| 4 | fdoctype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: A :普通领料 |
| 5 | fworkshop | 车间 | varchar | 50 |  | √ | ' ' | 车间 |
| 6 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 7 | fsupplierid | 委外供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_req_df |  | fdoctype |
| 2 | pk_t_im_mdc_mreqoutbill_m |  | fid |

---

## 生产领料单-多语言表 t_im_mdc_mreqoutbill_l

- **表名称：** 生产领料单-多语言表
- **表名：** t_im_mdc_mreqoutbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | '' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_mreqoutbill_l |  | fpkid |
