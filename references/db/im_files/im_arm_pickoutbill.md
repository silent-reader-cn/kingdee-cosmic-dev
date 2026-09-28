# 重复生产领料单-im_arm_pickoutbill

## 重复生产领料单-主表 t_im_arm_pickoutbill

- **表名称：** 重复生产领料单-主表
- **表名：** t_im_arm_pickoutbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 3 | fischargeagainstbill | fischargeagainstbill | bpchar | 1 |  | √ | '0' |  |
| 4 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fconsumingorg | 领用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmaterielid | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fbiztime | 出库日期 | timestamp | 0 |  |  | null | 出库日期 |
| 9 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fasyncstatus | fasyncstatus | bpchar | 1 |  | √ | 'B' |  |
| 15 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 16 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fprdline | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 19 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 24 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fisbackflush | 倒冲 | bpchar | 1 |  |  | ' ' | 倒冲 |
| 28 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 31 | isbackflush | isbackflush | bpchar | 1 |  |  | ' ' |  |
| 32 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 33 | fisalreadychargeagainst | fisalreadychargeagainst | bpchar | 1 |  | √ | '0' |  |
| 34 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 35 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 36 | fbizdeptid | 领用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fsettlecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 40 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_arm_pickoutbill_custm |  | fcustomerid |
| 2 | idx_im_arm_pickoutbill_org |  | forgid |
| 3 | idx_im_arm_pobill_bktorgno |  | fbookdate,forgid,fbillno |
| 4 | pk_im_arm_pickoutbill |  | fid |
| 5 | idx_im_arm_pobill_forbillno |  | fbillno,forgid |
| 6 | idx_im_arm_pobill_biztorgno |  | fbiztime,forgid,fbillno |

---

## 物料明细-子表 t_im_arm_pickoutbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_arm_pickoutbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 4 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 9 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | foutkeepertype | 出库保管者类型 | varchar | 36 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 12 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 14 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 15 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 17 | fcostaccountid | fcostaccountid | int8 | 64 |  | √ | 0 |  |
| 18 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 22 | fcostcurrencyid | fcostcurrencyid | int8 | 64 |  | √ | 0 |  |
| 23 | foutownertype | 出库货主类型 | varchar | 36 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 24 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 27 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 31 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 32 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 33 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 35 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 36 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 37 | fcompunit | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 38 | fproductid | fproductid | int8 | 64 |  | √ | 0 |  |
| 39 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 40 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 41 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 42 | fconsumingqty | 领用数量 | numeric | 23 | 10 | √ | 0 | 领用数量 |
| 43 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 44 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 47 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_arm_pobe_id_seq |  | fid,fseq |
| 2 | idx_t_im_arm_pobe_material |  | fmaterialid |
| 3 | pk_t_im_arm_pickoutbillentry |  | fentryid |
| 4 | idx_t_im_arm_pobe_e_mmt |  | fmaterialmasterid |
| 5 | idx_t_im_arm_pobe_e_wh |  | fwarehouseid |
| 6 | idx_t_im_arm_pobe_e_oow |  | foutownerid |

---

## 关联子实体-子表 t_im_arm_pickoutbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_arm_pickoutbill_lk

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
| 1 | idx_im_arm_pickoutbill_lk_fk |  | fid |
| 2 | pk_im_arm_pickoutbill_lk |  | fpkid |

---

## 物料明细-分表 t_im_arm_pickoutbillentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_arm_pickoutbillentry_c

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
| 1 | pk_t_im_arm_pickoutbillentry_c |  | fentryid |
| 2 | idx_id_cur_act |  | fid,fcostcurrencyid,fcostaccountid |

---

## 物料明细-分表 t_im_arm_pickoutbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_arm_pickoutbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_arm_pickoutbillentry_r |  | fentryid |
| 2 | idx_t_im_arm_pobe_r_id |  | fid |

---

## 重复生产领料单-多语言表 t_im_arm_pickoutbill_l

- **表名称：** 重复生产领料单-多语言表
- **表名：** t_im_arm_pickoutbill_l

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
| 1 | idx_t_im_arm_pickoutbill_l_fid |  | fid,flocaleid |
| 2 | pk_t_im_arm_pickoutbill_l |  | fpkid |

---

## 重复生产领料单-关联追踪表 t_im_arm_pickoutbill_tc

- **表名称：** 重复生产领料单-关联追踪表
- **表名：** t_im_arm_pickoutbill_tc

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
| 1 | idx_im_arm_pickoutbill_tc_tbill |  | ftbillid |
| 2 | pk_im_arm_pickoutbill_tc |  | fid |
| 3 | idx_im_arm_pickoutbill_tc_tid |  | ftid |

---

## 重复生产领料单-反写记录表 t_im_arm_pickoutbill_wb

- **表名称：** 重复生产领料单-反写记录表
- **表名：** t_im_arm_pickoutbill_wb

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
| 1 | idx_im_arm_pickoutbill_wb_fk |  | fid |
| 2 | pk_im_arm_pickoutbill_wb |  | fentryid |
