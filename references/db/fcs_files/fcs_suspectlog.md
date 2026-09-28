# 疑似防重日志-fcs_suspectlog

## 日志信息-子表 t_fcs_suspectlog_entry

- **表名称：** 日志信息-子表
- **表名：** t_fcs_suspectlog_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdestbilltype | 当前单类型 | varchar | 80 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 3 | fdestnumber | 当前单编码 | varchar | 80 |  | √ | ' ' | 当前单编码 |
| 4 | fdestbillid | 当前单ID | int8 | 64 |  | √ | 0 | 当前单ID |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fcs_suspectlog_entry |  | fid |
| 2 | pk_t_fcs_suspectlog_entry |  | fentryid |

---

## 疑似防重日志-主表 t_fcs_suspectlog

- **表名称：** 疑似防重日志-主表
- **表名：** t_fcs_suspectlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcosttime | 耗时(ms) | int4 | 32 |  | √ | 0 | 耗时(ms) |
| 4 | ftraceid | traceid | varchar | 80 |  | √ | ' ' | traceid |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fexception_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | frepeatsetid | 疑似防重配置 | int8 | 64 |  | √ | 0 | [疑似防重配置 fcs_suspectset](../fcs_files/fcs_suspectset.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fexception | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 13 | flogtype | 日志分类 | varchar | 30 |  | √ | ' ' | 日志分类,枚举: suspect :疑似防重 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_suspectlog |  | fid |
| 2 | idx_t_fcs_suspectlog |  | frepeatsetid |
