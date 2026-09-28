# 采购需求-ssm_purdemand

## 采购需求-主表 t_ssm_purdemand

- **表名称：** 采购需求-主表
- **表名：** t_ssm_purdemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssm_purdemand_m0 |  | fbillno |
| 2 | pk_ssm_purdemand |  | fid |

---

## 采购需求-子表 t_ssm_plandemand

- **表名称：** 采购需求-子表
- **表名：** t_ssm_plandemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 分录行内码 | int8 | 64 |  | √ | 0 | 分录行内码 |
| 3 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrcbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 5 | fbizunit | 业务单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fissuedqty | 已完成数量 | numeric | 23 | 10 | √ | 0 | 已完成数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdemandforecast | 需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 10 | fissuedbaseqty | 已完成基本数量 | numeric | 23 | 10 | √ | 0 | 已完成基本数量 |
| 11 | fdemandorg | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | forigin | 需求类型 | varchar | 20 |  | √ | ' ' | 需求类型,枚举: 0 :预测 1 :交货 2 :发货 3 :合并 |
| 14 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 15 | frelease | 发放号 | varchar | 50 |  | √ | ' ' | 发放号 |
| 16 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 17 | freqdate | 客户要货日期 | timestamp | 0 |  |  | null | 客户要货日期 |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 19 | fqty | 订单数量 | numeric | 23 | 10 | √ | 0 | 订单数量 |
| 20 | freqbillcreatetime | 需求单据创建时间 | timestamp | 0 |  |  | null | 需求单据创建时间 |
| 21 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 22 | fplandeliverydate | 计划发货日期 | timestamp | 0 |  |  | null | 计划发货日期 |
| 23 | freqbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 24 | fmastermaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 25 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 27 | fbaseunitqty | 订单基本数量 | numeric | 23 | 10 | √ | 0 | 订单基本数量 |
| 28 | fdemandtype | DemandTypeEnum | bpchar | 1 |  | √ | ' ' | DemandTypeEnum,枚举: 0 :--标准销售订单 1 :--委托代销订单 2 :--标准销售计划协议 3 :--委托代销计划协议 4 :采购独立需求 5 :重复生产用料清单 6 :销售订单 7 :销售计划协议 8 :生产工单用料清单 9 :委外工单用料清单 |
| 29 | flineenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 30 | fimportdatetime | 导入时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 导入时间 |
| 31 | fbillid | 单据内码 | int8 | 64 |  | √ | 0 | 单据内码 |
| 32 | fstockorg | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | freference | 参考值 | varchar | 50 |  | √ | ' ' | 参考值 |
| 34 | fcusmatid | 客户物料编码 | int8 | 64 |  | √ | 0 | [客户物料对应表明细信息 bd_customermaterialinfo](../basedata_files/bd_customermaterialinfo.md) |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fbilltype | 需求来源 | varchar | 50 |  | √ | ' ' | 需求来源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_plandemand |  | fentryid |
| 2 | idx_ssm_plandemand_fk |  | fid |
