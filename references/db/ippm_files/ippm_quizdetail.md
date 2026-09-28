# 考试明细-ippm_quizdetail

## 考试明细-主表 t_ippm_quizdetail

- **表名称：** 考试明细-主表
- **表名：** t_ippm_quizdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbestpaperid | 最好答卷 | int8 | 64 |  | √ | 0 | [答卷明细 ippm_paperdetail](../ippm_files/ippm_paperdetail.md) |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcourselistid | 课程清单 | int8 | 64 |  | √ | 0 | [课程清单 ippm_courselist](../ippm_files/ippm_courselist.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_quizdetail |  | fcourselistid |
| 2 | pk_t_ippm_quizdetail |  | fid |
