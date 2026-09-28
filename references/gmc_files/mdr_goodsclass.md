# 商品分类-mdr_goodsclass

## 商品分类-多语言表 t_mdr_itemclass_l

- **表名称：** 商品分类-多语言表
- **表名：** t_mdr_itemclass_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 分类名称 | varchar | 255 |  | √ | ' ' | 分类名称 |
| 3 | ffullname | 全称 | varchar | 2000 |  | √ | ' ' | 全称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdr_itemclassl_fname |  | fname |
| 2 | idx_mdr_itemclassl_fidflid |  | fid,flocaleid |
| 3 | t_mdr_itemclass_l_pkey |  | fpkid |

---

## 商品分类-主表 t_mdr_itemclass

- **表名称：** 商品分类-主表
- **表名：** t_mdr_itemclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 3 | fcreatechannelid | 创建渠道 | int8 | 64 |  | √ | 0 | 创建渠道 |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fpicture | 商品分类图片 | varchar | 255 |  | √ | ' ' | 商品分类图片 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcommenttempid | fcommenttempid | int8 | 64 |  | √ | 0 |  |
| 11 | foffering | 关联offering | int8 | 64 |  | √ | 0 | 产品目录 bd_productsummary |
| 12 | fgrade | 分类等级 | bpchar | 1 |  | √ | ' ' | 分类等级,枚举: A :LV0 品牌 B :LV1 分类 C :LV2 系列 D :LV3 SPU E :LV4 Offering |
| 13 | feasnumber | EAS编码 | varchar | 30 |  | √ | ' ' | EAS编码 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | 分类名称 | varchar | 255 |  | √ | ' ' | 分类名称 |
| 16 | fparentid | 上级分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_goodsclass |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | ffullname | ffullname | varchar | 2000 |  | √ | ' ' |  |
| 19 | flongnumber | 长编码 | varchar | 2000 |  | √ | ' ' | 长编码 |
| 20 | fmaterialclassid | 物料分类Id | int8 | 64 |  | √ | 0 | 物料分类Id |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 23 | fstandardid | 商品分类标准 | int8 | 64 |  | √ | 0 | 商品分类标准 bd_goodsclassstandard |
| 24 | fclasstype | 分类类型 | varchar | 10 |  | √ | '0' | 分类类型,枚举: 0 :公有分类 1 :渠道私有分类 2 :供应商私有分类 |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 分类编码 | varchar | 255 |  | √ | ' ' | 分类编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdr_itemclass_fno |  | fnumber |
| 2 | t_mdr_itemclass_pkey |  | fid |
| 3 | idx_mdr_itemclass_fpid |  | fparentid |

---

## 商品分类-分表 t_mdr_itemclass_p

- **表名称：** 商品分类-分表
- **表名：** t_mdr_itemclass_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismallclassification | fismallclassification | bpchar | 1 |  | √ | '0' |  |
| 3 | fseifclassification | 对应电商/自建分类 | varchar | 80 |  | √ | ' ' | 对应电商/自建分类 |
| 4 | fisonhomepage | 首页显示 | bpchar | 1 |  | √ | '0' | 首页显示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mdr_itemclass_p |  | fid |
| 2 | idx_mdr_itemclassp |  | fisonhomepage,fismallclassification,fseifclassification |
