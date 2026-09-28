# 全宗管理(弃用)-eafc_general_archive

## 全宗管理(弃用)-主表 tk_eafc_general_archive

- **表名称：** 全宗管理(弃用)-主表
- **表名：** tk_eafc_general_archive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fk_eafc_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :未启用 2 :启用 3 :禁用 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fk_eafc_full_name | 全宗名称 | varchar | 50 |  | √ | ' ' | 全宗名称 |
| 12 | fk_eafc_booktype | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 13 | fk_eafc_superior_org | 上级业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fk_eafc_enterprise_tax | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |
| 15 | fk_eafc_desc | 全宗描述 | varchar | 50 |  | √ | ' ' | 全宗描述 |
| 16 | fbillno | 全宗号 | varchar | 30 |  | √ | ' ' | 全宗号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fk_eafc_effective_time | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_general_archive |  | fid |
