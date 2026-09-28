# 标准成本后台参数-sco_bgparam

## 标准成本后台参数-主表 t_sco_bgparam

- **表名称：** 标准成本后台参数-主表
- **表名：** t_sco_bgparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fvalue | 值 | varchar | 30 |  | √ | ' ' | 值 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fkey | key标识 | varchar | 30 |  | √ | ' ' | key标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_bgparam |  | fid |
| 2 | idx_sco_bgparam |  | forgid |
