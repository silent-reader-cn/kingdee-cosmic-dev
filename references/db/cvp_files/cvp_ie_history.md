# 文档信息提取历史-cvp_ie_history

## 文档信息提取历史-主表 t_cvp_ie_history

- **表名称：** 文档信息提取历史-主表
- **表名：** t_cvp_ie_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbilldoc | 文件名 | varchar | 255 |  |  | null | 文件名 |
| 3 | fextractstatus | 状态 | varchar | 50 |  |  | null | 状态,枚举: running :提取中 extract_suc :通用提取成功 llm_suc :大模型提取成功 success :提取完成 cancel :取消任务 error :提取失败 |
| 4 | fllmtaskid | 大模型任务id | varchar | 50 |  |  | null | 大模型任务id |
| 5 | fcallresult | 回调结果 | varchar | 50 |  |  | ' ' | 回调结果 |
| 6 | fbilldocpath | 文件路径 | varchar | 2000 |  |  | null | 文件路径 |
| 7 | fprogressinfo | 进度 | varchar | 200 |  |  | null | 进度 |
| 8 | fbillvalid | 是否有效 | varchar | 50 |  |  | null | 是否有效,枚举: 1 :有效 0 :无效 |
| 9 | fwithctieresult | 是否需要携带复杂文档提取结果 | bpchar | 1 |  |  | '1' | 是否需要携带复杂文档提取结果 |
| 10 | fintegratedllmresult_tag | 子任务大模型提取结果整合_详情 | text | 0 |  |  | null | 子任务大模型提取结果整合_详情 |
| 11 | ftotalpage | 总页数 | int4 | 32 |  | √ | 0 | 总页数 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fllmnumber | 大模型编码 | varchar | 80 |  |  | ' ' | 大模型编码 |
| 14 | fistest | 是否测试任务 | bpchar | 1 |  |  | '0' | 是否测试任务 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fisupdate | 是否已更新 | bpchar | 1 |  |  | null | 是否已更新 |
| 17 | freqvrsp | 是否请求调度 | bpchar | 1 |  | √ | '1' | 是否请求调度 |
| 18 | fdocstr_tag | 待提取文档文字内容_详情 | text | 0 |  |  | '' | 待提取文档文字内容_详情 |
| 19 | fbusbillname | 业务单据名称 | varchar | 255 |  |  | null | 业务单据名称 |
| 20 | ftietype | 提取类型 | varchar | 10 |  |  | '0' | 提取类型,枚举: 0 :通用信息提取 1 :大模型信息提取 2 :通用提取与大模型提取混合提取 3 :通用表格提取 4 :多模态提取 |
| 21 | fupdatedata | 更新提取结果 | text | 0 |  |  | null | 更新提取结果 |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | fbusinessobj | 使用的业务对象 | varchar | 36 |  |  | null | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbusbillno | 业务单据编号 | varchar | 255 |  |  | null | 业务单据编号 |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fcallback | 回调信息 | varchar | 2000 |  |  | ' ' | 回调信息 |
| 30 | fextractpages | 提取范围 | varchar | 255 |  |  | null | 提取范围 |
| 31 | fintegratedllmresult | 子任务大模型提取结果整合 | varchar | 255 |  | √ | ' ' | 子任务大模型提取结果整合 |
| 32 | fbillenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 33 | fdocstr | 待提取文档文字内容 | varchar | 255 |  |  | null | 待提取文档文字内容 |
| 34 | fbillcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 35 | fbillid | 业务单据id | int8 | 64 |  |  | null | 业务单据id |
| 36 | fbillieresult | 提取结果 | text | 0 |  |  | null | 提取结果 |
| 37 | fiemould | 提取方案 | int8 | 64 |  |  | null | [文档信息提取 cvp_ie_mouldplan](../cvp_files/cvp_ie_mouldplan.md) |
| 38 | ftaskid | 任务id | varchar | 255 |  |  | null | 任务id |
| 39 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_history |  | fid |
| 2 | idx_t_cvp_ie_history |  | fbillno,fbillstatus,ftaskid |

---

## 单据体-子表 t_cvp_ie_subtask_history

- **表名称：** 单据体-子表
- **表名：** t_cvp_ie_subtask_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubdocstr_tag | 子任务-待提取文档文字内容_详情 | text | 0 |  |  | null | 子任务-待提取文档文字内容_详情 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsubllmtaskid | 子任务-大模型任务id | varchar | 50 |  | √ | ' ' | 子任务-大模型任务id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsubdocstr | 子任务-待提取文档文字内容 | varchar | 255 |  | √ | ' ' | 子任务-待提取文档文字内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cvp_ie_subtask_history |  | fentryid |
| 2 | idx_cvp_ie_subtask_history_fk |  | fid |
