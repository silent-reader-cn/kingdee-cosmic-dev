# 知识管理全局信息-som_knowledge_global

## 知识管理全局信息-主表 t_tk_scs_global

- **表名称：** 知识管理全局信息-主表
- **表名：** t_tk_scs_global

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskillid | 技能id | int8 | 64 |  | √ | 0 | 技能id |
| 3 | fqxtenantid | 苍穹租户id | varchar | 100 |  | √ | ' ' | 苍穹租户id |
| 4 | ftenantid | AI租户id | int8 | 64 |  | √ | 0 | AI租户id |
| 5 | fpulltime | 日志拉取时间 | timestamp | 0 |  |  | null | 日志拉取时间 |
| 6 | frobotid | 机器人id | int8 | 64 |  | √ | 0 | 机器人id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_scs_global |  | fid |
| 2 | idx_ssc_scs_global_tent |  | fqxtenantid |
