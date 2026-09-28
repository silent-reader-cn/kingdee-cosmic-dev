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
| 4 | fecgoodsid | fecgoodsid | int8 | 64 |  | √ | 0 |  |
| 5 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 6 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 8 | fbilldate | fbilldate | timestamp | 0 |  |  | null |  |
| 9 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fpurchasetype | fpurchasetype | int8 | 64 |  | √ | 0 |  |
| 12 | fplatform | fplatform | bpchar | 1 |  | √ | ' ' |  |
| 13 | fbillno | fbillno | varchar | 80 |  | √ | ' ' |  |

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
