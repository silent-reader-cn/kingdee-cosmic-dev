# 工程变更申请单F7-pdm_bom_ecoapply_headf7

## 工程变更申请单F7-主表 t_pdm_bomecoapply

- **表名称：** 工程变更申请单F7-主表
- **表名：** t_pdm_bomecoapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据id | int8 | 64 |  | √ | 1 | 单据id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 1 |  |
| 3 | fdeptid | fdeptid | int8 | 64 |  |  | null |  |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 申请组织 | int8 | 64 |  | √ | 1 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 8 | fapplytime | fapplytime | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 1 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fapplyreason | fapplyreason | varchar | 2000 |  |  | null |  |
| 12 | fapplier | fapplier | int8 | 64 |  |  | null |  |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fbilltype | fbilltype | int8 | 64 |  |  | null |  |
| 15 | fauditorid | fauditorid | int8 | 64 |  | √ | 1 |  |
| 16 | fcustomerid | fcustomerid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdmecoapply_fbillno |  | fbillno |
| 2 | pk_pdm_bomecoapply |  | fid |
| 3 | idx_pdmecoapply_forgid |  | forgid |
