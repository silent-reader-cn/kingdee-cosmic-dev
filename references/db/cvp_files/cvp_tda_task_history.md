# 历史对比任务-cvp_tda_task_history

## 历史对比任务-主表 t_cvp_tda_comparison_task

- **表名称：** 历史对比任务-主表
- **表名：** t_cvp_tda_comparison_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fprogressinfo | 进度 | varchar | 200 |  |  | null | 进度 |
| 4 | fbillvalid | 是否有效 | varchar | 50 |  | √ | ' ' | 是否有效,枚举: 1 :有效 0 :无效 |
| 5 | fbillcomparedoc | 比较文档 | varchar | 255 |  |  | ' ' | 比较文档 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fdifnumber | 差异总数 | int8 | 64 |  | √ | 0 | 差异总数 |
| 8 | ftotalpage | 总页数 | int4 | 32 |  | √ | 0 | 总页数 |
| 9 | fvariationrate | 整体差异率 | numeric | 23 | 10 | √ | 0.0 | 整体差异率 |
| 10 | fbilloriginalimagespath | 原文档转图片地址 | varchar | 255 |  |  | null | 原文档转图片地址 |
| 11 | foriginaldoc | 原文档 | varchar | 255 |  |  | ' ' | 原文档 |
| 12 | fbilltdaresult | 差异分析结果 | text | 0 |  |  | ' ' | 差异分析结果 |
| 13 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 14 | fbusinessobj | 业务对象 | varchar | 255 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 15 | fbillstatus | 状态 | varchar | 255 |  |  | ' ' | 状态,枚举: running :比对中 success :比对完成 error :比对失败 cancel :取消任务 |
| 16 | fbillcomparedocpath | 比较文档地址 | varchar | 255 |  |  | ' ' | 比较文档地址 |
| 17 | fbillcompareimagespath | 比较文档转图片地址 | varchar | 255 |  |  | null | 比较文档转图片地址 |
| 18 | fplanname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 19 | fbillname | 单据名称 | varchar | 255 |  |  | ' ' | 单据名称 |
| 20 | fbillenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 21 | fbillcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 23 | fbilloriginaldocpath | 原文档地址 | varchar | 255 |  |  | ' ' | 原文档地址 |
| 24 | ftaskid | 任务ID | varchar | 255 |  | √ | ' ' | 任务ID |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_tda_task_2 |  | fbillid,fbillvalid |
| 2 | idx_cvp_tda_comparison_task |  | fbillno,fbillname |
| 3 | pk_t_cvp_tda_comparison_task |  | fentryid |
