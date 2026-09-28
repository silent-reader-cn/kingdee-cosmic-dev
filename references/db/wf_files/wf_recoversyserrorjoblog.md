# 系统异常流程自动恢复记录-wf_recoversyserrorjoblog

## 系统异常流程自动恢复记录-主表 t_wf_recoversyserrlog

- **表名称：** 系统异常流程自动恢复记录-主表
- **表名：** t_wf_recoversyserrlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 3 | fduration | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 4 | frecoverdetails | 恢复详情 | varchar | 255 |  | √ | ' ' | 恢复详情 |
| 5 | ffixtotal | 修复总数 | int8 | 64 |  | √ | 0 | 修复总数 |
| 6 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | ferrortype | 错误类型 | varchar | 50 |  | √ | ' ' | 错误类型,枚举: syserror :调度及基础组件异常 |
| 8 | frecoverdetails_tag | 恢复详情_详情 | text | 0 |  |  | null | 恢复详情_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_recoversyserrlog |  | fid |
| 2 | idx_wf_recovsyserrlog_enddate |  | fenddate |
| 3 | idx_wf_recovsyserrlog_stadate |  | fstartdate |
