# 指标库分录F7-src_indexentryf7

## 指标库分录F7-主表 t_src_indexentry

- **表名称：** 指标库分录F7-主表
- **表名：** t_src_indexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 指标ID | int8 | 64 |  | √ | 0 | 指标ID |
| 2 | fvaluefrom | 定量值从(大于等于) | numeric | 19 | 6 | √ | 0 | 定量值从(大于等于) |
| 3 | fvalueto | 定量值至(小于) | numeric | 19 | 6 | √ | 0 | 定量值至(小于) |
| 4 | fitemmaxscore | 最高得分(≤) | numeric | 23 | 10 | √ | 0 | 最高得分(≤) |
| 5 | fitem | 规则描述 | varchar | 1020 |  | √ | ' ' | 规则描述 |
| 6 | fitemvalue | 定性值 | varchar | 100 |  | √ | ' ' | 定性值 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fitemscore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fitemminscore | 最低得分(≥) | numeric | 23 | 10 | √ | 0 | 最低得分(≥) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_indexentry_id |  | fid |
| 2 | pk_src_indexentry |  | fentryid |
