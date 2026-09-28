# 客户状态排除表-bd_customerstatusexclude

## 客户状态排除表-主表 t_bd_customerstatusexclud

- **表名称：** 客户状态排除表-主表
- **表名：** t_bd_customerstatusexclud

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomerstatus | 客户状态 | int8 | 64 |  | √ | 0 | 客户状态 bd_customerstatus |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_customerstatusexclud |  | fid |
| 2 | idx_bd_customerstatusexclud |  | fcustomerstatus |
