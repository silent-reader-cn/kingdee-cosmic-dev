# 需求-mpdm_kitting_demand

## 需求-主表 t_mpdm_kittingdemand

- **表名称：** 需求-主表
- **表名：** t_mpdm_kittingdemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkittingid | 齐套ID | int8 | 64 |  | √ | 0 | 齐套ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsrcbillno | 来源单据编号 | varchar | 30 |  | √ | ' ' | 来源单据编号 |
| 5 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 8 | fparentbillno | 上级单据编号 | varchar | 50 |  | √ | ' ' | 上级单据编号 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fparententryseq | 上级单据分录行号 | int8 | 64 |  | √ | 0 | 上级单据分录行号 |
| 11 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fsrcbillentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fparententryid | 上级单据分录ID | int8 | 64 |  | √ | 0 | 上级单据分录ID |
| 16 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kittingdemand |  | fid |
| 2 | idx_kitting_d_kittingid |  | fkittingid |

---

## 需求-分表 t_mpdm_kittingdemand_s

- **表名称：** 需求-分表
- **表名：** t_mpdm_kittingdemand_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasenumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 3 | freceivedbaseqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 11 | ffeedingqty | 补料数量 | numeric | 23 | 10 | √ | 0 | 补料数量 |
| 12 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 13 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 14 | freplaceplan | 替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 15 | freltransqty | 关联调拨数量 | numeric | 23 | 10 | √ | 0 | 关联调拨数量 |
| 16 | freltransbaseqty | 关联调拨基本数量 | numeric | 23 | 10 | √ | 0 | 关联调拨基本数量 |
| 17 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 18 | ffeedingbaseqty | 补料基本数量 | numeric | 23 | 10 | √ | 0 | 补料基本数量 |
| 19 | fmasterid | 物料（主数据） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 20 | fdemandbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 21 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 22 | frelreceivedqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 23 | frelreceivedbaseqty | 关联领料基本数量 | numeric | 23 | 10 | √ | 0 | 关联领料基本数量 |
| 24 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | ftransbaseqty | 已调拨基本数量 | numeric | 23 | 10 | √ | 0 | 已调拨基本数量 |
| 26 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 27 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 29 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 30 | foutlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 31 | freceivedqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 32 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 33 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 34 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 35 | frejectedbaseqty | 退料基本数量 | numeric | 23 | 10 | √ | 0 | 退料基本数量 |
| 36 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 37 | ftransqty | 已调拨数量 | numeric | 23 | 10 | √ | 0 | 已调拨数量 |
| 38 | fisbackflush | 倒冲 | varchar | 30 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 39 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 40 | frejectedqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 41 | fbasedenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0 | 基本单位分母 |
| 42 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | flocationid | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 44 | fixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 45 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 46 | fdeptorg | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | fdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 48 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kittingdemand_s |  | fid |
