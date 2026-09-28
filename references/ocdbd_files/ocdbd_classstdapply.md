# 商品分类标准应用-ocdbd_classstdapply

## 商品分类标准应用-主表 t_ocdbd_classstdapply

- **表名称：** 商品分类标准应用-主表
- **表名：** t_ocdbd_classstdapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplyplatform | 应用场景 | varchar | 30 |  | √ | ' ' | 应用场景,枚举: 0 :B2B商城 1 :POS收银 2 :在线购 3 :大屏购 4 :订货批量设置 5 :可销商品设置 6 :促销政策设置 7 :在线商城 8 :费用预算 |
| 3 | fclassstandardid | 商品分类标准 | int8 | 64 |  | √ | 0 | 商品分类标准 bd_goodsclassstandard |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_classstdapply |  | fid |
| 2 | idx_ocdbd_csapply_platform |  | fapplyplatform |
