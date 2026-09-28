# 仓位移动单-im_locationtransfer

## 物料明细-分表 t_im_locationtransentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_locationtransentry_c

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
| 1 | idx_im_locationtransentry_c |  | fid |
| 2 | pk_im_locationtransentry_c |  | fentryid |

---

## 仓位移动单-多语言表 t_im_locationtransfer_l

- **表名称：** 仓位移动单-多语言表
- **表名：** t_im_locationtransfer_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | ftransfercause | 移动原因 | varchar | 255 |  | √ | ' ' | 移动原因 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_localts_l_flid |  | fid,flocaleid |
| 2 | t_im_locationtransfer_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_im_locationtransfer_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_locationtransfer_lk

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
| 1 | pk_im_locationtransfer_lk |  | fpkid |
| 2 | idx_im_locationtransfer_lk_fk |  | fid |

---

## 仓位移动单-主表 t_im_locationtransfer

- **表名称：** 仓位移动单-主表
- **表名：** t_im_locationtransfer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 9 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 14 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 17 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 22 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 25 | ftransfercause | 移动原因 | varchar | 255 |  | √ | ' ' | 移动原因 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 28 | fsettlescurrency | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_locationtransfer_pkey |  | fid |
| 2 | idx_im_localts_biztorgno |  | fbiztime,forgid,fbillno |
| 3 | idx_im_localts_forgbillno |  | fbillno,forgid |
| 4 | idx_im_localts_org |  | forgid |
| 5 | idx_im_ltbill_bktorgno |  | fbookdate,forgid,fbillno |

---

## 物料明细-子表 t_im_locationtransentry

- **表名称：** 物料明细-子表
- **表名：** t_im_locationtransentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flogisticsbill | 物流单据 | bpchar | 1 |  | √ | '0' | 物流单据 |
| 3 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | flocation | 移入仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | foutlocation | 移出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 12 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 14 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 15 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 16 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 17 | finvtype | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 18 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 20 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 23 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 26 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 28 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 31 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 32 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 33 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 35 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量(2) |
| 36 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 37 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 38 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 39 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 40 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 41 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 44 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 45 | fisfreegift | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_locationtransentry_pkey |  | fentryid |
| 2 | idx_im_localts_e_mmt |  | fmaterialmasterid |
| 3 | idx_im_localts_e_wh |  | fwarehouseid |
| 4 | idx_im_localts_e_fowid |  | fownerid |
| 5 | idx_im_localts_e_fid |  | fid |

---

## 仓位移动单-关联追踪表 t_im_locationtransfer_tc

- **表名称：** 仓位移动单-关联追踪表
- **表名：** t_im_locationtransfer_tc

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
| 1 | t_im_locationtransfer_tc_pkey |  | fid |
| 2 | idx_im_locationtsf_tc_ftbidtid |  | ftbillid,ftid |
| 3 | idx_im_locationtransfer_tc_tbill |  | ftbillid |
| 4 | idx_im_locationtransfer_tc_tid |  | ftid |

---

## 仓位移动单-反写记录表 t_im_locationtransfer_wb

- **表名称：** 仓位移动单-反写记录表
- **表名：** t_im_locationtransfer_wb

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
| 1 | t_im_locationtransfer_wb_pkey |  | fentryid |
| 2 | idx_im_locationtransfer_wb_fk |  | fid |

---

## 关联子实体-子表 t_im_locationtransentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_locationtransentry_lk

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
| 1 | t_im_locationtransentry_lk_pkey |  | fpkid |
| 2 | idx_im_locationtransentry_lk_fk |  | fentryid |
