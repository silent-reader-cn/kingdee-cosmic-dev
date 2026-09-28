# 需求申请单-pm_requirapplybill

## 需求申请单-关联追踪表 t_pm_requirapplybill_tc

- **表名称：** 需求申请单-关联追踪表
- **表名：** t_pm_requirapplybill_tc

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
| 1 | idx_pm_requirapplybill_tc_tid |  | ftid |
| 2 | idx_pm_requirapplybill_tc_tbill |  | ftbillid |
| 3 | t_pm_requirapplybill_tc_pkey |  | fid |

---

## 需求申请单-主表 t_pm_requirapplybill

- **表名称：** 需求申请单-主表
- **表名：** t_pm_requirapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdeptid | 需求部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fbizuserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 11 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 14 | fbiztime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 15 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbizorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 21 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_requirapplybill_pkey |  | fid |
| 2 | idx_pm_requirapplybill_time |  | fbiztime |
| 3 | idx_pm_requirapplybill_org |  | forgid,fbiztime,fbillno |
| 4 | idx_pm_requirapply_billno_org |  | fbillno,forgid |

---

## 需求申请单-反写记录表 t_pm_requirapplybill_wb

- **表名称：** 需求申请单-反写记录表
- **表名：** t_pm_requirapplybill_wb

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
| 1 | idx_pm_requirapplybill_wb_fk |  | fid |
| 2 | t_pm_requirapplybill_wb_pkey |  | fentryid |

---

## 需求申请单-多语言表 t_pm_requirapplybill_l

- **表名称：** 需求申请单-多语言表
- **表名：** t_pm_requirapplybill_l

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
| 1 | t_pm_requirapplybill_l_pkey |  | fpkid |
| 2 | idx_pm_requirapplybill_l |  | fid,flocaleid |

---

## 关联子实体-子表 t_pm_requirapplybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_requirapplybill_lk

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
| 1 | t_pm_requirapplybill_lk_pkey |  | fpkid |
| 2 | idx_pm_requirapplybill_lk_fk |  | fid |

---

## 物料明细-子表 t_pm_requirapplybillentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_requirapplybillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 3 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fmaterialid | 物料策略(封存) | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fapplybaseqty | 已请购基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已请购基本数量 |
| 9 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fmatapplyqty | 已出库申请数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库申请数量 |
| 11 | freqdes | 需求原因 | varchar | 512 |  |  | ' ' | 需求原因 |
| 12 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | freqdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 15 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fmatoutbaseqty | 已出库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库基本数量 |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 19 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 21 | funmatapplybaseqty | 未出库申请基本数量 | numeric | 23 | 10 | √ | 0 | 未出库申请基本数量 |
| 22 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 23 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fentryorgid | 分录需求组织(封存) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | funmatapplyqty | 未出库申请数量 | numeric | 23 | 10 | √ | 0 | 未出库申请数量 |
| 26 | fsupplierid | 建议供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 27 | fmaterialmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 28 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 30 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 31 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 32 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 33 | fapplyqty | 已请购数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已请购数量 |
| 34 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fmatapplybaseqty | 已出库申请基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库申请基本数量 |
| 38 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 39 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 40 | fmatoutqty | 已出库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已出库数量 |
| 41 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_requirapplybillentry |  | fid |
| 2 | t_pm_requirapplybillentry_pkey |  | fentryid |

---

## 关联子实体-子表 t_pm_requirapplybillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_requirapplybillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fapplybaseqty_old | 已请购基本数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已请购基本数量_原始携带值 |
| 2 | fapplybaseqty | 已请购基本数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已请购基本数量_确认携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_requirapplybillentry_lk_pkey |  | fpkid |
| 2 | idx_pm_requirapplybillentry_lk_fk |  | fentryid |
