# 费用全局配置-er_stdconfig

## 费用全局配置-主表 t_er_stdconfig

- **表名称：** 费用全局配置-主表
- **表名：** t_er_stdconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | value | varchar | 255 |  | √ | ' ' | value |
| 3 | fkey | key | varchar | 255 |  | √ | ' ' | key |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_stdconfig_pkey |  | fid |
| 2 | idx_er_stdconfig_fkey |  | fkey |
