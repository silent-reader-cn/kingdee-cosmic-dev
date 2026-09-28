# 技能访问日志-fgptas_skillaccesslog

## 技能访问日志-主表 t_fgptas_skillaccesslog

- **表名称：** 技能访问日志-主表
- **表名：** t_fgptas_skillaccesslog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskillnumber | 技能编码 | varchar | 50 |  | √ | ' ' | 技能编码 |
| 3 | fuserid | 访问用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fresult | 结果 | bpchar | 1 |  | √ | '1' | 结果 |
| 5 | fskillname | 技能名称 | varchar | 50 |  | √ | ' ' | 技能名称 |
| 6 | faccesstime | 访问时间 | timestamp | 0 |  |  | null | 访问时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_skillaccesslog_1 |  | faccesstime,fskillnumber |
| 2 | pk_fgptas_skillaccesslog |  | fid |
