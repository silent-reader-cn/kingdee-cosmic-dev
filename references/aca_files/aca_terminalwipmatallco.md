# 期末在产材料盘点分配(后台表)-aca_terminalwipmatallco

## 期末在产材料盘点分配(后台表)-主表 t_aca_terminalwipmatallco

- **表名称：** 期末在产材料盘点分配(后台表)-主表
- **表名：** t_aca_terminalwipmatallco

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillnumber | 源单单据编码 | varchar | 80 |  | √ | ' ' | 源单单据编码 |
| 3 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 4 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fmodifierid | 最后修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fperiodid | 核算期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 11 | fsrcbillrow | 源单行号 | int8 | 64 |  | √ | 0 | 源单行号 |
| 12 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 13 | fsource | 来源 | varchar | 30 |  | √ | 'hand' | 来源,枚举: |
| 14 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 15 | fchecktype | 盘点方式 | varchar | 30 |  | √ | ' ' | 盘点方式,枚举: qty :数量 amount :金额 |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 17 | fcalqty | 分配数量 | numeric | 23 | 10 | √ | 0 | 分配数量 |
| 18 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 19 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fentryid | 源单分录id | int8 | 64 |  | √ | 0 | 源单分录id |
| 21 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aca_terwipmatall_ocpc |  | forgid,fcostaccountid,fcostcenterid,fperiodid |
| 2 | pk_t_aca_terminalwipmatallco |  | fid |
| 3 | idx_aca_terwipmatall_entryid |  | fentryid |
