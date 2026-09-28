# 答卷明细-ippm_paperdetail

## 答卷明细-主表 t_ippm_paperdetail

- **表名称：** 答卷明细-主表
- **表名：** t_ippm_paperdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpaperid | 答卷ID | varchar | 50 |  | √ | ' ' | 答卷ID |
| 3 | fquiztime | 答卷考试时间 | timestamp | 0 |  |  | null | 答卷考试时间 |
| 4 | fquizid | 考试明细ID | int8 | 64 |  | √ | 0 | 考试明细ID |
| 5 | fresult | 答卷结果 | varchar | 50 |  | √ | ' ' | 答卷结果,枚举: -1 :待考试 0 :不通过 1 :通过 |
| 6 | fscore | 答卷得分 | int4 | 32 |  | √ | 0 | 答卷得分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_paperdetail |  | fquizid |
| 2 | pk_t_ippm_paperdetail |  | fid |
