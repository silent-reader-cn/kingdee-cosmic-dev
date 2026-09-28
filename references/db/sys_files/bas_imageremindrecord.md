# 影像超期提醒记录-bas_imageremindrecord

## 影像超期提醒记录-主表 t_bas_imageremindrecord

- **表名称：** 影像超期提醒记录-主表
- **表名：** t_bas_imageremindrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fimagenumber | 影像编码 | varchar | 100 |  | √ | ' ' | 影像编码 |
| 3 | fmessageid | 消息id | varchar | 100 |  | √ | ' ' | 消息id |
| 4 | fremindtime | 提醒次数 | varchar | 100 |  | √ | ' ' | 提醒次数 |
| 5 | flatestremind | 最近提醒日期 | timestamp | 0 |  |  | null | 最近提醒日期 |
| 6 | ffirstremind | 首次提醒时间 | timestamp | 0 |  |  | null | 首次提醒时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_imageremindrecord_pkey |  | fid |
| 2 | index_t_bas_imageremindrecord |  | fimagenumber |
