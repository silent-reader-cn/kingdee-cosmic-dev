# 成本变更记录-sca_costchangerecord

## 成本变更记录-主表 t_sca_costchangerecord

- **表名称：** 成本变更记录-主表
- **表名：** t_sca_costchangerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchangecontext_tag | 变更内容_详情 | text | 0 |  |  | null | 变更内容_详情 |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbizstatus | 业务状态 | varchar | 30 |  | √ | 'A' | 业务状态,枚举: A :未结算 B :已结算 |
| 8 | fbusinessbill | 业务单据 | varchar | 255 |  | √ | ' ' | 业务单据,枚举: cad_costobject :成本核算对象 cad_plannedoutputbill :计划生产数量归集 cad_factnedoutputbill :完工入库数量归集 sca_matusecollect :材料耗用归集 sca_resourceuse :资源耗用量归集 sca_absorbadjust :吸收成本调整 sca_matalloc :材料耗用分配 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 12 | fchangecontext | 变更内容 | varchar | 1000 |  | √ | ' ' | 变更内容 |
| 13 | fsourcebiztime | 源单业务日期 | timestamp | 0 |  |  | null | 源单业务日期 |
| 14 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sca_costchangerecord |  | fid |
| 2 | idx_sca_costchangerecord |  | forgid,fcostobjectid,fcostcenterid,fbusinessbill |
