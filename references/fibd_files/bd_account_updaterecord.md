# 科目版本化更新记录-bd_account_updaterecord

## 科目版本化更新记录-主表 t_bd_accountuprecord

- **表名称：** 科目版本化更新记录-主表
- **表名：** t_bd_accountuprecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fversiondate | 版本化日期 | timestamp | 0 |  |  | null | 版本化日期 |
| 3 | fmetadata | 元数据 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 4 | fdataid | 基础资料数据主键ID | int8 | 64 |  | √ | 0 | 基础资料数据主键ID |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ffieldname | 字段名 | varchar | 36 |  | √ | ' ' | 字段名 |
| 7 | fentryname | 分录标识 | varchar | 50 |  | √ | ' ' | 分录标识 |
| 8 | fafaccountid | 版本化后ID | int8 | 64 |  | √ | 0 | 版本化后ID |
| 9 | frecordsource | 记录来源 | bpchar | 1 |  | √ | '0' | 记录来源,枚举: 0 :统一处理 1 :特殊处理 |
| 10 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fdataentryid | 基础资料数据分录ID | int8 | 64 |  | √ | 0 | 基础资料数据分录ID |
| 13 | ffieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: acct :科目 accttable :科目表 |
| 14 | freaccountid | 版本化前ID | int8 | 64 |  | √ | 0 | 版本化前ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountuprecord |  | fid |
| 2 | idx_bd_accountuprecord |  | fmetadata,freaccountid,ffieldtype,frecordsource |
