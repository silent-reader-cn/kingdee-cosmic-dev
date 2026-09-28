# 要货订单数据唯一表-ocbsoc_saleorderunique

## 要货订单数据唯一表-主表 t_ocbsoc_orderunique

- **表名称：** 要货订单数据唯一表-主表
- **表名：** t_ocbsoc_orderunique

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuuid | 数据唯一ID | varchar | 36 |  | √ | ' ' | 数据唯一ID |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocbsoc_orderunique_fuuid |  | fuuid |
| 2 | pk_ocbsoc_orderunique |  | fid |
