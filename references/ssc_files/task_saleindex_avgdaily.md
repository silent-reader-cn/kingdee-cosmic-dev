# 业务员首页日均任务处理情况-task_saleindex_avgdaily

## 业务员首页日均任务处理情况-主表 t_tk_avgdaily

- **表名称：** 业务员首页日均任务处理情况-主表
- **表名：** t_tk_avgdaily

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fisquality | 是否质检任务 | bpchar | 1 |  | √ | ' ' | 是否质检任务 |
| 4 | fnormalnum | 正常任务数 | int8 | 64 |  | √ | 0 | 正常任务数 |
| 5 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fdate | 完成日期 | timestamp | 0 |  |  | null | 完成日期 |
| 7 | fexpirenum | 超期任务数 | int8 | 64 |  | √ | 0 | 超期任务数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_avgdaily_date |  | fdate |
| 2 | t_tk_avgdaily_pkey |  | fid |
| 3 | index_ssc_avgdaily_user |  | fuser |
