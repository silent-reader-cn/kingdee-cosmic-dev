# 商务条款分析-src_bizitemf7

## 商务条款分析-多语言表 t_src_purlist_item_l

- **表名称：** 商务条款分析-多语言表
- **表名：** t_src_purlist_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_purlist_item_l |  | fentryid,flocaleid |
| 2 | pk_src_purlist_item_l |  | fpkid |

---

## 商务条款分析-主表 t_src_purlist_item

- **表名称：** 商务条款分析-主表
- **表名：** t_src_purlist_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freply | 供应商回复 | varchar | 510 |  | √ | ' ' | 供应商回复 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fdemandvalue | 采购方要求值 | varchar | 510 |  | √ | ' ' | 采购方要求值 |
| 7 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 8 | frequest | 商务条款名称 | varchar | 510 |  | √ | ' ' | 商务条款名称 |
| 9 | fbizitemld | 商务条款编码 | int8 | 64 |  | √ | 0 | [寻源商务条款 src_bizitem](../src_files/src_bizitem.md) |
| 10 | fitemtype | 商务条款类型 | varchar | 50 |  | √ | ' ' | 商务条款类型 |
| 11 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别 |
| 12 | freplyvalue | 供应商回复值 | varchar | 510 |  | √ | ' ' | 供应商回复值 |
| 13 | fdemand | 采购方要求 | varchar | 510 |  | √ | ' ' | 采购方要求 |
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
