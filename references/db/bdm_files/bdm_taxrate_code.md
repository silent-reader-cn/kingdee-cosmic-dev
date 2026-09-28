# 税收分类编码(废弃)-bdm_taxrate_code

## 税收分类编码(废弃)-多语言表 t_bdm_taxrate_code_l

- **表名称：** 税收分类编码(废弃)-多语言表
- **表名：** t_bdm_taxrate_code_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_taxrate_code_l |  | fpkid |
| 2 | idx_bdm_taxrate_code_l_0 |  | fid,flocaleid |

---

## 税收分类编码(废弃)-主表 t_bdm_taxrate_code

- **表名称：** 税收分类编码(废弃)-主表
- **表名：** t_bdm_taxrate_code

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 3 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率 |
| 4 | flslvbs | 零税率标识 | varchar | 50 |  | √ | ' ' | 零税率标识 |
| 5 | fyhzc | 优惠政策 | varchar | 150 |  | √ | ' ' | 优惠政策 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fzzstsnrdm | 增值税特殊内容代码 | varchar | 50 |  | √ | ' ' | 增值税特殊内容代码 |
| 8 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fbmbbbh | 编码表版本号 | varchar | 50 |  | √ | ' ' | 编码表版本号 |
| 12 | fsimplecodename | 分类编码简称 | varchar | 50 |  | √ | ' ' | 分类编码简称 |
| 13 | fzzstsgl | 增值税特殊管理 | varchar | 100 |  | √ | ' ' | 增值税特殊管理 |
| 14 | fyhzcmc | 优惠政策名称 | varchar | 50 |  | √ | ' ' | 优惠政策名称 |
| 15 | fxfsgl | 消费税管理 | varchar | 50 |  | √ | ' ' | 消费税管理 |
| 16 | fcode | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [税收分类编码(废弃) bdm_taxrate_code](../bdm_files/bdm_taxrate_code.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fxfszcyj | 消费税政策依据 | varchar | 1000 |  | √ | ' ' | 消费税政策依据 |
| 21 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 22 | fzzszcyj | 增值税特殊依据 | varchar | 1000 |  | √ | ' ' | 增值税特殊依据 |
| 23 | fdescription | 说明 | varchar | 2000 |  | √ | ' ' | 说明 |
| 24 | fhzx | 汇总项 | varchar | 50 |  | √ | ' ' | 汇总项 |
| 25 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 26 | fenable | 使用状态 | varchar | 4 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 商品税收分类编码 | varchar | 50 |  | √ | ' ' | 商品税收分类编码 |
| 28 | fgjz | 关键字 | varchar | 1000 |  | √ | ' ' | 关键字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_taxrate_code |  | fid |
| 2 | idx_bdm_taxrate_code |  | fnumber,fsimplecodename |
