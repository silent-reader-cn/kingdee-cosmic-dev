# 重复生产工单-arm_productionorder

## 用料清单-子表 t_arm_prodorderentry

- **表名称：** 用料清单-子表
- **表名：** t_arm_prodorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmasterid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fxferfromlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | freplaceparts | 替代件 | bpchar | 1 |  | √ | ' ' | 替代件 |
| 6 | fistransferrequired | 备料调拨 | bpchar | 1 |  | √ | ' ' | 备料调拨 |
| 7 | fissuemode | 领送料方式 | varchar | 8 |  | √ | ' ' | 领送料方式,枚举: 11010 :生产领料 11030 :看板 11050 :直送 11040 :不领料 |
| 8 | fbackflushtime | 倒冲时机 | varchar | 8 |  | √ | ' ' | 倒冲时机,枚举: |
| 9 | fissuedqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | freppriority | 替代优先级 | int4 | 32 |  | √ | 0 | 替代优先级 |
| 12 | fnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 13 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 14 | fkeyparts | 关键件 | bpchar | 1 |  | √ | ' ' | 关键件 |
| 15 | frequireddatetime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 16 | freplaceplan | 替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 17 | fdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 18 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 19 | fassociatepickqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 20 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | ' ' | 来源于BOM展开 |
| 21 | fstandardqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 22 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 23 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 24 | fxferfromorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 26 | fcompauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 27 | fcompbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 28 | fbackflush | 倒冲 | bpchar | 1 |  | √ | ' ' | 倒冲 |
| 29 | fqtytype | 用量类型 | varchar | 8 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 30 | fcompunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fissueorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fcomptracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 33 | fcompmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 34 | fusagerate | 使用比例% | numeric | 23 | 10 | √ | 0 | 使用比例% |
| 35 | fissuelocationid | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 36 | fmatcommon | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 37 | fcomponentid | 子项编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 38 | fxferfromwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 39 | fissuewarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 40 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 41 | fleadtimeoffset | 提前期偏置(天) | int4 | 32 |  | √ | 0 | 提前期偏置(天) |
| 42 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 43 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | frequiredqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 46 | fproductrtinsp | 生产退料检验 | bpchar | 1 |  | √ | ' ' | 生产退料检验 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_prodorderentry_fid |  | fid |
| 2 | pk_t_arm_prodorderentry |  | fentryid |

---

## 重复生产工单-主表 t_arm_productionorder

- **表名称：** 重复生产工单-主表
- **表名：** t_arm_productionorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrcentryseq | 来源单据分录 | varchar | 50 |  | √ | ' ' | 来源单据分录 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsrcbillname | 来源单据标识 | varchar | 50 |  | √ | ' ' | 来源单据标识 |
| 7 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 8 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | forderstatus | 状态 | varchar | 8 |  | √ | ' ' | 状态,枚举: P :计划 F :计划确认 E :锁定 R :下达 C :关闭 |
| 10 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 11 | fdemandbilltype | 需求单据类型 | varchar | 50 |  | √ | ' ' | 需求单据类型 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fqtytoscrap | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fdemandentryseqid | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 16 | fversion | 版本号 | int4 | 32 |  | √ | 1 | 版本号 |
| 17 | fincompleteqty | 未入库良品数 | numeric | 23 | 10 | √ | 0 | 未入库良品数 |
| 18 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 19 | fdemandbillnumber | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 20 | fmaterialno | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 21 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 24 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 25 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fdemandbillname | 需求单据标识 | varchar | 50 |  | √ | ' ' | 需求单据标识 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | funreportqty | 未汇报数量 | numeric | 23 | 10 | √ | 0 | 未汇报数量 |
| 29 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 30 | fyieldpercent | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 31 | fproductionseq | 生产顺序 | numeric | 23 | 10 | √ | 0 | 生产顺序 |
| 32 | fstartdatetime | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 33 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 34 | fdemandbillid | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |
| 35 | fqtytocomplete | 预计完工数量 | numeric | 23 | 10 | √ | 0 | 预计完工数量 |
| 36 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 37 | fneeddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 38 | fworkshopid | 车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fdemandentryseq | 需求单据分录 | varchar | 50 |  | √ | ' ' | 需求单据分录 |
| 40 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 41 | fleadtime | 提前期 | int4 | 32 |  | √ | 0 | 提前期 |
| 42 | fduedatetime | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 43 | fremark | 备注 | varchar | 510 |  |  | null | 备注 |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fcompletebaseqty | 入库基本数量 | numeric | 23 | 10 | √ | 0 | 入库基本数量 |
| 46 | fbaseqtytostart | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 47 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 48 | fcompleteqty | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 49 | fsrcentryseqid | 来源单据分录行ID | int8 | 64 |  | √ | 0 | 来源单据分录行ID |
| 50 | fqtytostart | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 51 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 52 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_productionorder_org |  | forgid |
| 2 | pk_t_arm_productionorder |  | fid |
