# 投资资产处置收益调整底稿-tccit_asset_dispose_sum

## 投资资产处置收益调整底稿-主表 t_tccit_asset_dispose_sum

- **表名称：** 投资资产处置收益调整底稿-主表
- **表名：** t_tccit_asset_dispose_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fkjqrczsdss | 会计确认的处置所得或损失 | numeric | 23 | 10 | √ | 0.0000000000 | 会计确认的处置所得或损失 |
| 4 | fkjqrczsr | 会计确认的处置收入 | numeric | 23 | 10 | √ | 0.0000000000 | 会计确认的处置收入 |
| 5 | fczzczmjz | 处置资产的账面价值 | numeric | 23 | 10 | √ | 0.0000000000 | 处置资产的账面价值 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | fswjsczsdss | 税务计算的处置所得或损失 | numeric | 23 | 10 | √ | 0.0000000000 | 税务计算的处置所得或损失 |
| 8 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fczzcjsjc | 处置资产的计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 处置资产的计税基础 |
| 10 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 13 | fssjsczsr | 税收计算的处置收入 | numeric | 23 | 10 | √ | 0.0000000000 | 税收计算的处置收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_asset_dispose_sum |  | forgid,fskssqq,fskssqz,fitemtype |
| 2 | pk_tccit_asset_dispose_sum |  | fid |
