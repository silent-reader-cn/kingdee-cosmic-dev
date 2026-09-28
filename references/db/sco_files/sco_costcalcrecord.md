# 标准成本卷算任务报告-sco_costcalcrecord

## 标准成本卷算任务报告-主表 t_sco_costcalcrecord

- **表名称：** 标准成本卷算任务报告-主表
- **表名：** t_sco_costcalcrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftasktype | 任务类型 | varchar | 200 |  | √ | ' ' | 任务类型,枚举: cad_taskexecutelog :任务执行日志 cad_checkitem :合法性检查项 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fnextpagepara | 页面携带参数 | varchar | 500 |  | √ | ' ' | 页面携带参数 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fcosttypeid | 标准成本方案 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 11 | ftask | 任务 | int8 | 64 |  | √ | 0 | 标准成本任务 sco_task |
| 12 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_costcalcrecord |  | fid |
| 2 | idx_sco_costcalcrecord_billno |  | fbillno |
