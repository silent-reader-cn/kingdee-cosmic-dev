# 委外收货单-om_outsourcereceipt

## 委外收货单-多语言表 t_om_osreceipt_l

- **表名称：** 委外收货单-多语言表
- **表名：** t_om_osreceipt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_osreceipt_l_id_localeid |  | fid,flocaleid |
| 2 | pk_om_osreceipt_l |  | fpkid |

---

## 委外收货单-反写记录表 t_om_osreceipt_wb

- **表名称：** 委外收货单-反写记录表
- **表名：** t_om_osreceipt_wb

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
| 1 | pk_om_osreceipt_wb |  | fentryid |
| 2 | idx_om_osreceipt_wb_fk |  | fid |

---

## WBS-多选基础资料表 t_om_osreportwbs

- **表名称：** WBS-多选基础资料表
- **表名：** t_om_osreportwbs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | WBS pmts_wbs |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_osreportwbs_fentryid |  | fentryid |
| 2 | pk_om_osreportwbs |  | fpkid |

---

## 关联子实体-子表 t_om_osreceiptsummary_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_osreceiptsummary_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_osreceiptsummary_lk_fk |  | fentryid |
| 2 | pk_om_osreceiptsummary_lk |  | fpkid |

---

## 委外收货单-主表 t_om_osreceipt

- **表名称：** 委外收货单-主表
- **表名：** t_om_osreceipt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpuroperator | 采购员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | freceiptorgroupid | 收货组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 5 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | freportdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fischargeoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | freceiptoperatorid | 收料员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 12 | fstaffreport | 人员汇报 | varchar | 50 |  | √ | ' ' | 人员汇报,枚举: qty :按数量 cooportion :按比例 |
| 13 | freceiptorg | 收货组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fprovidersupplier | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :检修工单手工创建 B :收工操作创建 |
| 22 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 23 | freceiptdeptid | 收货部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 27 | fbilltypeid | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: |
| 28 | fpurorgroup | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreceipt |  | fid |
| 2 | idx_om_osreceipt_fbillno |  | fbillno |

---

## 委外收货单-关联追踪表 t_om_osreceipt_tc

- **表名称：** 委外收货单-关联追踪表
- **表名：** t_om_osreceipt_tc

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
| 1 | idx_om_osreceipt_tc_tid |  | ftid |
| 2 | pk_om_osreceipt_tc |  | fid |
| 3 | idx_om_osreceipt_tc_tbill |  | ftbillid |

---

## 物料明细-分表 t_om_osreceiptsummary_a

- **表名称：** 物料明细-分表
- **表名：** t_om_osreceiptsummary_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 4 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 5 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 6 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 7 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | frejectdiscountamount | 不良品折让金额 | numeric | 23 | 10 | √ | 0 | 不良品折让金额 |
| 11 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 12 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | finvdpallowanceamount | 入库关联不良品折让金额 | numeric | 23 | 10 | √ | 0 | 入库关联不良品折让金额 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 15 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreceiptsummary_a |  | fentryid |
| 2 | idx_om_osreceiptsummary_a_fid |  | fid |

---

## 项目任务-多选基础资料表 t_om_osreporttask

- **表名称：** 项目任务-多选基础资料表
- **表名：** t_om_osreporttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目任务清单 pmts_task |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_osreporttask_fentryid |  | fentryid |
| 2 | pk_om_osreporttask |  | fpkid |

---

## 物料明细-多语言表 t_om_osreceiptsummary_l

- **表名称：** 物料明细-多语言表
- **表名：** t_om_osreceiptsummary_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreceiptsummary_l |  | fpkid |
| 2 | idx_om_osrcl_entryid_localeid |  | fentryid,flocaleid |
| 3 | idx_om_osrtl_entryid_localeid |  | fentryid,flocaleid |

---

## 物料明细-子表 t_om_osreceiptsummary

- **表名称：** 物料明细-子表
- **表名：** t_om_osreceiptsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstaworhours | fstaworhours | numeric | 23 | 10 | √ | 0 |  |
| 3 | forgfield | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 6 | fmanufacturebillrow | 委外工单行号 | int8 | 64 |  | √ | 0 | 委外工单行号 |
| 7 | funqualifywarebizqty | 不合格品入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fcheckedqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 12 | fpurorderbillno | fpurorderbillno | varchar | 50 |  | √ | ' ' |  |
| 13 | fpushdownwarebizqty | 关联入库数量 | numeric | 23 | 10 | √ | 0 | 关联入库数量 |
| 14 | fisautowarehouse | 是否自动入库 | bpchar | 1 |  | √ | '0' | 是否自动入库 |
| 15 | freworkbsqty | 返工基本数量 | numeric | 23 | 10 | √ | 0 | 返工基本数量 |
| 16 | ftotalworkhours | ftotalworkhours | numeric | 23 | 10 | √ | 0 |  |
| 17 | fmanufacturebill | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 18 | fquaretqty | 合格品关联退货数量 | numeric | 23 | 10 | √ | 0 | 合格品关联退货数量 |
| 19 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 20 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | fscrapqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 22 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 23 | fworkwastebsqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 25 | fscrapbsqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |
| 26 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 27 | fcompletqty | 收货数量 | numeric | 23 | 10 | √ | 0 | 收货数量 |
| 28 | fquaretbaseqty | 合格品关联退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格品关联退货基本数量 |
| 29 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 30 | frepairqty | 判退数量 | numeric | 23 | 10 | √ | 0 | 判退数量 |
| 31 | foprunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 32 | fconcesionqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 33 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 34 | fosentryid | 委外工单分录id | varchar | 50 |  | √ | ' ' | 委外工单分录id |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fmatertype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 37 | fqualifywareqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品入库基本数量 |
| 38 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 39 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 40 | fcheckqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 41 | fconcesionbsqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 42 | fretqty | 判退品关联退货数量 | numeric | 23 | 10 | √ | 0 | 判退品关联退货数量 |
| 43 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 44 | fscrappedwareqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品入库基本数量 |
| 45 | fcompletbsqty | 收货基本数量 | numeric | 23 | 10 | √ | 0 | 收货基本数量 |
| 46 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 47 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 48 | fmaterialcode | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 49 | frepairbsqty | 判退基本数量 | numeric | 23 | 10 | √ | 0 | 判退基本数量 |
| 50 | fscrappedbsqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 51 | fscrappedwarebizqty | 报废品入库数量 | numeric | 23 | 10 | √ | 0 | 报废品入库数量 |
| 52 | fretbaseqty | 判退品关联退货基本数量 | numeric | 23 | 10 | √ | 0 | 判退品关联退货基本数量 |
| 53 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 54 | fbackflishflag | 倒冲标识 | varchar | 50 |  | √ | ' ' | 倒冲标识,枚举: not :未倒冲 sucess :倒冲成功 part :部分倒冲 |
| 55 | fpersonnel | fpersonnel | int8 | 64 |  | √ | 0 |  |
| 56 | fqualifywarebizqty | 合格品入库数量 | numeric | 23 | 10 | √ | 0 | 合格品入库数量 |
| 57 | fqualifyqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 58 | funqualifywareqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库基本数量 |
| 59 | fserialnumber | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 60 | fpushdownwareqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库基本数量 |
| 61 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 62 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 63 | fqualifybsqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 64 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 65 | fscrappedqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 66 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreceiptsummary |  | fentryid |
| 2 | idx_om_osreceiptsummary_fid |  | fid |

---

## 物料明细-分表 t_om_osreceiptsummary_x

- **表名称：** 物料明细-分表
- **表名：** t_om_osreceiptsummary_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstaworhours | 单位标准工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 单位标准工时(工时汇报) |
| 3 | fworkunitid | 工时单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fsupplyaddress | 供货地址 | varchar | 300 |  | √ | ' ' | 供货地址 |
| 5 | fconcesionnonreqty | 让步接收未退货数量 | numeric | 23 | 10 | √ | 0 | 让步接收未退货数量 |
| 6 | fqualifyreqty | 合格品已退货数量 | numeric | 23 | 10 | √ | 0 | 合格品已退货数量 |
| 7 | fqualifyreturnbaseqty | 合格品已退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格品已退货基本数量 |
| 8 | fpushcheckbillqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 9 | fqualifynonreqty | 合格品未退货数量 | numeric | 23 | 10 | √ | 0 | 合格品未退货数量 |
| 10 | flabworprehours | 人工准备工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 人工准备工时(工时汇报) |
| 11 | fconcesionbnonrebsqty | 让步接收未退货基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收未退货基本数量 |
| 12 | facttotprohours | 实际生产总工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 实际生产总工时(工时汇报) |
| 13 | fpurorderbillno | 采购订单编号 | varchar | 50 |  | √ | ' ' | 采购订单编号 |
| 14 | fplanconsumedhours | 计划消耗工时 | numeric | 23 | 10 | √ | 0 | 计划消耗工时 |
| 15 | fentryreworknrqty | 返工未退货数量 | numeric | 23 | 10 | √ | 0 | 返工未退货数量 |
| 16 | freporttype | 汇报类型 | varchar | 50 |  | √ | ' ' | 汇报类型,枚举: 10080 :有效工时 10090 :无效工时 10100 :中性工时 |
| 17 | ftotalworkhours | 预计生产总工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 预计生产总工时(工时汇报) |
| 18 | fprofessionid | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 19 | fentryreworknonrebsqty | 返工未退货基本数量 | numeric | 23 | 10 | √ | 0 | 返工未退货基本数量 |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 21 | fsampledestoryrelinvqty | 样本破坏关联入库数量 | numeric | 23 | 10 | √ | 0 | 样本破坏关联入库数量 |
| 22 | fscrappedrelateinvqty | 报废品关联入库数量 | numeric | 23 | 10 | √ | 0 | 报废品关联入库数量 |
| 23 | fmachprehours | 机器准备工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器准备工时(工时汇报) |
| 24 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | ftimestop | 结束时间(工时汇报) | timestamp | 0 |  |  | null | 结束时间(工时汇报) |
| 26 | ftimeunit | 时间单位(工时汇报) | varchar | 50 |  | √ | ' ' | 时间单位(工时汇报),枚举: hour :小时 minute :分钟 second :秒 |
| 27 | fmacworhours | 机器实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器实作工时(工时汇报) |
| 28 | fconcesionbreturnbsqty | 让步接收已退货基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收已退货基本数量 |
| 29 | frepairnonreturnqty | 判退品未退货数量 | numeric | 23 | 10 | √ | 0 | 判退品未退货数量 |
| 30 | flinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | 供应商联系人 bd_supplierlinkman |
| 31 | fischeckmaterial | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | ftotalconsumedhours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 34 | fteamsgroups | 班组(工时汇报) | int8 | 64 |  | √ | 0 | 班组 mpdm_classgroup |
| 35 | ftotalinspectionhours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 36 | fqualifynonreturnbaseqty | 合格品未退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格品未退货基本数量 |
| 37 | fconcesionreturnqty | 让步接收已退货数量 | numeric | 23 | 10 | √ | 0 | 让步接收已退货数量 |
| 38 | fsampledestorybsqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 39 | fqualifyrelateinvbsqty | 合格品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品关联入库基本数量 |
| 40 | frepairreturnbaseqty | 判退品已退货基本数量 | numeric | 23 | 10 | √ | 0 | 判退品已退货基本数量 |
| 41 | fscrappedrelateinvbsqty | 报废品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品关联入库基本数量 |
| 42 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 43 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 44 | finwarelocation | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 45 | forderentryid | 采购订单行ID | int8 | 64 |  | √ | 0 | 采购订单行ID |
| 46 | frepairreturnqty | 判退品已退货数量 | numeric | 23 | 10 | √ | 0 | 判退品已退货数量 |
| 47 | funqualifyrelateinvbsqty | 不合格品关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品关联入库基本数量 |
| 48 | fentryreworkreturnqty | 返工已退货数量 | numeric | 23 | 10 | √ | 0 | 返工已退货数量 |
| 49 | fpurorderbillrow | 采购订单行号 | int8 | 64 |  | √ | 0 | 采购订单行号 |
| 50 | fentryreworkrebsqty | 返工已退货基本数量 | numeric | 23 | 10 | √ | 0 | 返工已退货基本数量 |
| 51 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fpersonnel | 人员(工时汇报) | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 54 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | funqualifyrelateinvqty | 不合格品关联入库数量 | numeric | 23 | 10 | √ | 0 | 不合格品关联入库数量 |
| 56 | fhourconsumptionrate | 工时消耗率（%） | numeric | 23 | 10 | √ | 0 | 工时消耗率（%） |
| 57 | fpurorderid | 采购订单ID | int8 | 64 |  | √ | 0 | 采购订单ID |
| 58 | ftimeon | 开始时间(工时汇报) | timestamp | 0 |  |  | null | 开始时间(工时汇报) |
| 59 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 60 | fqualifyrelateinvqty | 合格品关联入库数量 | numeric | 23 | 10 | √ | 0 | 合格品关联入库数量 |
| 61 | fsampledestoryrelinvbsqty | 样本破坏关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏关联入库基本数量 |
| 62 | fpurunit | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 63 | freceiptpurqty | 采购收货数量 | numeric | 23 | 10 | √ | 0 | 采购收货数量 |
| 64 | frepairnonreturnbaseqty | 判退品未退货基本数量 | numeric | 23 | 10 | √ | 0 | 判退品未退货基本数量 |
| 65 | flabworkhours | 人工实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 人工实作工时(工时汇报) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreceiptsummary_x |  | fentryid |
| 2 | idx_om_osreceiptsummary_x_fid |  | fid |
