# 应付转销日志-ap_transferlog

## 应付转销日志-主表 t_ap_transferlog

- **表名称：** 应付转销日志-主表
- **表名：** t_ap_transferlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftraceid | 本次转销唯一标识 | varchar | 255 |  | √ | ' ' | 本次转销唯一标识 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | ftransferstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: success :成功 fail :失败 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftransamount | 转销金额 | numeric | 23 | 10 | √ | 0 | 转销金额 |
| 8 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftransferno | 转销序号 | varchar | 30 |  | √ | ' ' | 转销序号 |
| 13 | fplanentryid | 计划行id | int8 | 64 |  | √ | 0 | 计划行id |
| 14 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_translog_traceid |  | ftraceid |
| 2 | pk_t_ap_transferlog |  | fid |
