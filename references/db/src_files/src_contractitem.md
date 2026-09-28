# 签约商务条款-src_contractitem

## 签约商务条款-主表 t_src_contractitem

- **表名称：** 签约商务条款-主表
- **表名：** t_src_contractitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 寻源项目 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 2 | freply | 供应商回复 | varchar | 510 |  | √ | ' ' | 供应商回复 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fdemandvalue | 采购方要求值 | varchar | 510 |  | √ | ' ' | 采购方要求值 |
| 6 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 7 | frequest | 商务条款名称 | varchar | 510 |  | √ | ' ' | 商务条款名称 |
| 8 | fbizitemld | 商务条款编码 | int8 | 64 |  | √ | 0 | 寻源商务条款 src_bizitem |
| 9 | fitemtype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 10 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别 |
| 11 | freplyvalue | 供应商回复值 | varchar | 510 |  | √ | ' ' | 供应商回复值 |
| 12 | fdemand | 采购方要求 | varchar | 510 |  | √ | ' ' | 采购方要求 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_contractitem_fid |  | fid |
| 2 | idx_src_contractitem_fsid |  | fsupplierid |
| 3 | pk_src_contractitem |  | fentryid |
