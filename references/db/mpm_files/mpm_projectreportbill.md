# 项目汇报单-mpm_projectreportbill

## 项目汇报单-分表 t_mpm_taskreport_e

- **表名称：** 项目汇报单-分表
- **表名：** t_mpm_taskreport_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustfield031 | 自定义复选框001 | bpchar | 1 |  | √ | '0' | 自定义复选框001 |
| 3 | fcustfield030 | 自定义日期005 | timestamp | 0 |  |  | null | 自定义日期005 |
| 4 | fcustfield011 | 自定义文本011 | varchar | 80 |  | √ | ' ' | 自定义文本011 |
| 5 | fcustfield033 | 自定义复选框003 | bpchar | 1 |  | √ | '0' | 自定义复选框003 |
| 6 | fcustfield010 | 自定义文本010 | varchar | 80 |  | √ | ' ' | 自定义文本010 |
| 7 | fcustfield032 | 自定义复选框002 | bpchar | 1 |  | √ | '0' | 自定义复选框002 |
| 8 | fcustfield017 | 自定义文本017 | varchar | 80 |  | √ | ' ' | 自定义文本017 |
| 9 | fcustfield016 | 自定义文本016 | varchar | 80 |  | √ | ' ' | 自定义文本016 |
| 10 | fcustfield019 | 自定义文本019 | varchar | 80 |  | √ | ' ' | 自定义文本019 |
| 11 | fcustfield018 | 自定义文本018 | varchar | 80 |  | √ | ' ' | 自定义文本018 |
| 12 | fcustfield013 | 自定义文本013 | varchar | 80 |  | √ | ' ' | 自定义文本013 |
| 13 | fcustfield035 | 自定义复选框005 | bpchar | 1 |  | √ | '0' | 自定义复选框005 |
| 14 | fcustfield012 | 自定义文本012 | varchar | 80 |  | √ | ' ' | 自定义文本012 |
| 15 | fcustfield034 | 自定义复选框004 | bpchar | 1 |  | √ | '0' | 自定义复选框004 |
| 16 | fcustfield015 | 自定义文本015 | varchar | 80 |  | √ | ' ' | 自定义文本015 |
| 17 | fcustfield014 | 自定义文本014 | varchar | 80 |  | √ | ' ' | 自定义文本014 |
| 18 | fcustfield020 | 自定义文本020 | varchar | 80 |  | √ | ' ' | 自定义文本020 |
| 19 | fcustfield022 | 自定义数字002 | numeric | 23 | 10 | √ | 0 | 自定义数字002 |
| 20 | fcustfield021 | 自定义数字001 | numeric | 23 | 10 | √ | 0 | 自定义数字001 |
| 21 | fcustfield009 | 自定义文本009 | varchar | 80 |  | √ | ' ' | 自定义文本009 |
| 22 | fcustfield006 | 自定义文本006 | varchar | 80 |  | √ | ' ' | 自定义文本006 |
| 23 | fcustfield028 | 自定义日期003 | timestamp | 0 |  |  | null | 自定义日期003 |
| 24 | fcustfield005 | 自定义文本005 | varchar | 80 |  | √ | ' ' | 自定义文本005 |
| 25 | fcustfield027 | 自定义日期002 | timestamp | 0 |  |  | null | 自定义日期002 |
| 26 | fcustfield008 | 自定义文本008 | varchar | 80 |  | √ | ' ' | 自定义文本008 |
| 27 | fcustfield007 | 自定义文本007 | varchar | 80 |  | √ | ' ' | 自定义文本007 |
| 28 | fcustfield029 | 自定义日期004 | timestamp | 0 |  |  | null | 自定义日期004 |
| 29 | fcustfield002 | 自定义文本002 | varchar | 80 |  | √ | ' ' | 自定义文本002 |
| 30 | fcustfield024 | 自定义数字004 | numeric | 23 | 10 | √ | 0 | 自定义数字004 |
| 31 | fcustfield001 | 自定义文本001 | varchar | 80 |  | √ | ' ' | 自定义文本001 |
| 32 | fcustfield023 | 自定义数字003 | numeric | 23 | 10 | √ | 0 | 自定义数字003 |
| 33 | fcustfield004 | 自定义文本004 | varchar | 80 |  | √ | ' ' | 自定义文本004 |
| 34 | fcustfield026 | 自定义日期001 | timestamp | 0 |  |  | null | 自定义日期001 |
| 35 | fcustfield003 | 自定义文本003 | varchar | 80 |  | √ | ' ' | 自定义文本003 |
| 36 | fcustfield025 | 自定义数字005 | numeric | 23 | 10 | √ | 0 | 自定义数字005 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskreport_e |  | fid |

---

## 项目汇报单-分表 t_mpm_taskreport_a

- **表名称：** 项目汇报单-分表
- **表名：** t_mpm_taskreport_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskprodes_tag | 任务进展描述_详情 | text | 0 |  |  | ' ' | 任务进展描述_详情 |
| 3 | ftaskprodes | 任务进展描述 | varchar | 255 |  | √ | ' ' | 任务进展描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_taskreport_a |  | fid |
| 2 | idx_mpm_taskreport_a |  | fid |

---

## 项目汇报单-主表 t_mpm_taskreport

- **表名称：** 项目汇报单-主表
- **表名：** t_mpm_taskreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | factualenddate | 实际结束时间 | timestamp | 0 |  |  | null | 实际结束时间 |
| 6 | freporthours | freporthours | numeric | 23 | 10 | √ | 0 |  |
| 7 | factualstartdate | 实际开始时间 | timestamp | 0 |  |  | null | 实际开始时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | freportdate | 汇报日期 | timestamp | 0 |  |  | null | 汇报日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fplanhours | fplanhours | numeric | 23 | 10 | √ | 0 |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fschedule | 累计进度(%) | numeric | 23 | 10 | √ | 0 | 累计进度(%) |
| 14 | fcurreporthours | 本次汇报工时(小时) | numeric | 23 | 10 | √ | 0 | 本次汇报工时(小时) |
| 15 | ftaskid | 项目任务 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 16 | freportuserid | 汇报用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_taskreport |  | fid |
| 2 | idx_mpm_taskreport_fbillno |  | fbillno |
| 3 | pk_mpm_taskreport |  | fid |
