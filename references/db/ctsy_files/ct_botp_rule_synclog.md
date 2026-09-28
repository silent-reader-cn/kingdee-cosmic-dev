# 数据协同同步记录-ct_botp_rule_synclog

## 数据协同同步记录-主表 t_ctbotp_rule_synclog

- **表名称：** 数据协同同步记录-主表
- **表名：** t_ctbotp_rule_synclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetdatacenter | 目标单数据中心 | varchar | 50 |  | √ | ' ' | 目标单数据中心 |
| 3 | fsynccontent_tag | 同步内容_详情 | text | 0 |  |  | null | 同步内容_详情 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftargetstatus | 下游同步状态 | varchar | 50 |  | √ | 'A' | 下游同步状态,枚举: A :同步中 S :同步成功 F :同步失败 |
| 6 | fmodifier | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsourcedatacenter | 源单数据中心 | varchar | 50 |  | √ | ' ' | 源单数据中心 |
| 8 | fsourcenumber | 源单标识 | varchar | 36 |  | √ | ' ' | 源单标识 |
| 9 | fsynccontent | 同步内容 | varchar | 255 |  |  | null | 同步内容 |
| 10 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 11 | fcreater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftargettenant | 目标单租户 | varchar | 50 |  | √ | ' ' | 目标单租户 |
| 13 | ftargetnumber | 目标单标识 | varchar | 36 |  | √ | ' ' | 目标单标识 |
| 14 | fruleid | 转换规则id | varchar | 50 |  | √ | ' ' | 转换规则id |
| 15 | fdesc | 备注 | varchar | 255 |  |  | null | 备注 |
| 16 | fsourcestatus | 上游同步状态 | varchar | 50 |  | √ | 'A' | 上游同步状态,枚举: A :同步中 S :同步成功 F :同步失败 |
| 17 | fdesc_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 18 | fsourcetenant | 源单租户 | varchar | 50 |  | √ | ' ' | 源单租户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctbotp_sy_ruleid |  | fruleid |
| 2 | pk_t_ctbotp_rule_synclog |  | fid |
