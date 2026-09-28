# 客户服务水平-invp_cus_servicelevel

## 客户服务水平-主表 t_invp_servicelevel

- **表名称：** 客户服务水平-主表
- **表名：** t_invp_servicelevel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcoefficient | 安全系数 | numeric | 23 | 10 | √ | 0 | 安全系数 |
| 3 | fservicelevel | 客户服务水平 | numeric | 23 | 10 | √ | 0 | 客户服务水平 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_invp_servicelevel |  | fid |
