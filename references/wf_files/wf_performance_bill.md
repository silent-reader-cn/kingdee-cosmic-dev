# 工作流性能测试单据-wf_performance_bill

## 工作流性能测试单据-主表 t_wf_performancebill

- **表名称：** 工作流性能测试单据-主表
- **表名：** t_wf_performancebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核通过 E :审核不通过 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | freason | 事由 | varchar | 100 |  | √ | ' ' | 事由 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: visit :拜访客户 support :支持项目 study :知识培训 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 12 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 13 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_performancebill_pkey |  | fid |
| 2 | idx_wf_performancebill_number |  | fbillno |
