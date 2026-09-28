# 科目替换注册信息-bd_acct_reginfo

## 科目替换注册信息-主表 t_bd_acct_reginfo

- **表名称：** 科目替换注册信息-主表
- **表名：** t_bd_acct_reginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmetadata | 元数据 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 5 | fismutibasedata | 是否多选基础资料 | bpchar | 1 |  | √ | '0' | 是否多选基础资料 |
| 6 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: acct :科目 accttable :科目表 |
| 7 | fuseorg | 使用组织 | varchar | 50 |  | √ | ' ' | 使用组织 |
| 8 | ffieldname | 字段名 | varchar | 36 |  | √ | ' ' | 字段名 |
| 9 | fentryname | 分录标识 | varchar | 50 |  | √ | ' ' | 分录标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_acct_reginfo |  | fid |
| 2 | idx_bd_acct_reginfo |  | fmetadata,ffieldtype,fismutibasedata |
