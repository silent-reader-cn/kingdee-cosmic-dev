# 当周发货订单数据存储-mrp_weeksendorder

## 当周发货订单数据存储-主表 t_mrp_weeksendorder

- **表名称：** 当周发货订单数据存储-主表
- **表名：** t_mrp_weeksendorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ftype | 单据类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_weeksendorder |  | fbillno |
| 2 | pk_t_mrp_weeksendorder |  | fid |

---

## 单据体-子表 t_mrp_weeksendorderentry

- **表名称：** 单据体-子表
- **表名：** t_mrp_weeksendorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 单据数量 | numeric | 23 | 10 | √ | 0 | 单据数量 |
| 3 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdeliverydate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 6 | fmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_weeksendorderentry |  | fid |
| 2 | pk_t_mrp_weeksendorderentry |  | fentryid |
