# 生产倒冲记录-im_mdc_backflushstock

## 生产倒冲记录-主表 t_im_mdc_bfstock

- **表名称：** 生产倒冲记录-主表
- **表名：** t_im_mdc_bfstock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbfclose | 倒冲关闭 | bpchar | 1 |  | √ | '0' | 倒冲关闭 |
| 3 | fsourcebillentryid | 来源单据分录id | int8 | 64 |  | √ | 0 | 来源单据分录id |
| 4 | fsourcebillentry | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型,枚举: A :完工入库单/委外完工入库单 B :工单汇报单 C :工序汇报单(废弃) D :工序转移单 F :完工退库单/委外完工退库单 SR :工序汇报单 SO :委外接收单 SI :内协接收单 |
| 5 | factissuebfqty | 已倒冲数量 | int8 | 64 |  | √ | 0 | 已倒冲数量 |
| 6 | fstockentryid | 组件清单分录id | int8 | 64 |  | √ | 0 | 组件清单分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_mdc_bfstock_fsid |  | fsourcebillentryid |
| 2 | idx_im_mdc_bfstock_fstid |  | fstockentryid |
| 3 | pk_im_mdc_bfstock |  | fid |
