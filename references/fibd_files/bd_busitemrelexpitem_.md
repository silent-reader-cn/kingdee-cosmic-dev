# 业务类型关联业务项目-bd_busitemrelexpitem_

## 业务类型关联业务项目-主表 t_bd_busitemrelexpitem

- **表名称：** 业务类型关联业务项目-主表
- **表名：** t_bd_busitemrelexpitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseitemid | 业务项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fbusinessitemid | 业务类型 | int8 | 64 |  | √ | 0 | 报账业务类型 bd_businessitem |
| 4 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_rel_exp |  | fbusinessitemid,fexpenseitemid |
| 2 | t_bd_busitemrelexpitem_pkey |  | fid |
