# 源单同步记录-bos_ctbotp_synclog_s

## 源单同步记录-主表 t_ctbotp_synclog

- **表名称：** 源单同步记录-主表
- **表名：** t_ctbotp_synclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funiquekey | 唯一标识 | varchar | 100 |  | √ | ' ' | 唯一标识 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | fsynctype | 同步类型 | bpchar | 1 |  | √ | '0' | 同步类型,枚举: 0 :正向同步 1 :反向同步 |
| 5 | fstenantcode | 源单租户 | varchar | 50 |  | √ | ' ' | 源单租户 |
| 6 | ftentitykey | 目标单标识 | varchar | 36 |  | √ | ' ' | 目标单标识 |
| 7 | fsbillno | 源单编码 | varchar | 500 |  | √ | ' ' | 源单编码 |
| 8 | fsaccountid | 源单数据中心 | varchar | 50 |  | √ | ' ' | 源单数据中心 |
| 9 | ftbillid | 目标单内码 | int8 | 64 |  | √ | 0 | 目标单内码 |
| 10 | fttenantcode | 目标单租户 | varchar | 50 |  | √ | ' ' | 目标单租户 |
| 11 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :同步中 1 :同步成功 2 :同步失败 |
| 12 | fupdatestatuscount | 更新状态次数 | int4 | 32 |  | √ | 0 | 更新状态次数 |
| 13 | fopuser | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsentitykey | 源单标识 | varchar | 36 |  | √ | ' ' | 源单标识 |
| 15 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 16 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 17 | ftbillno | 目标单编码 | varchar | 500 |  | √ | ' ' | 目标单编码 |
| 18 | flksyncstatus | 关联关系同步状态 | bpchar | 1 |  | √ | '0' | 关联关系同步状态,枚举: 0 :同步中 1 :同步成功 2 :同步失败 |
| 19 | ftaccountid | 目标单数据中心 | varchar | 50 |  | √ | ' ' | 目标单数据中心 |
| 20 | fruleid | 转换规则id | varchar | 50 |  | √ | ' ' | 转换规则id |
| 21 | fsourceoperate | 操作来源 | bpchar | 1 |  | √ | '0' | 操作来源,枚举: 0 :操作 1 :事件订阅 2 :其他 |
| 22 | frootjobid | 事件id | int8 | 64 |  | √ | 0 | 事件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctbotp_ssynclog_sbillid |  | fsbillid |
| 2 | idx_ctbotp_synclog_rootjobid |  | frootjobid |
| 3 | idx_ctbotp_ssynclog_tbillid |  | ftbillid |
| 4 | idx_ctbotp_ssynclog_uniquekey |  | funiquekey |
| 5 | pk_t_ctbotp_synclog |  | fid |

---

## 源单同步记录-分表 t_ctbotp_synclog_c

- **表名称：** 源单同步记录-分表
- **表名：** t_ctbotp_synclog_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsynccontent | 同步内容 | varchar | 255 |  |  | null | 同步内容 |
| 3 | fsynccontent_tag | 同步内容_详情 | text | 0 |  |  | null | 同步内容_详情 |
| 4 | fdesc | 备注 | varchar | 255 |  |  | null | 备注 |
| 5 | frulename | 转换规则名称 | varchar | 500 |  | √ | ' ' | 转换规则名称 |
| 6 | fdesc_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctbotp_synclog_c |  | fid |
