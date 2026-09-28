# 指标树配置-mai_indextreecfg

## 指标树配置-主表 t_mai_indextreecfg

- **表名称：** 指标树配置-主表
- **表名：** t_mai_indextreecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftype | 配置方式 | bpchar | 1 |  | √ | ' ' | 配置方式,枚举: 0 :复合方式 1 :相关拆解 |
| 8 | fexecstatus | 执行状态 | bpchar | 10 |  | √ | ' ' | 执行状态,枚举: loading :执行中 finfish :执行完成 error :执行失败 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftree | 指标树 | varchar | 255 |  | √ | ' ' | 指标树 |
| 12 | ftree_tag | 指标树_详情 | text | 0 |  |  | null | 指标树_详情 |
| 13 | fperiod | 执行周期 | bpchar | 10 |  | √ | ' ' | 执行周期,枚举: year :年 quarter :季 month :月 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 15 | fdesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 16 | findicator | 顶层指标 | int8 | 64 |  | √ | 0 | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mai_indextreecfg |  | fid |
| 2 | idx_mai_indextreecfg_findex |  | findicator |
