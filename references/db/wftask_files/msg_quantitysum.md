# 消息数量统计-msg_quantitysum

## 消息数量统计-主表 t_msg_quantitysum

- **表名称：** 消息数量统计-主表
- **表名：** t_msg_quantitysum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 3 | fbilltype | 单据类型 | varchar | 200 |  | √ | ' ' | 单据类型 |
| 4 | fdatatype | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 5 | fquantitysum | 统计数量 | int4 | 32 |  | √ | 0 | 统计数量 |
| 6 | fupdatedate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msg_quantitysum |  | fid |
| 2 | idx_msg_qtysum_userid |  | fuserid,fdatatype |
| 3 | idx_msg_qtysum_billtype |  | fbilltype,fuserid,fdatatype |
