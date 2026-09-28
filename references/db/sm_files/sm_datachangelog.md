# 单据数据更新日志-sm_datachangelog

## 单据数据更新日志-主表 t_sm_datachangelog

- **表名称：** 单据数据更新日志-主表
- **表名：** t_sm_datachangelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | foldvalue | 更新前的值 | varchar | 100 |  | √ | ' ' | 更新前的值 |
| 4 | fopposition | 操作位置 | varchar | 100 |  | √ | ' ' | 操作位置 |
| 5 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 操作用户 |
| 6 | ftablename | 更新表名 | varchar | 50 |  | √ | ' ' | 更新表名 |
| 7 | fentryid | 更新主键值 | int8 | 64 |  | √ | 0 | 更新主键值 |
| 8 | fformid | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 9 | ffieldkey | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 10 | fnewvalue | 更新后的值 | varchar | 100 |  | √ | ' ' | 更新后的值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sm_datachangelog |  | fentryid |
| 2 | pk_sm_datachangelog |  | fid |
