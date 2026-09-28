# 复杂文档提取历史记录-cvp_ctie_history

## 复杂文档提取历史记录-主表 t_cvp_ctie_history

- **表名称：** 复杂文档提取历史记录-主表
- **表名：** t_cvp_ctie_history

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextractstatus | 状态 | varchar | 50 |  |  | ' ' | 状态,枚举: running :提取中 error :提取失败 success :提取完成 cancel :取消任务 |
| 3 | fprogressinfo | 进度 | varchar | 200 |  |  | ' ' | 进度 |
| 4 | fmodifytime | 提取结束时间 | timestamp | 0 |  |  | null | 提取结束时间 |
| 5 | fdocpath | 文件路径 | varchar | 2000 |  |  | ' ' | 文件路径 |
| 6 | fextracttable | 是否提取文档中表格 | bpchar | 1 |  | √ | '0' | 是否提取文档中表格 |
| 7 | fistest | 是否测试 | bpchar | 1 |  | √ | '0' | 是否测试 |
| 8 | fpagecount | 提取页数 | int4 | 32 |  | √ | 0 | 提取页数 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | freqmodel | 是否调用调度算法模型 | bpchar | 1 |  | √ | '1' | 是否调用调度算法模型 |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fversion | 接口版本 | varchar | 10 |  | √ | ' ' | 接口版本 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | varchar | 50 |  |  | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcallbackresult | 回调结果 | varchar | 10 |  |  | ' ' | 回调结果 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fdocname | 文件名 | varchar | 255 |  |  | ' ' | 文件名 |
| 18 | fextractimageindoc | 是否提取文档中图片内容 | bpchar | 1 |  | √ | '0' | 是否提取文档中图片内容 |
| 19 | ftableoutputtype | 表格输出形式 | varchar | 50 |  | √ | ' ' | 表格输出形式 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fcallback | 回调信息 | varchar | 2000 |  |  | ' ' | 回调信息 |
| 22 | flayoutdata_tag | 复杂文档提取结果_详情 | text | 0 |  |  | '' | 复杂文档提取结果_详情 |
| 23 | fpageinfo | 页码信息结果 | varchar | 255 |  |  | ' ' | 页码信息结果 |
| 24 | fdocwithsiteandpage | word格式提取页码和位置信息 | bpchar | 1 |  | √ | '0' | word格式提取页码和位置信息 |
| 25 | flayoutdata | 复杂文档提取结果 | varchar | 255 |  |  | ' ' | 复杂文档提取结果 |
| 26 | ftaskid | 任务id | varchar | 50 |  |  | ' ' | 任务id |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fpageinfo_tag | 页码信息结果_详情 | text | 0 |  |  | '' | 页码信息结果_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_ctie_history |  | ftaskid |
| 2 | pk_t_cvp_ctie_history |  | fid |
