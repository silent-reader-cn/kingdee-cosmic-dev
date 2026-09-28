# 简版复杂文档提取-cvp_simple_ctie_history

## 简版复杂文档提取-主表 t_cvp_simple_extract

- **表名称：** 简版复杂文档提取-主表
- **表名：** t_cvp_simple_extract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextractstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: running :提取中 error :提取失败 success :提取完成 cancel :取消任务 |
| 3 | fdoccontent | 复杂文档提取结果 | varchar | 2000 |  |  | ' ' | 复杂文档提取结果 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdoccontent_tag | 复杂文档提取结果_详情 | text | 0 |  |  | null | 复杂文档提取结果_详情 |
| 8 | fdocname | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fprogress | 进度 | varchar | 500 |  |  | ' ' | 进度 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdocpath | 文件路径 | varchar | 2000 |  |  | ' ' | 文件路径 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_simple_extract_status |  | fextractstatus |
| 2 | pk_cvp_simple_extract |  | fid |
