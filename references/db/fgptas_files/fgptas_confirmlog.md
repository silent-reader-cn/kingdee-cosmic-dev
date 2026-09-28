# 财务AI助手试用确认日志-fgptas_confirmlog

## 财务AI助手试用确认日志-主表 t_fgptas_confirmlog

- **表名称：** 财务AI助手试用确认日志-主表
- **表名：** t_fgptas_confirmlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisnotice | 是否已通知 | bpchar | 1 |  | √ | '0' | 是否已通知 |
| 4 | fnoticetime | 通知时间 | timestamp | 0 |  |  | null | 通知时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_confirmlog |  | fuserid,fisnotice |
| 2 | pk_t_fgptas_confirmlog |  | fid |
