# 生产线需求-psw_linedemand

## 生产线需求-主表 t_psw_linedemand

- **表名称：** 生产线需求-主表
- **表名：** t_psw_linedemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t__psw_linedemand |  | fbillno,fid |
| 2 | pk_t_psw_linedemand |  | fid |

---

## 生产线需求-子表 t_psw_plandemand

- **表名称：** 生产线需求-子表
- **表名：** t_psw_plandemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyorg | 供应组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrcentryid | 分录行内码 | int8 | 64 |  |  | null | 分录行内码 |
| 4 | fsrcbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 5 | fbizunit | 业务单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 8 | fissuedqty | 已完成数量 | numeric | 23 | 10 |  | null | 已完成数量 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fdemandforecast | 需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 11 | fbaseunit | 基本单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fdemandorg | 需求组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fissuedbaseqty | 已完成基本数量 | numeric | 23 | 10 |  | null | 已完成基本数量 |
| 14 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 15 | forigin | 需求类型 | varchar | 20 |  | √ | ' ' | 需求类型,枚举: 0 :预测 1 :交货 2 :发货 3 :合并 |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | freqdate | 客户要货日期 | timestamp | 0 |  |  | null | 客户要货日期 |
| 18 | flineno | 行号 | int8 | 64 |  |  | null | 行号 |
| 19 | fqty | 订单数量 | numeric | 23 | 10 |  | null | 订单数量 |
| 20 | freqbillcreatetime | 需求单据创建时间 | timestamp | 0 |  |  | null | 需求单据创建时间 |
| 21 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 22 | fplandeliverydate | 计划发货日期 | timestamp | 0 |  |  | null | 计划发货日期 |
| 23 | freqbaseqty | 需求基本数量 | numeric | 23 | 10 |  | null | 需求基本数量 |
| 24 | fmastermaterielid | 物料编码 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 25 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 27 | fdemandtype | DemandTypeEnum | bpchar | 1 |  | √ | ' ' | DemandTypeEnum,枚举: 0 :--标准销售订单 1 :--委托代销订单 2 :--标准销售计划协议 3 :--委托代销计划协议 4 :生产线独立需求 5 :重复生产用料清单 6 :销售订单 7 :销售计划协议 8 :生产工单用料清单 9 :委外工单用料清单 A :模拟需求 |
| 28 | fbaseunitqty | 订单基本数量 | numeric | 23 | 10 |  | null | 订单基本数量 |
| 29 | flineenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 30 | fimportdatetime | 导入时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 导入时间 |
| 31 | fbillid | 单据内码 | int8 | 64 |  |  | null | 单据内码 |
| 32 | freleaseno | 发放号 | varchar | 50 |  | √ | ' ' | 发放号 |
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
| 1 | idx_t_psw_plandemand |  | fid |
| 2 | pk_t_psw_plandemand |  | fentryid |
