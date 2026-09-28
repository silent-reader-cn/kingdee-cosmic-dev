# 目标单同步记录-bos_ctbotp_synclog_t

## 目标单同步记录-主表 t_ctbotp_tsynclog

- **表名称：** 目标单同步记录-主表
- **表名：** t_ctbotp_tsynclog

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
| 12 | fopuser | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsentitykey | 源单标识 | varchar | 36 |  | √ | ' ' | 源单标识 |
| 14 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 15 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 16 | ftbillno | 目标单编码 | varchar | 500 |  | √ | ' ' | 目标单编码 |
| 17 | flksyncstatus | 关联关系同步状态 | bpchar | 1 |  | √ | '0' | 关联关系同步状态,枚举: 0 :同步中 1 :同步成功 2 :同步失败 |
| 18 | ftaccountid | 目标单数据中心 | varchar | 50 |  | √ | ' ' | 目标单数据中心 |
| 19 | fruleid | 转换规则id | varchar | 50 |  | √ | ' ' | 转换规则id |
| 20 | fsourceoperate | 操作来源 | bpchar | 1 |  | √ | '0' | 操作来源,枚举: 0 :操作 1 :事件订阅 2 :其他 |
| 21 | frootjobid | 事件id | int8 | 64 |  | √ | 0 | 事件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctbotp_tsynclog_tbillid |  | ftbillid |
| 2 | idx_ctbotp_tsynclog_uniquekey |  | funiquekey |
| 3 | idx_ctbotp_tsynclog_rootjobid |  | frootjobid |
| 4 | pk_t_ctbotp_tsynclog |  | fid |
| 5 | idx_ctbotp_tsynclog_sbillid |  | fsbillid |

---

## 目标单同步记录-分表 t_ctbotp_tsynclog_c

- **表名称：** 目标单同步记录-分表
- **表名：** t_ctbotp_tsynclog_c

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
| 1 | pk_t_ctbotp_tsynclog_c |  | fid |
