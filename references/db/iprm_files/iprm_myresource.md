# 我的应用-iprm_myresource

## 我的应用-主表 t_iprm_myresource

- **表名称：** 我的应用-主表
- **表名：** t_iprm_myresource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdomain | 领域 | varchar | 20 |  | √ | ' ' | 领域 |
| 7 | fcontenttype | 内容类型 | varchar | 20 |  | √ | ' ' | 内容类型,枚举: 4 : |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | ftypename | 主题 | varchar | 20 |  | √ | ' ' | 主题 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreateorg | 创作组织 | varchar | 20 |  | √ | ' ' | 创作组织 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | flabtype | 标签类型 | varchar | 20 |  | √ | ' ' | 标签类型 |
| 14 | findustry | 行业 | varchar | 20 |  | √ | ' ' | 行业 |
| 15 | fbrief | 简介 | varchar | 255 |  | √ | ' ' | 简介 |
| 16 | fbillno | 编码 | varchar | 20 |  | √ | ' ' | 编码 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iprm_myresource |  | fid |
| 2 | idx_iprm_myresource_fid |  | fbillno |
