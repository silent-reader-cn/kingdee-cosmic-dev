# 导出任务-fea_export_task

## 导出任务-主表 t_fea_exporttask

- **表名称：** 导出任务-主表
- **表名：** t_fea_exporttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fbookid | 账簿类型 | int8 | 64 |  | √ | 0 | 账簿类型 bd_accountbookstype |
| 4 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | ftotalprocess | 任务进度 | numeric | 19 | 6 | √ | 0 | 任务进度 |
| 6 | fperiodtypeid | 会计期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fendperiodid | 结束期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 9 | ftaskstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :等待 B :进行中 C :已完成 D :出错 E :终止 |
| 10 | fbeginperiodid | 开始期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 11 | fnumber | 任务编码 | varchar | 255 |  | √ | ' ' | 任务编码 |
| 12 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | fexportplanid | 导出方案 | int8 | 64 |  | √ | 0 | 导出方案 fea_plan |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fea_exporttask_num |  | fnumber |
| 2 | pk_t_fea_exporttask |  | fid |

---

## 子单据体-子表 t_fea_tasksubentry

- **表名称：** 子单据体-子表
- **表名：** t_fea_tasksubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fstructid | 数据结构 | int8 | 64 |  | √ | 0 | 数据结构 fea_datastructure |
| 2 | ftaskdetailstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :等待 B :进行中 C :已完成 D :出错 |
| 3 | fendindex | 结束行 | int4 | 32 |  | √ | 0 | 结束行 |
| 4 | ftmpfileurl | 临时文件地址 | varchar | 500 |  | √ | ' ' | 临时文件地址 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffilesize | 文件大小(字节) | int4 | 32 |  | √ | 0 | 文件大小(字节) |
| 7 | ferrortext | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fbeginindex | 起始行 | int4 | 32 |  | √ | 0 | 起始行 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | ferrortext_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fea_tasksubentry |  | fdetailid |
| 2 | idx_fea_tasksubentry |  | fentryid |

---

## 任务明细-子表 t_fea_exporttaskentry

- **表名称：** 任务明细-子表
- **表名：** t_fea_exporttaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrorinfo | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fzipfileurl | 文件下载地址 | varchar | 500 |  | √ | ' ' | 文件下载地址 |
| 5 | ftaskendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffileexpiretime | 文件过期时间 | timestamp | 0 |  |  | null | 文件过期时间 |
| 8 | fsubtaskstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :等待 B :进行中 C :已完成 D :出错 E :终止 |
| 9 | fstandardentryid | 文件标准分录ID | int8 | 64 |  | √ | 0 | 文件标准分录ID |
| 10 | fstructid | 数据结构 | int8 | 64 |  | √ | 0 | 数据结构 fea_datastructure |
| 11 | fsubprocess | 进度 | numeric | 16 | 9 | √ | 0 | 进度 |
| 12 | fzipfilesize | 文件大小(字节) | int8 | 64 |  | √ | 0 | 文件大小(字节) |
| 13 | ftaskstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 14 | fsrvinstance | 实例节点 | varchar | 255 |  | √ | ' ' | 实例节点 |
| 15 | fzipname | 打包文件名 | varchar | 255 |  | √ | ' ' | 打包文件名 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | ferrorinfo_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fea_exporttaskentry |  | fid |
| 2 | pk_t_fea_exporttaskentry |  | fentryid |
