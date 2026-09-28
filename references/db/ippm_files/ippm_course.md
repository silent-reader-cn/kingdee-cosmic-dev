# 课程-ippm_course

## 课程-主表 t_ippm_course

- **表名称：** 课程-主表
- **表名：** t_ippm_course

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 时长 | varchar | 50 |  | √ | ' ' | 时长 |
| 3 | fname | 课程名称 | varchar | 255 |  | √ | ' ' | 课程名称 |
| 4 | fcourseid | 课程ID | varchar | 50 |  | √ | ' ' | 课程ID |
| 5 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: video :视频 document :文档 html :图文 courseware :微课件 customization :定制课程 |
| 6 | fvideoid | 视频ID | varchar | 255 |  | √ | ' ' | 视频ID |
| 7 | fsourcetype | 资源类型 | varchar | 50 |  | √ | ' ' | 资源类型,枚举: LearningCourse :学习课程 |
| 8 | furl | 链接 | varchar | 2000 |  | √ | ' ' | 链接 |
| 9 | fcourselistid | 课程清单 | int8 | 64 |  | √ | 0 | [课程清单 ippm_courselist](../ippm_files/ippm_courselist.md) |
| 10 | fnumber | 课程编码 | varchar | 50 |  | √ | ' ' | 课程编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_course |  | fid |
| 2 | idx_ippm_course |  | fcourseid |
