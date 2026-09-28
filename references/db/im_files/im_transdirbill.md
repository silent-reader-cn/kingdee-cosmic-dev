# 直接调拨单-im_transdirbill

## 直接调拨单-反写记录表 t_im_transdirbill_wb

- **表名称：** 直接调拨单-反写记录表
- **表名：** t_im_transdirbill_wb

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
| 1 | t_im_transdirbill_wb_pkey |  | fentryid |
| 2 | idx_im_transdirbill_wb_fk |  | fid |

---

## 辅料比例-子表 tk_bj73_transaux

- **表名称：** 辅料比例-子表
- **表名：** tk_bj73_transaux

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fk_bj73_materielfield | 所需辅料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 2 | fk_bj73_warehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fk_bj73_qtyfield | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fk_bj73_unitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fk_bj73_batch | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | null | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__bj73_transaux_fk |  | fentryid |
| 2 | pk__bj73_transaux |  | fdetailid |

---

## 直接调拨单-多语言表 t_im_transdirbill_l

- **表名称：** 直接调拨单-多语言表
- **表名：** t_im_transdirbill_l

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
| 1 | idx_im_transdirbill_l |  | fid,flocaleid |
| 2 | t_im_transdirbill_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_im_transdirbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transdirbill_lk

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
| 1 | idx_im_transdirbill_lk_fk |  | fid |
| 2 | t_im_transdirbill_lk_pkey |  | fpkid |

---

## 关联子实体-子表 t_im_transdirbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_transdirbillentry_lk

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
| 1 | t_im_transdirbillentry_lk_pkey |  | fpkid |
| 2 | idx_im_transdirbillentry_lk_fk |  | fentryid |

---

## 物料明细-子表 t_im_transdirbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_transdirbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finlotid | 调入批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 3 | finprojectid | 调入项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fserialqty | fserialqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | finvstatusid | 调入库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 10 | fk_bj73_billtypefield | fk_bj73_billtypefield | int8 | 64 |  | √ | 0 |  |
| 11 | finlicenseno | 调入许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 12 | foutinvtypeid | 调出库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 13 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 14 | fownertype | 调入货主类型 | varchar | 36 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 15 | finkeepertype | finkeepertype | varchar | 36 |  | √ | ' ' |  |
| 16 | fkeeperid | 调入保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | finownerid | finownerid | int8 | 64 |  | √ | 0 |  |
| 19 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fentryinorgid | fentryinorgid | int8 | 64 |  | √ | 0 |  |
| 21 | foutkeeperid | 调出保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 23 | feincostcenterid | 调入成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 24 | fecostcenterid | 调出成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fserialunitid | fserialunitid | int8 | 64 |  | √ | 0 |  |
| 26 | fprojectid | 调出项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fkeepertype | 调入保管者类型 | varchar | 36 |  | √ | ' ' | 调入保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 29 | fwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | foutinvstatusid | 调出库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 31 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 32 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 33 | fqtyunit2nd | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 34 | fownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | flotid | 调出批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 36 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 39 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 40 | flicenseno | 调出许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 41 | fenterinvstatusid | fenterinvstatusid | int8 | 64 |  | √ | 0 |  |
| 42 | flotnumber | 调出批号 | varchar | 80 |  | √ | ' ' | 调出批号 |
| 43 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 44 | fsettleroute | 结算路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 45 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 46 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | fserialunitrate | fserialunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 48 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 49 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 50 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 51 | foutkeepertype | 调出保管者类型 | varchar | 36 |  | √ | ' ' | 调出保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 52 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 53 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 54 | finwarehouseid | finwarehouseid | int8 | 64 |  | √ | 0 |  |
| 55 | fk_bj73_manubill | 生产工单 | int8 | 64 |  | √ | 0 | [生产工单 sfc_bd_mftorer](../sfc_files/sfc_bd_mftorer.md) |
| 56 | finkeeperid | finkeeperid | int8 | 64 |  | √ | 0 |  |
| 57 | finmpmtaskno | 调入项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 58 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 59 | fk_bj73_datefield2 | 包装日期 | timestamp | 0 |  |  | null | 包装日期 |
| 60 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 61 | foutownertype | 调出货主类型 | varchar | 36 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 62 | fk_bj73_billnofield | fk_bj73_billnofield | varchar | 30 |  | √ | ' ' |  |
| 63 | finvtypeid | 调入库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 64 | finlocationid | finlocationid | int8 | 64 |  | √ | 0 |  |
| 65 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 66 | fk_bj73_basedatafield2 | fk_bj73_basedatafield2 | int8 | 64 |  | √ | 0 |  |
| 67 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 68 | flocationid | 调入仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 69 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 70 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 71 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 72 | fk_bj73_textfield | fk_bj73_textfield | varchar | 50 |  | √ | ' ' |  |
| 73 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 74 | fmpmtaskno | 调出项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 75 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 76 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 77 | fenterinvtypeid | fenterinvtypeid | int8 | 64 |  | √ | 0 |  |
| 78 | finownertype | finownertype | varchar | 36 |  | √ | ' ' |  |
| 79 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 80 | finlotnumber | 调入批号 | varchar | 80 |  | √ | ' ' | 调入批号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_transdirbillentry_pkey |  | fentryid |
| 2 | idx_im_transdirbill_e_oow |  | foutownerid |
| 3 | idx_im_transdirbill_e_mmt |  | fmaterialmasterid |
| 4 | idx_im_transdirbill_e_wh |  | fwarehouseid |
| 5 | idx_im_transdirbill_e_ow |  | fownerid |
| 6 | idx_im_transdirbillentry |  | fid |

---

## 物料明细-分表 t_im_transdirbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_transdirbillentry_c

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
| 1 | idx_im_transdirbillentry_c |  | fid |
| 2 | pk_im_transdirbillentry_c |  | fentryid |

---

## 直接调拨单-关联追踪表 t_im_transdirbill_tc

- **表名称：** 直接调拨单-关联追踪表
- **表名：** t_im_transdirbill_tc

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
| 1 | idx_im_transdirbill_tc_tbill |  | ftbillid |
| 2 | idx_im_transdirbill_tc_tid |  | ftid |
| 3 | idx_im_transdir_tc_ftbidtid |  | ftbillid,ftid |
| 4 | t_im_transdirbill_tc_pkey |  | fid |

---

## 物料明细-分表 t_im_transdirbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_transdirbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 6 | freloeminqty | 关联受托入库数量 | numeric | 23 | 10 | √ | 0 | 关联受托入库数量 |
| 7 | fmainbillentity | 核心单据实体 | varchar | 100 |  | √ | ' ' | 核心单据实体 |
| 8 | freturnbaseqty | 已退回基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退回基本数量 |
| 9 | fgroupnumber | 成组号 | varchar | 50 |  | √ | ' ' | 成组号 |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fsrcoeminid | 来源受托退料id | int8 | 64 |  | √ | 0 | 来源受托退料id |
| 12 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 13 | fgroupseq | 成组行号 | varchar | 50 |  | √ | ' ' | 成组行号 |
| 14 | funoeminbaseqty | 受托未入库基本数量 | numeric | 23 | 10 | √ | 0 | 受托未入库基本数量 |
| 15 | foeminbaseqty | 受托已入库基本数量 | numeric | 23 | 10 | √ | 0 | 受托已入库基本数量 |
| 16 | fremainreturnbaseqty | 未退回基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退回基本数量 |
| 17 | foeminqty | 受托已入库数量 | numeric | 23 | 10 | √ | 0 | 受托已入库数量 |
| 18 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 19 | freloeminbaseqty | 关联受托入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联受托入库基本数量 |
| 20 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | fmainbillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 23 | freturnqty | 已退回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退回数量 |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 26 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 27 | funoeminqty | 受托未入库数量 | numeric | 23 | 10 | √ | 0 | 受托未入库数量 |
| 28 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 29 | fremainreturnqty | 未退回数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未退回数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 31 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transdirentry_r_fid |  | fid |
| 2 | t_im_transdirbillentry_r_pkey |  | fentryid |

---

## 直接调拨单-主表 t_im_transdirbill

- **表名称：** 直接调拨单-主表
- **表名：** t_im_transdirbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_bj73_basedatafield | 生产部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 3 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 4 | foperatorid | 调入库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | forgid | 调入组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 14 | fk_bj73_datefield | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 15 | fk_bj73_datefield1 | fk_bj73_datefield1 | timestamp | 0 |  |  | null |  |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 21 | fdeptid | 调入部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | foutoperator | 调出库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 23 | foemorgid | 受托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 26 | foperatorgroupid | 调入库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | foutdept | 调出部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 32 | foutoperatorgroup | 调出库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 33 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 34 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 35 | foutorgid | 调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | finorgid | finorgid | int8 | 64 |  | √ | 0 |  |
| 37 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 38 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 41 | fsettlescurrency | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_transdirbill_biztorgno |  | fbiztime,foutorgid,fbillno |
| 2 | idx_im_transdirbill_org |  | forgid |
| 3 | idx_im_transdirbill_oorg |  | foutorgid |
| 4 | idx_im_tdbill_bktorgno |  | fbookdate,forgid,fbillno |
| 5 | t_im_transdirbill_pkey |  | fid |
| 6 | idx_im_transdirbill_forgbillno |  | fbillno,forgid |
