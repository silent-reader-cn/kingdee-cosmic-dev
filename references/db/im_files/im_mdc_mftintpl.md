# 完工入库单(制造模板)-im_mdc_mftintpl

## 完工入库单(制造模板)-关联追踪表 t_im_productinbill_tc

- **表名称：** 完工入库单(制造模板)-关联追踪表
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

## 完工入库单(制造模板)-分表 t_im_mdc_productinbill_m

- **表名称：** 完工入库单(制造模板)-分表
- **表名：** t_im_mdc_productinbill_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshipperid | 货主 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcostcenter | 成本中心(废弃) | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fproduceorg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_productinbill_m |  | fid |
| 2 | idx_im_mdc_pro_m_fd |  | fproduceorg |

---

## 完工入库单(制造模板)-多语言表 t_im_mdc_productinbill_l

- **表名称：** 完工入库单(制造模板)-多语言表
- **表名：** t_im_mdc_productinbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | '' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_productinbill_l |  | fpkid |
| 2 | idx_im_mdc_productinbill_l_0 |  | fid,flocaleid |

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

## 完工入库单(制造模板)-反写记录表 t_im_productinbill_wb

- **表名称：** 完工入库单(制造模板)-反写记录表
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

## 物料明细-子表 t_im_mdc_prblentry

- **表名称：** 物料明细-子表
- **表名：** t_im_mdc_prblentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | fcrosslegalperson | varchar | 5 |  | √ | '0' |  |
| 3 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 4 | flogisticsbill | flogisticsbill | bpchar | 1 |  | √ | '0' |  |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 255 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fk_bj73_decimalfield | 涨发率 | numeric | 23 | 2 |  | null | 涨发率 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 11 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 12 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fownertype | 入库货主类型 | varchar | 30 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fisadd | 是否新增行 | bpchar | 1 |  | √ | '0' | 是否新增行 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fqty | 库存单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存单位数量 |
| 19 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | fk_bj73_decimalfield2 | 产品系数 | numeric | 23 | 4 |  | null | 产品系数 |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fkeepertype | 入库保管者类型 | varchar | 30 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 24 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fk_bj73_decimalfield1 | 成本系数 | numeric | 23 | 4 |  | null | 成本系数 |
| 26 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 27 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 28 | fqtyunit2nd | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 29 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 31 | famounts | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 32 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 35 | fendwork | fendwork | bpchar | 1 |  | √ | '0' |  |
| 36 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 37 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 38 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 39 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 40 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 41 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 43 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 45 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 46 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 47 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 48 | fsettlerouteid | fsettlerouteid | int8 | 64 |  | √ | 0 |  |
| 49 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 50 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 51 | fprices | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 52 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 53 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 54 | fprdqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 55 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 56 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 57 | fentrycomment | 备注 | varchar | 512 |  | √ | '' | 备注 |
| 58 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 59 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 60 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 61 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 62 | fmaindeptid | 主制部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_prblentry_ftracknumber |  | ftracknumberid |
| 2 | idx_im_mdc_prble_foutowner |  | foutownerid |
| 3 | idx_prblentry_fconfiguredcode |  | fconfiguredcodeid |
| 4 | pk_im_mdc_prblentry |  | fentryid |
| 5 | idx_im_mdc_prble_warehouse |  | fwarehouseid |
| 6 | idx_im_mdc_prblentry_fk |  | fid |

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

---

## 物料明细-分表 t_im_mdc_prblentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_prblentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 7 | fremainreturnbaseqtys | 剩余退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余退库基本数量 |
| 8 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 11 | freturnqtys | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 12 | fremainreturnqtys | 剩余退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余退库数量 |
| 13 | freturnbaseqtys | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 14 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
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
| 1 | idx_im_mdcin_fsrcbillentryid |  | fsrcbillentryid |
| 2 | idx_im_mdcin_fsrcbillid |  | fsrcbillid |
| 3 | pk_im_mdc_prblentry_r |  | fentryid |
| 4 | idx_im_mdc_prblentry_r_fk |  | fid |

---

## 物料明细-分表 t_im_mdc_prblentry_m

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_prblentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmanuentryid | 生产工单行ID | int8 | 64 |  | √ | 0 | 生产工单行ID |
| 3 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 4 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 5 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 6 | fworkshop | 车间(废弃) | varchar | 50 |  | √ | ' ' | 车间(废弃) |
| 7 | fqualitystatus | 质量状态 | varchar | 30 |  | √ | ' ' | 质量状态,枚举: A :合格品 B :不合格品 C :待检品 D :报废品 |
| 8 | fdownreturnqty | fdownreturnqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | forderentryid | forderentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fbonded | fbonded | bpchar | 1 |  | √ | '0' |  |
| 11 | fshift | 班次 | int8 | 64 |  | √ | 0 | [班次 mpdm_workshifts](../mpdm_files/mpdm_workshifts.md) |
| 12 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 13 | fworkshopid | 车间ID(废弃) | int8 | 64 |  | √ | 0 | 车间ID(废弃) |
| 14 | fprocessplanentryf7id | fprocessplanentryf7id | int8 | 64 |  | √ | 0 |  |
| 15 | fprocessplan | fprocessplan | varchar | 50 |  | √ | ' ' |  |
| 16 | fpid | fpid | varchar | 50 |  | √ | ' ' |  |
| 17 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 18 | funit3rd | funit3rd | int8 | 64 |  | √ | 0 |  |
| 19 | fisadd | fisadd | bpchar | 1 |  | √ | '0' |  |
| 20 | fpurinentryid | fpurinentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fpurinno | fpurinno | varchar | 252 |  | √ | ' ' |  |
| 22 | fmanuentry | 生产工单行号 | varchar | 50 |  | √ | ' ' | 生产工单行号 |
| 23 | fmaterialattr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |
| 24 | fprocessplanf7id | fprocessplanf7id | int8 | 64 |  | √ | 0 |  |
| 25 | freceivedqty | 已收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收基本数量 |
| 26 | fmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 27 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 28 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fproducttype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 30 | fisdevproduce | fisdevproduce | bpchar | 1 |  | √ | '0' |  |
| 31 | fworkcenter | 工作中心文本 | varchar | 50 |  | √ | ' ' | 工作中心文本 |
| 32 | fiscopy | 是否复制行 | bpchar | 1 |  | √ | '0' | 是否复制行 |
| 33 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 34 | fqtyunit3rd | fqtyunit3rd | numeric | 23 | 10 | √ | 0 |  |
| 35 | fpurinid | fpurinid | int8 | 64 |  | √ | 0 |  |
| 36 | freceivalqty | 应收基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应收基本数量 |
| 37 | fbackflushstatus | fbackflushstatus | varchar | 100 |  | √ | ' ' |  |
| 38 | fmanubill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | flicenseno | flicenseno | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_prblentry_m_fk |  | fid |
| 2 | idx_im_mdcin_forderentryid |  | fmanuentryid |
| 3 | idx_im_mdcin_forderid |  | fmanubillid |
| 4 | idx_im_mdcin_fmainbillid |  | fmainbillid |
| 5 | pk_im_mdc_prblentry_m |  | fentryid |
| 6 | idx_im_mdcin_fmainbillentryid |  | fmainbillentryid |
| 7 | idx_im_mdcin_fproducedept |  | fproducedept |

---

## 完工入库单(制造模板)-主表 t_im_mdc_productinbill

- **表名称：** 完工入库单(制造模板)-主表
- **表名：** t_im_mdc_productinbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 7 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 8 | finnerbilltype | finnerbilltype | varchar | 50 |  | √ | ' ' |  |
| 9 | fbiztimes | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 14 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 15 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 16 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 19 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 27 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 28 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 29 | fbiztypeids | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 30 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 31 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 32 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fsettlecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_prbl_idtn |  | forgid,fbiztimes,fbillno |
| 2 | idx_im_mdc_productinbill |  | finvschemeid |
| 3 | pk_im_mdc_productinbill |  | fid |
