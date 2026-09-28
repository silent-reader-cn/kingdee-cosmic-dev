# 科目日志-ict_pullacctdetaillog

## 科目日志-主表 t_ict_pullacctdetaillog

- **表名称：** 科目日志-主表
- **表名：** t_ict_pullacctdetaillog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 执行结果 | bpchar | 1 |  | √ | ' ' | 执行结果,枚举: 1 :成功 2 :失败 |
| 3 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fvchnumber | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 8 | fexecdetail | 执行详情 | varchar | 500 |  | √ | ' ' | 执行详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ict_pullacctdetaillog |  | fid |
| 2 | idx_ict_pullacctdetaillog_sc |  | fstatus,fcreatetime |
