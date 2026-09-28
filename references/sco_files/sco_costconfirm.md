# 成本确认单-sco_costconfirm

## 成本确认单-主表 t_sco_costconfirm

- **表名称：** 成本确认单-主表
- **表名：** t_sco_costconfirm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 确认人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fdiffrate | 差异率 | numeric | 23 | 10 | √ | 0 | 差异率 |
| 5 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 6 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fstdamount | 标准成本 | numeric | 23 | 10 | √ | 0 | 标准成本 |
| 11 | fdiff | 完工结算差异 | numeric | 23 | 10 | √ | 0 | 完工结算差异 |
| 12 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fbizstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :未确认 B :已确认 |
| 14 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 15 | fsrcbill | 计算结果ID | int8 | 64 |  | √ | 0 | 计算结果ID |
| 16 | fmodifytime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fabsorbamount | 吸收成本 | numeric | 23 | 10 | √ | 0 | 吸收成本 |
| 19 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 20 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 sco_costobjectf7 |
| 21 | fbomversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 22 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 23 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_costconfirm |  | forgid,fperiodid,fcostaccountid,fcostobjectid |
| 2 | pk_sco_costconfirm |  | fid |
