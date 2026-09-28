# 即时余额表（分片用）-im_inv_realbalance_sp

## 即时余额表（分片用）-主表 t_im_inv_realbalance_sp

- **表名称：** 即时余额表（分片用）-主表
- **表名：** t_im_inv_realbalance_sp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | fupdatetype | 更新方向 | int8 | 64 |  | √ | 1 | 更新方向 |
| 4 | fqty2nd_sp | 辅助数量sp | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量sp |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fqty_sp | 数量sp | numeric | 23 | 10 | √ | 0.0000000000 | 数量sp |
| 7 | fbaseqty_sp | 基本数量sp | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量sp |
| 8 | fqty3rd_sp | 辅助数量(2)sp | numeric | 23 | 10 | √ | 0 | 辅助数量(2)sp |
| 9 | fentryseq | 分录序号 | int8 | 64 |  | √ | 0 | 分录序号 |
| 10 | fbillname | 单据实体名称 | varchar | 50 |  | √ | ' ' | 单据实体名称 |
| 11 | fstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态 |
| 12 | fqty2nd | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 13 | fupdatetime | 更新流水号 | int8 | 64 |  | √ | 0 | 更新流水号 |
| 14 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 15 | fisnew | 最新版本 | bpchar | 1 |  | √ | '0' | 最新版本 |
| 16 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 17 | fentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 18 | fupdateruleid | 更新规则ID | varchar | 36 |  | √ | ' ' | 更新规则ID |
| 19 | fmovetime | fmovetime | timestamp | 0 |  |  | null |  |
| 20 | fkeycol | keycol | varchar | 50 |  | √ | ' ' | keycol |
| 21 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_inv_realbalance_sp_pkey |  | fid |
| 2 | idx_im_realbalc_sp_updtime |  | fupdatetime |
| 3 | idx_im_realbalc_sp_billid |  | fbillid |
| 4 | idx_im_realbalc_sp_entryid |  | fentryid |
| 5 | idx_im_realbalc_sp_bno |  | fbillno |
| 6 | idx_im_realbalc_sp_keycol |  | fkeycol |
