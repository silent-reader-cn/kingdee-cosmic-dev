# 进项税额抵扣台账明细-tcvat_deduction_detail

## 进项税额抵扣台账明细-主表 t_tcvat_deduction_detail

- **表名称：** 进项税额抵扣台账明细-主表
- **表名：** t_tcvat_deduction_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxperiod | 所属月份 | varchar | 100 |  | √ | ' ' | 所属月份 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fjzjtflag | 是否包含即征即退业务 | bpchar | 1 |  | √ | ' ' | 是否包含即征即退业务 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 9 | fvoucherdate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 10 | famount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 11 | fvoucherno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 12 | feffectivetaxamount | 有效税额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效税额 |
| 13 | fvehicletype | 车辆类型 | varchar | 50 |  | √ | ' ' | 车辆类型 |
| 14 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 15 | ftype | 发票类型 | varchar | 32 |  | √ | ' ' | 发票类型,枚举: 15 :通行费电子发票 2 :电子专票 4 :纸质专票 |
| 16 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 17 | fgoodsname | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 18 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 19 | ftaxaccountserialno | 台账流水号 | varchar | 100 |  | √ | ' ' | 台账流水号 |
| 20 | fexportflag | 是否包含出口业务 | bpchar | 1 |  | √ | ' ' | 是否包含出口业务 |
| 21 | finvoicecode | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 22 | ftaxdeductionid | 抵扣台账ID | int8 | 64 |  | √ | 0 | 抵扣台账ID |
| 23 | fdeductiontype | 抵扣类型 | varchar | 30 |  | √ | ' ' | 抵扣类型,枚举: 1 :增值税专用发票 1-export :用于出口业务 1-jzjt :用于即征即退业务 2 :通行费发票 2-export :用于出口业务 2-jzjt :用于即征即退业务 3 :海关进口增值税专用缴款书 3-export :用于出口业务 3-jzjt :用于即征即退业务 4 :农产品收购发票或者销售发票 4-export :用于出口业务 4-jzjt :用于即征即退业务 5 :代扣代缴税收缴款凭证 5-export :用于出口业务 5-jzjt :用于即征即退业务 6 :加计扣除农产品进项税额 6-export :用于出口业务 6-jzjt :用于即征即退业务 7 :旅客运输服务扣税凭证 7-export :用于出口业务 7-jzjt :用于即征即退业务 |
| 24 | fvehicleidenticode | 车辆识别代码 | varchar | 50 |  | √ | ' ' | 车辆识别代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_deduction_detail |  | forgid,ftaxperiod |
| 2 | t_tcvat_deduction_detail_pkey |  | fid |
