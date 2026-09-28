# 采购清单要求F7-src_purlistitemf7

## 采购清单要求F7-主表 t_src_purlist_item

- **表名称：** 采购清单要求F7-主表
- **表名：** t_src_purlist_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 采购清单要求id | int8 | 64 |  | √ | 0 | 采购清单要求id |
| 2 | freply | 供应商回复 | varchar | 510 |  | √ | ' ' | 供应商回复 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fdemandvalue | fdemandvalue | varchar | 510 |  | √ | ' ' |  |
| 7 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 8 | frequest | 采购方要求 | varchar | 510 |  | √ | ' ' | 采购方要求 |
| 9 | fbizitemld | fbizitemld | int8 | 64 |  | √ | 0 |  |
| 10 | fitemtype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 11 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :正式供应商 |
| 12 | freplyvalue | freplyvalue | varchar | 510 |  | √ | ' ' |  |
| 13 | fdemand | fdemand | varchar | 510 |  | √ | ' ' |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_project_item_fsid |  | fsupplierid |
| 2 | pk_src_purlist_item |  | fentryid |
| 3 | idx_src_project_item_fid |  | fid |
| 4 | idx_src_project_item_fpid |  | fprojectid |
