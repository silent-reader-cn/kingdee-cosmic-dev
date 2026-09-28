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
| 2 | finlotid | 调入批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 3 | finprojectid | 调入项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fserialqty | fserialqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | finvstatusid | 调入库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | foutinvtypeid | 调出库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 11 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fownertype | 调入货主类型 | varchar | 36 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | finkeepertype | finkeepertype | varchar | 36 |  | √ | ' ' |  |
| 14 | fkeeperid | 调入保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | finownerid | finownerid | int8 | 64 |  | √ | 0 |  |
| 17 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | fentryinorgid | fentryinorgid | int8 | 64 |  | √ | 0 |  |
| 19 | foutkeeperid | 调出保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 21 | feincostcenterid | 调入成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fecostcenterid | 调出成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fserialunitid | fserialunitid | int8 | 64 |  | √ | 0 |  |
| 24 | fprojectid | 调出项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fkeepertype | 调入保管者类型 | varchar | 36 |  | √ | ' ' | 调入保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 27 | fwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 28 | foutinvstatusid | 调出库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 29 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 30 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 31 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 32 | fownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | flotid | 调出批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 34 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 37 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 38 | fenterinvstatusid | fenterinvstatusid | int8 | 64 |  | √ | 0 |  |
| 39 | flotnumber | 调出批号 | varchar | 80 |  | √ | ' ' | 调出批号 |
| 40 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 41 | fsettleroute | 结算路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 42 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 43 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fserialunitrate | fserialunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 45 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 47 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 48 | foutkeepertype | 调出保管者类型 | varchar | 36 |  | √ | ' ' | 调出保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 49 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 50 | finwarehouseid | finwarehouseid | int8 | 64 |  | √ | 0 |  |
| 51 | finkeeperid | finkeeperid | int8 | 64 |  | √ | 0 |  |
| 52 | finmpmtaskno | 调入项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 53 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 54 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 55 | foutownertype | 调出货主类型 | varchar | 36 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 56 | finvtypeid | 调入库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 57 | finlocationid | finlocationid | int8 | 64 |  | √ | 0 |  |
| 58 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 59 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 60 | flocationid | 调入仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 61 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 62 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 63 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 64 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 65 | fmpmtaskno | 调出项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 66 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 67 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 68 | fenterinvtypeid | fenterinvtypeid | int8 | 64 |  | √ | 0 |  |
| 69 | finownertype | finownertype | varchar | 36 |  | √ | ' ' |  |
| 70 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 71 | finlotnumber | 调入批号 | varchar | 80 |  | √ | ' ' | 调入批号 |

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
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
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
| 1 | t_im_transdirbillentry_r_pkey |  | fentryid |
| 2 | idx_im_transdirentry_r_fid |  | fid |

---

## 直接调拨单-主表 t_im_transdirbill

- **表名称：** 直接调拨单-主表
- **表名：** t_im_transdirbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 3 | foperatorid | 调入库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 调入组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 6 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 9 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 12 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 18 | fdeptid | 调入部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | foutoperator | 调出库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 20 | foemorgid | 受托组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 23 | foperatorgroupid | 调入库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | foutdept | 调出部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 29 | foutoperatorgroup | 调出库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | ftranstype | 调拨类型 | varchar | 5 |  | √ | ' ' | 调拨类型,枚举: A :组织内调拨 B :跨组织调拨 |
| 32 | foutorgid | 调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | finorgid | finorgid | int8 | 64 |  | √ | 0 |  |
| 34 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 35 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 38 | fsettlescurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
