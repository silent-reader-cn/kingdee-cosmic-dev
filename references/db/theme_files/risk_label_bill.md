# IPO风险标签管理单据-risk_label_bill

## IPO风险标签管理单据-主表 t_risk_label_management

- **表名称：** IPO风险标签管理单据-主表
- **表名：** t_risk_label_management

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 树节点id | varchar | 50 |  | √ | ' ' | 树节点id |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | frulecontent | 内容规则 | varchar | 255 |  | √ | ' ' | 内容规则 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fipoorgld | IPO主体 | int8 | 64 |  |  | null | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 9 | fdefault | 是否预置 | bpchar | 1 |  | √ | '1' | 是否预置 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | frulecontent_tag | 内容规则_详情 | text | 0 |  |  | null | 内容规则_详情 |
| 12 | frulecontentsql | 内容规则sql | varchar | 255 |  | √ | ' ' | 内容规则sql |
| 13 | ftabcode | 页签编码 | varchar | 50 |  | √ | ' ' | 页签编码 |
| 14 | frulecontentsql_tag | 内容规则sql_详情 | text | 0 |  |  | null | 内容规则sql_详情 |
| 15 | fisshow | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_label_management_group |  | forgid,fgroupid |
| 2 | pk_risk_label_management |  | fid |
