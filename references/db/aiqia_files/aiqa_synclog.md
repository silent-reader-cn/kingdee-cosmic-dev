# 多模态同步日志-aiqa_synclog

## 多模态同步日志-主表 t_aiqa_synclog

- **表名称：** 多模态同步日志-主表
- **表名：** t_aiqa_synclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsyncbatch | 同步批次 | int8 | 64 |  | √ | 0 | 同步批次 |
| 7 | fsyncsttus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 1 :成功 0 :失败 |
| 8 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ffailcount | 失败数量 | int8 | 64 |  | √ | 0 | 失败数量 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcount | 同步数量 | int8 | 64 |  | √ | 0 | 同步数量 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fsuccesscount | 成功数量 | int8 | 64 |  | √ | 0 | 成功数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aiqa_synclog_m0 |  | fbillno |
| 2 | pk_aiqa_synclog |  | fid |
