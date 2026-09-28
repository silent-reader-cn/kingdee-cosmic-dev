# 委外完工入库单-im_mdc_omprdinbill

## 委外完工入库单-关联追踪表 t_im_productinbill_tc

- **表名称：** 委外完工入库单-关联追踪表
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

## 委外完工入库单-反写记录表 t_im_productinbill_wb

- **表名称：** 委外完工入库单-反写记录表
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

## 委外完工入库单-主表 t_im_mdc_omprdin

- **表名称：** 委外完工入库单-主表
- **表名：** t_im_mdc_omprdin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 6 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 9 | fischargeoff | 冲销 | bpchar | 1 |  | √ | '0' | 冲销 |
| 10 | finnerbilltype | 内部交易单据类别 | varchar | 50 |  | √ | ' ' | 内部交易单据类别,枚举: in :对内 out :对外 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 12 | fbiztimes | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fasyncstatus | 异步状态 | varchar | 50 |  | √ | ' ' | 异步状态,枚举: A :处理中 B :已完成 |
| 17 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 18 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | funitsrctype | 计量单位来源 | varchar | 50 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 23 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 29 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 32 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 33 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 34 | fsupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 35 | fproduceorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fbiztypeids | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 37 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 38 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 39 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_omprdin |  | fid |

---

## 委外完工入库单-多语言表 t_im_mdc_omprdin_l

- **表名称：** 委外完工入库单-多语言表
- **表名：** t_im_mdc_omprdin_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_omprdin_l |  | fid,flocaleid |
| 2 | pk_im_mdc_omprdin_l |  | fpkid |

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

## 物料明细-子表 t_im_mdc_omprdinentry

- **表名称：** 物料明细-子表
- **表名：** t_im_mdc_omprdinentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcrosslegalperson | 是否跨法人 | varchar | 5 |  | √ | '0' | 是否跨法人,枚举: 0 :否 1 :是 |
| 3 | fproductnum | 生产编号 | varchar | 255 |  | √ | ' ' | 生产编号 |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 6 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 11 | foutkeepertype | 出库保管者类型 | varchar | 50 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 14 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 15 | fownertype | 入库货主类型 | varchar | 50 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 17 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 21 | foutownertype | 出库货主类型 | varchar | 50 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fprices | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 26 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fkeepertype | 入库保管者类型 | varchar | 50 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 28 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 29 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 30 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 31 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 32 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 34 | famounts | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 35 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 36 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 37 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 38 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 39 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 41 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 42 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 43 | fmaindeptid | 主制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 46 | fendwork | 完工 | bpchar | 1 |  | √ | '0' | 完工 |
| 47 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 48 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_omprdinentry |  | fentryid |
| 2 | idx_im_omprdinentry_fid |  | fid |

---

## 物料明细-分表 t_im_mdc_omprdinentry_c

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_omprdinentry_c

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
| 1 | idx_im_omprdinentry_c_fid |  | fid |
| 2 | pk_im_mdc_omprdinentry_c |  | fentryid |

---

## 物料明细-分表 t_im_mdc_omprdinentry_m

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_omprdinentry_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyaddress | 供货地址 | varchar | 512 |  | √ | ' ' | 供货地址 |
| 3 | fdownreturnbaseqty | 关联退库基本数量 | numeric | 23 | 10 | √ | 0 | 关联退库基本数量 |
| 4 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 5 | fmanuentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 6 | fsampledestorybsqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 7 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 8 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 9 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 10 | fqualitystatus | 质量状态 | varchar | 50 |  | √ | ' ' | 质量状态,枚举: A :合格品 B :不合格品 C :待检品 D :报废品 |
| 11 | fpurorderseq | 采购订单行号 | varchar | 50 |  | √ | ' ' | 采购订单行号 |
| 12 | fdownreturnqty | 关联退库数量 | numeric | 23 | 10 | √ | 0 | 关联退库数量 |
| 13 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 14 | fpurorderno | 采购订单编号 | varchar | 50 |  | √ | ' ' | 采购订单编号 |
| 15 | fprdunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fpid | 联副产品父ID | varchar | 50 |  | √ | ' ' | 联副产品父ID |
| 17 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | frejectdiscountamount | 不良品折让金额 | numeric | 23 | 10 | √ | 0 | 不良品折让金额 |
| 19 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 20 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fisadd | 是否新增行 | bpchar | 1 |  | √ | '0' | 是否新增行 |
| 22 | fpurinentryid | 采购入库单行ID | int8 | 64 |  | √ | 0 | 采购入库单行ID |
| 23 | fpurinno | 采购入库单号 | varchar | 252 |  | √ | ' ' | 采购入库单号 |
| 24 | fmanuentry | 委外工单行号 | varchar | 50 |  | √ | ' ' | 委外工单行号 |
| 25 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |
| 26 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 27 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 28 | fmanubillid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 29 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 30 | fsupplyperson | 供货联系人 | int8 | 64 |  | √ | 0 | 供应商联系人 bd_supplierlinkman |
| 31 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 32 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 33 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 34 | fprdqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 35 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 36 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 37 | fiscopy | 是否复制行 | bpchar | 1 |  | √ | '0' | 是否复制行 |
| 38 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 39 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 40 | fshipperid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fpurinid | 采购入库单ID | int8 | 64 |  | √ | 0 | 采购入库单ID |
| 42 | fbackflushstatus | 倒冲标识 | varchar | 50 |  | √ | ' ' | 倒冲标识,枚举: B :部分倒冲 C :倒冲成功 D : |
| 43 | fmanubill | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_omprdinentry_m |  | fentryid |
| 2 | idx_im_omprdinentry_m_fid |  | fid |

---

## 物料明细-分表 t_im_mdc_omprdinentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_mdc_omprdinentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 7 | fremainreturnbaseqtys | 剩余退库基本数量 | numeric | 23 | 10 | √ | 0 | 剩余退库基本数量 |
| 8 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 11 | freturnqtys | 已退库数量 | numeric | 23 | 10 | √ | 0 | 已退库数量 |
| 12 | fremainreturnqtys | 剩余退库数量 | numeric | 23 | 10 | √ | 0 | 剩余退库数量 |
| 13 | freturnbaseqtys | 已退库基本数量 | numeric | 23 | 10 | √ | 0 | 已退库基本数量 |
| 14 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
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
| 1 | idx_im_omprdinentry_r_fid |  | fid |
| 2 | pk_im_mdc_omprdinentry_r |  | fentryid |
