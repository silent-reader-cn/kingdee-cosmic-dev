# 告警信息-fatvs_alarmmessage

## 告警信息-主表 t_fatvs_alarmmessage

- **表名称：** 告警信息-主表
- **表名：** t_fatvs_alarmmessage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | falarmtime | 告警时间 | timestamp | 0 |  |  | null | 告警时间 |
| 3 | findexvalue | 技能指标值 | varchar | 50 |  | √ | ' ' | 技能指标值 |
| 4 | falarmstatus | 预警状态 | varchar | 2 |  | √ | ' ' | 预警状态,枚举: 0 :正常 1 :异常 |
| 5 | fwarndetailid | 技能预警 | int8 | 64 |  | √ | 0 | 技能预警 |
| 6 | fnumber | 预警编码 | varchar | 50 |  | √ | ' ' | 预警编码 |
| 7 | fruntimedate | 技能运行数据 | int8 | 64 |  | √ | 0 | [技能运行数据 fatvs_skill_runtimedata](../fatvs_files/fatvs_skill_runtimedata.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fatvs_alarmmessage |  | fid |
| 2 | idx_fatvs_alarmmessage_no |  | fnumber |
