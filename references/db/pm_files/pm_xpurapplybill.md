# 采购申请变更单-pm_xpurapplybill

## 采购申请变更单-反写记录表 t_pm_purapplybill_wb

- **表名称：** 采购申请变更单-反写记录表
- **表名：** t_pm_purapplybill_wb

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
| 1 | idx_pm_purapplybill_wb_fk |  | fid |
| 2 | t_pm_purapplybill_wb_pkey |  | fentryid |

---

## 物料明细-分表 t_pm_xpurapplybillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_pm_xpurapplybillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqty | 已收货数量 | numeric | 23 | 10 | √ | 0 | 已收货数量 |
| 3 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 4 | fjointracesourceqty | 关联寻源数量 | numeric | 23 | 10 | √ | 0 | 关联寻源数量 |
| 5 | ftracesourcetype | 寻源方式 | varchar | 50 |  | √ | ' ' | 寻源方式,枚举: INQUIRY :询价 BIDDING :竞价 INVITE_BIDS :招标 |
| 6 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 7 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 8 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fconbillnumber | 合同编号 | varchar | 100 |  | √ | ' ' | 合同编号 |
| 11 | freceivebaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0 | 已收货基本数量 |
| 12 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 13 | forderqty | 已订货数量 | numeric | 23 | 10 | √ | 0 | 已订货数量 |
| 14 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 15 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 16 | fconbillentryseq | 合同分录序号 | varchar | 50 |  | √ | ' ' | 合同分录序号 |
| 17 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 18 | favinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 19 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 20 | fsalbillnumber | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 23 | forderbaseqty | 已订货基本数量 | numeric | 23 | 10 | √ | 0 | 已订货基本数量 |
| 24 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 25 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 26 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 27 | fsalbillentryseq | 销售订单分录序号 | int8 | 64 |  | √ | 0 | 销售订单分录序号 |
| 28 | fsalbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 29 | ftracesourcestatus | 寻源状态 | varchar | 50 |  | √ | ' ' | 寻源状态,枚举: TRACING :寻源中 TRACED :已寻源 |
| 30 | fjointracesourcebaseqty | 关联寻源基本数量 | numeric | 23 | 10 | √ | 0 | 关联寻源基本数量 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |
| 33 | fsalbillentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xpabillentry_r |  | fid |
| 2 | pk_t_pm_xpurapplybillentry_r |  | fentryid |

---

## 采购申请变更单-主表 t_pm_xpurapplybill

- **表名称：** 采购申请变更单-主表
- **表名：** t_pm_xpurapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsourcebillentity | 申请单实体标识 | varchar | 36 |  | √ | ' ' | 申请单实体标识 |
| 4 | fbidstatus | 竞价状态 | varchar | 5 |  | √ | ' ' | 竞价状态,枚举: A :竞价中 B :已竞价 |
| 5 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 8 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 D :原始源单备份 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 12 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 15 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 16 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillno | 申请单编号 | varchar | 80 |  | √ | ' ' | 申请单编号 |
| 19 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 20 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |
| 21 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fchangereason | 变更原因 | varchar | 512 |  |  | null | 变更原因 |
| 28 | fbizuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 30 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 33 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 34 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 35 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 36 | fchangebillno | 变更单编号 | varchar | 80 |  | √ | ' ' | 变更单编号 |
| 37 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 38 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 39 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 40 | fmanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 41 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fsourcebillid | 申请单ID | int8 | 64 |  | √ | 0 | 申请单ID |
| 43 | finquirystatus | 寻源状态 | varchar | 5 |  | √ | ' ' | 寻源状态,枚举: A :寻源中 B :已寻源 |
| 44 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 45 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 46 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_xpurapplybill |  | fid |
| 2 | idx_pm_xpurapply_billno_org |  | fchangebillno,forgid |
| 3 | idx_pm_xpurapplybill_biztime |  | fchangebizdate |
| 4 | idx_pm_xpurapplybill_org |  | forgid,fchangebillno,fchangebizdate |

---

## 采购申请变更单-多语言表 t_pm_xpurapplybill_l

- **表名称：** 采购申请变更单-多语言表
- **表名：** t_pm_xpurapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xpurapplybill_l |  | fid,flocaleid |
| 2 | pk_t_pm_xpurapplybill_l |  | fpkid |

---

## 关联子实体-子表 t_pm_purapplybillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purapplybillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fapplyqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_确认携带值 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 9 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 10 | fapplyqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 数量_原始携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purapplybillentry_lk_pkey |  | fpkid |
| 2 | idx_pm_purapplybillentry_lk_fk |  | fentryid |

---

## 采购申请变更单-关联追踪表 t_pm_purapplybill_tc

- **表名称：** 采购申请变更单-关联追踪表
- **表名：** t_pm_purapplybill_tc

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
| 1 | t_pm_purapplybill_tc_pkey |  | fid |
| 2 | idx_pm_purapplybill_tc_tid |  | ftid |
| 3 | idx_pm_purapplybill_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_pm_purapplybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purapplybill_lk

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
| 1 | t_pm_purapplybill_lk_pkey |  | fpkid |
| 2 | idx_pm_purapplybill_lk_fk |  | fid |

---

## 物料明细-子表 t_pm_xpurapplybillentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_xpurapplybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 5 | fassortbillno | 配套单据信息 | varchar | 2000 |  | √ | ' ' | 配套单据信息 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fisredordermate | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | frootdemandentryseq | 根需求单据分录行号 | int4 | 32 |  | √ | 0 | 根需求单据分录行号 |
| 10 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 12 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fpurdate | 建议采购日期 | timestamp | 0 |  |  | null | 建议采购日期 |
| 16 | fbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 17 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 18 | fqty | 核准数量 | numeric | 23 | 10 | √ | 0 | 核准数量 |
| 19 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 20 | fentrysrcid | 申请单行ID | int8 | 64 |  | √ | 0 | 申请单行ID |
| 21 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fentrymanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 25 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 28 | fentrypurogid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fentrypurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 34 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0 | 件数 |
| 35 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 36 | fpurleadday | 采购提前期 | int4 | 32 |  | √ | 0 | 采购提前期 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 39 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 40 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | null | 物料名称(历史) |
| 41 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 43 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 44 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 45 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 46 | frootdemandentity | 根需求单据实体 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 47 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 48 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 49 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 50 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 51 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 52 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 54 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 55 | freqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 56 | frootdemandbillno | 根需求单据编码 | varchar | 120 |  | √ | ' ' | 根需求单据编码 |
| 57 | fpurmethod | 采购方式 | varchar | 5 |  | √ | ' ' | 采购方式,枚举: order :订单 mall :商城 sourc :寻源 |
| 58 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 59 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 60 | fentryrecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 61 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 63 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 64 | fapplyqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 65 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 66 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xprentry_matastertid |  | fmaterialmasterid,fid |
| 2 | idx_pm_xpurapplybillentry |  | fid |
| 3 | pk_t_pm_xpurapplybillentry |  | fentryid |
| 4 | idx_pm_xprentry_matid |  | fmaterialid,fid |
