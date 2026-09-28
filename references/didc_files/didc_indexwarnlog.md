# 指标风险项日志-didc_indexwarnlog

## 指标风险项日志-主表 t_didc_indexwarnlog

- **表名称：** 指标风险项日志-主表
- **表名：** t_didc_indexwarnlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | flogstatus | 预警日志状态 | varchar | 50 |  | √ | ' ' | 预警日志状态 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |
| 8 | fplanid | 预警方案id | varchar | 250 |  | √ | ' ' | 预警方案id |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fplanrowid | 预警方案行id | varchar | 50 |  | √ | ' ' | 预警方案行id |
| 11 | fcontent | 预警内容 | varchar | 2000 |  | √ | ' ' | 预警内容 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_indexwarnlog |  | fid |
| 2 | idx_didc_indexwarnlog |  | fplanrowid |
