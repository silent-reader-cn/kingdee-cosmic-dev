# 反写记录-er_caswriteback

## 反写记录-主表 t_er_caswriteback

- **表名称：** 反写记录-主表
- **表名：** t_er_caswriteback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecid | 收款单id | int8 | 64 |  | √ | 0 | 收款单id |
| 3 | foperatetype | 操作 | varchar | 30 |  | √ | ' ' | 操作 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fvalid | 有效 | bpchar | 1 |  | √ | '1' | 有效 |
| 6 | ftargetentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 7 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型 |
| 8 | ftargetbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_er_writeback_billid |  | ftargetbillid |
| 2 | pk_er_caswriteback |  | fid |
