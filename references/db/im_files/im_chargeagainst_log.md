# 冲销日志-im_chargeagainst_log

## 单据体-子表 t_im_chargeagainst_log_e

- **表名称：** 单据体-子表
- **表名：** t_im_chargeagainst_log_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcagenerbillno | 生成冲销单据编号 | varchar | 50 |  | √ | ' ' | 生成冲销单据编号 |
| 3 | fcagenerid | 生成冲销单据id | int8 | 64 |  | √ | 0 | 生成冲销单据id |
| 4 | fsourcetype | 来源单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | ffailmessage | 失败原因 | varchar | 2000 |  | √ | ' ' | 失败原因 |
| 6 | fsourceid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fgeneratstatus | 冲销单据状态 | bpchar | 1 |  | √ | ' ' | 冲销单据状态,枚举: 1 :已保存 2 :已提交 3 :已审核 4 :已删除 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsourcebillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_chargeagainst_log_e_id |  | fid |
| 2 | pk_t_im_chargeagainst_log_e |  | fentryid |

---

## 冲销日志-主表 t_im_chargeagainst_log

- **表名称：** 冲销日志-主表
- **表名：** t_im_chargeagainst_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcasourceid | 冲销发起方单据id | int8 | 64 |  | √ | 0 | 冲销发起方单据id |
| 4 | fcasourcebillno | 冲销发起方单据编号 | varchar | 50 |  | √ | ' ' | 冲销发起方单据编号 |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | ftraceid | 日志请求id | varchar | 50 |  | √ | ' ' | 日志请求id |
| 7 | fcastatus | 冲销状态 | bpchar | 1 |  | √ | ' ' | 冲销状态,枚举: 1 :冲销成功 2 :冲销失败回滚失败 3 :冲销失败回滚成功 |
| 8 | fcasourcetype | 单据类型 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 9 | fwfparams | 核销回滚参数 | varchar | 2000 |  | √ | ' ' | 核销回滚参数 |
| 10 | fcabillfailcause | 冲销失败原因 | varchar | 2000 |  | √ | ' ' | 冲销失败原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_chargeagainst_log_fcasourcebillno |  | fcasourcebillno |
| 2 | pk_t_im_chargeagainst_log |  | fid |
