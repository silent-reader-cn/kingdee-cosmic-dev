# 考勤同步行程明细表-er_syntripentry

## 考勤同步行程明细表-主表 t_er_syntripentry

- **表名称：** 考勤同步行程明细表-主表
- **表名：** t_er_syntripentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcitynumber | 出差城市编码 | varchar | 50 |  | √ | ' ' | 出差城市编码 |
| 3 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcityname | 出差城市名称 | varchar | 50 |  | √ | ' ' | 出差城市名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_syntripentry |  | fid |
| 2 | idx_er_syntripentry_fcitynum |  | fcitynumber |
