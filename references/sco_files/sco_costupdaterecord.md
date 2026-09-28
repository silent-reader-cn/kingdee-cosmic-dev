# 标准成本更新任务报告-sco_costupdaterecord

## 标准成本更新任务报告-主表 t_sco_costupdaterecord

- **表名称：** 标准成本更新任务报告-主表
- **表名：** t_sco_costupdaterecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetcosttypeid | 目标标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsrccosttypeid | 源标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftasktype | 任务类型 | varchar | 255 |  | √ | ' ' | 任务类型,枚举: cad_taskexecutelog :任务执行日志 cad_checkitem :合法性检查项 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fnextpagepara | 页面携带参数 | varchar | 512 |  | √ | ' ' | 页面携带参数 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fupdatebillno | 更新申请单单号 | varchar | 255 |  | √ | ' ' | 更新申请单单号 |
| 13 | fisupdatecurlevel | 仅更新本层 | bpchar | 1 |  | √ | ' ' | 仅更新本层 |
| 14 | fisspecifymaterial | 指定物料更新 | bpchar | 1 |  | √ | ' ' | 指定物料更新 |
| 15 | ftask | 任务 | int8 | 64 |  | √ | 0 | 标准成本任务 sco_task |
| 16 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costupdaterecord |  | fid |
| 2 | idx_sco_updaterecord_billno |  | fbillno |
