# 移交配置-eafc_deliver_config

## 移交配置-主表 tk_eafc_deliver_config

- **表名称：** 移交配置-主表
- **表名：** tk_eafc_deliver_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_modifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fk_eafc_modifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_eafc_close_flag | 是否终止 | varchar | 50 |  | √ | ' ' | 是否终止,枚举: 1 :是 2 :否 |
| 5 | fk_eafc_createrfield | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fk_eafc_sleep_seconds | 等待执行间隔 | varchar | 50 |  | √ | ' ' | 等待执行间隔 |
| 7 | fk_eafc_execute_count | 最大线程数 | varchar | 50 |  | √ | ' ' | 最大线程数 |
| 8 | fk_eafc_createdatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fk_eafc_apply_no | 申请单号 | varchar | 50 |  | √ | ' ' | 申请单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_deliver_config |  | fid |
