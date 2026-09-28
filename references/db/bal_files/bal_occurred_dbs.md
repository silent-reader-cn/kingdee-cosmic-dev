# 余额更新发生记录-bal_occurred_dbs

## 余额更新发生记录-主表 t_bal_occurred_dbs

- **表名称：** 余额更新发生记录-主表
- **表名：** t_bal_occurred_dbs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :完全异步更新 2 :部分异步更新 |
| 3 | fdb | 数据库标识 | varchar | 20 |  | √ | ' ' | 数据库标识 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | '0' | 人员 bos_user |
| 6 | fbal | 余额表 | varchar | 36 |  | √ | ' ' | 余额表 bal_balanceinfo |
| 7 | fappid | 应用标识 | varchar | 36 |  | √ | ' ' | 应用标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_occurred_dbs |  | fid |
