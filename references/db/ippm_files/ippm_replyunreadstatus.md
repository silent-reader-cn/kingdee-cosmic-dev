# 反馈与建议回复未读状态-ippm_replyunreadstatus

## 反馈与建议回复未读状态-主表 t_ippm_replyunreadstatus

- **表名称：** 反馈与建议回复未读状态-主表
- **表名：** t_ippm_replyunreadstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: read :答复均已读 unread :存在未读 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_replyunreadstatus |  | fid |
| 2 | idx_ippm_replyunreadstatus |  | fuserid |
