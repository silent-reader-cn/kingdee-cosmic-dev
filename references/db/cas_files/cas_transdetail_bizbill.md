# 流水生成收付款单记录-cas_transdetail_bizbill

## 流水生成收付款单记录-主表 t_cas_transdetail_bizbill

- **表名称：** 流水生成收付款单记录-主表
- **表名：** t_cas_transdetail_bizbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 5 | fsrcbilltype | 源单类型 | varchar | 128 |  | √ | ' ' | 源单类型,枚举: bei_intelrec :收款入账中心 bei_intelpay :付款入账中心 cas_claimcenterbill :收付认领处理中心 |
| 6 | fdetailid | 明细流水号 | varchar | 200 |  | √ | ' ' | 明细流水号 |
| 7 | fbilltype | 单据类型 | varchar | 64 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_detail_bill |  | fdetailid |
| 2 | pk_t_cas_transdetail_bizbill |  | fid |
