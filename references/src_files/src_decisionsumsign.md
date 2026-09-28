# 中标供应商(子单据体后台元数据)-src_decisionsumsign

## 中标供应商(子单据体后台元数据)-主表 t_src_decisionsumsign

- **表名称：** 中标供应商(子单据体后台元数据)-主表
- **表名：** t_src_decisionsumsign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :人员 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 2 | fsignrate | 分配比例(%) | numeric | 23 | 10 | √ | 0 | 分配比例(%) |
| 3 | fsignamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 4 | fsigntaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 5 | fcontractid | fcontractid | int8 | 64 |  | √ | 0 |  |
| 6 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionsumsign_fcid |  | fcontractid |
| 2 | idx_src_decisionsumsign_fsup |  | fsupplierid |
| 3 | idx_src_decisionsumsign_feid |  | fentryid |
| 4 | pk_src_decisionsumsign |  | fdetailid |
