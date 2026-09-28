# 管控策略关系数据固化消息-bd_rel_solidify_msg

## 管控策略关系数据固化消息-主表 t_bd_solidify_msg

- **表名称：** 管控策略关系数据固化消息-主表
- **表名：** t_bd_solidify_msg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentity | 基础资料 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fstatus | 消息状态 | bpchar | 1 |  | √ | '0' | 消息状态,枚举: 1 :已消费 0 :未消费 |
| 4 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fopuserid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | foptype | 操作类型 | bpchar | 1 |  | √ | ' ' | 操作类型,枚举: 1 :新增 0 :删除 |
| 7 | fbitdata | fbitdata | bytea | 0 |  |  | null |  |
| 8 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_solidify_msg_fentity |  | fentity |
| 2 | idx_bd_solidify_msg_fuseorgid |  | fuseorgid |
| 3 | pk_t_bd_solidify_msg |  | fid |
