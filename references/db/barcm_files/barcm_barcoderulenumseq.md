# 条码规则流水表-barcm_barcoderulenumseq

## 条码规则流水表-主表 t_barcm_bcrulenumseq

- **表名称：** 条码规则流水表-主表
- **表名：** t_barcm_bcrulenumseq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsortitemvalue | 流水号依据字段值 | varchar | 500 |  | √ | ' ' | 流水号依据字段值 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaxflowno | 最大流水号 | int8 | 64 |  | √ | 0 | 最大流水号 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fbarcoderuleid | 条码规则ID | int8 | 64 |  | √ | 0 | [条码规则 barcm_barcoderule](../barcm_files/barcm_barcoderule.md) |
| 7 | finitserial | 初始值 | int8 | 64 |  | √ | 0 | 初始值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_bcrulenumseq |  | fid |
| 2 | idx_barcm_bcrulenumseq_ridsv |  | fbarcoderuleid,fsortitemvalue |
