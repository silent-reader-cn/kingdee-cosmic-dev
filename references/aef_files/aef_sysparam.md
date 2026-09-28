# 电子档案系统配置-aef_sysparam

## 电子档案系统配置-主表 t_aef_sysparam

- **表名称：** 电子档案系统配置-主表
- **表名：** t_aef_sysparam

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
| 1 | pk_aef_sysparam |  | fid |
| 2 | idx_aef_sysparam |  | fkey |
