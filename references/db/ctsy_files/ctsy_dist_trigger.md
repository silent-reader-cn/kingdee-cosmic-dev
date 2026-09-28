# 主数据分发启动方案-ctsy_dist_trigger

## 主数据分发启动方案-主表 t_ctsy_disttriggers

- **表名称：** 主数据分发启动方案-主表
- **表名：** t_ctsy_disttriggers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fdistid | 分发方案 | int8 | 64 |  | √ | 0 | [主数据分发方案 ctsy_distribut_scheme](../ctsy_files/ctsy_distribut_scheme.md) |
| 5 | ftenantid | 租户 | int8 | 64 |  | √ | 0 | [租户配置 ctsy_tenant](../ctsy_files/ctsy_tenant.md) |
| 6 | ftriggerid | 启动方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 7 | ftriggertype | 分发类型 | varchar | 30 |  | √ | ' ' | 分发类型,枚举: auto :定时启动 manual :人工启动 event :事件触发 message :消息启动 |
| 8 | fiscdataid | 数据集成方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctsy_disttriggers_tenantid |  | fdistid,ftenantid,fiscdataid |
| 2 | pk_t_ctsy_disttriggers |  | fid |
