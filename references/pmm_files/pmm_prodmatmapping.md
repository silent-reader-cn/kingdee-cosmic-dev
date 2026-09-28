# 商品对应表-pmm_prodmatmapping

## 商品对应表-主表 t_mal_prodmatmapping

- **表名称：** 商品对应表-主表
- **表名：** t_mal_prodmatmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcategory | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_goodsclass |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | 商品管理 pmm_prodmanage |
| 6 | fmaterialid | ERP物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fpurchasetype | 采购类型 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 9 | fbilldate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

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
