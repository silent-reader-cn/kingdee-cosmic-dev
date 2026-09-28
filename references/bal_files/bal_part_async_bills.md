# 更新中单据-bal_part_async_bills

## 更新中单据-主表 t_bal_updating

- **表名称：** 更新中单据-主表
- **表名：** t_bal_updating

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fapp | 应用标识 | varchar | 20 |  | √ | ' ' | 应用标识 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | finstanceid | 节点ID | varchar | 100 |  | √ | ' ' | 节点ID |
| 5 | fdb | 数据库 | varchar | 20 |  | √ | ' ' | 数据库 |
| 6 | ftxid | 事务ID | int8 | 64 |  | √ | '0' | 事务ID |
| 7 | fcreaterid | 创建人 | int8 | 64 |  | √ | '0' | 人员 bos_user |
| 8 | fbillid | 单据ID | int8 | 64 |  | √ | '0' | 单据ID |
| 9 | fbal | 余额表 | varchar | 36 |  | √ | ' ' | 余额表 bal_balanceinfo |
| 10 | fruleid | 更新规则 | varchar | 36 |  | √ | ' ' | 余额更新规则列表 bal_balanceupdaterule |
| 11 | fbillentity | 实体对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_updating_ftx |  | ftxid |
| 2 | pk_bal_updating |  | fid |
| 3 | idx_bal_updating_fct |  | fcreatetime |
| 4 | idx_bal_updating_fbr |  | fbillid,fruleid |
