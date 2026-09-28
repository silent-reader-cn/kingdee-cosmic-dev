# 信息提取大模型提取历史记录-cvp_ie_llm_history

## 信息提取大模型提取历史记录-主表 t_cvp_ie_llm_history

- **表名称：** 信息提取大模型提取历史记录-主表
- **表名：** t_cvp_ie_llm_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fllmtaskid | 大模型任务id | varchar | 50 |  |  | null | 大模型任务id |
| 3 | fextractstatus | 状态 | varchar | 50 |  |  | null | 状态,枚举: running :提取中 success :提取完成 cancel :取消任务 error :提取失败 |
| 4 | ffirstextract | 第一次提取 | bpchar | 1 |  |  | '1' | 第一次提取 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | freqparam_tag | 请求大模型参数_详情 | text | 0 |  |  | ' ' | 请求大模型参数_详情 |
| 7 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fieplan | 信息提取方案 | int8 | 64 |  |  | null | [文档信息提取 cvp_ie_mouldplan](../cvp_files/cvp_ie_mouldplan.md) |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | flayoutdata_tag | 复杂文档提取结果_详情 | text | 0 |  |  | null | 复杂文档提取结果_详情 |
| 12 | fpageinfo | 页码信息结果 | varchar | 255 |  |  | null | 页码信息结果 |
| 13 | frequesttask | 是否有效 | bpchar | 1 |  |  | '1' | 是否有效 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fllmresult | 大模型提取结果 | varchar | 255 |  |  | null | 大模型提取结果 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | flayoutdata | 复杂文档提取结果 | varchar | 255 |  |  | null | 复杂文档提取结果 |
| 18 | fllmresult_tag | 大模型提取结果_详情 | text | 0 |  |  | null | 大模型提取结果_详情 |
| 19 | fiehistory | 文档提取历史记录id | varchar | 50 |  |  | null | 文档提取历史记录id |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 22 | freqparam | 请求大模型参数 | varchar | 80 |  |  | ' ' | 请求大模型参数 |
| 23 | fpageinfo_tag | 页码信息结果_详情 | text | 0 |  |  | null | 页码信息结果_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_llm_history |  | fid |
| 2 | idx_t_cvp_ie_llm_history |  | fbillno,fiehistory,fllmtaskid |
