# 年报规则树子节点-tccit_rule_nbchild

## 年报规则树子节点-主表 t_tccit_rule_nbchild

- **表名称：** 年报规则树子节点-主表
- **表名：** t_tccit_rule_nbchild

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchildid | 子节点id | int8 | 64 |  | √ | 0 | 子节点id |
| 3 | ftype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型 |
| 4 | fentryid | 节点id | int8 | 64 |  | √ | 0 | 节点id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tccit_rule_nbchild_1 |  | fentryid |
| 2 | pk_tccit_rule_nbchild |  | fid |
