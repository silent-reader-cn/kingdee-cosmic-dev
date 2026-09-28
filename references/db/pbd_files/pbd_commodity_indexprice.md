# 大宗商品指标价格单-pbd_commodity_indexprice

## 大宗商品指标价格单-主表 t_pbd_commodity_indiprice

- **表名称：** 大宗商品指标价格单-主表
- **表名：** t_pbd_commodity_indiprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatadate | 数据日期 | timestamp | 0 |  |  | null | 数据日期 |
| 3 | findexcode | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 4 | fdatavalue | 数据值 | numeric | 23 | 10 | √ | 0 | 数据值 |
| 5 | fpublishtime | 数据发布时间戳 | int8 | 64 |  | √ | 0 | 数据发布时间戳 |
| 6 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 我的钢铁网 :我的钢铁网 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_commodity_indiprice_se |  | findexcode,fdatasource |
| 2 | pk_pbd_commodity_indiprice |  | fid |
| 3 | idx_pbd_commodity_indiprice_de |  | fdatadate |
