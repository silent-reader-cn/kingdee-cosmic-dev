# 条码打印日志-barcm_printinglog

## 条码打印日志-主表 t_barcm_printlog

- **表名称：** 条码打印日志-主表
- **表名：** t_barcm_printlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fprinter | 打印人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcloudprinterid | 打印机 | int8 | 64 |  | √ | 0 | [云打印机 bos_cloudprinter](../frame_files/bos_cloudprinter.md) |
| 7 | fissavepaperprint | 节纸打印 | bpchar | 1 |  | √ | ' ' | 节纸打印 |
| 8 | fprintcopies | 打印份数 | int4 | 32 |  | √ | 0 | 打印份数 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbarcodemainfileid | 条码主档ID | int8 | 64 |  | √ | 0 | [条码主档 barcm_barcodemainfile](../barcm_files/barcm_barcodemainfile.md) |
| 12 | fprinttemplateid | 打印模板 | int8 | 64 |  | √ | 0 | [维护打印模板 bos_manageprinttpl](../cts_files/bos_manageprinttpl.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fprintdatetime | 打印时间 | timestamp | 0 |  |  | null | 打印时间 |
| 15 | fbarcodevalue | 条形码 | varchar | 255 |  | √ | ' ' | 条形码 |
| 16 | fprintmode | 打印模式 | bpchar | 1 |  | √ | ' ' | 打印模式,枚举: A :连续打印 B :成套打印 |
| 17 | fprinttimecost | 打印耗时 | int4 | 32 |  | √ | 0 | 打印耗时 |
| 18 | fbillno | 日志流水号 | varchar | 80 |  | √ | ' ' | 日志流水号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_printlog |  | fid |
| 2 | idx_barcm_printlog_fbillno |  | fbillno |
