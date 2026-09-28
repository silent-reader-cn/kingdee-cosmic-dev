# 条码操作记录-fa_barcode_operatelog

## 条码操作记录-主表 t_fa_barcode_opelog

- **表名称：** 条码操作记录-主表
- **表名：** t_fa_barcode_opelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 3 | frealcardid | 资产卡片 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 4 | fbarcodeid | 条码id | int8 | 64 |  | √ | 0 | 条码主档_资产_F7 bcmainfile_fa_f7 |
| 5 | fformid | 业务实体 | varchar | 50 |  | √ | ' ' | 业务实体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_barcode_opelog |  | fid |
| 2 | idx_fa_barcode_opelog_id |  | fbillid,fformid |
