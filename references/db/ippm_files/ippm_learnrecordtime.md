# 学习记录调用时间-ippm_learnrecordtime

## 学习记录调用时间-主表 t_ippm_learnrecordtime

- **表名称：** 学习记录调用时间-主表
- **表名：** t_ippm_learnrecordtime

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 调用类型 | varchar | 50 |  | √ | ' ' | 调用类型,枚举: learn :学习课程 quiz :考试测验 |
| 3 | fuid | uid | varchar | 50 |  | √ | ' ' | uid |
| 4 | fcourselistid | 课程清单 | int8 | 64 |  | √ | 0 | [课程清单 ippm_courselist](../ippm_files/ippm_courselist.md) |
| 5 | finvoketime | 调用时间 | timestamp | 0 |  |  | null | 调用时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_learnrecordtime |  | fid |
| 2 | idx_ippm_learnrecordtime |  | fcourselistid |
