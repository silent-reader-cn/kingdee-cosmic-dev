# 课程清单-ippm_courselist

## 课程清单-主表 t_ippm_courselist

- **表名称：** 课程清单-主表
- **表名：** t_ippm_courselist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fquizqualification | 测试资格系数 | numeric | 23 | 10 | √ | 0 | 测试资格系数 |
| 3 | fname | 课程清单名称 | varchar | 50 |  | √ | ' ' | 课程清单名称 |
| 4 | fexistquiz | 是否包含试题 | varchar | 1 |  | √ | '0' | 是否包含试题 |
| 5 | fquizid | 试题ID | varchar | 50 |  | √ | ' ' | 试题ID |
| 6 | fcourselistid | 课程清单ID | varchar | 50 |  | √ | ' ' | 课程清单ID |
| 7 | fnumber | 课程清单编码 | varchar | 50 |  | √ | ' ' | 课程清单编码 |
| 8 | fdesc | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_courselist |  | fid |
| 2 | idx_ippm_courselist |  | fcourselistid |
