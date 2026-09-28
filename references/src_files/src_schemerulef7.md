# 评分规则F7-src_schemerulef7

## 评分规则F7-主表 t_src_schemerule

- **表名称：** 评分规则F7-主表
- **表名：** t_src_schemerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvaluefrom | 定量值从(大于等于) | numeric | 23 | 10 | √ | 0 | 定量值从(大于等于) |
| 2 | fvalueto | 定量值至(小于) | numeric | 23 | 10 | √ | 0 | 定量值至(小于) |
| 3 | fitemmaxscore | 最高得分(≤) | numeric | 23 | 10 | √ | 0 | 最高得分(≤) |
| 4 | fitem | 规则描述 | varchar | 510 |  | √ | ' ' | 规则描述 |
| 5 | fitemvalue | 定性值 | varchar | 50 |  | √ | ' ' | 定性值 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fitemscore | 得分 | numeric | 23 | 10 | √ | 0 | 得分 |
| 10 | fentryid | 评分指标 | int8 | 64 |  | √ | 0 | 评分指标F7 src_indexf7 |
| 11 | fitemminscore | 最低得分(≥) | numeric | 23 | 10 | √ | 0 | 最低得分(≥) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_src_schemerule_eid |  | fentryid |
| 2 | pk_src_schemerule |  | fdetailid |
