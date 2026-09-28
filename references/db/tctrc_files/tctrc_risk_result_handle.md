# 风险处理-tctrc_risk_result_handle

## 风险处理-主表 t_tctrc_handle_entity

- **表名称：** 风险处理-主表
- **表名：** t_tctrc_handle_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :重新审核 |
| 4 | friskresult | 风险历史结果 | varchar | 255 |  | √ | ' ' | 风险历史结果 |
| 5 | fhandler | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fsuggestion | fsuggestion | varchar | 2000 |  | √ | ' ' |  |
| 7 | ftransuggestion | ftransuggestion | varchar | 510 |  | √ | ' ' |  |
| 8 | fresult | 单选按钮组 | varchar | 30 |  | √ | ' ' | 单选按钮组,枚举: 2 :标为正常 3 :存在风险 |
| 9 | ftransmit | ftransmit | int8 | 64 |  | √ | 0 |  |
| 10 | friskresult_tag | 风险历史结果_详情 | text | 0 |  |  | null | 风险历史结果_详情 |
| 11 | ftype | 处理类型 | varchar | 30 |  | √ | ' ' | 处理类型,枚举: sdjs :手工计算 rgcl :人工处理 dsjs :定时计算运行 sbmx :申报模型触发运行 cxjs :重新计算 jkjc :健康检查触发运行 |
| 12 | fhandleoption | 处理意见 | varchar | 2000 |  | √ | ' ' | 处理意见 |
| 13 | fresultid | 结果id | varchar | 100 |  | √ | ' ' | 结果id |

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

## 附件-附件表 t_tctrc_riskhandle_attach

- **表名称：** 附件-附件表
- **表名：** t_tctrc_riskhandle_attach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctrc_riskhandle_attach |  | fpkid |
| 2 | idx_tctrc_riskhandle_attach_fk |  | fid |
