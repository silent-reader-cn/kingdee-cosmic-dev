# debug模式设置表-sca_debugsetting

## debug模式设置表-主表 t_sca_debugsetting

- **表名称：** debug模式设置表-主表
- **表名：** t_sca_debugsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 参数名称 | varchar | 100 |  | √ | ' ' | 参数名称 |
| 3 | fisdebug | 是否调试 | int8 | 64 |  | √ | 0 | 是否调试 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_debugsetting |  | fname |
| 2 | pk_sca_debugsetting |  | fid |
