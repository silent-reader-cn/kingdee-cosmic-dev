# 协同用料清单-pur_modulelist

## 用料信息-子表 t_pur_modulelist_sub

- **表名称：** 用料信息-子表
- **表名：** t_pur_modulelist_sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freturnsubbaseqty | 已退料基本数量 | numeric | 23 | 10 | √ | 0 | 已退料基本数量 |
| 2 | fconsumesubbaseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 3 | fissuemode | 领送料方式 | bpchar | 1 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fextraratiobasicqty | 发料上限基本数量 | numeric | 23 | 10 | √ | 0 | 发料上限基本数量 |
| 6 | fscraprate | 变动损耗率 | numeric | 23 | 10 | √ | 0 | 变动损耗率 |
| 7 | fsubsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 8 | fparentmaterialid | 父项物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 10 | fsubconfiguredcodeid | 用料配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 11 | fwasteformula | 损耗计算公式 | bpchar | 1 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 12 | fparententryid | 父级行主键 | varchar | 50 |  | √ | '0' | 父级行主键 |
| 13 | fsubmaterialid | 用料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 16 | fqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 17 | freturnsubqty | 已退料数量 | numeric | 23 | 10 | √ | 0 | 已退料数量 |
| 18 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 19 | fsubsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 20 | fsubrequireqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 21 | fsubbaseqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 22 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fsubsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 24 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsubbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 27 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 28 | fsupplymode | 货主类型 | varchar | 80 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 29 | foutstocksubqty | 已发料数量 | numeric | 23 | 10 | √ | 0 | 已发料数量 |
| 30 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fextraratioqty | 发料上限数量 | numeric | 23 | 10 | √ | 0 | 发料上限数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fsubremarks | fsubremarks | varchar | 512 |  | √ | ' ' |  |
| 34 | fsubrequirebaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 35 | frowid | 行主键 | varchar | 50 |  | √ | ' ' | 行主键 |
| 36 | fsubunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | fsubqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 38 | foverissuecontrl | 控制发料数量 | bpchar | 1 |  | √ | ' ' | 控制发料数量,枚举: A :可超发 B :不可超发 |
| 39 | foutstocksubbaseqty | 已发料基本数量 | numeric | 23 | 10 | √ | 0 | 已发料基本数量 |
| 40 | fqtytype | 用量类型 | bpchar | 1 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 |
| 41 | fqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 42 | fconsumesubqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 43 | freceiptsubbaseqty | 已收料基本数量 | numeric | 23 | 10 | √ | 0 | 已收料基本数量 |
| 44 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 45 | fsubstitute | 替代料 | bpchar | 1 |  | √ | '0' | 替代料 |
| 46 | freceiptsubqty | 已收料数量 | numeric | 23 | 10 | √ | 0 | 已收料数量 |
| 47 | fsubsrcbillno | 来源单据编码 | varchar | 80 |  | √ | ' ' | 来源单据编码 |
| 48 | fisbackflushnew | 倒冲 | bpchar | 1 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 49 | fsubsrcbillentryseq | 来源单据行号 | varchar | 20 |  | √ | ' ' | 来源单据行号 |
| 50 | fsubmaterialnametext | 用料名称 | varchar | 255 |  | √ | ' ' | 用料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_modulelist_sub |  | fdetailid |
| 2 | idx_pur_modulelist_sub_fid |  | fentryid,fseq |

---

## 用料信息-多语言表 t_pur_modulelist_sub_l

- **表名称：** 用料信息-多语言表
- **表名：** t_pur_modulelist_sub_l

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
| 1 | idx_pur_modulelist_sub_l |  | fdetailid,flocaleid |
| 2 | pk_t_pur_modulelist_sub_l |  | fpkid |

---

## 关联子实体-子表 t_pur_modulelist_sub_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_modulelist_sub_lk

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
| 1 | pk_pur_modulelist_sub_lk |  | fpkid |
| 2 | idx_pur_modulelist_sub_lk_fk |  | fdetailid |

---

## 协同用料清单-主表 t_pur_modulelist

- **表名称：** 协同用料清单-主表
- **表名：** t_pur_modulelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 2 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 3 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 9 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fmftorderentryid | 委外工单分录Id | varchar | 50 |  | √ | ' ' | 委外工单分录Id |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | fpoentryseq | 采购订单行号 | varchar | 20 |  | √ | ' ' | 采购订单行号 |
| 20 | fentrypurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fmaterialnametext | 产品名称 | varchar | 255 |  | √ | ' ' | 产品名称 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fpobillno | 采购订单编号 | varchar | 80 |  | √ | ' ' | 采购订单编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fmftordernumber | 委外工单编号 | varchar | 80 |  | √ | ' ' | 委外工单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_modulelist_fpobillno |  | fpobillno,fmftorderentryid |
| 2 | idx_pur_modulelist_fbizid |  | fbizpartnerid |
| 3 | pk_t_pur_modulelist |  | fentryid |
| 4 | idx_pur_modulelist_fbillno |  | fbillno,fcreatetime |

---

## 协同用料清单-多语言表 t_pur_modulelist_l

- **表名称：** 协同用料清单-多语言表
- **表名：** t_pur_modulelist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_modulelist_l_fid |  | fentryid,flocaleid |
| 2 | pk_t_pur_modulelist_l |  | fpkid |

---

## 协同用料清单-关联追踪表 t_pur_modulelist_tc

- **表名称：** 协同用料清单-关联追踪表
- **表名：** t_pur_modulelist_tc

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
| 1 | idx_pur_modulelist_tc_tbill |  | ftbillid |
| 2 | pk_pur_modulelist_tc |  | fid |
| 3 | idx_pur_modulelist_tc_tid |  | ftid |

---

## 协同用料清单-反写记录表 t_pur_modulelist_wb

- **表名称：** 协同用料清单-反写记录表
- **表名：** t_pur_modulelist_wb

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
| 1 | idx_pur_modulelist_wb_fk |  | fid |
| 2 | pk_pur_modulelist_wb |  | fentryid |
