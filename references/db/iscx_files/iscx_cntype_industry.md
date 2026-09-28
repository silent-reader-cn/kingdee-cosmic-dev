# 连接类型_行业-iscx_cntype_industry

## 连接类型_行业-主表 t_iscx_cntype_industry

- **表名称：** 连接类型_行业-主表
- **表名：** t_iscx_cntype_industry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcntype | 连接类型编码 | varchar | 50 |  | √ | ' ' | 连接类型编码 |
| 3 | findustry | 行业的名称 | varchar | 50 |  | √ | ' ' | 行业的名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscx_cntype_industry |  | fcntype |
| 2 | pk_t_iscx_cntype_industry |  | fid |
