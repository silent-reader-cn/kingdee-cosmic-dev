# 用料消耗-scp_moduleconsume

## 附件-附件表 t_pur_moduleconsumerejatt

- **表名称：** 附件-附件表
- **表名：** t_pur_moduleconsumerejatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_mocosrejatt_fid |  | fid |
| 2 | idx__pur_mocosrejatt_fbaseid |  | fbasedataid |
| 3 | pk_pur_moduleconsumerejatt |  | fpkid |

---

## 用料信息-多语言表 t_pur_moduleconsubentry_l

- **表名称：** 用料信息-多语言表
- **表名：** t_pur_moduleconsubentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fsubremarks | 备注 | varchar | 512 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_moconsubentry_l_fdid |  | fdetailid,flocaleid |
| 2 | pk_pur_moduleconsubentry_l |  | fpkid |

---

## 关联子实体-子表 t_pur_moduleconsubentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_moduleconsubentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_moduleconsubentry_lk_fk |  | fdetailid |
| 2 | pk_pur_moduleconsubentry_lk |  | fpkid |

---

## 用料信息-子表 t_pur_moduleconsubentry

- **表名称：** 用料信息-子表
- **表名：** t_pur_moduleconsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubmainbillentity | 核心单据实体 | varchar | 80 |  | √ | ' ' | 核心单据实体 |
| 2 | fdownstreambillid | 下游单据ID | varchar | 50 |  | √ | ' ' | 下游单据ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fextraratiobasicqty | 发料上限基本数量 | numeric | 23 | 10 | √ | 0 | 发料上限基本数量 |
| 5 | fsubunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fsubsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 7 | fsubqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 8 | fsubconfiguredcodeid | 用料配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | fsubmainbillnumber | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 10 | fsubmaterialid | 用料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | foverissuecontrl | 控制发料数量 | bpchar | 1 |  | √ | ' ' | 控制发料数量,枚举: A :可超发 B :不可超发 |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fsubmainbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 14 | fsubmainbillentryseq | 核心单据分录序号 | varchar | 20 |  | √ | ' ' | 核心单据分录序号 |
| 15 | fsubsumconbaseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 16 | fsubsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 17 | fsubbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 18 | fsubmainbillentryid | 核心单据行ID | varchar | 50 |  | √ | ' ' | 核心单据行ID |
| 19 | fsubsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 20 | fsubbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fsubcurrconqty | 本次消耗数量 | numeric | 23 | 10 | √ | 0 | 本次消耗数量 |
| 22 | fdownstreambillno | 下游单据编号 | varchar | 80 |  | √ | ' ' | 下游单据编号 |
| 23 | fsubsrcbillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 24 | fsaloutnum | 发货单编码 | varchar | 80 |  | √ | ' ' | 发货单编码 |
| 25 | fsubsumconqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 26 | fdownstreambilltype | 下游单据类型 | varchar | 80 |  | √ | ' ' | 下游单据类型,枚举: im_mdc_omoutbill :委外领料单 im_mdc_omreturnbill :委外退料单 im_mdc_omfeedbill :委外补料单 |
| 27 | fdownstreambillentryid | 下游单据行ID | varchar | 50 |  | √ | ' ' | 下游单据行ID |
| 28 | fsaloutid | 发货单id | int8 | 64 |  | √ | 0 | 发货单id |
| 29 | fsaloutentryid | 发货单用料分录行id | int8 | 64 |  | √ | 0 | 发货单用料分录行id |
| 30 | fsubcurrconbaseqty | 本次消耗基本数量 | numeric | 23 | 10 | √ | 0 | 本次消耗基本数量 |
| 31 | fisbackflushnew | 倒冲 | bpchar | 1 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 32 | fextraratioqty | 发料上限数量 | numeric | 23 | 10 | √ | 0 | 发料上限数量 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 34 | fsubsrcbillentryseq | 来源单据行号 | varchar | 20 |  | √ | ' ' | 来源单据行号 |
| 35 | fsubremarks | fsubremarks | varchar | 512 |  | √ | ' ' |  |
| 36 | fsubmaterialnametext | 用料名称 | varchar | 255 |  | √ | ' ' | 用料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_moduleconsubentry |  | fdetailid |
| 2 | idx_pur_moconsentry_fdownbid |  | fdownstreambillid |
| 3 | idx_pur_moconsentry_fsaloutbid |  | fsaloutid |
| 4 | idx_pur_moconsentry_feid_fseq |  | fentryid,fseq |

---

## 产品信息-子表 t_pur_moduleconsumeentry

- **表名称：** 产品信息-子表
- **表名：** t_pur_moduleconsumeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 4 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 5 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 10 | fsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 11 | fsrcbillentryseq | 来源单据行号 | varchar | 20 |  | √ | ' ' | 来源单据行号 |
| 12 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 13 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 15 | fsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 18 | fpobillno | 订单编号 | varchar | 80 |  | √ | ' ' | 订单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_moduleconsumeentry |  | fentryid |
| 2 | inx_pur_moduleconentry_fid |  | fid,fseq |

---

## 用料消耗-关联追踪表 t_pur_moduleconsume_tc

- **表名称：** 用料消耗-关联追踪表
- **表名：** t_pur_moduleconsume_tc

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
| 1 | pk_pur_moduleconsume_tc |  | fid |
| 2 | idx_pur_moduleconsume_tc_tid |  | ftid |
| 3 | idx_pur_moduleconsume_tc_tbill |  | ftbillid |

---

## 用料消耗-主表 t_pur_moduleconsume

- **表名称：** 用料消耗-主表
- **表名：** t_pur_moduleconsume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fconsumetype | 消耗类型 | bpchar | 1 |  | √ | ' ' | 消耗类型,枚举: 0 :消耗 1 :超耗 2 :消耗退回 |
| 7 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | frejectreason | 打回原因 | varchar | 512 |  | √ | ' ' | 打回原因 |
| 16 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 19 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 21 | fsrctype | 来源类型 | bpchar | 1 |  | √ | ' ' | 来源类型,枚举: 1 :采购订单 2 :发货单 |
| 22 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | 'A' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 E :自动确认 |
| 23 | fpersonid | 采购方联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 25 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_modulecon_fbilldate |  | fbilldate |
| 2 | idx_pur_moduleconsume_fbizid |  | fbizpartnerid |
| 3 | pk_pur_moduleconsume |  | fid |
| 4 | idx_pur_moduleconsume_fbillno |  | fbillno |

---

## 用料消耗-多语言表 t_pur_moduleconsume_l

- **表名称：** 用料消耗-多语言表
- **表名：** t_pur_moduleconsume_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_moduleconsume_l |  | fpkid |
| 2 | idx_pur_moduleconsume_l_fid |  | fid,flocaleid |

---

## 用料消耗-反写记录表 t_pur_moduleconsume_wb

- **表名称：** 用料消耗-反写记录表
- **表名：** t_pur_moduleconsume_wb

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
| 1 | idx_pur_moduleconsume_wb_fk |  | fid |
| 2 | pk_pur_moduleconsume_wb |  | fentryid |

---

## 关联子实体-子表 t_pur_moduleconsumeentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_moduleconsumeentry_lk

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
| 1 | pk_pur_moduleconsumeentry_lk |  | fpkid |
| 2 | idx_pur_moduleconsumeentry_lk_fk |  | fentryid |
