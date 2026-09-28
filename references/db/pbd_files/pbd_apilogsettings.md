# 日志设置-pbd_apilogsettings

## 日志设置-主表 t_mal_apilogsetting

- **表名称：** 日志设置-主表
- **表名：** t_mal_apilogsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fautocleartime | 自动清理期限 | int8 | 64 |  | √ | 0 | 自动清理期限 |
| 3 | fautoarchiveamt | 自动归档数量 | int8 | 64 |  | √ | 0 | 自动归档数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_apilogsetting |  | fid |
| 2 | pk_mal_apilogsetting |  | fautoarchiveamt |
