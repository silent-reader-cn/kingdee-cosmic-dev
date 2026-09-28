# 重复生产完工入库单-im_arm_productinvbill

## 重复生产完工入库单-关联追踪表 t_im_productinbill_tc

- **表名称：** 重复生产完工入库单-关联追踪表
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

## 物料明细-子表 t_im_arm_prdlentry

- **表名称：** 物料明细-子表
- **表名：** t_im_arm_prdlentry

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
| 9 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | fcostaccountid | fcostaccountid | int8 | 64 |  | √ | 0 |  |
| 11 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fqty | 库存数量 | numeric | 23 | 10 | √ | 0 | 库存数量 |
| 15 | fcostcurrencyid | fcostcurrencyid | int8 | 64 |  | √ | 0 |  |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 21 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 22 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 23 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 24 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 26 | famounts | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 27 | fprdunit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 31 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 32 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 33 | flotnumber | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 34 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 35 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | fqualitystatus | 质量状态 | varchar | 2 |  | √ | 'A' | 质量状态,枚举: A :合格品 B :不合格品 C :待检品 D :报废品 |
| 37 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 38 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 39 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 40 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 41 | fprices | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 42 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 43 | fprdqty | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 44 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 45 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 46 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 47 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 48 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 49 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 50 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 51 | fmaindeptid | 主制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_arm_prdlentry_fokid |  | foutkeeperid |
| 2 | idx_im_arm_prdlentry_mmt |  | fmaterialmasterid |
| 3 | idx_im_arm_prdlentry_fkid |  | fkeeperid |
| 4 | idx_im_arm_prdlentry_foowid |  | foutownerid |
| 5 | pk_im_arm_prdlentry |  | fentryid |
| 6 | idx_im_arm_prdlentry_e_wh |  | fwarehouseid |
| 7 | idx_im_arm_prdlentry_fowid |  | fownerid |
| 8 | idx_im_arm_prdlentry_material |  | fmaterialid |
| 9 | idx_im_arm_prdlentry_seq |  | fid,fseq |

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

## 重复生产完工入库单-主表 t_im_arm_productinbill

- **表名称：** 重复生产完工入库单-主表
- **表名：** t_im_arm_productinbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 6 | fischargeoff | 冲销 | bpchar | 1 |  |  | null | 冲销 |
| 7 | fbiztimes | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbizorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 12 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 14 | fprdline | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 15 | funitsrctype | 计量单位来源 | varchar | 50 |  |  | null | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fischargeoffed | 已被冲销 | bpchar | 1 |  |  | null | 已被冲销 |
| 18 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 26 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fbiztypeids | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 29 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 30 | fisvoucher | 已生成凭证 | bpchar | 1 |  |  | null | 已生成凭证 |
| 31 | fbizdeptid | 车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsettlecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_arm_prdinbill_bktorno |  | fbookdate,forgid,fbillno |
| 2 | pk_im_arm_productinbill |  | fid |
| 3 | idx_im_arm_prdinbill_forgbno |  | forgid,fbillno |
| 4 | idx_im_arm_prdinbill_biztorno |  | fbiztimes,forgid,fbillno |
| 5 | idx_im_arm_prdinbill_finvsc |  | finvschemeid |

---

## 重复生产完工入库单-反写记录表 t_im_productinbill_wb

- **表名称：** 重复生产完工入库单-反写记录表
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

## 重复生产完工入库单-多语言表 t_im_arm_productinbill_l

- **表名称：** 重复生产完工入库单-多语言表
- **表名：** t_im_arm_productinbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_arm_productinbill_l |  | fid,flocaleid |
| 2 | pk_t_im_arm_productinbill_l |  | fpkid |

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

## 物料明细-分表 t_im_arm_prdlentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_arm_prdlentry_c

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
| 1 | pk_t_im_arm_prdlentry_c |  | fentryid |
| 2 | idx_fid_cur_act |  | fid,fcostaccountid,fcostcurrencyid |

---

## 物料明细-分表 t_im_arm_prdlentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_arm_prdlentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 7 | fremainreturnbaseqtys | 剩余退库基本数量 | numeric | 23 | 10 | √ | 0 | 剩余退库基本数量 |
| 8 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 11 | freturnqtys | 已退库数量 | numeric | 23 | 10 | √ | 0 | 已退库数量 |
| 12 | fremainreturnqtys | 剩余退库数量 | numeric | 23 | 10 | √ | 0 | 剩余退库数量 |
| 13 | freturnbaseqtys | 已退库基本数量 | numeric | 23 | 10 | √ | 0 | 已退库基本数量 |
| 14 | fsrcbillentity | 来源单据实体 | varchar | 100 |  | √ | ' ' | 来源单据实体 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_arm_prdlentry_r |  | fentryid |
| 2 | idx_im_arm_prdlentry_r_fid |  | fid |
