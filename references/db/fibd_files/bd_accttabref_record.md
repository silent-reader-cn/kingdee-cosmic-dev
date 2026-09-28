# 新科目表对照启用记录-bd_accttabref_record

## 新科目表对照启用记录-主表 t_bd_accttabref_record

- **表名称：** 新科目表对照启用记录-主表
- **表名：** t_bd_accttabref_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faccountrefid | 新科目表对照关系 | int8 | 64 |  | √ | 0 | 科目表版本化 bd_accounttableref |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fenablestatus | 启用状态 | bpchar | 1 |  | √ | 'A' | 启用状态,枚举: A :未启用 B :正在启用 C :已启用 D :已反启用 E :待重新启用 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnewaccttabid | 新版科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 6 | foldaccttabid | 旧版科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 7 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 8 | fdisabledate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_accttabref_record |  | forgid |
| 2 | pk_t_bd_accttabref_record |  | fid |
