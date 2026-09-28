# 金蝶多模态提取大模型任务-cvp_ie_kdllm_task

## 金蝶多模态提取大模型任务-主表 t_cvp_kdllm_task_history

- **表名称：** 金蝶多模态提取大模型任务-主表
- **表名：** t_cvp_kdllm_task_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | ftasktype | 任务类型 | varchar | 10 |  | √ | ' ' | 任务类型,枚举: ie :信息提取 cls :分类 |
| 6 | fresult | 请求结果 | varchar | 255 |  | √ | ' ' | 请求结果 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 9 | frequestbody | 请求体 | varchar | 255 |  | √ | ' ' | 请求体 |
| 10 | frequestbody_tag | 请求体_详情 | text | 0 |  |  | null | 请求体_详情 |
| 11 | fresult_tag | 请求结果_详情 | text | 0 |  |  | null | 请求结果_详情 |
| 12 | fisstream | 流式任务 | bpchar | 1 |  | √ | '0' | 流式任务 |
| 13 | fcallbackstatus | 回调状态 | bpchar | 1 |  | √ | '0' | 回调状态 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftaskstatus | 任务状态 | varchar | 30 |  | √ | ' ' | 任务状态,枚举: create :新建 running :执行中 error :失败 success :成功 |
| 16 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fformid | 单据对象 | varchar | 50 |  | √ | ' ' | 单据对象 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ie_kdllm_taskid_formid |  | ftaskid,fformid |
| 2 | pk_cvp_kdllm_task_history |  | fid |
