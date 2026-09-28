# git快速开放管理-bos_devp_gitmanager

## git快速开放管理-主表 t_meta_gitmanager

- **表名称：** git快速开放管理-主表
- **表名：** t_meta_gitmanager

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissupport | git是否支持 | varchar | 20 |  | √ | ' ' | git是否支持 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_meta_gitmanager |  | fid |
