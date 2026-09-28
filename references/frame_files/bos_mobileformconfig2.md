# 移动平台单据启用设置2-bos_mobileformconfig2

## 移动平台单据启用设置2-主表 t_bas_mobileformconfig

- **表名称：** 移动平台单据启用设置2-主表
- **表名：** t_bas_mobileformconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | fstatus | bpchar | 1 |  |  | null |  |
| 3 | fname | fname | varchar | 30 |  | √ | ' ' |  |
| 4 | fentrymarkid | 单据体 | varchar | 255 |  |  | null | 单据体,枚举: |
| 5 | fbilldetailform | 待办任务自定义详情 | varchar | 255 |  |  | null | 业务对象 bos_objecttype |
| 6 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 7 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fisusemobile | 启用移动审批 | bpchar | 1 |  |  | null | 启用移动审批 |
| 9 | fenable | fenable | bpchar | 1 |  | √ | '0' |  |
| 10 | fshowcount | 审批项 | varchar | 255 |  |  | null | 审批项,枚举: |
| 11 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fbilltype | 单据 | varchar | 255 |  |  | null | 业务对象 bos_objecttype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_mobileformconfig |  | fnumber |
| 2 | t_bas_mobileformconfig_pkey |  | fid |

---

## 单据体-子表 t_bas_mobileconfigentry

- **表名称：** 单据体-子表
- **表名：** t_bas_mobileconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrylocation | fentrylocation | varchar | 50 |  |  | null |  |
| 3 | ffieldtypename | ffieldtypename | varchar | 20 |  |  | null |  |
| 4 | fbaseproperty | fbaseproperty | varchar | 50 |  |  | null |  |
| 5 | ffieldname | 字段名称 | varchar | 50 |  |  | null | 字段名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 7 | ffontsize | ffontsize | varchar | 100 |  |  | null |  |
| 8 | fisheadfield | 单据头字段 | bpchar | 1 |  | √ | '0' | 单据头字段 |
| 9 | ffieldkey | 字段标识 | varchar | 50 |  |  | null | 字段标识 |
| 10 | flocal | flocal | varchar | 50 |  |  | null |  |
| 11 | ffieldpercen | ffieldpercen | varchar | 100 |  |  | null |  |
| 12 | ffieldtype | 字段类型 | varchar | 50 |  |  | null | 字段类型 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffontcolor | ffontcolor | varchar | 100 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_mobileconfigentry_pkey |  | fentryid |
| 2 | idx_bas_mobileconfigety_id |  | fid |
