# 公式登记表-xkrpt_formularegister

## 公式登记表-主表 t_xkrpt_formularegister

- **表名称：** 公式登记表-主表
- **表名：** t_xkrpt_formularegister

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 3 | fservice | 服务名 | varchar | 100 |  | √ | ' ' | 服务名 |
| 4 | fcloudid | 云应用id | varchar | 20 |  | √ | ' ' | 云应用id |
| 5 | fmethod | 接口名 | varchar | 100 |  | √ | ' ' | 接口名 |
| 6 | fclasspath | 微服务工程路径 | varchar | 50 |  | √ | ' ' | 微服务工程路径 |
| 7 | fappid | 应用id | varchar | 20 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_formularegister |  | fid |
| 2 | idx_xkrpt_fr_fappid |  | fappid |
