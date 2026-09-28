# 处理意见单据-tctrc_handle_entity

## 处理意见单据-主表 t_tctrc_handle_entity

- **表名称：** 处理意见单据-主表
- **表名：** t_tctrc_handle_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 3 | ftype | 处理类型 | varchar | 30 |  | √ | ' ' | 处理类型,枚举: sdjs :手动计算 rgcl :人工处理 |
| 4 | friskresult | 风险历史结果 | varchar | 255 |  | √ | ' ' | 风险历史结果 |
| 5 | fhandler | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fsuggestion | fsuggestion | varchar | 2000 |  | √ | ' ' |  |
| 7 | ftransuggestion | 转交意见 | varchar | 510 |  | √ | ' ' | 转交意见 |
| 8 | fresult | 处理结果 | varchar | 30 |  | √ | ' ' | 处理结果,枚举: 1 :- 2 :正常 3 :风险 4 :重新计算 5 :取消处理 |
| 9 | ftransmit | 转交他人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | friskresult_tag | 风险历史结果_详情 | text | 0 |  |  | null | 风险历史结果_详情 |
| 11 | fresultid | 结果id | varchar | 100 |  | √ | ' ' | 结果id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_handle_entity |  | fresultid |
| 2 | t_tctrc_handle_entity_pkey |  | fid |

---

## 单据体-子表 t_tctrc_handle_suggestion

- **表名称：** 单据体-子表
- **表名：** t_tctrc_handle_suggestion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fsuggestion | 处理意见 | varchar | 500 |  | √ | ' ' | 处理意见 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_handle_suggestion_pkey |  | fentryid |
| 2 | idx_tctrc_handle_suggestion |  | fid |
