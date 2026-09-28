# 商品对应表-pmm_prodmatmapping

## 商品对应表-主表 t_mal_prodmatmapping

- **表名称：** 商品对应表-主表
- **表名：** t_mal_prodmatmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcategory | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_goodsclass](../gmc_files/mdr_goodsclass.md) |
| 4 | fecgoodsid | 电商商品 | int8 | 64 |  | √ | 0 | [电商商品 pbd_mallgoods](../pbd_files/pbd_mallgoods.md) |
| 5 | fgoodsid | 自建商品 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 6 | fmaterialid | ERP物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbilldate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fpurchasetype | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 12 | fplatform | 商品来源 | bpchar | 1 |  | √ | ' ' | 商品来源,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |

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
