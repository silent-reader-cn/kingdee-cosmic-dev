# 存货核算测试日志-cal_debuglog

## 存货核算测试日志-主表 t_cal_debuglog

- **表名称：** 存货核算测试日志-主表
- **表名：** t_cal_debuglog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftitle | 标题 | varchar | 255 |  | √ | ' ' | 标题 |
| 3 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 4 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_debuglog_pkey |  | fid |
| 2 | idx_cal_debuglog_ftitle |  | ftitle |
