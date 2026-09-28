# 即时汇率同步管理-xkbd_exrate_sync

## 即时汇率同步管理-主表 t_bd_exrate_sync

- **表名称：** 即时汇率同步管理-主表
- **表名：** t_bd_exrate_sync

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forigincurid | 原币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | ftargetcurid | 目标币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fsynctime | 系统当天汇率同步时间 | int4 | 32 |  | √ | 0 | 系统当天汇率同步时间 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsyncstartdate | 汇率开始同步日期 | timestamp | 0 |  |  | null | 汇率开始同步日期 |
| 9 | fsynctype | 汇率同步类型 | bpchar | 1 |  | √ | ' ' | 汇率同步类型,枚举: 0 :仅同步历史汇率 1 :同步历史汇率和系统当天汇率 |
| 10 | fenable | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :未启用 1 :启用 2 :禁用 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_exrate_sync_curid |  | forigincurid,ftargetcurid |
| 2 | pk_bd_exrate_sync |  | fid |
