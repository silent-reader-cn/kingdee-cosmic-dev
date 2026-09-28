# 文档提取历史-cvp_ie_history

## 文档提取历史-主表 t_cvp_ie_history

- **表名称：** 文档提取历史-主表
- **表名：** t_cvp_ie_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbilldoc | 文件名 | varchar | 255 |  |  | null | 文件名 |
| 3 | fextractstatus | 状态 | varchar | 50 |  |  | null | 状态,枚举: running :提取中 error :提取失败 success :提取完成 cancel :取消任务 |
| 4 | fbilldocpath | 文件路径 | varchar | 2000 |  |  | null | 文件路径 |
| 5 | fprogressinfo | 进度 | varchar | 200 |  |  | null | 进度 |
| 6 | fbillvalid | 是否有效 | varchar | 50 |  |  | null | 是否有效,枚举: 1 :有效 0 :无效 |
| 7 | ftotalpage | 总页数 | int4 | 32 |  | √ | 0 | 总页数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 10 | fisupdate | 是否已更新 | bpchar | 1 |  |  | null | 是否已更新 |
| 11 | fbusbillname | 业务单据名称 | varchar | 255 |  |  | null | 业务单据名称 |
| 12 | fupdatedata | 更新提取结果 | text | 0 |  |  | null | 更新提取结果 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fbusinessobj | 使用的业务对象 | varchar | 36 |  |  | null | 主实体对象 bos_entityobject |
| 15 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 16 | fbusbillno | 业务单据编号 | varchar | 255 |  |  | null | 业务单据编号 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | fextractpages | 提取范围 | varchar | 255 |  |  | null | 提取范围 |
| 21 | fbillenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 22 | fbillcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fbillid | 业务单据id | int8 | 64 |  |  | null | 业务单据id |
| 24 | fbillieresult | 提取结果 | text | 0 |  |  | null | 提取结果 |
| 25 | fiemould | 提取方案 | int8 | 64 |  |  | null | 信息提取方案 cvp_ie_mouldplan |
| 26 | ftaskid | 任务id | varchar | 255 |  |  | null | 任务id |
| 27 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cvp_ie_history |  | fid |
| 2 | idx_t_cvp_ie_history |  | fbillno,fbillstatus |
