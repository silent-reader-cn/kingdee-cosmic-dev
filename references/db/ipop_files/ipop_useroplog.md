# 用户操作日志-ipop_useroplog

## 用户操作日志-主表 t_ipop_useroplog

- **表名称：** 用户操作日志-主表
- **表名：** t_ipop_useroplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 3 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fsync | 是否同步 | varchar | 50 |  | √ | ' ' | 是否同步 |
| 5 | frefdata | 关联数据 | varchar | 50 |  | √ | ' ' | 关联数据 |
| 6 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbizobject | 业务对象名称 | varchar | 50 |  | √ | ' ' | 业务对象名称 |
| 8 | fopdesc | 操作描述 | varchar | 2000 |  | √ | ' ' | 操作描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_useroplog |  | fsync |
| 2 | pk_t_ipop_useroplog |  | fid |
