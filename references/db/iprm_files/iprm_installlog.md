# 内容包加载日志-iprm_installlog

## 内容包加载日志-主表 t_iprm_installlog

- **表名称：** 内容包加载日志-主表
- **表名：** t_iprm_installlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finstallmsg | 安装日志 | varchar | 255 |  | √ | ' ' | 安装日志 |
| 3 | fsubfailsize | 子包失败个数 | int4 | 32 |  | √ | 0 | 子包失败个数 |
| 4 | finstallmsg_tag | 安装日志_详情 | text | 0 |  |  | null | 安装日志_详情 |
| 5 | flogno | 日志编号 | varchar | 30 |  | √ | ' ' | 日志编号 |
| 6 | fsubsuccesssize | 子包成功个数 | int4 | 32 |  | √ | 0 | 子包成功个数 |
| 7 | fstarttime | 安装开始时间 | timestamp | 0 |  |  | null | 安装开始时间 |
| 8 | fstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 1 :成功 2 :失败 3 :部分成功 |
| 9 | fduration | 安装时长 | varchar | 50 |  | √ | ' ' | 安装时长 |
| 10 | flogcreaterid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fpid | 内容包编码 | varchar | 50 |  | √ | ' ' | 内容包编码 |
| 12 | fpname | 内容包名称 | varchar | 50 |  |  | ' ' | 内容包名称 |
| 13 | fendtime | 安装结束时间 | timestamp | 0 |  |  | null | 安装结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iprm_installlog |  | fid |
| 2 | idx_iprm_installlog_logno |  | flogno |
| 3 | idx_iprm_installlog_pid |  | fpid |

---

## 单据体-子表 t_iprm_installlogentry

- **表名称：** 单据体-子表
- **表名：** t_iprm_installlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubinstallmsg_tag | 子包安装日志_详情 | text | 0 |  |  | null | 子包安装日志_详情 |
| 3 | fsubinstallmsg | 子包安装日志 | varchar | 255 |  | √ | ' ' | 子包安装日志 |
| 4 | fsubduration | 执行时长 | varchar | 100 |  | √ | ' ' | 执行时长 |
| 5 | fsubname | 业务对象标识 | varchar | 100 |  | √ | ' ' | 业务对象标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsubobj | 业务对象名称 | varchar | 100 |  | √ | ' ' | 业务对象名称 |
| 8 | fsubtitle | 子文件名 | varchar | 100 |  | √ | ' ' | 子文件名 |
| 9 | ffailcount | 失败条数 | int4 | 32 |  | √ | 0 | 失败条数 |
| 10 | fsubinstallstarttime | 加载日期 | timestamp | 0 |  |  | null | 加载日期 |
| 11 | fsubtype | 数据类别 | varchar | 100 |  | √ | ' ' | 数据类别 |
| 12 | fsubstatus | 子包执行状态 | bpchar | 1 |  | √ | ' ' | 子包执行状态,枚举: 1 :成功 2 :失败 3 :部分成功 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fsuccesscount | 成功条数 | int4 | 32 |  | √ | 0 | 成功条数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iprm_installlogentry |  | fsubname |
| 2 | pk_t_iprm_installlogentry |  | fentryid |
