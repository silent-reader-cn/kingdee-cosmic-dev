# 报表重算列表-xkrpt_reportcal

## 报表重算列表-主表 t_xkrpt_rptcal

- **表名称：** 报表重算列表-主表
- **表名：** t_xkrpt_rptcal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 0 :待重算 1 :重算中 2 :重算完成 3 :重算失败 |
| 3 | fcaldate | 重算时间 | timestamp | 0 |  |  | null | 重算时间 |
| 4 | frptid | 报表 | varchar | 36 |  | √ | ' ' | [报表 xkrpt_report](../xkrpt_files/xkrpt_report.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | ferrormsg | 错误消息 | varchar | 2000 |  | √ | ' ' | 错误消息 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | frpttype | 报表类型 | varchar | 10 |  | √ | ' ' | 报表类型,枚举: 1 :报表 17 :个别报表 31 :抵销表 71 :附表个别报表 14 :汇总报表 15 :合并报表 16 :工作底稿 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkrpt_rptcal |  | fid |
