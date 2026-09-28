# 开票抬头映射（弃用）-bdm_issue_title_mapping

## 开票抬头映射（弃用）-主表 t_bdm_issue_title_mapping

- **表名称：** 开票抬头映射（弃用）-主表
- **表名：** t_bdm_issue_title_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | foriginalbuyertaxno | 购方税号 | varchar | 50 |  | √ | ' ' | 购方税号 |
| 5 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fsysbuerypk | 开票购方ID | varchar | 50 |  | √ | ' ' | 开票购方ID |
| 7 | foriginalbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsysbuyername | 开票购方名称 | varchar | 50 |  | √ | ' ' | 开票购方名称 |
| 10 | fsysbuyertaxno | 开票购方税号 | varchar | 50 |  | √ | ' ' | 开票购方税号 |
| 11 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_issue_title_mapping |  | fsysbuyertaxno |
| 2 | pk_bdm_issue_title_mapping |  | fid |
