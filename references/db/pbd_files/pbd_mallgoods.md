# 电商商品-pbd_mallgoods

## 电商商品-主表 t_mal_goods

- **表名称：** 电商商品-主表
- **表名：** t_mal_goods

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodel | 规格型号 | text | 0 |  |  | null | 规格型号 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmainpic | 主图 | varchar | 255 |  | √ | ' ' | 主图 |
| 10 | fsource | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbrandid | 品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 13 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 17 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 商品编码 | varchar | 80 |  | √ | ' ' | 商品编码 |
| 19 | fstatusinfoid | 状态信息 | int8 | 64 |  | √ | 0 | 电商商品状态 pbd_mallgoods_status |
| 20 | fpriceinfoid | 价格信息 | int8 | 64 |  | √ | 0 | 电商商品价格 pbd_mallgoods_price |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_goods_fclassid |  | fclassid |
| 2 | idx_mal_goods_fnumber |  | fnumber |
| 3 | pk_t_mal_goods |  | fid |
| 4 | idx_mal_goods_fmodstat |  | fmodifytime,fstatusinfoid |

---

## 电商商品-多语言表 t_mal_goods_l

- **表名称：** 电商商品-多语言表
- **表名：** t_mal_goods_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_goods_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_goods_l |  | fpkid |
