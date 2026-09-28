# 功能使用日志-xklic_funcuselog

## 功能使用日志-主表 t_xklic_funcuselog

- **表名称：** 功能使用日志-主表
- **表名：** t_xklic_funcuselog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 操作时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 操作时间 |
| 3 | flicexpiredate | 许可日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 许可日期 |
| 4 | flicgroupld | 许可功能 | int8 | 64 |  | √ | 0 | [许可分组 lic_group](../base_files/lic_group.md) |
| 5 | fenable | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :冻结 B :解冻 C :成功 |
| 6 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbizsn | 流水号 | varchar | 50 |  |  | ' ' | 流水号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_func_fenable |  | fenable |
| 2 | pk_t_lic_func_flicdate |  | flicexpiredate |
| 3 | pk_t_lic_func_fbizsn |  | fbizsn |
| 4 | pk_t_xklic_funcuselog |  | fid |
| 5 | pk_t_lic_func_groupld |  | flicgroupld |
