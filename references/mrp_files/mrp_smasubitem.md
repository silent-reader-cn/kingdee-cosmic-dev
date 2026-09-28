# 缺料需求单据-mrp_smasubitem

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
| 5 | fsubmainorgid | 生产组织/委外生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbaserelqty | 采购申请/生产选单基本数量 | numeric | 23 | 10 | √ | 0 | 采购申请/生产选单基本数量 |
| 7 | fstockmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 8 | fstandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 9 | fsrcbillentryno | 用料清单行号 | int8 | 64 |  | √ | 0 | 用料清单行号 |
| 10 | fstockmaterielmaster | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 13 | fproductmaster | 产品(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
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

## 缺料需求单据-主表 t_mrp_smabill

- **表名称：** 缺料需求单据-主表
- **表名：** t_mrp_smabill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fsmascheme | fsmascheme | int8 | 64 |  | √ | 0 |  |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |
| 10 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 11 | fbilltype | fbilltype | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

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
