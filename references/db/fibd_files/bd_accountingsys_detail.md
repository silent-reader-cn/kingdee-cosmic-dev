# 核算体系政策明细注册-bd_accountingsys_detail

## 核算体系政策明细注册-主表 t_bd_accountingsys_detail

- **表名称：** 核算体系政策明细注册-主表
- **表名：** t_bd_accountingsys_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbizapp | 应用 | varchar | 80 |  | √ | ' ' | 应用 |
| 3 | fbizform | 表单标识 | varchar | 80 |  | √ | ' ' | 表单标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountingsys_detail_pkey |  | fid |
| 2 | idx_bd_accountingsys_detail |  | fbizapp |
