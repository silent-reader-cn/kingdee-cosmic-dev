# 委外退货单-om_outsourcereturn

## 委外退货单-多语言表 t_om_osreturn_l

- **表名称：** 委外退货单-多语言表
- **表名：** t_om_osreturn_l

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
| 1 | pk_om_osreturn_l |  | fpkid |
| 2 | idx_om_osreturn_l_id_localeid |  | fid,flocaleid |

---

## WBS-多选基础资料表 t_om_osreportreturnwbs

- **表名称：** WBS-多选基础资料表
- **表名：** t_om_osreportreturnwbs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [WBS pmts_wbs](../fmm_files/pmts_wbs.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreportreturnwbs |  | fpkid |
| 2 | idx_om_osrtwbs_fentryid |  | fentryid |

---

## 物料明细-子表 t_om_osreturnsummary

- **表名称：** 物料明细-子表
- **表名：** t_om_osreturnsummary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstaworhours | fstaworhours | numeric | 23 | 10 | √ | 0 |  |
| 3 | forgfield | 入库组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 5 | fauxptyqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 6 | fmanufacturebillrow | 委外工单行号 | int8 | 64 |  | √ | 0 | 委外工单行号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fcheckedqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 11 | fpurorderbillno | fpurorderbillno | varchar | 50 |  | √ | ' ' |  |
| 12 | fisautowarehouse | 是否自动入库 | bpchar | 1 |  | √ | '0' | 是否自动入库 |
| 13 | freworkbsqty | 返工退货基本数量 | numeric | 23 | 10 | √ | 0 | 返工退货基本数量 |
| 14 | ftotalworkhours | ftotalworkhours | numeric | 23 | 10 | √ | 0 |  |
| 15 | fosrcentryrowid | 委外收货单分录ID | int8 | 64 |  | √ | 0 | 委外收货单分录ID |
| 16 | fmanufacturebill | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 17 | fischargeoffed | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 18 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fscrapqty | 料废退货数量 | numeric | 23 | 10 | √ | 0 | 料废退货数量 |
| 20 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 21 | fworkwastebsqty | 工废退货基本数量 | numeric | 23 | 10 | √ | 0 | 工废退货基本数量 |
| 22 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 23 | fscrapbsqty | 料废退货基本数量 | numeric | 23 | 10 | √ | 0 | 料废退货基本数量 |
| 24 | fworkwasteqty | 工废退货数量 | numeric | 23 | 10 | √ | 0 | 工废退货数量 |
| 25 | fcompletqty | 退货数量 | numeric | 23 | 10 | √ | 0 | 退货数量 |
| 26 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 27 | frepairqty | 判退退货数量 | numeric | 23 | 10 | √ | 0 | 判退退货数量 |
| 28 | foprunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fconcesionqty | 让步接收退货数量 | numeric | 23 | 10 | √ | 0 | 让步接收退货数量 |
| 30 | freworkqty | 返工退货数量 | numeric | 23 | 10 | √ | 0 | 返工退货数量 |
| 31 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 32 | fshiporderentryid | 发货单行ID | int8 | 64 |  | √ | 0 | 发货单行ID |
| 33 | fosentryid | 委外工单分录id | varchar | 50 |  | √ | ' ' | 委外工单分录id |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 36 | fmatertype | 产品类型 | varchar | 50 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 37 | fqualifywareqty | 合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 合格品入库基本数量 |
| 38 | fsupplierlot | 供应商批号 | varchar | 50 |  | √ | ' ' | 供应商批号 |
| 39 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 40 | fauxptyunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 41 | fcheckqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 42 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 43 | fconcesionbsqty | 让步接收退货基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收退货基本数量 |
| 44 | fosrcno | 委外收货单编码 | varchar | 50 |  | √ | ' ' | 委外收货单编码 |
| 45 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 46 | fscrappedwareqty | 报废品入库基本数量 | numeric | 23 | 10 | √ | 0 | 报废品入库基本数量 |
| 47 | fcompletbsqty | 退货基本数量 | numeric | 23 | 10 | √ | 0 | 退货基本数量 |
| 48 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 49 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 50 | fmaterialcode | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 51 | frepairbsqty | 判退退货基本数量 | numeric | 23 | 10 | √ | 0 | 判退退货基本数量 |
| 52 | fscrappedbsqty | 报废退货基本数量 | numeric | 23 | 10 | √ | 0 | 报废退货基本数量 |
| 53 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 54 | fbackflishflag | 倒冲标识 | varchar | 50 |  | √ | ' ' | 倒冲标识,枚举: not :未倒冲 sucess :倒冲成功 part :部分倒冲 |
| 55 | fpersonnel | fpersonnel | int8 | 64 |  | √ | 0 |  |
| 56 | fqualifyqty | 合格退货数量 | numeric | 23 | 10 | √ | 0 | 合格退货数量 |
| 57 | funqualifywareqty | 不合格品入库基本数量 | numeric | 23 | 10 | √ | 0 | 不合格品入库基本数量 |
| 58 | fserialnumber | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 59 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 60 | fpushdownwareqty | 关联入库基本数量 | numeric | 23 | 10 | √ | 0 | 关联入库基本数量 |
| 61 | fosrcid | 委外收货单ID | int8 | 64 |  | √ | 0 | 委外收货单ID |
| 62 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 63 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 64 | fosrcentryrow | 委外收货单分录行号 | int8 | 64 |  | √ | 0 | 委外收货单分录行号 |
| 65 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 66 | fshiporderid | 发货单ID | int8 | 64 |  | √ | 0 | 发货单ID |
| 67 | fqualifybsqty | 合格退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格退货基本数量 |
| 68 | fauxptyunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 69 | fscrappedqty | 报废退货数量 | numeric | 23 | 10 | √ | 0 | 报废退货数量 |
| 70 | fauxptyqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreturnsummary |  | fentryid |
| 2 | idx_om_osreturnsummary_fid |  | fid |

---

## 委外退货单-反写记录表 t_om_osreturn_wb

- **表名称：** 委外退货单-反写记录表
- **表名：** t_om_osreturn_wb

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
| 1 | pk_om_osreturn_wb |  | fentryid |
| 2 | idx_om_osreturn_wb_fk |  | fid |

---

## 委外退货单-主表 t_om_osreturn

- **表名称：** 委外退货单-主表
- **表名：** t_om_osreturn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpuroperator | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | freceiptorgroupid | 收货组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 5 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | freportdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fischargeoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 9 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | freceiptoperatorid | 收料员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 12 | fstaffreport | 人员汇报 | varchar | 50 |  | √ | ' ' | 人员汇报,枚举: qty :按数量 cooportion :按比例 |
| 13 | freceiptorg | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fprovidersupplier | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fbillcretype | 单据生成类型 | varchar | 5 |  | √ | ' ' | 单据生成类型,枚举: 9 :迁移生成 |
| 22 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :检修工单手工创建 B :收工操作创建 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | freceiptdeptid | 收货部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 28 | fbilltypeid | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: |
| 29 | fpurorgroup | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreturn |  | fid |
| 2 | idx_om_osreturn_fbillno |  | fbillno |

---

## 物料明细-多语言表 t_om_osreturnsummary_l

- **表名称：** 物料明细-多语言表
- **表名：** t_om_osreturnsummary_l

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
| 1 | pk_om_osreturnsummary_l |  | fpkid |
| 2 | idx_om_osrtl_entry_local |  | fentryid,flocaleid |

---

## 委外退货单-关联追踪表 t_om_osreturn_tc

- **表名称：** 委外退货单-关联追踪表
- **表名：** t_om_osreturn_tc

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
| 1 | idx_om_osreturn_tc_tbill |  | ftbillid |
| 2 | idx_om_osreturn_tc_tid |  | ftid |
| 3 | pk_om_osreturn_tc |  | fid |

---

## 物料明细-分表 t_om_osreturnsummary_x

- **表名称：** 物料明细-分表
- **表名：** t_om_osreturnsummary_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstaworhours | 单位标准工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 单位标准工时(工时汇报) |
| 3 | fworkunitid | 工时单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
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
| 18 | fprofessionid | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 19 | fentryreworknonrebsqty | 返工未退货基本数量 | numeric | 23 | 10 | √ | 0 | 返工未退货基本数量 |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fmachprehours | 机器准备工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器准备工时(工时汇报) |
| 22 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fosrttype | 退货类型 | varchar | 50 |  | √ | ' ' | 退货类型,枚举: A :判退品退货 B :合格品退货 |
| 24 | ftimestop | 结束时间(工时汇报) | timestamp | 0 |  |  | null | 结束时间(工时汇报) |
| 25 | ftimeunit | 时间单位(工时汇报) | varchar | 50 |  | √ | ' ' | 时间单位(工时汇报),枚举: hour :小时 minute :分钟 second :秒 |
| 26 | fmacworhours | 机器实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 机器实作工时(工时汇报) |
| 27 | fconcesionbreturnbsqty | 让步接收已退货基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收已退货基本数量 |
| 28 | frepairnonreturnqty | 判退品未退货数量 | numeric | 23 | 10 | √ | 0 | 判退品未退货数量 |
| 29 | flinkmanid | 供货联系人 | int8 | 64 |  | √ | 0 | [供应商联系人 bd_supplierlinkman](../sbd_files/bd_supplierlinkman.md) |
| 30 | fischeckmaterial | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 32 | ftotalconsumedhours | 维修消耗工时 | numeric | 23 | 10 | √ | 0 | 维修消耗工时 |
| 33 | fteamsgroups | 班组(工时汇报) | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 34 | ftotalinspectionhours | 检验消耗工时 | numeric | 23 | 10 | √ | 0 | 检验消耗工时 |
| 35 | fqualifynonreturnbaseqty | 合格品未退货基本数量 | numeric | 23 | 10 | √ | 0 | 合格品未退货基本数量 |
| 36 | fconcesionreturnqty | 让步接收已退货数量 | numeric | 23 | 10 | √ | 0 | 让步接收已退货数量 |
| 37 | frepairreturnbaseqty | 判退品已退货基本数量 | numeric | 23 | 10 | √ | 0 | 判退品已退货基本数量 |
| 38 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 39 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 40 | finwarelocation | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 41 | forderentryid | 采购订单行ID | int8 | 64 |  | √ | 0 | 采购订单行ID |
| 42 | frepairreturnqty | 判退品已退货数量 | numeric | 23 | 10 | √ | 0 | 判退品已退货数量 |
| 43 | fentryreworkreturnqty | 返工已退货数量 | numeric | 23 | 10 | √ | 0 | 返工已退货数量 |
| 44 | fpurorderbillrow | 采购订单行号 | int8 | 64 |  | √ | 0 | 采购订单行号 |
| 45 | fentryreworkrebsqty | 返工已退货基本数量 | numeric | 23 | 10 | √ | 0 | 返工已退货基本数量 |
| 46 | fqualityorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | fpersonnel | 人员(工时汇报) | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fhourconsumptionrate | 工时消耗率（%） | numeric | 23 | 10 | √ | 0 | 工时消耗率（%） |
| 50 | ftimeon | 开始时间(工时汇报) | timestamp | 0 |  |  | null | 开始时间(工时汇报) |
| 51 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 52 | fpurunit | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 53 | freceiptpurqty | 采购退货数量 | numeric | 23 | 10 | √ | 0 | 采购退货数量 |
| 54 | frepairnonreturnbaseqty | 判退品未退货基本数量 | numeric | 23 | 10 | √ | 0 | 判退品未退货基本数量 |
| 55 | flabworkhours | 人工实作工时(工时汇报) | numeric | 23 | 10 | √ | 0 | 人工实作工时(工时汇报) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreturnsummary_x |  | fentryid |
| 2 | idx_om_osreturnsummary_x_fid |  | fid |

---

## 项目任务-多选基础资料表 t_om_osreportreturntask

- **表名称：** 项目任务-多选基础资料表
- **表名：** t_om_osreportreturntask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目任务清单 pmts_task](../fmm_files/pmts_task.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_osreportreturntask |  | fpkid |
| 2 | idx_om_osrttask_fentryid |  | fentryid |

---

## 关联子实体-子表 t_om_osreturnsummary_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_osreturnsummary_lk

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
| 1 | pk_om_osreturnsummary_lk |  | fpkid |
| 2 | idx_om_osreturnsummary_lk_fk |  | fentryid |

---

## 物料明细-分表 t_om_osreturnsummary_a

- **表名称：** 物料明细-分表
- **表名：** t_om_osreturnsummary_a

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
| 10 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 11 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_osreturnsummary_a_fid |  | fid |
| 2 | pk_om_osreturnsummary_a |  | fentryid |
