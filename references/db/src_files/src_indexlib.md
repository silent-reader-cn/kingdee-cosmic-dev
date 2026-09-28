# 指标库F7-src_indexlib

## 指标库F7-主表 t_src_indexentry

- **表名称：** 指标库F7-主表
- **表名：** t_src_indexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 指标ID | int8 | 64 |  | √ | 0 | 指标ID |
| 2 | fvaluefrom | 定量值从 | numeric | 19 | 6 | √ | 0 | 定量值从 |
| 3 | fvalueto | 定量值至 | numeric | 19 | 6 | √ | 0 | 定量值至 |
| 4 | fitemmaxscore | fitemmaxscore | numeric | 23 | 10 | √ | 0 |  |
| 5 | fitem | 评分规则描述 | varchar | 1020 |  | √ | ' ' | 评分规则描述 |
| 6 | fitemvalue | 定性值 | varchar | 100 |  | √ | ' ' | 定性值 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fitemscore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |
| 10 | fentryid | 明细分录ID | int8 | 64 |  | √ | 0 | 明细分录ID |
| 11 | fitemminscore | fitemminscore | numeric | 23 | 10 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_indexentry_id |  | fid |
| 2 | pk_src_indexentry |  | fentryid |
