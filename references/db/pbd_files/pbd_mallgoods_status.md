# 电商商品状态-pbd_mallgoods_status

## 电商商品状态-主表 t_mal_goods_status

- **表名称：** 电商商品状态-主表
- **表名：** t_mal_goods_status

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsaleable | 可售状态 | bpchar | 1 |  | √ | ' ' | 可售状态,枚举: 0 :不可售 1 :可售 |
| 3 | fmallgoodsid | 电商商品 | int8 | 64 |  | √ | 0 | [电商商品 pbd_mallgoods](../pbd_files/pbd_mallgoods.md) |
| 4 | fecstatus | 电商上架状态 | bpchar | 1 |  | √ | ' ' | 电商上架状态,枚举: 1 :上架 0 :下架 |
| 5 | fmallstatus | 企业上架状态 | bpchar | 1 |  | √ | ' ' | 企业上架状态,枚举: 1 :上架 0 :下架 |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_goods_status |  | fid |
| 2 | idx_mal_goods_status_fmalid |  | fmallgoodsid |
