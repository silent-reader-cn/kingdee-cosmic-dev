# 业务类型关联参数-bd_busitemrelparam

## 业务类型关联参数-主表 t_bd_businessitemrelparam

- **表名称：** 业务类型关联参数-主表
- **表名：** t_bd_businessitemrelparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbusinessitemparamid | 参数 | int8 | 64 |  | √ | 0 | 业务类型参数 bd_businessitemparam |
| 3 | fvalue | 参数值 | varchar | 500 |  | √ | ' ' | 参数值 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbusinessitemid | 业务类型 | int8 | 64 |  | √ | 0 | 报账业务类型 bd_businessitem |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdbus_birp_fbi |  | fbusinessitemid |
| 2 | idx_bdbus_birp_fparam |  | fbusinessitemparamid |
| 3 | t_bd_businessitemrelparam_pkey |  | fid |
