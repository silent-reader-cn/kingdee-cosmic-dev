# 学习明细-ippm_learningdetail

## 学习明细-主表 t_ippm_learningdetail

- **表名称：** 学习明细-主表
- **表名：** t_ippm_learningdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 完成状态 | varchar | 50 |  | √ | ' ' | 完成状态,枚举: unstart :未开始 learning :学习中 complete :已完成 |
| 3 | flastlearntime | 最近一次学习时间 | timestamp | 0 |  |  | null | 最近一次学习时间 |
| 4 | fcourseid | 课程 | int8 | 64 |  | √ | 0 | [课程 ippm_course](../ippm_files/ippm_course.md) |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcompletetime | 学习完成时间 | timestamp | 0 |  |  | null | 学习完成时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_learningdetail_course |  | fcourseid |
| 2 | idx_ippm_learningdetail_user |  | fuserid |
| 3 | pk_t_ippm_learningdetail |  | fid |
