# 核销日志（废弃）-msmod_log

## 反核销明细-子表 t_msmod_log_back_entry

- **表名称：** 反核销明细-子表
- **表名：** t_msmod_log_back_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbackbill | 反写单据 | varchar | 1000 |  | √ | ' ' | 反写单据 |
| 3 | ffailmessageback | 失败原因 | varchar | 2000 |  | √ | ' ' | 失败原因 |
| 4 | fwfrecordback | 核销记录 | varchar | 50 |  | √ | ' ' | 核销记录 |
| 5 | fwfseqback | 原核销批号 | varchar | 50 |  | √ | ' ' | 原核销批号 |
| 6 | fwfcreater | 核销人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fautobillback | 已删除自动生成单据 | varchar | 1000 |  | √ | ' ' | 已删除自动生成单据 |
| 9 | fwftypeback | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_back_entry_fid |  | fid |
| 2 | pk_t_msmod_log_back_entry |  | fentryid |

---

## 核销日志（废弃）-主表 t_msmod_log

- **表名称：** 核销日志（废弃）-主表
- **表名：** t_msmod_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 核销/反核销批号 | varchar | 50 |  | √ | ' ' | 核销/反核销批号 |
| 3 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fstartbillnumber_tag | 发起方单据编号_详情 | text | 0 |  |  | null | 发起方单据编号_详情 |
| 6 | fwfmode | 核销方式 | varchar | 50 |  | √ | ' ' | 核销方式 |
| 7 | fstartbillnumber | 发起方单据编号 | varchar | 255 |  | √ | ' ' | 发起方单据编号 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fheadfailmessage | 失败原因 | varchar | 2000 |  | √ | ' ' | 失败原因 |
| 10 | fwfresult | 执行结果 | varchar | 50 |  | √ | ' ' | 执行结果 |
| 11 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fwftype | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_log |  | fid |
| 2 | idx_t_msmod_log_fwfseq |  | fwfseq |

---

## 核销明细-子表 t_msmod_log_entry

- **表名称：** 核销明细-子表
- **表名：** t_msmod_log_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwfrecord | 核销记录编码 | varchar | 1000 |  | √ | ' ' | 核销记录编码 |
| 3 | ffailmessage | 失败原因 | varchar | 2000 |  | √ | ' ' | 失败原因 |
| 4 | fwfscheme | 核销方案 | int8 | 64 |  | √ | 0 | [核销方案 msmod_scheme](../mscommon_files/msmod_scheme.md) |
| 5 | fautobill | 自动生成单据 | varchar | 1000 |  | √ | ' ' | 自动生成单据 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fgroupcondition | 匹配条件 | varchar | 1000 |  | √ | ' ' | 匹配条件 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fwfstrategy | 核销策略 | varchar | 50 |  | √ | ' ' | 核销策略 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_msmod_log_entry_fid |  | fid |
| 2 | pk_t_msmod_log_entry |  | fentryid |
