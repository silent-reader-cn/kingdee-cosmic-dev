# 浏览记录-mal_browsinghistory

## 浏览记录-主表 t_mal_browsinghistory

- **表名称：** 浏览记录-主表
- **表名：** t_mal_browsinghistory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 最近浏览时间 | timestamp | 0 |  |  | null | 最近浏览时间 |
| 3 | fnum | 当日浏览次数 | int4 | 32 |  | √ | 0 | 当日浏览次数 |
| 4 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fgoodsimg | 商品图片 | varchar | 255 |  | √ | ' ' | 商品图片 |
| 6 | fgoodsid | 商品 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 7 | fuserid | 浏览人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ftaxprice | 价格 | numeric | 23 | 10 | √ | 0 | 价格 |
| 9 | fgoodsstatus | 商品状态 | bpchar | 1 |  | √ | ' ' | 商品状态,枚举: 1 :无货 2 :不可售 3 :已下架 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_history_goodsid |  | fgoodsid |
| 2 | idx_mal_history_fuser_ftime |  | fuserid,ftime |
| 3 | pk_mal_browsinghistory |  | fid |
