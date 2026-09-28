# 巡检修复日志-msbd_fixdatalog

## 修复明细-子表 t_msbd_fixdatalog_e

- **表名称：** 修复明细-子表
- **表名：** t_msbd_fixdatalog_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffixpluginurl | 修复插件 | varchar | 255 |  | √ | ' ' | 修复插件 |
| 3 | ffixfieldmark | 修复字段标识 | varchar | 100 |  | √ | ' ' | 修复字段标识 |
| 4 | fbillentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 5 | ffixbeforevalue | 修复前值 | varchar | 1000 |  |  | null | 修复前值 |
| 6 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fbillentryseq | 单据行号 | int8 | 64 |  | √ | 0 | 单据行号 |
| 9 | ffixaftervalue | 修复后值 | varchar | 1000 |  |  | null | 修复后值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffixfieldname | 修复字段名称 | varchar | 100 |  | √ | ' ' | 修复字段名称 |
| 12 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_fixdatalog_e |  | fentryid |
| 2 | idx_msbd_fixdatalog_e_id |  | fid |

---

## 巡检修复日志-主表 t_msbd_fixdatalog

- **表名称：** 巡检修复日志-主表
- **表名：** t_msbd_fixdatalog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 修复时间 | timestamp | 0 |  |  | null | 修复时间 |
| 3 | ftraceid | 全链路ID | varchar | 64 |  | √ | ' ' | 全链路ID |
| 4 | fopuserid | 修复人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fentityid | 修复单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fopreason | 异常信息 | varchar | 1000 |  |  | null | 异常信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_fixdatalog_traceid |  | ftraceid |
| 2 | pk_t_msbd_fixdatalog |  | fid |
