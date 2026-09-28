# 车船税税源明细表（车辆）-totf_tcvvt_vehiclesdtl

## 车船税税源明细表（车辆）-主表 t_totf_tcvvt_vehiclesdtl

- **表名称：** 车船税税源明细表（车辆）-主表
- **表名：** t_totf_tcvvt_vehiclesdtl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodel | 品牌型号 | varchar | 50 |  | √ | ' ' | 品牌型号 |
| 3 | ffueltype | 燃料种类 | varchar | 50 |  | √ | ' ' | 燃料种类 |
| 4 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 5 | fvinno | 车辆识别代码(车架号) | varchar | 50 |  | √ | ' ' | 车辆识别代码(车架号) |
| 6 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 7 | fvehicletype | 车辆类型 | varchar | 50 |  | √ | ' ' | 车辆类型 |
| 8 | fplatenumber | 号牌号码 | varchar | 50 |  | √ | ' ' | 号牌号码 |
| 9 | fengineno | 发动机号 | varchar | 50 |  | √ | ' ' | 发动机号 |
| 10 | fusernature | 使用性质 | varchar | 50 |  | √ | ' ' | 使用性质 |
| 11 | fzbzl | 整备质量 | numeric | 23 | 10 | √ | 0 | 整备质量 |
| 12 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 13 | finvoicedate | 车辆发票日期或注册登记日期 | timestamp | 0 |  |  | null | 车辆发票日期或注册登记日期 |
| 14 | fsbclzs | 申报车辆总数（辆） | int4 | 32 |  | √ | 0 | 申报车辆总数（辆） |
| 15 | fhdzk | 核定载客 | numeric | 23 | 10 | √ | 0 | 核定载客 |
| 16 | fdisplacement | 排(气)量 | varchar | 50 |  | √ | ' ' | 排(气)量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_tcvvt_vehiclesdtl |  | fsbbid,fewblxh |
| 2 | pk_totf_tcvvt_vehiclesdtl |  | fid |
