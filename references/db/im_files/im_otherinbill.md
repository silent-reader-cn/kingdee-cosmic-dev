# 其他入库单-im_otherinbill

## 其他入库单-主表 t_im_otherinbill

- **表名称：** 其他入库单-主表
- **表名：** t_im_otherinbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 8 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 9 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 14 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 19 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 22 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 27 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 31 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 32 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fsettlecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 36 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_otherinbill_org |  | forgid |
| 2 | t_im_otherinbill_pkey |  | fid |
| 3 | idx_im_otherinbill_suppl |  | fsupplierid |
| 4 | idx_im_otherinbill_forgbillno |  | fbillno,forgid |
| 5 | idx_im_oibill_bktorgno |  | fbookdate,forgid,fbillno |
| 6 | idx_im_otherinbill_biztorgno |  | fbiztime,forgid,fbillno |

---

## 关联子实体-子表 t_im_otherinbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_otherinbill_lk

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
| 1 | idx_im_otherinbill_lk_fk |  | fid |
| 2 | t_im_otherinbill_lk_pkey |  | fpkid |

---

## 物料明细-子表 t_im_otherinbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_otherinbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 4 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 11 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 12 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 14 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 16 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 17 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 18 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 19 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 23 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 24 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 27 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 29 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 30 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 31 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 32 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 33 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 34 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 36 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 37 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 38 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 39 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 40 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 41 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 42 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 43 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 46 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_otherinbill_e_fow |  | fownerid |
| 2 | t_im_otherinbillentry_pkey |  | fentryid |
| 3 | idx_im_otherinbill_e_mmt |  | fmaterialmasterid |
| 4 | idx_im_otherinbill_e_wh |  | fwarehouseid |
| 5 | idx_im_otherinbillentry_fid |  | fid |

---

## 其他入库单-关联追踪表 t_im_otherinbill_tc

- **表名称：** 其他入库单-关联追踪表
- **表名：** t_im_otherinbill_tc

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
| 1 | idx_im_otherin_tc_ftbidtid |  | ftbillid,ftid |
| 2 | idx_im_otherinbill_tc_tid |  | ftid |
| 3 | t_im_otherinbill_tc_pkey |  | fid |
| 4 | idx_im_otherinbill_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_im_otherinbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_otherinbillentry_lk

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
| 1 | t_im_otherinbillentry_lk_pkey |  | fpkid |
| 2 | idx_im_otherinbillentry_lk_fk |  | fentryid |

---

## 物料明细-分表 t_im_otherinbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_otherinbillentry_c

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
| 1 | pk_im_otherinbillentry_c |  | fentryid |
| 2 | idx_im_otherinbillentry_c |  | fid |

---

## 物料明细-分表 t_im_otherinbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_otherinbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | freturnqty | 已退回数量 | numeric | 23 | 10 | √ | 0 | 已退回数量 |
| 7 | funreturnqty | 未退回数量 | numeric | 23 | 10 | √ | 0 | 未退回数量 |
| 8 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | freturnbaseqty | 已退回基本数量 | numeric | 23 | 10 | √ | 0 | 已退回基本数量 |
| 10 | funreturnbaseqty | 未退回基本数量 | numeric | 23 | 10 | √ | 0 | 未退回基本数量 |
| 11 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 12 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 13 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 14 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_otherinbillentry_r_pkey |  | fentryid |
| 2 | idx_im_otherinbillentry_r_fid |  | fid |

---

## 其他入库单-多语言表 t_im_otherinbill_l

- **表名称：** 其他入库单-多语言表
- **表名：** t_im_otherinbill_l

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
| 1 | t_im_otherinbill_l_pkey |  | fpkid |
| 2 | idx_im_otherinbill_l_flid |  | fid,flocaleid |
| 3 | idx_im_otherinbill_l_fid |  | fid |

---

## 其他入库单-反写记录表 t_im_otherinbill_wb

- **表名称：** 其他入库单-反写记录表
- **表名：** t_im_otherinbill_wb

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
| 1 | t_im_otherinbill_wb_pkey |  | fentryid |
| 2 | idx_im_otherinbill_wb_fk |  | fid |
