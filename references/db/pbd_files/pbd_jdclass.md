# 京东分类-pbd_jdclass

## 京东分类-多语言表 t_mal_prodclass_l

- **表名称：** 京东分类-多语言表
- **表名：** t_mal_prodclass_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 分类名称 | varchar | 100 |  | √ | ' ' | 分类名称 |
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
| 1 | t_mal_prodclass_l_pkey |  | fpkid |
| 2 | idx_mal_prodclass_l_fid |  | fid,flocaleid |

---

## 京东分类-主表 t_mal_prodclass

- **表名称：** 京东分类-主表
- **表名：** t_mal_prodclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 3 | fisonhomepage | 在商城首页展示 | bpchar | 1 |  | √ | ' ' | 在商城首页展示,枚举: 0 :否 1 :是 |
| 4 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fsource | 分类来源 | bpchar | 1 |  | √ | ' ' | 分类来源,枚举: 1 :自建商城 2 :京东 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpurtypeid | fpurtypeid | int8 | 64 |  | √ | 0 |  |
| 10 | fmappingid | 对应自建分类 | int8 | 64 |  | √ | 0 | [商品分类 pbd_goodsclass](../pbd_files/pbd_goodsclass.md) |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 17 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [京东分类 pbd_jdclass](../pbd_files/pbd_jdclass.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 20 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 23 | fenable2 | fenable2 | bpchar | 1 |  | √ | ' ' |  |
| 24 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 分类编码 | varchar | 30 |  | √ | ' ' | 分类编码 |
| 27 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_prodclass_pkey |  | fid |
| 2 | idx_mal_prodclass_number |  | fnumber |
