# 税务管控视图默认方案-tctb_org_default_view

## 税务管控视图默认方案-主表 t_bastax_org_view

- **表名称：** 税务管控视图默认方案-主表
- **表名：** t_bastax_org_view

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 7 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 8 | fisdefault | 是否默认方案 | bpchar | 1 |  | √ | ' ' | 是否默认方案 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_org_view |  | fid |
| 2 | idx_idx_bastax_org_view |  | fnumber |
