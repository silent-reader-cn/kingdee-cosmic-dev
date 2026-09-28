# 需求计划单明细-ids_requireplan_entry

## 统计指标单据体-子表 t_ids_req_indicator_entry

- **表名称：** 统计指标单据体-子表
- **表名：** t_ids_req_indicator_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue_9 | T-9 | numeric | 23 | 10 | √ | 0 | T-9 |
| 3 | fvalue_8 | T-8 | numeric | 23 | 10 | √ | 0 | T-8 |
| 4 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fentrymodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fvalue_5 | T-5 | numeric | 23 | 10 | √ | 0 | T-5 |
| 7 | fvalue_4 | T-4 | numeric | 23 | 10 | √ | 0 | T-4 |
| 8 | fvalue_7 | T-7 | numeric | 23 | 10 | √ | 0 | T-7 |
| 9 | fvalue_6 | T-6 | numeric | 23 | 10 | √ | 0 | T-6 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fvalue_11 | T-11 | numeric | 23 | 10 | √ | 0 | T-11 |
| 12 | fvalue_12 | T-12 | numeric | 23 | 10 | √ | 0 | T-12 |
| 13 | fvalue_10 | T-10 | numeric | 23 | 10 | √ | 0 | T-10 |
| 14 | fvalue2 | T+2 | numeric | 23 | 10 | √ | 0 | T+2 |
| 15 | fvalue1 | T+1 | numeric | 23 | 10 | √ | 0 | T+1 |
| 16 | fvalue4 | T+4 | numeric | 23 | 10 | √ | 0 | T+4 |
| 17 | fvalue3 | T+3 | numeric | 23 | 10 | √ | 0 | T+3 |
| 18 | fvalue12 | T+12 | numeric | 23 | 10 | √ | 0 | T+12 |
| 19 | fvalue6 | T+6 | numeric | 23 | 10 | √ | 0 | T+6 |
| 20 | fvalue5 | T+5 | numeric | 23 | 10 | √ | 0 | T+5 |
| 21 | fvalue8 | T+8 | numeric | 23 | 10 | √ | 0 | T+8 |
| 22 | fvalue7 | T+7 | numeric | 23 | 10 | √ | 0 | T+7 |
| 23 | fvalue11 | T+11 | numeric | 23 | 10 | √ | 0 | T+11 |
| 24 | fvalue9 | T+9 | numeric | 23 | 10 | √ | 0 | T+9 |
| 25 | fvalue10 | T+10 | numeric | 23 | 10 | √ | 0 | T+10 |
| 26 | fvalue_1 | T-1 | numeric | 23 | 10 | √ | 0 | T-1 |
| 27 | fvalue_3 | T-3 | numeric | 23 | 10 | √ | 0 | T-3 |
| 28 | findicator | 统计指标 | varchar | 50 |  | √ | ' ' | 统计指标,枚举: actqty :实际销售数量 preqty :预测销售数量 fillqty :业务填报数量 adoptqty :最终采纳数量 amount :销售金额 avgprice :销售均价 offsetvalue :绝对误差 offsetpercent :绝对百分比误差 |
| 29 | fvalue_2 | T-2 | numeric | 23 | 10 | √ | 0 | T-2 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_req_indicator_entry |  | fentryid |
| 2 | idx_ids_req_indic_entry_fid |  | fid |

---

## 需求计划单明细-主表 t_ids_requireplan_entry

- **表名称：** 需求计划单明细-主表
- **表名：** t_ids_requireplan_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcustid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | frequireplanid | 需求计划单FID（隐藏字段） | int8 | 64 |  | √ | 0 | 需求计划单FID（隐藏字段） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_requireplan_entry |  | fid |
| 2 | idx_ids_reqplan_entry_planid |  | frequireplanid |
