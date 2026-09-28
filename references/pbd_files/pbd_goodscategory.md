# 商品分类对应-pbd_goodscategory

## 商品分类对应-主表 t_mal_goodscategory

- **表名称：** 商品分类对应-主表
- **表名：** t_mal_goodscategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | feccatogryid | 电商分类编码 | int8 | 64 |  | √ | 0 | 商品分类 mdr_goodsclass |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fselfcatogryid | 自建分类编码 | int8 | 64 |  | √ | 0 | 商品分类 mdr_goodsclass |
| 9 | fsource | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁商城 4 :得力商城 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_gcategory_fselfid |  | fselfcatogryid |
| 2 | pk_t_mal_goodscategory |  | fid |
| 3 | idx_mal_gcategory_fecid |  | feccatogryid |
