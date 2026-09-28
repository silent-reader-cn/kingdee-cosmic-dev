# 销售计划单-ids_salesplan

## 销售计划单-主表 t_ids_salesplan

- **表名称：** 销售计划单-主表
- **表名：** t_ids_salesplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 单据名称 | int8 | 64 |  | √ | 0 | [销售计划周期 ids_salesplan_period](../ids_files/ids_salesplan_period.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcustid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 8 | fbosuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmodeltypename | 预测方案名称 | varchar | 100 |  | √ | ' ' | 预测方案名称 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmodeltypeid | 预测方案 | varchar | 50 |  | √ | ' ' | 预测方案,枚举: |
| 17 | fissysgen | 系统自动生成 | bpchar | 1 |  | √ | '1' | 系统自动生成 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_salesplan_fbilldate |  | fbilldate |
| 2 | idx_ids_salesplan_fperiodid |  | fperiodid |
| 3 | idx_ids_salesplan_fbillno |  | fbillno |
| 4 | pk_t_ids_salesplan |  | fid |

---

## 明细信息-子表 t_ids_salesplan_entry

- **表名称：** 明细信息-子表
- **表名：** t_ids_salesplan_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fentrymodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 5 | fbase2level | 基本分类2级分组 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 6 | fmaterialid | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fbase3level | 基本分类3级分组 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fbase1level | 基本分类1级分组 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_salesplan_entry |  | fentryid |
| 2 | idx_ids_salesplan_entry_fid |  | fid |

---

## 预测信息-子表 t_ids_salesplan_indicator

- **表名称：** 预测信息-子表
- **表名：** t_ids_salesplan_indicator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalue2 | T+2 | numeric | 23 | 10 | √ | 0 | T+2 |
| 2 | fvalue1 | T+1 | numeric | 23 | 10 | √ | 0 | T+1 |
| 3 | fvalue4 | T+4 | numeric | 23 | 10 | √ | 0 | T+4 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fvalue3 | T+3 | numeric | 23 | 10 | √ | 0 | T+3 |
| 6 | fvalue12 | T+12 | numeric | 23 | 10 | √ | 0 | T+12 |
| 7 | fvalue6 | T+6 | numeric | 23 | 10 | √ | 0 | T+6 |
| 8 | fvalue5 | T+5 | numeric | 23 | 10 | √ | 0 | T+5 |
| 9 | fvalue8 | T+8 | numeric | 23 | 10 | √ | 0 | T+8 |
| 10 | fvalue7 | T+7 | numeric | 23 | 10 | √ | 0 | T+7 |
| 11 | fvalue11 | T+11 | numeric | 23 | 10 | √ | 0 | T+11 |
| 12 | fvalue9 | T+9 | numeric | 23 | 10 | √ | 0 | T+9 |
| 13 | fvalue10 | T+10 | numeric | 23 | 10 | √ | 0 | T+10 |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | findicator | 统计指标 | varchar | 50 |  | √ | ' ' | 统计指标,枚举: fpreqty :预测销售数量 ffillqty :业务填报数量 fpreamount :预测销售金额 ffillamount :业务填报金额 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ids_salesplan_indicator |  | fdetailid |
| 2 | idx_ids_salesplan_indic_id |  | fentryid |
