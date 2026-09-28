# 商品信息商品分类-ocdbd_itemclassentry

## 商品信息商品分类-主表 t_ocdbd_itemclassentry

- **表名称：** 商品信息商品分类-主表
- **表名：** t_ocdbd_itemclassentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 商品id | int8 | 64 |  | √ | 0 | 商品id |
| 2 | fgoodsclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 3 | fclassstandardid | 商品分类标准 | int8 | 64 |  | √ | 0 | [商品分类标准 bd_goodsclassstandard](../gmc_files/bd_goodsclassstandard.md) |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_itemclassentry |  | fentryid |
| 2 | idx_ocdbd_icentry_fid |  | fid |
