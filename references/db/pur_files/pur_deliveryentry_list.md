# 订单交货计划分录-pur_deliveryentry_list

## 交货计划分录-子表 t_pur_orderentry_delsub

- **表名称：** 交货计划分录-子表
- **表名：** t_pur_orderentry_delsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplanqty | 计划交货数量 | numeric | 23 | 10 | √ | 0 | 计划交货数量 |
| 2 | fplandeliverdate | 计划交货日期 | timestamp | 0 |  |  | null | 计划交货日期 |
| 3 | fplanentryseq | 交货计划分录序号 | int4 | 32 |  | √ | 0 | 交货计划分录序号 |
| 4 | fchasedeliverdate | 追料到货日期 | timestamp | 0 |  |  | null | 追料到货日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fplanunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fdelentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fdelentrycreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fplanbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fplanbasicqty | 计划交货基本数量 | numeric | 23 | 10 | √ | 0 | 计划交货基本数量 |
| 11 | fplanpoentryid | 订单分录id | varchar | 50 |  | √ | ' ' | 订单分录id |
| 12 | fdelentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fplancomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 14 | fplanlocation | 交货地点 | varchar | 512 |  | √ | ' ' | 交货地点 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fplanaddress | 交货地址 | varchar | 512 |  | √ | ' ' | 交货地址 |
| 18 | fplanentryid | 交货计划分录id | varchar | 50 |  | √ | ' ' | 交货计划分录id |
| 19 | fdelentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_orderentry_delsub |  | fdetailid |
| 2 | idx_pur_orderentry_delsubpoeid |  | fplanpoentryid |
| 3 | idx_pur_orderentry_delsub |  | fentryid,fseq |

---

## 订单交货计划分录-主表 t_pur_orderentry_deliver

- **表名称：** 订单交货计划分录-主表
- **表名：** t_pur_orderentry_deliver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fpoentryseq | 采购订单行号 | varchar | 50 |  | √ | ' ' | 采购订单行号 |
| 8 | fpoentryid | 采购订单分录Id | varchar | 50 |  | √ | ' ' | 采购订单分录Id |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fpobillno | 采购订单编号 | varchar | 80 |  | √ | ' ' | 采购订单编号 |
| 12 | fbillno | 单据编号 | varchar | 150 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_orderentry_deliver |  | fpobillno |
| 2 | pk_pur_orderentry_deliver |  | fentryid |
| 3 | idx_pur_orderentry_deliver_ct |  | fcreatetime |
