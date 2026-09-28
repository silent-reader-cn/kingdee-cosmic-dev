# 开票方实体-sim_drawer_setting

## 开票方实体-主表 t_sim_drawer_setting

- **表名称：** 开票方实体-主表
- **表名：** t_sim_drawer_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawerid | 开票人id | varchar | 50 |  | √ | ' ' | 开票人id |
| 3 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 4 | fpayee | 收款人 | varchar | 50 |  | √ | ' ' | 收款人 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | fpayeestrategy | 收款人取值方式 | varchar | 50 |  | √ | ' ' | 收款人取值方式 |
| 7 | ftaxno | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 8 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 9 | freviewerstrategy | 收款人取值方式 | varchar | 50 |  | √ | ' ' | 收款人取值方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_drawer_setting |  | fid |
| 2 | idx_sim_drawer_setting |  | ftaxno |
