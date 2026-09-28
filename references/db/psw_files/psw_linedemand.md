# 生产线需求-psw_linedemand

## 生产线需求-主表 t_psw_linedemand

- **表名称：** 生产线需求-主表
- **表名：** t_psw_linedemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
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

## 计划需求-子表 t_psw_plandemand

- **表名称：** 计划需求-子表
- **表名：** t_psw_plandemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyorg | 供应组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 3 | fsrcentryid | 分录行内码 | int8 | 64 |  |  | null | 分录行内码 |
| 4 | fsrcbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 5 | fbizunit | 业务单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  |  | null | 物料生产信息 bd_materialmftinfo |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 8 | fissuedqty | 发货数量 | numeric | 23 | 10 |  | null | 发货数量 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  |  | null | 计量单位 bd_measureunits |
| 11 | fdemandorg | 需求组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 12 | fissuedbaseqty | 已发货基本数量 | numeric | 23 | 10 |  | null | 已发货基本数量 |
| 13 | fenddate | 计划完成日期 | timestamp | 0 |  |  | null | 计划完成日期 |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  |  | null | 物料版本 bd_bomversion_new |
| 15 | freqdate | 要货日期 | timestamp | 0 |  |  | null | 要货日期 |
| 16 | flineno | 行号 | int8 | 64 |  |  | null | 行号 |
| 17 | fqty | 订单数量 | numeric | 23 | 10 |  | null | 订单数量 |
| 18 | freqbaseqty | 需求基本数量 | numeric | 23 | 10 |  | null | 需求基本数量 |
| 19 | fmastermaterielid | 物料编码 | int8 | 64 |  |  | null | 物料 bd_material |
| 20 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 21 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 22 | fdemandtype | 需求类型 | bpchar | 1 |  | √ | ' ' | 需求类型,枚举: 0 :标准销售订单 1 :委托代销订单 2 :标准销售计划协议 3 :委托代销计划协议 4 :生产线独立需求 5 :重复生产用料清单 |
| 23 | fbaseunitqty | 订单基本数量 | numeric | 23 | 10 |  | null | 订单基本数量 |
| 24 | flineenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 25 | fbillid | 单据内码 | int8 | 64 |  |  | null | 单据内码 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_psw_plandemand |  | fid |
| 2 | pk_t_psw_plandemand |  | fentryid |
