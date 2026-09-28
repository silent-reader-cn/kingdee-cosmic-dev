# 产品分类-bd_productgroup

## 产品分类-主表 t_bd_productgroup

- **表名称：** 产品分类-主表
- **表名：** t_bd_productgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcategory | 本级分组 | varchar | 30 |  | √ | ' ' | 本级分组,枚举: Consumers BUnit BG :Lv0 Product Category Product Line :Lv1 Product Category Product Area :Lv2 Product Category Product Family :Lv3 Product Category Product Series :Lv4 Product Series |
| 5 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [产品分类 bd_productgroup](../basedata_files/bd_productgroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | findustrialtype | 工业类型 | varchar | 255 |  | √ | ' ' | 工业类型 |
| 8 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fznname | 名称（中文） | varchar | 255 |  | √ | ' ' | 名称（中文） |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fenname | 名称（英文） | varchar | 255 |  | √ | ' ' | 名称（英文） |
| 13 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstandardid | fstandardid | int8 | 64 |  | √ | 0 |  |
| 16 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 17 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_productgroup_number |  | fnumber |
| 2 | pk_t_bd_productgroup |  | fid |

---

## 产品分类-多语言表 t_bd_productgroup_l

- **表名称：** 产品分类-多语言表
- **表名：** t_bd_productgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ids_idx_t_bd_productgroup_l_fi |  | fid,flocaleid |
| 2 | pk_t_bd_productgroup_l |  | fpkid |
