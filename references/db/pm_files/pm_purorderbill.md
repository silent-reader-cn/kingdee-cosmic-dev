# 采购订单-pm_purorderbill

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

## 采购订单-多语言表 t_pm_purorderbill_l

- **表名称：** 采购订单-多语言表
- **表名：** t_pm_purorderbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purorderbill_l_pkey |  | fpkid |
| 2 | idx_pm_purorderbill_l |  | fid,flocaleid |

---

## 采购订单-反写记录表 t_pm_purorderbill_wb

- **表名称：** 采购订单-反写记录表
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

## 采购订单-关联追踪表 t_pm_purorderbill_tc

- **表名称：** 采购订单-关联追踪表
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

## 物料明细-分表 t_pm_purorderbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_pm_purorderbillentry_r

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
| 12 | freleasedupqty | 已释放上游单据数量 | numeric | 23 | 10 | √ | 0 | 已释放上游单据数量 |
| 13 | fconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 14 | fjoinpriceqty | 关联应付数量 | numeric | 23 | 10 | √ | 0 | 关联应付数量 |
| 15 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 16 | funreceiveqty | 未收货数量 | numeric | 23 | 10 | √ | 0 | 未收货数量 |
| 17 | fexecutedamountandtax | 已执行价税合计 | numeric | 23 | 10 | √ | 0 | 已执行价税合计 |
| 18 | funjoinpurinvoiceqty | 应付未关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票数量 |
| 19 | freceivebaseqty | 已收货基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货基本数量 |
| 20 | fjoinbusqty | 暂估应付数量 | numeric | 23 | 10 | √ | 0 | 暂估应付数量 |
| 21 | fsrcsysbillno | 来源系统编号 | varchar | 100 |  | √ | ' ' | 来源系统编号 |
| 22 | freleasedamountandtax | 已释放价税合计 | numeric | 23 | 10 | √ | 0 | 已释放价税合计 |
| 23 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 24 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 25 | freleasedamount | 已释放金额 | numeric | 23 | 10 | √ | 0 | 已释放金额 |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 27 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已入库数量 |
| 28 | fmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 29 | fsoubillnumber | 协同单据编号 | varchar | 80 |  | √ | ' ' | 协同单据编号 |
| 30 | freceiptnoticbaseqty | 已收货通知基本数量 | numeric | 23 | 10 | √ | 0 | 已收货通知基本数量 |
| 31 | freleasedcuramountandtax | 已释放价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 已释放价税合计(本位币) |
| 32 | fjoinbusunwoffqty | 暂估应付未冲回数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量 |
| 33 | freleasedupbaseqty | 已释放上游单据基本数量 | numeric | 23 | 10 | √ | 0 | 已释放上游单据基本数量 |
| 34 | fsalbillentryseq | 销售订单分录序号 | int8 | 64 |  | √ | 0 | 销售订单分录序号 |
| 35 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 36 | fsalbillid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 37 | freleasedcuramount | 已释放金额(本位币) | numeric | 23 | 10 | √ | 0 | 已释放金额(本位币) |
| 38 | frecretqty | 收货可退数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货可退数量 |
| 39 | freturnreceiptqty | 已退验数量 | numeric | 23 | 10 | √ | 0 | 已退验数量 |
| 40 | fjoinpushamountandtax | 关联下推价税合计 | numeric | 23 | 10 | √ | 0 | 关联下推价税合计 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 42 | fsoubillentryseq | 协同单据分录序号 | int8 | 64 |  | √ | 0 | 协同单据分录序号 |
| 43 | fjoinbusbaseqty | 暂估应付基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付基本数量 |
| 44 | fsalbillentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |
| 45 | freceiveqty | 已收货数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已收货数量 |
| 46 | fconbillid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 47 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 48 | fjoinpurinvoicebaseqty | 关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票基本数量 |
| 49 | fconbillentity | 合同实体 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 50 | frecretbaseqty | 收货可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货可退基本数量 |
| 51 | fperformamount | 执行金额 | numeric | 23 | 10 | √ | 0 | 执行金额 |
| 52 | fconbillentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 53 | fmftorderid | 委外工单ID | int8 | 64 |  | √ | 0 | 委外工单ID |
| 54 | fjoinpricebaseqty | 关联应付基本数量 | numeric | 23 | 10 | √ | 0 | 关联应付基本数量 |
| 55 | fjoinpayablebaseqty | 关联验收应付基本数量 | numeric | 23 | 10 | √ | 0 | 关联验收应付基本数量 |
| 56 | finvretbaseqty | 库存可退基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 库存可退基本数量 |
| 57 | fpayablebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0 | 应付基本数量 |
| 58 | funjoinpurinvoicebaseqty | 应付未关联采购发票基本数量 | numeric | 23 | 10 | √ | 0 | 应付未关联采购发票基本数量 |
| 59 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 60 | funjoinpriceqty | 未关联应付数量 | numeric | 23 | 10 | √ | 0 | 未关联应付数量 |
| 61 | fmftorderentryseq | 委外工单分录序号 | int8 | 64 |  | √ | 0 | 委外工单分录序号 |
| 62 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 63 | funinvbaseqty | 未入库基本数量 | numeric | 23 | 10 | √ | 0 | 未入库基本数量 |
| 64 | fconbillentryseq | 合同分录序号 | varchar | 50 |  | √ | ' ' | 合同分录序号 |
| 65 | fjoinamount | 关联金额 | numeric | 23 | 10 | √ | 0 | 关联金额 |
| 66 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联基本数量 |
| 67 | fsalbillnumber | 销售订单编号 | varchar | 80 |  | √ | ' ' | 销售订单编号 |
| 68 | freturnqty | 已退库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已退库数量 |
| 69 | fjoinpurinvoiceamount | 关联采购发票价税合计 | numeric | 23 | 10 | √ | 0 | 关联采购发票价税合计 |
| 70 | fsoubillentryid | 协同单据行ID | int8 | 64 |  | √ | 0 | 协同单据行ID |
| 71 | funinvqty | 未入库数量 | numeric | 23 | 10 | √ | 0 | 未入库数量 |
| 72 | fmftorderentryid | 委外工单行ID | int8 | 64 |  | √ | 0 | 委外工单行ID |
| 73 | fjoinbusunwoffbaseqty | 暂估应付未冲回基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量 |
| 74 | fpayablepriceqty | 应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应付数量 |
| 75 | fproducttype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 76 | fmftorderentrypid | 委外工单行父id | int8 | 64 |  | √ | 0 | 委外工单行父id |
| 77 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 78 | fsoubillentity | 协同单据实体 | varchar | 36 |  | √ | ' ' | 协同单据实体 |
| 79 | funreceivebaseqty | 未收货基本数量 | numeric | 23 | 10 | √ | 0 | 未收货基本数量 |
| 80 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 81 | fjoinpayablepriceqty | 关联验收应付数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联验收应付数量 |
| 82 | fjoinpurinvoiceqty | 关联采购发票数量 | numeric | 23 | 10 | √ | 0 | 关联采购发票数量 |
| 83 | freturnreceiptbaseqty | 已退验基本数量 | numeric | 23 | 10 | √ | 0 | 已退验基本数量 |
| 84 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |
| 85 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_pobillentry_r |  | fid |
| 2 | t_pm_purorderbillentry_r_pkey |  | fentryid |

---

## 回款依据-子表 t_pm_purorderpayrefentry

- **表名称：** 回款依据-子表
- **表名：** t_pm_purorderpayrefentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbtbpraentprojectid | 父项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fbtbprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fbtblinkedphaseid | 关联阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 5 | fbtbispraent | 按父项目回款 | bpchar | 1 |  | √ | '0' | 按父项目回款 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbtblinkedmilestoneid | 关联里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purorderpayrefentry |  | fid |
| 2 | pk_t_pm_purorderpayrefentry |  | fentryid |

---

## 付款计划-子表 t_pm_purorderpayentry

- **表名称：** 付款计划-子表
- **表名：** t_pm_purorderpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 3 | finvoicedamount | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 4 | fplanprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fplanmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 6 | fk_bj73_qtyfield | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fpayamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 9 | fplanprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 10 | fpayentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fplanmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 12 | fplanmainbillnumber | 核心单据号 | varchar | 80 |  | √ | ' ' | 核心单据号 |
| 13 | fisprepay | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 14 | fplanentrysettleorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fplanbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 16 | fpayentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fpayprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 18 | fprepaybillno | 预付款单编号 | varchar | 80 |  | √ | ' ' | 预付款单编号 |
| 19 | fplanexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | fplanmilestone | 里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 21 | fjoinpayamount | 关联付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 关联付款金额 |
| 22 | fpayentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fpaypriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 24 | fplanconbillnumber | 合同编号 | varchar | 255 |  | √ | ' ' | 合同编号 |
| 25 | fplanentrycomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 26 | fplanlicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 27 | fpayentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 28 | fpayentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fpayrate | 应付比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 应付比例(%) |
| 30 | fpaidamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 31 | fk_bj73_unitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fpaynameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 34 | fpaydate | 到期日 | timestamp | 0 |  |  | null | 到期日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_purorderpayentry_pkey |  | fentryid |
| 2 | idx_pm_purorderpayentry |  | fid |

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

## 物料明细-子表 t_pm_purorderbillentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_purorderbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqtyup | 收货上限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货上限数量 |
| 3 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.0000000000 | 单位折扣(率) |
| 4 | fdeliverlocationid | 交货地点 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frootdemandentryseq | 根需求单据分录行号 | int4 | 32 |  | √ | 0 | 根需求单据分录行号 |
| 8 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fprojectconfqty | 已确认项目服务数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务数量 |
| 10 | fdeliverdate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 11 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 金额(本位币) |
| 13 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | freceivebaseqtydown | 收货下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货下限基本数量 |
| 15 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 16 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 17 | fdeliveraddress | 交货地址 | varchar | 512 |  |  | ' ' | 交货地址 |
| 18 | freceivebaseqtyup | 收货上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货上限基本数量 |
| 19 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 22 | fprojectassamount | 关联项目结算额 | numeric | 23 | 10 | √ | 0 | 关联项目结算额 |
| 23 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fmaterialmasterid | 主物料(封存) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 25 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fmatchtype | 匹配类型 | bpchar | 1 |  | √ | ' ' | 匹配类型,枚举: A :订单匹配合同 |
| 27 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fentrychangetype | 变更方式 | varchar | 5 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 30 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 31 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 32 | freceiveqtydown | 收货下限数量 | numeric | 23 | 10 | √ | 0.0000000000 | 收货下限数量 |
| 33 | fsupplierlot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 34 | frootdemandentity | 根需求单据实体 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 35 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0.0000000000 | 折扣额 |
| 36 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 37 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 38 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 39 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | ftransportbaseqty | 已运输基本数量 | numeric | 23 | 10 |  | null | 已运输基本数量 |
| 41 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 42 | fiscontrolamountup | 控制上限金额 | bpchar | 1 |  | √ | '0' | 控制上限金额 |
| 43 | frootdemandbillno | 根需求单据编码 | varchar | 120 |  | √ | ' ' | 根需求单据编码 |
| 44 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 45 | fiscontrolmftqty | 控制产品委外入库数量 | bpchar | 1 |  | √ | '1' | 控制产品委外入库数量 |
| 46 | fentryrecdeptid | 收料部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | freceivingtype | 代收料组织类型 | varchar | 36 |  | √ | ' ' | 代收料组织类型,枚举: bd_supplier :供应商 bd_customer :客户 |
| 49 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 50 | fislogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 51 | frowterminatestatus | 行终止状态 | varchar | 5 |  | √ | ' ' | 行终止状态,枚举: A :正常 B :已终止 |
| 52 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 53 | fentrypurorgid | 分录采购组织(封存) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fentrycomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 55 | fprojectconfbaseqty | 已确认项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 已确认项目服务基本数量 |
| 56 | freceivedaydown | 允许延迟天数 | int4 | 32 |  | √ | 0 | 允许延迟天数 |
| 57 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 58 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 59 | fiscontrolqty | 控制收货数量 | bpchar | 1 |  | √ | '0' | 控制收货数量 |
| 60 | frootdemandentryid | 根需求单据分录ID | int8 | 64 |  | √ | 0 | 根需求单据分录ID |
| 61 | freceiverateup | 收货超收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货超收比率(%) |
| 62 | fentrysettledeptid | 结算部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 64 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 65 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 66 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 67 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 68 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 69 | fprojectassqty | 关联项目服务数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务数量 |
| 70 | fprojectassbaseqty | 关联项目服务基本数量 | numeric | 23 | 10 | √ | 0 | 关联项目服务基本数量 |
| 71 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 72 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 73 | fentrymanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 74 | fjointransportbaseqty | 关联运输基本数量 | numeric | 23 | 10 | √ | 0 | 关联运输基本数量 |
| 75 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 76 | fbizunitid | fbizunitid | int8 | 64 |  | √ | 0 |  |
| 77 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 78 | fmpmtasknoid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 79 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 80 | fjointransportqty | 关联运输数量 | numeric | 23 | 10 | √ | 0 | 关联运输数量 |
| 81 | fisdirectdelivery | 是否直送 | bpchar | 1 |  | √ | '0' | 是否直送 |
| 82 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 83 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 84 | fauxqty | 件数 | numeric | 23 | 10 | √ | 0.0000000000 | 件数 |
| 85 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计(本位币) |
| 86 | frootdemandbillid | 根需求单据ID | int8 | 64 |  | √ | 0 | 根需求单据ID |
| 87 | fentrypayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 88 | fmaterialname | 物料名称(历史) | varchar | 255 |  |  | ' ' | 物料名称(历史) |
| 89 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 90 | fqtybizunit | fqtybizunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 91 | frowclosestatus | 行关闭状态 | varchar | 5 |  | √ | ' ' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 92 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 93 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 94 | fk_bj73_textfield3 | requid | varchar | 50 |  | √ | ' ' | requid |
| 95 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 96 | freceiving | 代收料组织 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 97 | freceiveratedown | 收货欠收比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 收货欠收比率(%) |
| 98 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 99 | ftransportqty | 已运输数量 | numeric | 23 | 10 |  | null | 已运输数量 |
| 100 | fiscontrolday | 控制时间 | bpchar | 1 |  | √ | '0' | 控制时间 |
| 101 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 102 | ffloatingconversion | 浮动换算 | bpchar | 1 |  | √ | '0' | 浮动换算 |
| 103 | freceivedayup | 允许提前天数 | int4 | 32 |  | √ | 0 | 允许提前天数 |
| 104 | famountup | 上限金额 | numeric | 23 | 10 | √ | 0 | 上限金额 |
| 105 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 税额(本位币) |
| 106 | fprojrecamount | 已确认项目结算额 | numeric | 23 | 10 | √ | 0 | 已确认项目结算额 |
| 107 | fk_bj73_textfield | TZID | varchar | 50 |  | √ | ' ' | TZID |
| 108 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 109 | fbizunitrate | fbizunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_poentry_matid |  | fmaterialid,fid |
| 2 | t_pm_purorderbillentry_pkey |  | fentryid |
| 3 | idx_pm_purorderbillentry |  | fid |
| 4 | idx_pm_poentry_matmasterid |  | fmaterialmasterid,fid |

---

## 合同条款-子表 t_pm_purorderbilltentry

- **表名称：** 合同条款-子表
- **表名：** t_pm_purorderbilltentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | [合同条款分组 conm_termgroup](../conm_files/conm_termgroup.md) |
| 3 | ftermentrychangetype | 变更方式 | bpchar | 1 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 4 | ftermcontent | 条款内容 | varchar | 2000 |  | √ | ' ' | 条款内容 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftermid | 合同条款 | int8 | 64 |  | √ | 0 | [合同条款 conm_term](../conm_files/conm_term.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_purorderbilltentry |  | fentryid |
| 2 | idx_pm_purorderbilltentry |  | fid |

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
| 14 | fbaseplanunitid | 交货计划基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fbaseplanqty | 计划交货基本数量 | numeric | 23 | 10 | √ | 0 | 计划交货基本数量 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fdelentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbaseplanreceiveqty | 已交货基本数量 | numeric | 23 | 10 | √ | 0 | 已交货基本数量 |
| 19 | fplanuninvqty | 未入库数量 | numeric | 23 | 10 | √ | 0 | 未入库数量 |
| 20 | fplaninvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 21 | fdelentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fsurplusqty | 未交货数量 | numeric | 23 | 10 | √ | 0 | 未交货数量 |
| 23 | fplanunitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fconfirmdeliveryqty | 确认交货数量 | numeric | 23 | 10 | √ | 0 | 确认交货数量 |
| 25 | fplanreceivedate | 收货日期（废弃） | timestamp | 0 |  |  | null | 收货日期（废弃） |
| 26 | flatestdeliverydate | 最近交货日期 | timestamp | 0 |  |  | null | 最近交货日期 |
| 27 | fbasesurplusqty | 未交货基本数量 | numeric | 23 | 10 | √ | 0 | 未交货基本数量 |
| 28 | fmaterialtrackingdate | 追料到货日期 | timestamp | 0 |  |  | null | 追料到货日期 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 30 | fdelentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

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

## 采购订单-主表 t_pm_purorderbill

- **表名称：** 采购订单-主表
- **表名：** t_pm_purorderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmpmpaymethod | 项目支出确认方式 | varchar | 5 |  | √ | ' ' | 项目支出确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 3 | fpaidallamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 4 | fproviderlinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | fcancelstatus | 作废状态 | varchar | 5 |  | √ | ' ' | 作废状态,枚举: A :未作废 B :已作废 |
| 8 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 9 | fsplitschemeid | 付款计划方案 | int8 | 64 |  | √ | 0 | [付款计划方案 ap_plansplit_scheme](../ap_files/ap_plansplit_scheme.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 12 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fversion | 版本号 | varchar | 30 |  | √ | '1' | 版本号 |
| 17 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fmarginlevel | 保证金比例(%) | numeric | 23 | 10 | √ | 0 | 保证金比例(%) |
| 19 | fisinitbill | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 20 | ftrdbillno | 第三方业务编码 | varchar | 50 |  | √ | ' ' | 第三方业务编码 |
| 21 | fbtbpayrateset | 付款比例设置 | varchar | 30 |  | √ | ' ' | 付款比例设置,枚举: ZDY :自定义 TBL :收支同步 |
| 22 | fsupplierid | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | ftraderouteid | 贸易路线 | int8 | 64 |  | √ | 0 | [贸易路线 sbs_traderoute](../sbs_files/sbs_traderoute.md) |
| 24 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 25 | fpaidpreallamount | 已预付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预付金额 |
| 26 | fexchangetype | 换算方式 | varchar | 5 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 27 | fsettleorgid | 结算组织(废弃) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | ftradetermid | 贸易术语 | int8 | 64 |  | √ | 0 | [贸易术语 gtm_tradeterm](../gtm_files/gtm_tradeterm.md) |
| 32 | flogisticsstatus | 物流状态 | varchar | 5 |  | √ | ' ' | 物流状态,枚举: A :待发货 B :部分发货 C :已发货 D :部分收货 E :已收货 F :部分入库 G :已入库 |
| 33 | fk_bj73_operator | fk_bj73_operator | int8 | 64 |  | √ | 0 |  |
| 34 | fchangestatus | 变更状态 | varchar | 5 |  | √ | ' ' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 35 | fsupplytrans | 供应商直运 | bpchar | 1 |  | √ | '0' | 供应商直运 |
| 36 | fprovideraddress | 供货联系地址 | varchar | 512 |  |  | ' ' | 供货联系地址 |
| 37 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fpricelistid | 价目表 | int8 | 64 |  | √ | 0 | [采购价目表 pm_purpricelist](../pm_files/pm_purpricelist.md) |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fisvirtualbill | 内部交易单据 | bpchar | 1 |  | √ | '0' | 内部交易单据 |
| 41 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 42 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 43 | fmanualclosereason | 关闭原因 | varchar | 512 |  | √ | ' ' | 关闭原因 |
| 44 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 45 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | finternal | 内部购销 | bpchar | 1 |  | √ | '0' | 内部购销 |
| 49 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fwholediscountamount | 整单折扣额 | numeric | 23 | 10 | √ | 0 | 整单折扣额 |
| 51 | fsrcport | 交货地 | varchar | 512 |  | √ | ' ' | 交货地 |
| 52 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 53 | foutmargin | 转出保证金 | numeric | 23 | 10 | √ | 0 | 转出保证金 |
| 54 | fclosestatus | 关闭状态 | varchar | 5 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 55 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 56 | favailablemargin | 可用保证金 | numeric | 23 | 10 | √ | 0 | 可用保证金 |
| 57 | frelatemargin | 关联保证金 | numeric | 23 | 10 | √ | 0 | 关联保证金 |
| 58 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 59 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 60 | ftaxinprice | 价内税 | bpchar | 1 |  | √ | '0' | 价内税 |
| 61 | fcarrierid | 承运方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 62 | faddress | 联系地址 | varchar | 512 |  | √ | ' ' | 联系地址 |
| 63 | fk_bj73_basedatafield | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 64 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 65 | fassociatemargin | 已付保证金 | numeric | 23 | 10 | √ | 0 | 已付保证金 |
| 66 | ftransactepathid | 交易路径 | int8 | 64 |  | √ | 0 | [结算路径 ism_settlerelations](../ism_files/ism_settlerelations.md) |
| 67 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 68 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 69 | ftradestatus | 贸易转换状态 | bpchar | 1 |  | √ | ' ' | 贸易转换状态,枚举: 0 :未完成 1 :已完成 |
| 70 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 71 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 72 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 73 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 9 :迁移生成 |
| 74 | fdescountryid | 目的国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 75 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 76 | fmanualclose | 手工关闭 | bpchar | 1 |  | √ | '0' | 手工关闭 |
| 77 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 78 | flinkmanid | 联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 79 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 80 | fk_bj73_textfield4 | 发货地址 | varchar | 50 |  | √ | ' ' | 发货地址 |
| 81 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 82 | fdiscountlist | 折扣表 | int8 | 64 |  | √ | 0 | [采购折扣表 pm_purdiscountlist](../pm_files/pm_purdiscountlist.md) |
| 83 | fconfirmstatus | 确认状态 | varchar | 5 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :自动确认 |
| 84 | fk_bj73_textfield2 | foperatorid | varchar | 50 |  | √ | ' ' | foperatorid |
| 85 | fendbill | 尾单 | bpchar | 1 |  | √ | '0' | 尾单 |
| 86 | fbiztime | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 87 | fk_bj73_textfield1 | 采购订单 | varchar | 50 |  | √ | ' ' | 采购订单 |
| 88 | fpaystatus | 付款状态 | varchar | 5 |  | √ | ' ' | 付款状态,枚举: A :待付款 B :部分付款 C :已付款 |
| 89 | fsrccountryid | 装运国 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 90 | fiswholediscount | 录入整单折扣 | bpchar | 1 |  | √ | '0' | 录入整单折扣 |
| 91 | fisimport | 进口 | bpchar | 1 |  | √ | '0' | 进口 |
| 92 | fbtbpayref | 付款参考 | varchar | 30 |  | √ | ' ' | 付款参考,枚举: FKCK01 :项目收款 FKCK02 :阶段收款 FKCK03 :单个里程碑 FKCK04 :截止至固定里程碑 |
| 93 | fmargin | 应付保证金 | numeric | 23 | 10 | √ | 0 | 应付保证金 |
| 94 | fassrefundmargin | 已退保证金 | numeric | 23 | 10 | √ | 0 | 已退保证金 |
| 95 | fstep | 当前步骤 | int4 | 32 |  | √ | 0 | 当前步骤 |
| 96 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 97 | fdesport | 目的地 | varchar | 512 |  | √ | ' ' | 目的地 |
| 98 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 99 | fprovidersupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 100 | fpaymode | 付款方式 | varchar | 30 |  | √ | 'CREDIT' | 付款方式,枚举: CASH :现购 CREDIT :赊购 |
| 101 | fsubversion | 子版本号 | varchar | 30 |  | √ | '1' | 子版本号 |
| 102 | ftransportmodeid | 运输方式 | int8 | 64 |  | √ | 0 | [运输方式 gtm_transportmode](../gtm_files/gtm_transportmode.md) |
| 103 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 104 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purorder_supplier |  | fsupplierid |
| 2 | idx_pm_purorderbill_org |  | forgid,fbiztime,fid |
| 3 | idx_pm_purorder_billno_org |  | fbillno,forgid |
| 4 | t_pm_purorderbill_pkey |  | fid |
| 5 | idx_pm_purorder_biztime |  | fbiztime |

---

## 付款比例约束-子表 t_pm_purorderpayrateentry

- **表名称：** 付款比例约束-子表
- **表名：** t_pm_purorderpayrateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbtbpayratio | 累计付款比例(%) | numeric | 23 | 10 | √ | 0 | 累计付款比例(%) |
| 3 | fbtbpaydate | 到期日 | timestamp | 0 |  |  | null | 到期日 |
| 4 | fbtbrecratio | 累计收款比例(%) | numeric | 23 | 10 | √ | 0 | 累计收款比例(%) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbtbispre | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 8 | fbtbpayrate | 付款比例(%) | numeric | 23 | 10 | √ | 0 | 付款比例(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_purorderpayrateentry |  | fid |
| 2 | pk_t_pm_purorderpayrateentry |  | fentryid |
