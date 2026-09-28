# BOM维护-pdm_mftbom

## 子项信息-分表 t_pdm_mftbomentry_a

- **表名称：** 子项信息-分表
- **表名：** t_pdm_mftbomentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freplaceplanentryid | 替代方案分录ID | int8 | 64 |  | √ | 0 | 替代方案分录ID |
| 3 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 4 | fdisassmblerate | 拆卸成本比例% | numeric | 23 | 10 | √ | 0 | 拆卸成本比例% |
| 5 | fsuitedisassmblerate | 套件价格拆分比例% | numeric | 23 | 10 | √ | 0 | 套件价格拆分比例% |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

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
| 3 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 5 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | foperationnumber | 产出工序号 | varchar | 50 |  | √ | ' ' | 产出工序号 |
| 9 | fprodunitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | ftype | 产品类型 | varchar | 30 |  | √ | ' ' | 产品类型,枚举: 10720 :联产品 10730 :副产品 |
| 11 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 12 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fprodqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | foperationid | 产出工序 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 16 | fprocessseq | 产出序列号 | varchar | 50 |  | √ | ' ' | 产出序列号 |

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
| 2 | fgroupid | BOM分组 | int8 | 64 |  | √ | 0 | BOM分组 mpdm_bomgroup |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0.0000000000 | 成品率% |
| 5 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsalorderentryseq | 销售订单行号 | varchar | 50 |  | √ | ' ' | 销售订单行号 |
| 9 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fqty | 生产单位数量 | numeric | 23 | 10 | √ | 0 | 生产单位数量 |
| 12 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 13 | fsalorderid | 销售订单ID | int8 | 64 |  | √ | 0 | 销售订单ID |
| 14 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fqtybaseunit | 阶梯计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fversionid | 物料版本(屏蔽) | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | ftypeid | BOM类型 | int8 | 64 |  | √ | 0 | BOM类型 mpdm_bomtype |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdatasource | BOM来源 | bpchar | 1 |  | √ | 1 | BOM来源,枚举: 1 :直接创建 2 :引入创建 3 :PLM集成 4 :分配 |
| 21 | fnumber | BOM编码 | varchar | 30 |  | √ | ' ' | BOM编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fisdefault | 默认版本 | bpchar | 1 |  | √ | '0' | 默认版本 |
| 25 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 26 | fsalorderno | 销售订单编号 | varchar | 50 |  |  | ' ' | 销售订单编号 |
| 27 | fsalorderentryid | 销售订单行ID | int8 | 64 |  | √ | 0 | 销售订单行ID |
| 28 | fdisableuserid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 30 | fecn | ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 31 | fiscoproduct | 联副产品 | bpchar | 1 |  | √ | '0' | 联副产品 |
| 32 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 33 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 36 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 37 | fplmmaterialver | PLM物料版本 | varchar | 50 |  | √ | ' ' | PLM物料版本 |
| 38 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | freplacenoid | 替代号 | int8 | 64 |  | √ | 0 | BOM替代号 mpdm_replaceno |
| 40 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fecnversion | ECN版本 | varchar | 50 |  | √ | ' ' | ECN版本 |
| 44 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 45 | fmatid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 46 | fbomuse | BOM用途 | varchar | 36 |  | √ | ',A,B,C,D,' | BOM用途,枚举: A :自制 B :委外 C :报价 D :组装 |
| 47 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 |
| 48 | fplmbomid | PLMBOMID | int8 | 64 |  | √ | 0 | PLMBOMID |
| 49 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 50 | fsrcsuperbomid | 源配置BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 51 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 52 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 53 | fbaseqty | 基本单位数量 | numeric | 23 | 10 | √ | 0 | 基本单位数量 |

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
| 2 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 3 | fbatchendqty | 批量至（<） | numeric | 23 | 10 | √ | 0.0000000000 | 批量至（<） |
| 4 | fqtydenominator | 用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分母 |
| 5 | fqtynumerator | 用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 用量：分子 |
| 6 | fisstepfix | 启用固定损耗 | bpchar | 1 |  | √ | '0' | 启用固定损耗 |
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
| 1 | idx_pdm_mftbomqtyentry_fk |  | fentryid |
| 2 | t_pdm_mftbomqtyentry_pkey |  | fdetailid |

---

## 销售订单-子表 t_pdm_mftbomsaleorder

- **表名称：** 销售订单-子表
- **表名：** t_pdm_mftbomsaleorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsaleorderentryseq | 销售订单行号 | varchar | 8 |  | √ | ' ' | 销售订单行号 |
| 3 | fsaleorderno | 销售订单编码 | int8 | 64 |  | √ | 0 | 销售订单F7 sm_salorder_f7 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsaleorderentryid | 销售订单分录ID | int8 | 64 |  | √ | 0 | 销售订单分录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_mftbomsaleorder |  | fentryid |
| 2 | idx_pdm_prosaleorder_entryid |  | fsaleorderentryid |

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
| 8 | foperatemrp | MRP运算 | varchar | 30 |  | √ | ' ' | MRP运算,枚举: 0 :是 1 :否 |
| 9 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 10 | fchilddenominator | 用量：分母 | numeric | 23 | 10 | √ | 0 | 用量：分母 |
| 11 | fplmbomentryid | PLMBOM分录ID | int8 | 64 |  | √ | 0 | PLMBOM分录ID |
| 12 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | fentryecnid | 工程变更单ID | varchar | 100 |  | √ | ' ' | 工程变更单ID |
| 14 | fentrymatid | 子物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 16 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 17 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 18 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 19 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 20 | fentrychildtype | 子项类型 | varchar | 30 |  | √ | ' ' | 子项类型,枚举: 1 :标准件 2 :返还件 |
| 21 | fqtydenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分母 |
| 22 | fecnvaliddate | ECN生效时间 | timestamp | 0 |  |  | null | ECN生效时间 |
| 23 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 25 | fwarehouseid | 默认发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsupplymode | 领发料来源 | varchar | 30 |  | √ | ' ' | 领发料来源,枚举: A :供应商提供 B :客户提供 |
| 28 | fismodifiable | 可修改 | bpchar | 1 |  | √ | '0' | 可修改 |
| 29 | foutorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | ftimeunit | 时间单位 | varchar | 30 |  | √ | ' ' | 时间单位,枚举: D :天 H :时 M :分 S :秒 |
| 31 | fisoptional | 选配 | bpchar | 1 |  | √ | '0' | 选配 |
| 32 | fisreplaceshow | 替代显示 | bpchar | 1 |  | √ | '0' | 替代显示 |
| 33 | fnumber | 分录子项编码 | varchar | 50 |  | √ | ' ' | 分录子项编码 |
| 34 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fentryecn | 组件ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 37 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 38 | fsupplytype | 领发料类型 | varchar | 30 |  | √ | ' ' | 领发料类型,枚举: 10910 :本库存组织领料 10920 :跨库存组织调拨 10930 :跨库存组织领料 10940 :跨库存组织直送 |
| 39 | fiskey | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 40 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 41 | freplacemode | 替代方式 | varchar | 5 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 |
| 42 | fchildnumerator | 用量：分子 | numeric | 23 | 10 | √ | 0 | 用量：分子 |
| 43 | foperationnumber | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 44 | fleadtime | 提前期偏置时间(天) | int8 | 64 |  | √ | 0 | 提前期偏置时间(天) |
| 45 | fmaterialattr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10060 :内协（废弃） 10070 :特征件 |
| 46 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 47 | fentryconfigcode | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 48 | fisreplaceplanmm | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 49 | fchildunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 50 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 51 | fqtynumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分子 |
| 52 | fecnno | 工程变更单编码 | varchar | 50 |  | √ | ' ' | 工程变更单编码 |
| 53 | fisbackflush | fisbackflush | varchar | 30 |  | √ | ' ' |  |
| 54 | fisreplaceable | 可替换 | bpchar | 1 |  | √ | '0' | 可替换 |
| 55 | fprovidetype | 供应类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 56 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 57 | ftype | 选配类型（废弃） | varchar | 30 |  | √ | ' ' | 选配类型（废弃）,枚举: A :库存 |
| 58 | flocationid | 默认发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 59 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 60 | fisstockalloc | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 61 | freplaceplanstrategy | 替代策略 | varchar | 10 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 62 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 63 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 64 | fisselectable | 可选 | bpchar | 1 |  | √ | '0' | 可选 |
| 65 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 66 | fisbackflushnew | 倒冲 | varchar | 30 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :倒冲 C :工作中心决定是否倒冲 |
| 67 | freplaceplanid | 替代方案编码 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |

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
| 5 | fsetuplocation | 安装位置 | varchar | 50 |  | √ | ' ' | 安装位置 |

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
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
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
