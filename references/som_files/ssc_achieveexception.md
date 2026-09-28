# 异常监控补偿-ssc_achieveexception

## 异常监控补偿-主表 t_tk_achieveexception

- **表名称：** 异常监控补偿-主表
- **表名：** t_tk_achieveexception

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | frecalstatus | 重算状态 | bpchar | 1 |  | √ | ' ' | 重算状态,枚举: 0 :成功 1 :失败 |
| 6 | frecalculation | 重算次数 | int4 | 32 |  | √ | 0 | 重算次数 |
| 7 | flogdetail_tag | 详细日志_详情 | text | 0 |  |  | ' ' | 详细日志_详情 |
| 8 | fachievebasedata | 绩效底表 | bpchar | 1 |  | √ | ' ' | 绩效底表,枚举: 1 :线上工作量统计表 3 :共享任务时效质量统计表 4 :共享人员在岗时长统计表 |
| 9 | flogdetail | 详细日志 | varchar | 2000 |  | √ | ' ' | 详细日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_achieveexception |  | fid |
| 2 | idx_tk_achieveexception |  | fsscid,fcreatedate |
