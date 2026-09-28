# 缺料分析单-mrp_smabill

## 子项明细-子表 t_mrp_smasubentry

- **表名称：** 子项明细-子表
- **表名：** t_mrp_smasubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubdemandbillno | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 3 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 4 | forderbillno | 订单编码 | varchar | 50 |  | √ | ' ' | 订单编码 |
| 5 | fsubmainorgid | 生产/委外组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbaserelqty | 采购申请/生产选单基本数量 | numeric | 23 | 10 | √ | 0 | 采购申请/生产选单基本数量 |
| 7 | fstockmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 8 | fstandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 9 | fsrcbillentryno | 用料清单行号 | int8 | 64 |  | √ | 0 | 用料清单行号 |
| 10 | fstockmaterielmaster | 物料名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 13 | fproductmaster | 产品名称 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 14 | fbusactissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 15 | forderentryid | 订单明细分录id | int8 | 64 |  | √ | 0 | 订单明细分录id |
| 16 | fstocksrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 19 | fparententryid | 替代主料行id | int8 | 64 |  | √ | 0 | 替代主料行id |
| 20 | fbusstandqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 21 | fsubdemandseq | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 22 | fsubdemandentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 23 | forderseq | 订单行号 | int8 | 64 |  | √ | 0 | 订单行号 |
| 24 | fstocksrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 25 | fcalcseq | 计算顺序 | int8 | 64 |  | √ | 0 | 计算顺序 |
| 26 | fstocksrcbillno | 用料清单号 | varchar | 50 |  | √ | ' ' | 用料清单号 |
| 27 | frelqty | 采购申请/生产选单数量 | numeric | 23 | 10 | √ | 0 | 采购申请/生产选单数量 |
| 28 | fbusdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 29 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 30 | fsubdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 31 | fstocksrcentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 32 | fcommonmaterial | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 33 | fbaseorderqty | 订单基本数量 | numeric | 23 | 10 | √ | 0 | 订单基本数量 |
| 34 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fsubdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 36 | forderbaseunit | 产品基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fstockmanuentryid | 生产工单行ID | int8 | 64 |  | √ | 0 | 生产工单行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smasubentry |  | fentryid |
| 2 | idx_mrp_smasubentry |  | fid,fseq |

---

## 缺料分析单-关联追踪表 t_mrp_smabill_tc

- **表名称：** 缺料分析单-关联追踪表
- **表名：** t_mrp_smabill_tc

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
| 1 | idx_mrp_smabill_tc_tid |  | ftid |
| 2 | pk_mrp_smabill_tc |  | fid |
| 3 | idx_mrp_smabill_tc_tbill |  | ftbillid |

---

## 缺料清单-子表 t_mrp_smaentry

- **表名称：** 缺料清单-子表
- **表名：** t_mrp_smaentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsmatracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 3 | fbasecansupplyqty | 基本可用供应数量 | numeric | 23 | 10 | √ | 0 | 基本可用供应数量 |
| 4 | fsmamaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 6 | fcollecttag | 汇总标识 | varchar | 50 |  | √ | ' ' | 汇总标识 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbasepickedqtylack | 基本已领数量 | numeric | 23 | 10 | √ | 0 | 基本已领数量 |
| 9 | fcanpickedqtylack | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 10 | fbaselackqtylack | 基本缺料数量 | numeric | 23 | 10 | √ | 0 | 基本缺料数量 |
| 11 | fsmaunit | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :业务单元 |
| 13 | fsmaauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fonorderqty | 在途数量 | numeric | 23 | 10 | √ | 0 | 在途数量 |
| 15 | fsmabaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fmustqtylack | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 17 | flackqtylack | 缺料数量 | numeric | 23 | 10 | √ | 0 | 缺料数量 |
| 18 | fbasecanpickedqtylack | 基本可领数量 | numeric | 23 | 10 | √ | 0 | 基本可领数量 |
| 19 | fsmaprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fbaseonorderqty | 基本在途数量 | numeric | 23 | 10 | √ | 0 | 基本在途数量 |
| 21 | fbasemustqtylack | 基本应发数量 | numeric | 23 | 10 | √ | 0 | 基本应发数量 |
| 22 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 23 | fcansupplyqty | 可用供应数量 | numeric | 23 | 10 | √ | 0 | 可用供应数量 |
| 24 | finvqtylack | 库存数量 | numeric | 23 | 10 | √ | 0 | 库存数量 |
| 25 | fpickedqtylack | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 26 | fbaseinvqtylack | 基本库存数量 | numeric | 23 | 10 | √ | 0 | 基本库存数量 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smaentry |  | fentryid |
| 2 | idx_mrp_smaentry |  | fid,fseq |

---

## 缺料分析单-主表 t_mrp_smabill

- **表名称：** 缺料分析单-主表
- **表名：** t_mrp_smabill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsmascheme | 分析方案 | int8 | 64 |  | √ | 0 | 缺料分析方案 mrp_smascheme |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smabill |  | fid |
| 2 | idx_mrp_smabill |  | fbillno |

---

## 子项明细-分表 t_mrp_smasubentry_a

- **表名称：** 子项明细-分表
- **表名：** t_mrp_smasubentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 3 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 4 | fbackflushtime | 倒冲时机 | varchar | 50 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :汇报倒冲 |
| 5 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 6 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 7 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 8 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 9 | freplaceplan | 物料替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 10 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 11 | fentryprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 12 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 13 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 15 | freplacepriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 16 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 17 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 18 | fqtydenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0 | 基本单位分母 |
| 19 | fqtynumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 20 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 21 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 23 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 25 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 26 | fbusnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 27 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 28 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 29 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | fentrytracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 31 | fpicklocation | 领料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 32 | fpickorg | 领料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fpickwarehouse | 领料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smasubentry_a |  | fentryid |
| 2 | idx_mrp_smasubentry_a |  | fid |

---

## 缺料分析单-反写记录表 t_mrp_smabill_wb

- **表名称：** 缺料分析单-反写记录表
- **表名：** t_mrp_smabill_wb

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
| 1 | idx_mrp_smabill_wb_fk |  | fid |
| 2 | pk_mrp_smabill_wb |  | fentryid |

---

## 子项明细-分表 t_mrp_smasubentry_c

- **表名称：** 子项明细-分表
- **表名：** t_mrp_smasubentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubbaseinvqtylack | 基本单位即时库存 | numeric | 23 | 10 | √ | 0 | 基本单位即时库存 |
| 3 | fcollecttag | 汇总标识 | varchar | 50 |  | √ | ' ' | 汇总标识 |
| 4 | fbaseinvcanpickqty | 基本单位即时可领数量 | numeric | 23 | 10 | √ | 0 | 基本单位即时可领数量 |
| 5 | freservedqty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 6 | fbaseonordercanpickqty | 基本单位在途可领数量 | numeric | 23 | 10 | √ | 0 | 基本单位在途可领数量 |
| 7 | fsubonorderqty | 在途数量 | numeric | 23 | 10 | √ | 0 | 在途数量 |
| 8 | fbasereservedqty | 基本预留数量 | numeric | 23 | 10 | √ | 0 | 基本预留数量 |
| 9 | fsubinvqtylack | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |
| 10 | fcanpickedqty | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 11 | fsubbaseonorderqty | 基本单位在途数量 | numeric | 23 | 10 | √ | 0 | 基本单位在途数量 |
| 12 | finvcanpickqty | 即时可领数量 | numeric | 23 | 10 | √ | 0 | 即时可领数量 |
| 13 | fbasecanpickedqty | 基本单位可领数量 | numeric | 23 | 10 | √ | 0 | 基本单位可领数量 |
| 14 | fonordercanpickqty | 在途可领数量 | numeric | 23 | 10 | √ | 0 | 在途可领数量 |
| 15 | fsubcansupplyqty | 可用供应数量 | numeric | 23 | 10 | √ | 0 | 可用供应数量 |
| 16 | fsubbaselackqtylack | 基本缺料数量 | numeric | 23 | 10 | √ | 0 | 基本缺料数量 |
| 17 | fsubbasecansupplyqty | 基本可用供应数量 | numeric | 23 | 10 | √ | 0 | 基本可用供应数量 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 19 | fsublackqtylack | 缺料数量 | numeric | 23 | 10 | √ | 0 | 缺料数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smasubentry_c |  | fentryid |
| 2 | idx_mrp_smasubentry_c |  | fid,fcollecttag |

---

## 订单明细-子表 t_mrp_smaorderentry

- **表名称：** 订单明细-子表
- **表名：** t_mrp_smaorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillformid | 订单类型 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | fislack | 分析结果 | varchar | 50 |  | √ | ' ' | 分析结果,枚举: 0 :未计算 1 :库存充足 2 :材料短缺 3 :未参与计算 |
| 5 | fmanuentryid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录ID |
| 6 | fsrcbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 7 | frowtype | 行类型 | varchar | 50 |  | √ | ' ' | 行类型,枚举: 0 :选单 1 :新增 |
| 8 | fpriority | 需求优先级 | int8 | 64 |  | √ | 0 | 需求优先级 |
| 9 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 12 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fsrcentryseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 15 | fxkdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 16 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 18 | fxkdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 19 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 20 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 21 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | fmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 26 | fxkdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 27 | fisexpandall | 全展开 | bpchar | 1 |  | √ | '0' | 全展开 |
| 28 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 29 | fmainorgid | 生产/委外组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 31 | fxkdemandseq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 32 | fxkdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 33 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 34 | fmoselected | 分析 | bpchar | 1 |  | √ | '0' | 分析 |
| 35 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 36 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | funit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_smaorderentry |  | fentryid |
| 2 | idx_mrp_smaorderentry |  | fid,fseq |

---

## 关联子实体-子表 t_mrp_smaorderentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mrp_smaorderentry_lk

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
| 1 | idx_mrp_smaorderentry_lk_fk |  | fentryid |
| 2 | pk_mrp_smaorderentry_lk |  | fpkid |
