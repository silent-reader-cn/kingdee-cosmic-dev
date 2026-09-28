# 商品对应表-pmm_prodmatmapping_bd

## 商品对应表-主表 t_mal_prodmatmapping

- **表名称：** 商品对应表-主表
- **表名：** t_mal_prodmatmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcategory | fcategory | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 5 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | 商品管理 pmm_prodmanage |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 8 | fpurchasetype | fpurchasetype | int8 | 64 |  | √ | 0 |  |
| 9 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 10 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mal_prodmatmapping_pkey |  | fid |
| 2 | idx_mal_prodmap_fgoodsid |  | fgoodsid |
| 3 | idx_mal_prodmap_fpurtype |  | fpurchasetype |
| 4 | idx_mal_prodmap_fmaterialid |  | fmaterialid |
