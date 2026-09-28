# 工作流基础资料-chatbi_workflow_base

## 工作流基础资料-主表 t_cbi_workflow

- **表名称：** 工作流基础资料-主表
- **表名：** t_cbi_workflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmodifydate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 5 | fcontent_tag | fcontent_tag | text | 0 |  |  | null |  |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fenable | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :启用 0 :禁用 |
| 8 | fmodifier | 最近更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fcontent | fcontent | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_workflow |  | fid |
