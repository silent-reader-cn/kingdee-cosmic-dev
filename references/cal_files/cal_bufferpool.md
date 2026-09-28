# 核算缓冲池-cal_bufferpool

## 核算缓冲池-主表 t_cal_bufferpool

- **表名称：** 核算缓冲池-主表
- **表名：** t_cal_bufferpool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisdeletebill | 完成后删除单据 | bpchar | 1 |  | √ | '0' | 完成后删除单据 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fqueuetype | 序列类型 | bpchar | 1 |  | √ | '0' | 序列类型,枚举: 0 :入库 1 :出库 |
| 5 | factiontime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | factionname | 操作类型 | varchar | 30 |  | √ | ' ' | 操作类型,枚举: AUDIT :正向即时核算 UNAUDIT :反向即时核算 MATERIALWRITEOFF :材料核销 |
| 7 | fentity | 业务对象 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 8 | fbizbillid | 业务单据id | int8 | 64 |  | √ | 0 | 业务单据id |
| 9 | fismaterialtrans | 是否物料转换 | bpchar | 1 |  | √ | '0' | 是否物料转换 |
| 10 | fbillid | 核算成本记录id | int8 | 64 |  | √ | 0 | 核算成本记录id |
| 11 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 12 | fissucess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 13 | fentryid | 核算成本记录分录id | int8 | 64 |  | √ | 0 | 核算成本记录分录id |
| 14 | fbizbillentryid | 业务单据分录id | int8 | 64 |  | √ | 0 | 业务单据分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_bufferpool |  | fid |
| 2 | idx_cal_bufferpool_fmatid |  | fmaterialid |
| 3 | idx_cal_bufferpool_fbeid |  | fbillid,fentryid |
