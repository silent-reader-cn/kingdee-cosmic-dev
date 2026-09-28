# 数据比对结果日志-tdm_dc_resultlog

## 数据比对结果日志-主表 t_tdm_dc_resultlog

- **表名称：** 数据比对结果日志-主表
- **表名：** t_tdm_dc_resultlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatarange | 数据范围 | varchar | 255 |  | √ | ' ' | 数据范围 |
| 3 | fdatarange_tag | 数据范围_详情 | text | 0 |  |  | null | 数据范围_详情 |
| 4 | fstate | 运行状态 | varchar | 50 |  | √ | ' ' | 运行状态,枚举: C :创建 R :执行中 S :成功 F :失败 |
| 5 | ftar_noexistcount | 目标单据缺失行数 | int8 | 64 |  | √ | 0 | 目标单据缺失行数 |
| 6 | fsource_count | 源单据行数 | int8 | 64 |  | √ | 0 | 源单据行数 |
| 7 | fsuccess_count | 匹配成功行数 | int8 | 64 |  | √ | 0 | 匹配成功行数 |
| 8 | ftar_diffcount | 目标单据差异行数 | int8 | 64 |  | √ | 0 | 目标单据差异行数 |
| 9 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fresultid | 结果表ID | int8 | 64 |  | √ | 0 | 结果表ID |
| 11 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | ftar_count | 目标单据行数 | int8 | 64 |  | √ | 0 | 目标单据行数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_dc_resultlog |  | fid |
| 2 | idx_t_tdm_dc_resultlog_1 |  | fresultid |
