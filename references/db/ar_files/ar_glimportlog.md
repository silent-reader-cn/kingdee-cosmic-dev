# 从总账引入初始数据方案引入结果-ar_glimportlog

## 从总账引入初始数据方案引入结果-主表 t_ar_glimportlog

- **表名称：** 从总账引入初始数据方案引入结果-主表
- **表名：** t_ar_glimportlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farfinbillcount | 引入期初财务应收单数 | int4 | 32 |  | √ | 0 | 引入期初财务应收单数 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fschemeid | 方案id | int8 | 64 |  | √ | 0 | 从总账引入初始数据方案 ar_glimportscheme |
| 8 | fpaidbillcount | 引入期初预付单数 | int4 | 32 |  | √ | 0 | 引入期初预付单数 |
| 9 | farbusbillcount | 引入期初暂估应收单数 | int4 | 32 |  | √ | 0 | 引入期初暂估应收单数 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ferrordesc_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fapbusbillcount | 引入期初暂估应付单数 | int4 | 32 |  | √ | 0 | 引入期初暂估应付单数 |
| 16 | fimportstate | 引入状态 | varchar | 5 |  | √ | ' ' | 引入状态,枚举: 0 :引入完成 1 :引入中 |
| 17 | freceivedbillcount | 引入期初预收单数 | int4 | 32 |  | √ | 0 | 引入期初预收单数 |
| 18 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 19 | fusetime | 用时 | int8 | 64 |  | √ | 0 | 用时 |
| 20 | ferrordesc | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fapfinbillcount | 引入期初财务应付单数 | int4 | 32 |  | √ | 0 | 引入期初财务应付单数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_glimportlog |  | fid |
| 2 | idx_ar_glimpt_schemeid |  | fschemeid |
