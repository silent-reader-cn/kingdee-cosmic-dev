# 应收分组维度映射-ar_plansplit_mapping

## 应收分组维度映射-主表 t_ar_plansplitmapping

- **表名称：** 应收分组维度映射-主表
- **表名：** t_ar_plansplitmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_psm_fnumber |  | fnumber |
| 2 | pk_ar_plansplitmapping |  | fid |

---

## 单据体-子表 t_ar_plansplitmapentry

- **表名称：** 单据体-子表
- **表名：** t_ar_plansplitmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailkey | 物料行字段标识 | varchar | 255 |  | √ | ' ' | 物料行字段标识 |
| 3 | fhtdetailkey | 合同物料行字段标识 | varchar | 255 |  | √ | ' ' | 合同物料行字段标识 |
| 4 | fdetailname | 物料行字段名称 | varchar | 255 |  | √ | ' ' | 物料行字段名称 |
| 5 | fhtplanname | 合同计划行字段名称 | varchar | 255 |  | √ | ' ' | 合同计划行字段名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fhtdetailname | 合同物料行字段名称 | varchar | 255 |  | √ | ' ' | 合同物料行字段名称 |
| 8 | fplanname | 计划行字段名称 | varchar | 255 |  | √ | ' ' | 计划行字段名称 |
| 9 | fhtplankey | 合同计划行字段标识 | varchar | 255 |  | √ | ' ' | 合同计划行字段标识 |
| 10 | fddplanname | 订单计划行字段名称 | varchar | 255 |  | √ | ' ' | 订单计划行字段名称 |
| 11 | fddplankey | 订单计划行字段标识 | varchar | 255 |  | √ | ' ' | 订单计划行字段标识 |
| 12 | fdddetailname | 订单物料行字段名称 | varchar | 255 |  | √ | ' ' | 订单物料行字段名称 |
| 13 | fplankey | 计划行字段标识 | varchar | 255 |  | √ | ' ' | 计划行字段标识 |
| 14 | fdddetailkey | 订单物料行字段标识 | varchar | 255 |  | √ | ' ' | 订单物料行字段标识 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ar_plansplitmapentry |  | fentryid |
| 2 | idx_ar_psme_fid |  | fid |
