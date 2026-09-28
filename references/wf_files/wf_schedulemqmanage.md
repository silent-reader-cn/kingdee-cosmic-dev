# MQ状态与后台调度-wf_schedulemqmanage

## MQ状态与后台调度-多语言表 t_wf_schedulemqmanage_l

- **表名称：** MQ状态与后台调度-多语言表
- **表名：** t_wf_schedulemqmanage_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fappname | 应用名称 | varchar | 200 |  | √ | ' ' | 应用名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_schedulemqmanage_l |  | fid,flocaleid |
| 2 | pk_wf_schedulemqmanage_l |  | fpkid |

---

## MQ状态与后台调度-主表 t_wf_schedulemqmanage

- **表名称：** MQ状态与后台调度-主表
- **表名：** t_wf_schedulemqmanage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrorcode | 错误码 | varchar | 200 |  | √ | ' ' | 错误码 |
| 3 | ferrorinfo | 错误信息 | varchar | 255 |  | √ | ' ' | 错误信息 |
| 4 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 5 | fstate | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: begin :开始 error :异常 complete :完成 |
| 6 | fparentid | 上级id | int8 | 64 |  | √ | 0 | 上级id |
| 7 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fappname | 应用名称 | varchar | 200 |  | √ | ' ' | 应用名称 |
| 9 | ferrortype | 错误类型 | varchar | 50 |  | √ | ' ' | 错误类型,枚举: scheduleError :后台调度结果异常 mqError :MQ状态异常 success :正常 |
| 10 | ferrorinfo_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 11 | fappid | 轻应用id | varchar | 50 |  | √ | ' ' | 轻应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_schedulemqmanage |  | fid |
| 2 | idx_wf_schemqmanage_startdate |  | fstartdate |
| 3 | idx_wf_schemqmanage_parentid |  | fparentid |
| 4 | idx_wf_schemqmanage_state |  | fstate |
