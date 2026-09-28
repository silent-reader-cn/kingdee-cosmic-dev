# 采购订单变更单（废弃）-pm_xpurorderbill

## 关联子实体-子表 t_pm_purorderbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purorderbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量_确认携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purorderbillentry_lk_pkey |  | fpkid |
| 2 | idx_pm_purorderbillentry_lk_fk |  | fentryid |

---

## 物料明细-分表 t_pm_xpurorderbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_pm_xpurorderbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 3 | funjoinpricebaseqty | 未关联应付基本数量 | numeric | 23 | 10 | √ | 0 | 未关联应付基本数量 |
| 4 | finvretqty | 库存可退数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存可退数量 |
| 5 | fsoubillid | 协同单据ID | int8 | 64 |  | √ | 0 | 协同单据ID |
| 6 | freceiptnoticeqty | 已收货通知数量 | numeric | 23 | 10 | √ | 0 | 已收货通知数量 |
| 7 | finvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库基本数量 |
| 8 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | 核心单据实体 |
| 9 | freturnbaseqty | 已退库基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库基本数量 |
| 10 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 11 | fconbillrownum | 合同行号 | varchar | 50 |  | √ | ' ' | 合同行号 |
| 12 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 13 | fjoinpriceqty | 关联应付数量 | numeric | 23 | 10 | √ | 0 | 关联应付数量 |
| 14 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 15 | funjoinpurinvoiceqty | 应付未关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票数量 |
| 16 | freceivebaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货基本数量 |
| 17 | fjoinbusqty | 暂估应付数量 | numeric | 23 | 10 | √ | 0 | 暂估应付数量 |
| 18 | fsrcsysbillno | 来源系统编号 | varchar | 100 |  | √ | ' ' | 来源系统编号 |
| 19 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 20 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库数量 |
| 23 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 24 | fsoubillnumber | 协同单据编号 | varchar | 80 |  | √ | ' ' | 协同单据编号 |
| 25 | freceiptnoticbaseqty | 已收货通知基本数量 | numeric | 23 | 10 | √ | 0 | 已收货通知基本数量 |
| 26 | fjoinbusunwoffqty | 暂估应付未冲回数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量 |
| 27 | fsalbillentryseq | 销售订单分录序号 | int8 | 64 |  | √ | 0 | 销售订单分录序号 |
| 28 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 29 | fsalbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 30 | frecretqty | 收货可退数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货可退数量 |
| 31 | freturnreceiptqty | 已退验数量 | numeric | 23 | 10 | √ | 0 | 已退验数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fsoubillentryseq | 协同单据分录序号 | int8 | 64 |  | √ | 0 | 协同单据分录序号 |
| 34 | fjoinbusbaseqty | 暂估应付基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付基本数量 |
| 35 | fsalbillentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |
| 36 | freceiveqty | 已收货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货数量 |
| 37 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 38 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 39 | fjoinpurinvoicebaseqty | 关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票基本数量 |
| 40 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 41 | frecretbaseqty | 收货可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货可退基本数量 |
| 42 | fperformamount | 执行金额 | numeric | 23 | 10 | √ | 0 | 执行金额 |
| 43 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 44 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 45 | fjoinpricebaseqty | 关联应付基本数量 | numeric | 23 | 10 | √ | 0 | 关联应付基本数量 |
| 46 | fjoinpayablebaseqty | 关联验收应付基本数量 | numeric | 23 | 10 | √ | 0 | 关联验收应付基本数量 |
| 47 | finvretbaseqty | 库存可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存可退基本数量 |
| 48 | fpayablebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0 | 应付基本数量 |
| 49 | funjoinpurinvoicebaseqty | 应付未关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票基本数量 |
| 50 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 51 | funjoinpriceqty | 未关联应付数量 | numeric | 23 | 10 | √ | 0 | 未关联应付数量 |
| 52 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 53 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 54 | fconbillentryseq | 合同分录序号 | varchar | 50 |  | √ | ' ' | 合同分录序号 |
| 55 | fjoinamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 56 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 57 | fsalbillnumber | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 58 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 59 | fjoinpurinvoiceamount | 关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联采购发票价税合计 |
| 60 | fsoubillentryid | 协同单据行ID | int8 | 64 |  | √ | 0 | 协同单据行ID |
| 61 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 62 | fjoinbusunwoffbaseqty | 暂估应付未冲回基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量 |
| 63 | fpayablepriceqty | 应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付数量 |
| 64 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 65 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 66 | fsoubillentity | 协同单据实体 | varchar | 36 |  | √ | ' ' | 协同单据实体 |
| 67 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 68 | fjoinpayablepriceqty | 关联验收应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联验收应付数量 |
| 69 | fjoinpurinvoiceqty | 关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票数量 |
| 70 | freturnreceiptbaseqty | 已退验基本数量 | numeric | 23 | 10 | √ | 0 | 已退验基本数量 |
| 71 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |
| 72 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_xpurorderbillentry_r_pkey |  | fentryid |
| 2 | idx_pm_xpobillentry_r |  | fid |

---

## 采购订单变更单（废弃）-反写记录表 t_pm_purorderbill_wb

- **表名称：** 采购订单变更单（废弃）-反写记录表
- **表名：** t_pm_purorderbill_wb

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
| 1 | idx_pm_purorderbill_wb_fk |  | fid |
| 2 | t_pm_purorderbill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_pm_purorderbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purorderbill_lk

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
| 1 | idx_pm_purorderbill_lk_fk |  | fid |
| 2 | t_pm_purorderbill_lk_pkey |  | fpkid |

---

## 采购订单变更单（废弃）-多语言表 t_pm_xpurorderbill_l

- **表名称：** 采购订单变更单（废弃）-多语言表
- **表名：** t_pm_xpurorderbill_l

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
| 1 | t_pm_xpurorderbill_l_pkey |  | fpkid |
| 2 | idx_pm_xpurorderbill_l |  | fid,flocaleid |

---

## 采购订单变更单（废弃）-关联追踪表 t_pm_purorderbill_tc

- **表名称：** 采购订单变更单（废弃）-关联追踪表
- **表名：** t_pm_purorderbill_tc

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
| 1 | t_pm_purorderbill_tc_pkey |  | fid |
| 2 | idx_pm_purorderbill_tc_tbill |  | ftbillid |
| 3 | idx_pm_purorderbill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_pm_purorderpayentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_purorderpayentry_lk

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
| 1 | t_pm_purorderpayentry_lk_pkey |  | fpkid |
| 2 | idx_pm_purorderpayentry_lk_fk |  | fentryid |

---

## 采购订单变更单（废弃）-主表 t_pm_xpurorderbill

- **表名称：** 采购订单变更单（废弃）-主表
- **表名：** t_pm_xpurorderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpaidallamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 3 | faddress | 联系地址 | varchar | 512 |  | √ | ' ' | 联系地址 |
| 4 | fsourcebillentity | fsourcebillentity | varchar | 36 |  | √ | ' ' |  |
| 5 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | 供应商联系人 bd_supplierlinkman |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 8 | fsourceid | 订单ID | int8 | 64 |  | √ | 0 | 订单ID |
| 9 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 10 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 11 | fchangecanceler | fchangecanceler | int8 | 64 |  | √ | 0 |  |
| 12 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 13 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | 结算路径 ism_settlerelations |
| 14 | fsplitschemeid | 付款计划方案 | int8 | 64 |  | √ | 0 | 付款计划方案 ap_plansplit_scheme |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 17 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 18 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 19 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 21 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 24 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 27 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | freason | 变更原因 | varchar | 512 |  |  | ' ' | 变更原因 |
| 30 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 31 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 32 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 33 | fpaidpreallamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 34 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 35 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 37 | fsourcebiztime | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 38 | fsettleorgid | 结算组织(废弃) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | 供应商联系人 bd_supplierlinkman |
| 40 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 41 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 44 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 45 | fdiscountlist | 折扣表 | int8 | 64 |  | √ | 0 | 采购折扣表 pm_purdiscountlist |
| 46 | fconfirmstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :自动确认 |
| 47 | fbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 48 | flogisticsstatus | 物流状态 | varchar | 5 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 49 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 50 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 51 | fprovideraddress | 供货联系地址 | varchar | 512 |  |  | ' ' | 供货联系地址 |
| 52 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fpaystatus | 付款状态 | varchar | 5 |  | √ | ' ' | 付款状态,枚举: A :待付款 B :部分付款 C :已付款 |
| 54 | factiverid | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 55 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | 采购价目表 pm_purpricelist |
| 56 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 57 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 58 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 59 | fsourceno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |
| 60 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 61 | fsourcestatus | 订单状态 | varchar | 5 |  | √ | ' ' | 订单状态,枚举: |
| 62 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 63 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 64 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 65 | factivestatus | 生效状态 | varchar | 5 |  | √ | ' ' | 生效状态,枚举: A :未生效 B :已生效 |
| 66 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 67 | fchangecanceldate | fchangecanceldate | timestamp | 0 |  |  | null |  |
| 68 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 69 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 70 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 71 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 72 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 73 | fprovidersupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 74 | fchangecancelstatus | fchangecancelstatus | varchar | 5 |  | √ | ' ' |  |
| 75 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 76 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 77 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 78 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 79 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 80 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 81 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 82 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 83 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 84 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xpurorder_billno_org |  | fbillno,forgid |
| 2 | idx_pm_xpurorderbill_time |  | fbiztime |
| 3 | idx_pm_xpurorderbill_org |  | forgid,fbiztime,fbillno |
| 4 | t_pm_xpurorderbill_pkey |  | fid |

---

## 交货计划-子表 t_pm_purorderdeliverentry

- **表名称：** 交货计划-子表
- **表名：** t_pm_purorderdeliverentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplanqty | 计划交货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 计划交货数量 |
| 2 | fdeliveryaddress | 交货地址 | varchar | 512 |  | √ | ' ' | 交货地址 |
| 3 | fplandeliverdate | 计划交货日期 | timestamp | 0 |  |  | null | 计划交货日期 |
| 4 | fplanuninvbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0 | 未入库基本数量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fconfirmdeliverydate | 确认交货日期 | timestamp | 0 |  |  | null | 确认交货日期 |
| 7 | fplanreceiveqty | 已交货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已交货数量 |
| 8 | fdelentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 9 | fplaninvbaseqty | 已入库基本数量 | numeric | 23 | 10 | √ | 0 | 已入库基本数量 |
| 10 | fbaseconfirmdeliveryqty | 确认交货基本数量 | numeric | 23 | 10 | √ | 0 | 确认交货基本数量 |
| 11 | fdeliveryplace | 交货地点 | varchar | 512 |  | √ | ' ' | 交货地点 |
| 12 | fdelentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fplancomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fbaseplanunitid | 交货计划基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fbaseplanqty | 计划交货基本数量 | numeric | 23 | 10 | √ | 0 | 计划交货基本数量 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fdelentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fbaseplanreceiveqty | 已交货基本数量 | numeric | 23 | 10 | √ | 0 | 已交货基本数量 |
| 19 | fplanuninvqty | 未入库数量 | numeric | 23 | 10 | √ | 0 | 未入库数量 |
| 20 | fplaninvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 21 | fdelentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fsurplusqty | 未交货数量 | numeric | 23 | 10 | √ | 0 | 未交货数量 |
| 23 | fplanunitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fconfirmdeliveryqty | 确认交货数量 | numeric | 23 | 10 | √ | 0 | 确认交货数量 |
| 25 | fplanreceivedate | 收货日期（废弃） | timestamp | 0 |  |  | null | 收货日期（废弃） |
| 26 | flatestdeliverydate | 最近交货日期 | timestamp | 0 |  |  | null | 最近交货日期 |
| 27 | fbasesurplusqty | 未交货基本数量 | numeric | 23 | 10 | √ | 0 | 未交货基本数量 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 29 | fdelentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purorderdeliverentry_pkey |  | fdetailid |
| 2 | idx_pm_podeliverentry |  | fentryid |

---

## 物料明细-子表 t_pm_xpurorderbillentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_xpurorderbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqtyup | 收货上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货上限数量 |
| 3 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 6 | fiscontrolqty | 控制收货数量 | bpchar | 1 |  | √ | '0' | 控制收货数量 |
| 7 | fdeliverlocationid | 交货地点 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 8 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 9 | fsourceentryid | 订单行ID | int8 | 64 |  | √ | 0 | 订单行ID |
| 10 | freceiverateup | 收货超收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货超收比率(%) |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fentrysettledeptid | 结算部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 15 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 18 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 20 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 24 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 25 | freceivebaseqtydown | 收货下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货下限基本数量 |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 28 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fdeliveraddress | 交货地址 | varchar | 512 |  |  | ' ' | 交货地址 |
| 30 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 31 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 32 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 33 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 34 | freceivebaseqtyup | 收货上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货上限基本数量 |
| 35 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 38 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 39 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 41 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 44 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 45 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 48 | fentrypayorgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 49 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 50 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 51 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 53 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 54 | freceiveqtydown | 收货下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货下限数量 |
| 55 | fsupplierlot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 56 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 57 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 58 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 59 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 60 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 61 | freceiveratedown | 收货欠收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货欠收比率(%) |
| 62 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 63 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 64 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 65 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 66 | fiscontrolamountup | 控制上限金额 | bpchar | 1 |  | √ | '0' | 控制上限金额 |
| 67 | fiscontrolday | 控制时间 | bpchar | 1 |  | √ | '0' | 控制时间 |
| 68 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 69 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 70 | fentryrecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 71 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 72 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 73 | freceivedayup | 允许提前天数 | int4 | 32 |  | √ | 0 | 允许提前天数 |
| 74 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 75 | famountup | 上限金额 | numeric | 23 | 10 | √ | 0 | 上限金额 |
| 76 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 77 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 78 | fentrypurorgid | 分录采购组织(封存) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 79 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 80 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 81 | freceivedaydown | 允许延迟天数 | int4 | 32 |  | √ | 0 | 允许延迟天数 |
| 82 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_xpurorderbillentry |  | fid |
| 2 | t_pm_xpurorderbillentry_pkey |  | fentryid |

---

## 付款计划-子表 t_pm_xpurorderpayentry

- **表名称：** 付款计划-子表
- **表名：** t_pm_xpurorderpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoicedamount | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 3 | fplanprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 4 | fplanmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpayamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 7 | fpayentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fplanmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 9 | fplanmainbillnumber | 核心单据号 | varchar | 80 |  | √ | ' ' | 核心单据号 |
| 10 | fisprepay | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 11 | fplanentrysettleorg | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fpayentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fpayprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 14 | fprepaybillno | 预付款单编号 | varchar | 80 |  | √ | ' ' | 预付款单编号 |
| 15 | fplanexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 16 | fjoinpayamount | 关联付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联付款金额 |
| 17 | fpayentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fpaypriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 19 | fplanconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 20 | fplanentrycomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fpayentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 22 | fpayentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fpayrate | 应付比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 应付比例(%) |
| 24 | fpaidamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 25 | fsourcepayentryid | 订单付款计划ID | int8 | 64 |  | √ | 0 | 订单付款计划ID |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fpaynameid | 款项名称 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 28 | fpaydate | 到期日 | timestamp | 0 |  |  | null | 到期日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_xpurorderpayentry_pkey |  | fentryid |
| 2 | idx_pm_xpurorderpayentry |  | fid |
