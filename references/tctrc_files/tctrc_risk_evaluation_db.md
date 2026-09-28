# 风险评价表-tctrc_risk_evaluation_db

## 风险评价表-主表 t_tctrc_risk_evaluation

- **表名称：** 风险评价表-主表
- **表名：** t_tctrc_risk_evaluation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :指标 |
| 4 | fstarlevel | 星级 | int8 | 64 |  | √ | 0 | 星级 |
| 5 | fadvice | 建议 | varchar | 100 |  | √ | ' ' | 建议 |
| 6 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fadvicetag | 建议标签 | varchar | 100 |  | √ | ' ' | 建议标签 |
| 8 | fnumber | 指标编号 | varchar | 100 |  | √ | ' ' | 指标编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_evaluation |  | ftype,fnumber |
| 2 | t_tctrc_risk_evaluation_pkey |  | fid |
