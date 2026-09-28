# 共享异常记录-task_recordexcept

## 共享异常记录-多语言表 t_tk_recordexcept_l

- **表名称：** 共享异常记录-多语言表
- **表名：** t_tk_recordexcept_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | ssc_recoexcep_l_idx |  | fid,flocaleid |
| 2 | t_tk_recordexcept_l_pkey |  | fpkid |

---

## 共享异常记录-主表 t_tk_recordexcept

- **表名称：** 共享异常记录-主表
- **表名：** t_tk_recordexcept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fretrytime | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 3 | fexceptstack_tag | 异常堆栈_详情 | text | 0 |  |  | null | 异常堆栈_详情 |
| 4 | fretry | 是否重试 | bpchar | 1 |  | √ | '0' | 是否重试 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fappid | 应用 | varchar | 50 |  | √ | ' ' | 应用 |
| 7 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbusinessid | 业务单据ID | int8 | 64 |  |  | null | 业务单据ID |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fexceptstack | 异常堆栈 | varchar | 1000 |  | √ | ' ' | 异常堆栈 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fexceptmethod | 异常出错方法 | varchar | 255 |  | √ | ' ' | 异常出错方法 |
| 14 | fexceptdes | 异常信息 | varchar | 1000 |  | √ | ' ' | 异常信息 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fipaddress | IP地址 | varchar | 50 |  |  | null | IP地址 |
| 17 | fstatuscode | 响应状态码 | varchar | 10 |  |  | null | 响应状态码 |
| 18 | fexceptparam | 请求参数 | varchar | 255 |  | √ | ' ' | 请求参数 |
| 19 | fbusinessparam_tag | 业务参数_详情 | text | 0 |  |  | null | 业务参数_详情 |
| 20 | fduration | 响应时间 | int8 | 64 |  | √ | 0 | 响应时间 |
| 21 | ftype | 日志类型 | varchar | 50 |  |  | null | 日志类型 |
| 22 | fbusinessparam | 业务参数 | varchar | 1000 |  | √ | ' ' | 业务参数 |
| 23 | fbusinessvoucher | 业务单据表 | varchar | 50 |  | √ | ' ' | 业务单据表 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_recordexcept_pkey |  | fid |
| 2 | ssc_recoexcept_idx |  | fnumber |
