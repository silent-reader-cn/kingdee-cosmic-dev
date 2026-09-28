# 数据比对结果-tdm_dc_result

## 数据比对结果-主表 t_tdm_dc_result

- **表名称：** 数据比对结果-主表
- **表名：** t_tdm_dc_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fdatarange_tag | 数据范围_详情 | text | 0 |  |  | null | 数据范围_详情 |
| 4 | ftar_noexistcount | 目标单据缺失行数 | int8 | 64 |  | √ | 0 | 目标单据缺失行数 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | ferrormsg | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ftar_diffcount | 目标单据差异行数 | int8 | 64 |  | √ | 0 | 目标单据差异行数 |
| 9 | fschemeid | 数据比对方案 | int8 | 64 |  | √ | 0 | 数据比对方案 tdm_dc_scheme |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | ftar_count | 目标单行数 | int8 | 64 |  | √ | 0 | 目标单行数 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdatarange | 数据范围 | varchar | 255 |  | √ | ' ' | 数据范围 |
| 15 | fstate | 运行状态 | varchar | 50 |  | √ | ' ' | 运行状态,枚举: C :创建 R :执行中 S :完全匹配 F :失败 P :部分匹配 N :完全不匹配 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fsource_count | 源单据行数 | int8 | 64 |  | √ | 0 | 源单据行数 |
| 18 | fsuccess_count | 匹配成功行数 | int8 | 64 |  | √ | 0 | 匹配成功行数 |
| 19 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 20 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | ferrormsg_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_dc_result |  | fid |
| 2 | idx_t_tdm_dc_result_1 |  | fbillno |
