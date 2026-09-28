# 抵扣应纳税所得额调整明细-tccit_dkynssde_ajust

## 抵扣应纳税所得额调整明细-主表 t_tccit_dkynssde_ajust

- **表名称：** 抵扣应纳税所得额调整明细-主表
- **表名：** t_tccit_dkynssde_ajust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginal | 原数值 | numeric | 23 | 10 | √ | 0.0000000000 | 原数值 |
| 3 | fadjust | 调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整金额 |
| 4 | fajustnum | 调整编码 | varchar | 50 |  | √ | ' ' | 调整编码 |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | fresult | 结果值 | numeric | 23 | 10 | √ | 0.0000000000 | 结果值 |
| 8 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dkynssde_ajust |  | fid |
| 2 | idx_tccit_dkynssde_ajust |  | forgid,fskssqq,fskssqz |
