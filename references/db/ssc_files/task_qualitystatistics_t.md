# 任务质量统计中间表-task_qualitystatistics_t

## 任务质量统计中间表-主表 t_tk_qualitystatistics

- **表名称：** 任务质量统计中间表-主表
- **表名：** t_tk_qualitystatistics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperson | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 4 | ftaskcount | 处理总数 | int8 | 64 |  | √ | 0 | 处理总数 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fssc | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | funpasscount | 批退数 | int8 | 64 |  | √ | 0 | 批退数 |
| 9 | fexceptioncount | 异常数 | int8 | 64 |  | √ | 0 | 异常数 |
| 10 | fdaterange | 日期范围 | int8 | 64 |  | √ | 0 | 日期范围 |
| 11 | fpendingcount | 挂起数 | int8 | 64 |  | √ | 0 | 挂起数 |
| 12 | fbilltype | 业务单据 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |
| 13 | freturncount | 退回重扫数 | int8 | 64 |  | √ | 0 | 退回重扫数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_quality_billtype |  | fbilltype |
| 2 | t_tk_qualitystatistics_pkey |  | fid |
| 3 | idx_tk_quality_person |  | fperson |
| 4 | idx_tk_quality_daterange |  | fdaterange |
| 5 | idx_tk_quality_tasktype |  | ftasktype |
| 6 | idx_tk_quality_org |  | forg |
| 7 | idx_tk_quality_ssc |  | fssc |
