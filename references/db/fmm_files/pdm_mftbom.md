# BOM维护-pdm_mftbom

## 子项信息-分表 t_pdm_mftbomentry_a

- **表名称：** 子项信息-分表
- **表名：** t_pdm_mftbomentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | 工序序列 | int4 | 32 |  | √ | 0 | 工序序列 |
| 3 | fnetrequireratio | 净需求比例(%) | numeric | 23 | 10 | √ | 0 | 净需求比例(%) |
| 4 | ftagnum_tag | 位号_详情 | text | 0 |  |  | null | 位号_详情 |
| 5 | ftagnum | 位号 | varchar | 255 |  | √ | ' ' | 位号 |
| 6 | fchangetype | 变更类型 | varchar | 5 |  | √ | ' ' | 变更类型,枚举: A :立即变更 B :用完旧料 C :指定日期变更 |
| 7 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 8 | freplaceplanentryid | 替代方案分录ID | int8 | 64 |  | √ | 0 | 替代方案分录ID |
| 9 | fsuperiorfeaturebomid | 上级特征件BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 10 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 11 | fdisassmblerate | 拆卸成本比例% | numeric | 23 | 10 | √ | 0 | 拆卸成本比例% |
| 12 | fsuitedisassmblerate | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 14 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 15 | ffeaconfruleid | 特征配置规则 | int8 | 64 |  | √ | 0 | [特征配置规则 pdm_featureconfigrule](../pdm_files/pdm_featureconfigrule.md) |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_mftbomentry_a |  | fentryid |
| 2 | idx_pdm_mftbomentry_a |  | fid |

---

## 联副产品-子表 t_pdm_mftbomcopentry

- **表名称：** 联副产品-子表
- **表名：** t_pdm_mftbomcopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 基本单位数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位数量 |
| 3 | fprocesssequence | 产出序列号 | int4 | 32 |  | √ | 0 | 产出序列号 |
| 4 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 5 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 6 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 9 | foperationnumber | 产出工序号（废弃） | varchar | 50 |  | √ | ' ' | 产出工序号（废弃） |
| 10 | fprodunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | ftype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
| 12 | fentrymasterid | 分录行唯一标识 | int8 | 64 |  | √ | 0 | 分录行唯一标识 |
| 13 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 14 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fprocessnumber | 产出工序号 | int4 | 32 |  | √ | 0 | 产出工序号 |
| 16 | fprodqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | foperationid | 产出工序 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 19 | fprocessseq | 产出序列号（废弃） | varchar | 50 |  | √ | ' ' | 产出序列号（废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomcopentry_fid |  | fid |
| 2 | t_pdm_mftbomcopentry_pkey |  | fentryid |

---

## BOM维护-主表 t_pdm_mftbom

- **表名称：** BOM维护-主表
- **表名：** t_pdm_mftbom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | BOM分组 | int8 | 64 |  | √ | 0 | [BOM分组 mpdm_bomgroup](../mpdm_files/mpdm_bomgroup.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0.0000000000 | 成品率% |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsalorderentryseq | 销售订单行号 | varchar | 50 |  | √ | ' ' | 销售订单行号 |
| 9 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 12 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 13 | fsalorderid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 14 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fqtybaseunit | 阶梯计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fversionid | 物料版本(屏蔽) | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | ftypeid | BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdatasource | BOM来源 | bpchar | 1 |  | √ | 1 | BOM来源,枚举: 1 :直接创建 2 :引入创建 3 :PLM集成 4 :分配 |
| 21 | fnumber | BOM编码 | varchar | 100 |  | √ | ' ' | BOM编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fisdefault | 默认版本 | bpchar | 1 |  | √ | '0' | 默认版本 |
| 25 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 26 | fsalorderno | 销售订单编号 | varchar | 50 |  |  | ' ' | 销售订单编号 |
| 27 | fsalorderentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |
| 28 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 30 | fecn | ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 31 | fiscoproduct | 联副产品 | bpchar | 1 |  | √ | '0' | 联副产品 |
| 32 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 33 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 34 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 37 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 38 | fplmmaterialver | PLM物料版本 | varchar | 50 |  | √ | ' ' | PLM物料版本 |
| 39 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | freplacenoid | 替代号 | int8 | 64 |  | √ | 0 | [BOM替代号 mpdm_replaceno](../mpdm_files/mpdm_replaceno.md) |
| 41 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fecnversion | ECN版本 | varchar | 50 |  | √ | ' ' | ECN版本 |
| 45 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 46 | fmatid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 47 | fbomuse | BOM用途 | varchar | 36 |  | √ | ',A,B,C,D,' | BOM用途,枚举: A :自制 B :委外 C :报价 D :组装 |
| 48 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 49 | fplmbomid | PLMBOMID | int8 | 64 |  | √ | 0 | PLMBOMID |
| 50 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 51 | fsrcsuperbomid | 源配置BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 52 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 53 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 54 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbom_pkey |  | fid |
| 2 | idx_t_pdm_mftbom_createorg |  | fcreateorgid |
| 3 | idx_t_pdm_mftbom_master |  | fmasterid |
| 4 | idx_pdm_mftbom_compt3 |  | fmatid,ftypeid,fstatus,fenable |
| 5 | idx_pdm_mftbom_compt1 |  | fmatid,ftypeid,fstatus,fenable,freplacenoid,fversionid |
| 6 | idx_pdm_mftbom_compt2 |  | fmatid,ftypeid,fstatus,fenable,freplacenoid |
| 7 | idx_pdm_mftbom_fmaterial |  | fmaterialid |
| 8 | idx_pdm_mftbom_fnumber |  | fnumber |

---

## 子项信息-多语言表 t_pdm_mftbomentry_l

- **表名称：** 子项信息-多语言表
- **表名：** t_pdm_mftbomentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomentry_l_fid |  | fentryid,flocaleid |
| 2 | t_pdm_mftbomentry_l_pkey |  | fpkid |

---

## 联副产品-多语言表 t_pdm_mftbomcopentry_l

- **表名称：** 联副产品-多语言表
- **表名：** t_pdm_mftbomcopentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbomcopentry_l_pkey |  | fpkid |
| 2 | idx_pdm_mftbomcopentry_l_el |  | fentryid,flocaleid |

---

## 阶梯用量-子表 t_pdm_mftbomqtyentry

- **表名称：** 阶梯用量-子表
- **表名：** t_pdm_mftbomqtyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbatchstartqty | 批量从（>=） | numeric | 23 | 10 | √ | 0.0000000000 | 批量从（>=） |
| 2 | ffixscrap | 固定损耗(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗(废弃) |
| 3 | fbatchendqty | 批量至（<） | numeric | 23 | 10 | √ | 0.0000000000 | 批量至（<） |
| 4 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 5 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 6 | fisstepfix | 启用固定损耗(废弃) | bpchar | 1 |  | √ | '0' | 启用固定损耗(废弃) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbomqtyentry_pkey |  | fdetailid |
| 2 | idx_pdm_mftbomqtyentry_fk |  | fentryid |

---

## 位号具体值-子表 t_pdm_mftbomtagnumentry

- **表名称：** 位号具体值-子表
- **表名：** t_pdm_mftbomtagnumentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 2 | ftagnum | 位号 | varchar | 255 |  | √ | ' ' | 位号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | flineno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_mftbomtagnumentry |  | fdetailid |
| 2 | idx_pdm_mftbomtagnumentry_fk |  | fentryid |

---

## 子项信息-子表 t_pdm_mftbomentry

- **表名称：** 子项信息-子表
- **表名：** t_pdm_mftbomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 3 | fissuemode | 领送料方式 | varchar | 30 |  | √ | ' ' | 领送料方式,枚举: 11010 :生产领料 11030 :看板 11050 :直送 11040 :不领料 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | freppriority | 优先级 | int8 | 64 |  | √ | 0 | 优先级 |
| 6 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 7 | fecnverion | ECN版本 | varchar | 50 |  | √ | ' ' | ECN版本 |
| 8 | foperatemrp | MRP运算 | varchar | 30 |  | √ | ' ' | MRP运算 |
| 9 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 10 | fchilddenominator | 用量：分母 | numeric | 23 | 10 | √ | 0 | 用量：分母 |
| 11 | fplmbomentryid | PLMBOM分录ID | int8 | 64 |  | √ | 0 | PLMBOM分录ID |
| 12 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | fentryecnid | 工程变更单ID | varchar | 100 |  | √ | ' ' | 工程变更单ID |
| 14 | fentrymatid | 子物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 16 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 17 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 18 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fentrychildtype | 子项类型 | varchar | 30 |  | √ | ' ' | 子项类型,枚举: 1 :标准件 2 :返还件 |
| 21 | fqtydenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分母 |
| 22 | fecnvaliddate | ECN生效时间 | timestamp | 0 |  |  | null | ECN生效时间 |
| 23 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fwarehouseid | 默认发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 26 | frepacetype | frepacetype | varchar | 50 |  | √ | ' ' |  |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fsupplymode | 领发料来源(废弃) | varchar | 30 |  | √ | ' ' | 领发料来源(废弃),枚举: A :供应商提供 B :客户提供 |
| 29 | fismodifiable | 可修改 | bpchar | 1 |  | √ | '0' | 可修改 |
| 30 | foutorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | ftimeunit | 时间单位 | varchar | 30 |  | √ | ' ' | 时间单位,枚举: D :天 H :时 M :分 S :秒 |
| 32 | fisoptional | 选配 | bpchar | 1 |  | √ | '0' | 选配 |
| 33 | fentrymasterid | 分录行唯一标识 | int8 | 64 |  | √ | 0 | 分录行唯一标识 |
| 34 | fisreplaceshow | 替代显示 | bpchar | 1 |  | √ | '0' | 替代显示 |
| 35 | fnumber | 分录子项编码(废弃) | varchar | 50 |  | √ | ' ' | 分录子项编码(废弃) |
| 36 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fentryecn | 组件ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 39 | fprocessseq | 工序序列（废弃） | varchar | 50 |  | √ | ' ' | 工序序列（废弃） |
| 40 | fsupplytype | 供应类型 | varchar | 30 |  | √ | ' ' | 供应类型,枚举: 10040 :外购 10030 :自制 10050 :委外 |
| 41 | fiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 42 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 43 | freplacemode | 替代方式 | varchar | 5 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 C :按比例 |
| 44 | fchildnumerator | 用量：分子 | numeric | 23 | 10 | √ | 0 | 用量：分子 |
| 45 | foperationnumber | 工序号（废弃） | varchar | 50 |  | √ | ' ' | 工序号（废弃） |
| 46 | fleadtime | 提前期偏置(天) | int8 | 64 |  | √ | 0 | 提前期偏置(天) |
| 47 | fmaterialattr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10060 :内协（废弃） 10070 :特征件 |
| 48 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 49 | fentryconfigcode | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 50 | fisreplaceplanmm | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 51 | fchildunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 52 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 53 | fqtynumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分子 |
| 54 | fecnno | 工程变更单编码 | varchar | 50 |  | √ | ' ' | 工程变更单编码 |
| 55 | fisbackflush | fisbackflush | varchar | 30 |  | √ | ' ' |  |
| 56 | fisreplaceable | 可替换 | bpchar | 1 |  | √ | '0' | 可替换 |
| 57 | fprovidetype | 供应类型（废弃） | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 58 | ffixscrap | 固定损耗(废弃) | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗(废弃) |
| 59 | ftype | 选配类型（废弃） | varchar | 30 |  | √ | ' ' | 选配类型（废弃）,枚举: A :库存 |
| 60 | flocationid | 默认发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 61 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 62 | fisstockalloc | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 63 | freplaceplanstrategy | 替代策略 | varchar | 10 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 64 | fisbulkmaterial | 散装物料(废弃) | bpchar | 1 |  | √ | '0' | 散装物料(废弃) |
| 65 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 66 | fisselectable | 可选 | bpchar | 1 |  | √ | '0' | 可选 |
| 67 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 68 | fisbackflushnew | 倒冲 | varchar | 30 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :倒冲 C :工作中心决定是否倒冲 |
| 69 | freplaceplanid | 替代方案编码 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomentry_fid |  | fid |
| 2 | idx_pdm_mftbomentry_m1 |  | fmaterialid |
| 3 | t_pdm_mftbomentry_pkey |  | fentryid |
| 4 | idx_pdm_mftbomentry_c2 |  | fid,finvaliddate |
| 5 | idx_pdm_mftbomentry_c1 |  | fid,fvaliddate,finvaliddate |
| 6 | idx_pdm_mftbomentry_c3 |  | fid,finvaliddate,fissuemode |

---

## 安装位置-子表 t_pdm_mftbomsetupentry

- **表名称：** 安装位置-子表
- **表名：** t_pdm_mftbomsetupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 子项数量 | numeric | 23 | 10 | √ | 0.0000000000 | 子项数量 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomsetupentry_fk |  | fentryid |
| 2 | t_pdm_mftbomsetupentry_pkey |  | fdetailid |

---

## 安装位置-多语言表 t_pdm_mftbomsetupentry_l

- **表名称：** 安装位置-多语言表
- **表名：** t_pdm_mftbomsetupentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fsetuplocation | 安装位置 | varchar | 2000 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomsetupentry_l_el |  | fdetailid,flocaleid |
| 2 | t_pdm_mftbomsetupentry_l_pkey |  | fpkid |

---

## BOM维护-使用范围表 t_pdm_mftbom_u

- **表名称：** BOM维护-使用范围表
- **表名：** t_pdm_mftbom_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbom_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_pdm_mftbom_u_uo |  | fuseorgid |

---

## BOM维护-使用范围位图表 t_pdm_mftbom_m

- **表名称：** BOM维护-使用范围位图表
- **表名：** t_pdm_mftbom_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_mftbom_m |  | forgid |

---

## BOM维护-多语言表 t_pdm_mftbom_l

- **表名称：** BOM维护-多语言表
- **表名：** t_pdm_mftbom_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称（废弃） | varchar | 50 |  | √ | ' ' | 名称（废弃） |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pdm_mftbom_l_pkey |  | fpkid |
| 2 | idx_pdm_mftbom_l_fid |  | fid,flocaleid |
