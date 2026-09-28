# 供应链关系表-scrim_supply_relation

## 供应链关系表-主表 t_scrim_supply_relation

- **表名称：** 供应链关系表-主表
- **表名：** t_scrim_supply_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmasterid | 基础资料主数据内码 | int8 | 64 |  |  | null | 基础资料主数据内码 |
| 4 | fstandardname | 标准名称 | varchar | 256 |  | √ | ' ' | 标准名称 |
| 5 | fparentid | 父级id | int8 | 64 |  | √ | 0 | 父级id |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fenterprisetype | 企业类型 | varchar | 10 |  | √ | ' ' | 企业类型 |
| 8 | fcompanyid | 工商信息对应的企业id | varchar | 50 |  |  | null | 工商信息对应的企业id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_scrim_supply_relation |  | fid |
| 2 | idx_relation_parentid |  | fparentid |
