# 影像队列表-task_imagequeue

## 影像队列表-主表 t_tk_imagequeue

- **表名称：** 影像队列表-主表
- **表名：** t_tk_imagequeue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 3 | fstate | 识别状态 | varchar | 50 |  | √ | ' ' | 识别状态 |
| 4 | fimageseq | 影像序号 | varchar | 20 |  | √ | ' ' | 影像序号 |
| 5 | fbillid | 单据id | varchar | 100 |  | √ | ' ' | 单据id |
| 6 | fcreatime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_imagequeue |  | fbillid |
| 2 | t_tk_imagequeue_pkey |  | fid |
| 3 | idx_ssc_imgque_fimagenumber |  | fimagenumber |
