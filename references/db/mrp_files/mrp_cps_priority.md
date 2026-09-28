# 优先级设置-mrp_cps_priority

## 优先级设置-主表 t_mrp_cps_priority

- **表名称：** 优先级设置-主表
- **表名：** t_mrp_cps_priority

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialshortagetag | 欠料处理标志 | bpchar | 1 |  | √ | '0' | 欠料处理标志 |
| 3 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 4 | forderid | 订单id | int8 | 64 |  | √ | 0 | 订单id |
| 5 | fbillentity | 订单实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | forderentryid | 订单分录id | int8 | 64 |  | √ | 0 | 订单分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_cps_priority |  | fid |
| 2 | idx_mrp_cps_priority |  | forderentryid |
