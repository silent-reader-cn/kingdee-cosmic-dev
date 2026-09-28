# 引入结果-bos_importlog

## 引入结果-主表 t_bas_importlog

- **表名称：** 引入结果-主表
- **表名：** t_bas_importlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fname | 业务对象名称 | varchar | 255 |  |  | null | 业务对象名称 |
| 4 | fcreatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fbizobject | fbizobject | varchar | 36 |  | √ | ' ' |  |
| 6 | fisdeleted | 文件删除状态 | bpchar | 1 |  | √ | '0' | 文件删除状态,枚举: 0 :未删除 1 :引入文件和错误数据已删除 2 :引入文件已删除 |
| 7 | fmodifytime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | ffailed | 失败条数 | int8 | 64 |  | √ | 0 | 失败条数 |
| 10 | fsourceobj | 业务对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fmasterid | fmasterid | int8 | 64 |  |  | null |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fimportstatus | 引入状态 | bpchar | 1 |  | √ | '0' | 引入状态,枚举: 0 :引入中 1 :引入完成 |
| 14 | fnumber | 日志编码 | varchar | 255 |  | √ | ' ' | 日志编码 |
| 15 | ftotal | 执行总数 | int8 | 64 |  | √ | 0 | 执行总数 |
| 16 | fdata | 日志 | text | 0 |  |  | null | 日志 |
| 17 | fimporttype | 引入类型 | bpchar | 1 |  | √ | '1' | 引入类型,枚举: 2 :单据体引入 1 :单据引入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_importlog_pkey |  | fid |
| 2 | idx_bas_importlog_fnumber |  | fnumber |
| 3 | idx_bas_importing_creator |  | fcreatorid |
