# 文档切分多模态提取-cvp_ie_filesplit

## 文档切分多模态提取-主表 t_cvp_split_history

- **表名称：** 文档切分多模态提取-主表
- **表名：** t_cvp_split_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextractstatus | 提取状态 | varchar | 50 |  | √ | ' ' | 提取状态,枚举: running :提取中 success :提取完成 error :提取失败 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcallbackresult | 回调结果 | varchar | 50 |  | √ | ' ' | 回调结果 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdocname | 文件名称 | varchar | 255 |  |  | null | 文件名称 |
| 8 | fresult | 切分结果 | varchar | 255 |  |  | null | 切分结果 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fprogress | 进度提示 | varchar | 200 |  |  | null | 进度提示 |
| 11 | fcallback | 回调信息 | varchar | 255 |  |  | null | 回调信息 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fresult_tag | 切分结果_详情 | text | 0 |  |  | ' ' | 切分结果_详情 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftaskid | 任务id | varchar | 50 |  | √ | '0' | 任务id |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcallback_tag | 回调信息_详情 | text | 0 |  |  | ' ' | 回调信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_split_history_taskid |  | ftaskid |
| 2 | pk_cvp_split_history |  | fid |
