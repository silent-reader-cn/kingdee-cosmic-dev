# 签字任务-plmdc_signature_task

## 签字任务-主表 t_plmdc_signature_task

- **表名称：** 签字任务-主表
- **表名：** t_plmdc_signature_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fsignaturefileid | 签字文件 | int8 | 64 |  | √ | 0 | 物理文件属性 plm_plmdc_physical_file |
| 4 | fbatchno | 批次号 | int8 | 64 |  | √ | 0 | 批次号 |
| 5 | fcreatetime | 创建时间 | int8 | 64 |  | √ | 0 | 创建时间 |
| 6 | fversionvalue | 版本的值 | varchar | 255 |  | √ | ' ' | 版本的值 |
| 7 | fsignmark | 签字标识 | varchar | 50 |  | √ | ' ' | 签字标识 |
| 8 | fdocid | 逻辑文档 | int8 | 64 |  | √ | 0 | 文档版本 plm_pdm_document_revision |
| 9 | fwfexecutionid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 10 | fsignorder | 签字序号 | int4 | 32 |  | √ | 0 | 签字序号 |
| 11 | ftimevalue | 时间的值 | varchar | 50 |  | √ | ' ' | 时间的值 |
| 12 | fsignvalue | 签字值 | varchar | 255 |  | √ | ' ' | 签字值 |
| 13 | fcontrolledsealsignvalue | 受控章的值 | varchar | 255 |  | √ | ' ' | 受控章的值 |
| 14 | fcontrolledsealmark | 受控章标识 | varchar | 50 |  | √ | ' ' | 受控章标识 |
| 15 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: wait :等待 ongoing :进行中 fail :失败 complete :转换完成 |
| 16 | fversionmark | 版本标记 | varchar | 50 |  | √ | ' ' | 版本标记 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fwfcodeid | 流程节点id | varchar | 50 |  | √ | ' ' | 流程节点id |
| 19 | ftaskid | 任务ID | varchar | 50 |  | √ | ' ' | 任务ID |
| 20 | fremarkmark | 意见标记 | varchar | 50 |  | √ | ' ' | 意见标记 |
| 21 | fremarkvalue | 意见的值 | varchar | 255 |  | √ | ' ' | 意见的值 |
| 22 | fsigntype | 签字类型 | int4 | 32 |  | √ | 0 | 签字类型 |
| 23 | ftimemark | 时间标记 | varchar | 50 |  | √ | ' ' | 时间标记 |
| 24 | fsourcefileid | 原文件 | int8 | 64 |  | √ | 0 | 物理文件属性 plm_plmdc_physical_file |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_signature_task |  | fid |
| 2 | idx_signature_task_taskid |  | ftaskid |
