# MRP执行结果表数据-mrp_peginfodata

## MRP执行结果表数据-主表 t_mrp_peginfodata

- **表名称：** MRP执行结果表数据-主表
- **表名：** t_mrp_peginfodata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fbillno | 计划运算号 | varchar | 30 |  | √ | ' ' | 计划运算号 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_peginfodata |  | fid |
| 2 | idx_mrp_peginfodata |  | fbillno |

---

## 单据体-子表 t_mrp_peginfodataentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_peginfodataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductmodelid | 产品型号 | int8 | 64 |  | √ | 0 | 产品目录 bd_productsummary |
| 3 | frequiredate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 4 | fsupplybillno | 供应单据编码 | varchar | 100 |  | √ | ' ' | 供应单据编码 |
| 5 | frequireqty | 需求数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求数量 |
| 6 | fdemandauxpty | 需求物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | frequirepriority | 需求优先级 | varchar | 50 |  | √ | ' ' | 需求优先级 |
| 8 | fsupplydate | 要求可用日期 | timestamp | 0 |  |  | null | 要求可用日期 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | ftracknumberdem | 需求跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 11 | fsupplyunit | 供应计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fconfiguredcodedem | 需求配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 13 | fconfiguredcodesup | 供应配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 14 | fsupplantag | 供应计划标识 | varchar | 60 |  | √ | 'D' | 供应计划标识,枚举: A :通用 B :定制 C :选配 D :未设置 |
| 15 | fsupplyauxpty | 供应物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | frequireoperatorid | 需求物料计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fdemandbillf7 | 需求单据F7 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 18 | fsupplymaterialid | 供应物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 19 | freqbillno | 需求单据编号 | varchar | 100 |  | √ | ' ' | 需求单据编号 |
| 20 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | frequirematerialid | 需求物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 22 | frequirebillseq | 需求单据行号 | varchar | 50 |  | √ | ' ' | 需求单据行号 |
| 23 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0.0000000000 | 供应数量 |
| 24 | fproducttype | 产品系列 | int8 | 64 |  | √ | 0 | 产品分类 bd_productgroup |
| 25 | ftracknumbersup | 供应跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 26 | fsupplyoperatorid | 供应物料计划员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | factualdate | 实际供应日期 | timestamp | 0 |  |  | null | 实际供应日期 |
| 28 | fsupplydetail | 供应明细 | varchar | 100 |  | √ | ' ' | 供应明细 |
| 29 | fsupplybillf7 | 供应单据F7 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 30 | fsupplybillentryseq | 供应单据分录行号 | varchar | 50 |  | √ | ' ' | 供应单据分录行号 |
| 31 | frequirebillno | 需求来源号 | varchar | 100 |  | √ | ' ' | 需求来源号 |
| 32 | fproductfamilyid | 产品族 | int8 | 64 |  | √ | 0 | 产品分类 bd_productgroup |
| 33 | frequireunitid | 需求计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 34 | fsupplybilltpye | 供应类型 | varchar | 100 |  | √ | ' ' | 供应类型 |
| 35 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | frequirebilltpye | 需求类型 | varchar | 100 |  | √ | ' ' | 需求类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_peginfodataentry4 |  | fsupplymaterialid |
| 2 | pk_t_mrp_peginfodataentry |  | fentryid |
| 3 | idx_mrp_peginfodataentry3 |  | frequirematerialid |
| 4 | idx_mrp_peginfodataentry2 |  | frequirematerialid,fsupplymaterialid |
| 5 | idx_mrp_peginfodataentry1 |  | frequirebillno |
| 6 | idx_mrp_peginfodataentry |  | fid,fproductfamilyid,fproductmodelid |
