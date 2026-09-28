# 缺料分析单-mrp_smabill

## 子项明细-子表 t_mrp_smasubentry

- **表名称：** 子项明细-子表
- **表名：** t_mrp_smasubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubdemandbillno | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 3 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 4 | forderbillno | 订单编码 | varchar | 50 |  | √ | ' ' | 订单编码 |
| 5 | fsubmainorgid | 生产/委外组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbaserelqty | 采购申请/生产选单基本数量 | numeric | 23 | 10 | √ | 0 | 采购申请/生产选单基本数量 |
| 7 | fstockmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 8 | fstandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 9 | fsrcbillentryno | 用料清单行号 | int8 | 64 |  | √ | 0 | 用料清单行号 |
| 10 | fstockmaterielmaster | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 12 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 13 | fproductmaster | 产品名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fbusactissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 15 | forderentryid | 订单明细分录id | int8 | 64 |  | √ | 0 | 订单明细分录id |
| 16 | fstocksrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 19 | fordertype | 订单类型 | varchar | 10 |  | √ | ' ' | 订单类型,枚举: 10030 :自制 10050 :委外 10040 :外购 |
| 20 | fparententryid | 替代主料行id | int8 | 64 |  | √ | 0 | 替代主料行id |
| 21 | fbusstandqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 22 | fsubdemandseq | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 23 | fsubdemandentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | forderseq | 订单行号 | int8 | 64 |  | √ | 0 | 订单行号 |
| 25 | fstocksrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 26 | fcalcseq | 计算顺序 | int8 | 64 |  | √ | 0 | 计算顺序 |
| 27 | fstocksrcbillno | 用料清单号 | varchar | 50 |  | √ | ' ' | 用料清单号 |
| 28 | frelqty | 采购申请/生产选单数量 | numeric | 23 | 10 | √ | 0 | 采购申请/生产选单数量 |
| 29 | fbusdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 30 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 31 | fsubdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 32 | fstocksrcentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 33 | fcommonmaterial | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 34 | fbaseorderqty | 订单基本数量 | numeric | 23 | 10 | √ | 0 | 订单基本数量 |
| 35 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fsubdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 37 | forderbaseunit | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fstockmanuentryid | 生产工单行ID | int8 | 64 |  | √ | 0 | 生产工单行ID |

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

## 缺料分析单-主表 t_mrp_smabill

- **表名称：** 缺料分析单-主表
- **表名：** t_mrp_smabill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsmascheme | 分析方案 | int8 | 64 |  | √ | 0 | [缺料分析方案 mrp_smascheme](../mrp_files/mrp_smascheme.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
| 5 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 6 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 7 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 10 | freplaceplan | 物料替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 11 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 12 | fentryprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 13 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 14 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 16 | freplacepriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 17 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 18 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 19 | fqtydenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0 | 基本单位分母 |
| 20 | fqtynumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 21 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 22 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 24 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 26 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 27 | fbusnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 28 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 29 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 30 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | fentrytracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 32 | fpicklocation | 领料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 33 | fpickorg | 领料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fpickwarehouse | 领料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

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
| 2 | fsubbaseinvqtylack | 基本单位库存数量 | numeric | 23 | 10 | √ | 0 | 基本单位库存数量 |
| 3 | fcollecttag | 汇总标识 | varchar | 50 |  | √ | ' ' | 汇总标识 |
| 4 | fbaseinvcanpickqty | 基本单位即时可领数量 | numeric | 23 | 10 | √ | 0 | 基本单位即时可领数量 |
| 5 | freservedqty | 预留数量 | numeric | 23 | 10 | √ | 0 | 预留数量 |
| 6 | fbaseonordercanpickqty | 基本单位在途可领数量 | numeric | 23 | 10 | √ | 0 | 基本单位在途可领数量 |
| 7 | fsubonorderqty | 在途数量 | numeric | 23 | 10 | √ | 0 | 在途数量 |
| 8 | fbasereservedqty | 基本预留数量 | numeric | 23 | 10 | √ | 0 | 基本预留数量 |
| 9 | fsubinvqtylack | 库存数量 | numeric | 23 | 10 | √ | 0 | 库存数量 |
| 10 | fcanpickedqty | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 11 | fsubbaseonorderqty | 基本单位在途数量 | numeric | 23 | 10 | √ | 0 | 基本单位在途数量 |
| 12 | finvcanpickqty | 即时可领数量 | numeric | 23 | 10 | √ | 0 | 即时可领数量 |
| 13 | fsubinspectionqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 14 | fbasecanpickedqty | 基本单位可领数量 | numeric | 23 | 10 | √ | 0 | 基本单位可领数量 |
| 15 | fonordercanpickqty | 在途可领数量 | numeric | 23 | 10 | √ | 0 | 在途可领数量 |
| 16 | fsubcansupplyqty | 可用供应数量 | numeric | 23 | 10 | √ | 0 | 可用供应数量 |
| 17 | fsubbaselackqtylack | 基本缺料数量 | numeric | 23 | 10 | √ | 0 | 基本缺料数量 |
| 18 | fsubbaseinspectionqty | 基本单位待检数量 | numeric | 23 | 10 | √ | 0 | 基本单位待检数量 |
| 19 | fsubbasecansupplyqty | 基本可用供应数量 | numeric | 23 | 10 | √ | 0 | 基本可用供应数量 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fsublackqtylack | 缺料数量 | numeric | 23 | 10 | √ | 0 | 缺料数量 |

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
| 2 | fbillformid | 订单类型 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 4 | fislack | 分析结果 | varchar | 50 |  | √ | ' ' | 分析结果,枚举: 0 :未计算 1 :库存充足 2 :材料短缺 3 :未参与计算 |
| 5 | fmanuentryid | 生产工单分录ID | int8 | 64 |  | √ | 0 | 生产工单分录ID |
| 6 | fsrcbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 7 | frowtype | 行类型 | varchar | 50 |  | √ | ' ' | 行类型,枚举: 0 :选单 1 :新增 |
| 8 | fpriority | 需求优先级 | int8 | 64 |  | √ | 0 | 需求优先级 |
| 9 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: A :正常 B :挂起 C :关闭 D :已结算 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 12 | fyieldrate | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 13 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fsrcentryseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 15 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 16 | fxkdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 17 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 19 | fxkdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |
| 20 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 21 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 22 | fmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 23 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 24 | fmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 27 | fxkdemandbill | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 28 | fisexpandall | 全展开 | bpchar | 1 |  | √ | '0' | 全展开 |
| 29 | fplanstatus | 计划状态 | varchar | 50 |  | √ | ' ' | 计划状态,枚举: A :计划 B :计划确认 C :下达 |
| 30 | fmainorgid | 生产/委外组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 32 | fxkdemandseq | 需求单据分录行号 | int8 | 64 |  | √ | 0 | 需求单据分录行号 |
| 33 | fxkdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 34 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 35 | fmoselected | 分析 | bpchar | 1 |  | √ | '0' | 分析 |
| 36 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 37 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 39 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

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

---

## 缺料清单-子表 t_mrp_smaentry

- **表名称：** 缺料清单-子表
- **表名：** t_mrp_smaentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsmatracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 3 | fbasecansupplyqty | 基本可用供应数量 | numeric | 23 | 10 | √ | 0 | 基本可用供应数量 |
| 4 | fsmamaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fcollecttag | 汇总标识 | varchar | 50 |  | √ | ' ' | 汇总标识 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fbasepickedqtylack | 基本已领数量 | numeric | 23 | 10 | √ | 0 | 基本已领数量 |
| 10 | fcanpickedqtylack | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 11 | fbaselackqtylack | 基本缺料数量 | numeric | 23 | 10 | √ | 0 | 基本缺料数量 |
| 12 | fsmaunit | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :业务单元 |
| 14 | fsmaauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fonorderqty | 在途数量 | numeric | 23 | 10 | √ | 0 | 在途数量 |
| 16 | fsmabaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fmustqtylack | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 18 | flackqtylack | 缺料数量 | numeric | 23 | 10 | √ | 0 | 缺料数量 |
| 19 | fbasecanpickedqtylack | 基本可领数量 | numeric | 23 | 10 | √ | 0 | 基本可领数量 |
| 20 | fsmaprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fbaseonorderqty | 基本在途数量 | numeric | 23 | 10 | √ | 0 | 基本在途数量 |
| 22 | fbasemustqtylack | 基本应发数量 | numeric | 23 | 10 | √ | 0 | 基本应发数量 |
| 23 | finspectionqty | 待检数量 | numeric | 23 | 10 | √ | 0 | 待检数量 |
| 24 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 25 | fcansupplyqty | 可用供应数量 | numeric | 23 | 10 | √ | 0 | 可用供应数量 |
| 26 | finvqtylack | 库存数量 | numeric | 23 | 10 | √ | 0 | 库存数量 |
| 27 | fpickedqtylack | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 28 | fbaseinvqtylack | 基本库存数量 | numeric | 23 | 10 | √ | 0 | 基本库存数量 |
| 29 | fbaseinspectionqty | 基本待检数量 | numeric | 23 | 10 | √ | 0 | 基本待检数量 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

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
