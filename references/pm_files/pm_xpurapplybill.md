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
| 3 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 4 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 5 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 6 | freceivebaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0 | 已收货基本数量 |
| 7 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 8 | forderqty | 已订货数量 | numeric | 23 | 10 | √ | 0 | 已订货数量 |
| 9 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 10 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 11 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 12 | favinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 13 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 14 | fsalbillnumber | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 15 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 16 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 17 | forderbaseqty | 已订货基本数量 | numeric | 23 | 10 | √ | 0 | 已订货基本数量 |
| 18 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 19 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 20 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 21 | fsalbillentryseq | 销售订单分录序号 | int8 | 64 |  | √ | 0 | 销售订单分录序号 |
| 22 | fsalbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |
| 25 | fsalbillentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |

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
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsourcebillentity | 申请单实体标识 | varchar | 36 |  | √ | ' ' | 申请单实体标识 |
| 4 | fbidstatus | 竞价状态 | varchar | 5 |  | √ | ' ' | 竞价状态,枚举: A :竞价中 B :已竞价 |
| 5 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 8 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 D :原始源单备份 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 12 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 15 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 16 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fbillno | 申请单编号 | varchar | 80 |  | √ | ' ' | 申请单编号 |
| 19 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 20 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fchangereason | 变更原因 | varchar | 512 |  |  | null | 变更原因 |
| 27 | fbizuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 31 | fchangebizdate | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 32 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 33 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 34 | fchangebillno | 变更单编号 | varchar | 80 |  | √ | ' ' | 变更单编号 |
| 35 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 36 | fvalidstatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 37 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 38 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fsourcebillid | 申请单ID | int8 | 64 |  | √ | 0 | 申请单ID |
| 40 | finquirystatus | 询价状态 | varchar | 5 |  | √ | ' ' | 询价状态,枚举: A :询价中 B :已询价 |
| 41 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 42 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 43 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
| 4 | fassortbillno | 配套单据信息 | varchar | 2000 |  | √ | ' ' | 配套单据信息 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fisredordermate | 重新展算订单物料 | bpchar | 1 |  | √ | '1' | 重新展算订单物料 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 10 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fpurdate | 建议采购日期 | timestamp | 0 |  |  | null | 建议采购日期 |
| 14 | fbomtime | 展BOM时间 | timestamp | 0 |  |  | null | 展BOM时间 |
| 15 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 16 | fqty | 核准数量 | numeric | 23 | 10 | √ | 0 | 核准数量 |
| 17 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 18 | fentrysrcid | 申请单行ID | int8 | 64 |  | √ | 0 | 申请单行ID |
| 19 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 22 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fentrypurogid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fentrypurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 28 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 30 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 31 | fpurleadday | 采购提前期 | int4 | 32 |  | √ | 0 | 采购提前期 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 34 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 35 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | null | 物料名称(历史) |
| 36 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 38 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 39 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 40 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 41 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 42 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 43 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 44 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 46 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 47 | freqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 48 | fpurmethod | 采购方式 | varchar | 5 |  | √ | ' ' | 采购方式,枚举: order :订单 mall :商城 sourc :寻源 |
| 49 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 50 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 51 | fentryrecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 53 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 54 | fapplyqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 55 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 56 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

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
