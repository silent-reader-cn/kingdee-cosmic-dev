# 学习进度-ippm_learningrecord

## 学习进度-主表 t_ippm_learningrecord

- **表名称：** 学习进度-主表
- **表名：** t_ippm_learningrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funstart | 未开始 | int4 | 32 |  | √ | 0 | 未开始 |
| 3 | ftotalquiz | 总考试数 | int4 | 32 |  | √ | 0 | 总考试数 |
| 4 | fcompletequiz | 考试完成数 | int4 | 32 |  | √ | 0 | 考试完成数 |
| 5 | fcomplete | 已完成 | int4 | 32 |  | √ | 0 | 已完成 |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ftotal | 总课程数 | int4 | 32 |  | √ | 0 | 总课程数 |
| 9 | fquizpassrate | 考试完成率 | numeric | 23 | 10 | √ | 0 | 考试完成率 |
| 10 | flearning | 学习中 | int4 | 32 |  | √ | 0 | 学习中 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_learningrecord |  | fuserid |
| 2 | pk_t_ippm_learningrecord |  | fid |
