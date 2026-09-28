# 任务注册表-bd_datachecktask

## 任务注册表-主表 t_bd_datachecktask

- **表名称：** 任务注册表-主表
- **表名：** t_bd_datachecktask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fphone | 通知电话号 | varchar | 20 |  | √ | ' ' | 通知电话号 |
| 4 | fcloudid | 云标识 | varchar | 50 |  | √ | 'fi' | 云标识 |
| 5 | fenable | 单据状态 | bpchar | 1 |  | √ | '1' | 单据状态,枚举: 0 :禁用 1 :启用 |
| 6 | fplugin | 插件路径 | varchar | 255 |  | √ | ' ' | 插件路径 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fappid | 应用标识 | varchar | 50 |  | √ | ' ' | 应用标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_task_no |  | fnumber |
| 2 | pk_t_bd_datachecktask |  | fid |
