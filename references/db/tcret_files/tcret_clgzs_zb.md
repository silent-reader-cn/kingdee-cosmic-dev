# 车辆购置税主表-tcret_clgzs_zb

## 车辆购置税主表-主表 t_tcret_clgzs_zb

- **表名称：** 车辆购置税主表-主表
- **表名：** t_tcret_clgzs_zb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcardno | 证件号码 | varchar | 50 |  | √ | ' ' | 证件号码 |
| 3 | fsnse | 实纳税额 | numeric | 23 | 10 | √ | 0 | 实纳税额 |
| 4 | faddress | 地址 | varchar | 512 |  | √ | ' ' | 地址 |
| 5 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 6 | fsbmstjdm | 申报免（减）税条件或者代码 | varchar | 50 |  | √ | ' ' | 申报免（减）税条件或者代码 |
| 7 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 8 | freceiver | 受理人 | varchar | 50 |  | √ | ' ' | 受理人 |
| 9 | fconsignee | 被委托人 | varchar | 50 |  | √ | ' ' | 被委托人 |
| 10 | fothervoucherno | 其他有效凭证号码 | varchar | 50 |  | √ | ' ' | 其他有效凭证号码 |
| 11 | ftaxprice | 计税价格 | numeric | 23 | 10 | √ | 0 | 计税价格 |
| 12 | famount | 不含税价 | numeric | 23 | 10 | √ | 0 | 不含税价 |
| 13 | frecivetime | 受理时间 | timestamp | 0 |  |  | null | 受理时间 |
| 14 | fexcise | 消费税 | numeric | 23 | 10 | √ | 0 | 消费税 |
| 15 | fconsigneeidno | 被委托人证件号码 | varchar | 50 |  | √ | ' ' | 被委托人证件号码 |
| 16 | fcardname | 证件名称 | varchar | 50 |  | √ | ' ' | 证件名称 |
| 17 | finvcustomeno | 海关进口关税专用缴款书号码 | varchar | 50 |  | √ | ' ' | 海关进口关税专用缴款书号码 |
| 18 | foutvolume | 排量（cc） | numeric | 23 | 10 | √ | 0 | 排量（cc） |
| 19 | fbuydate | 购置日期 | timestamp | 0 |  |  | null | 购置日期 |
| 20 | freviewer | 复核人 | varchar | 50 |  | √ | ' ' | 复核人 |
| 21 | fcarsalebillno | 机动车销售统一发票号码 | varchar | 50 |  | √ | ' ' | 机动车销售统一发票号码 |
| 22 | fynse | 应纳税额 | numeric | 23 | 10 | √ | 0 | 应纳税额 |
| 23 | fcarregistadress | 车辆拟登记地点 | varchar | 512 |  | √ | ' ' | 车辆拟登记地点 |
| 24 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 25 | fdelayamount | 滞纳金金额 | numeric | 23 | 10 | √ | 0 | 滞纳金金额 |
| 26 | freviewtime | 复核时间 | timestamp | 0 |  |  | null | 复核时间 |
| 27 | fothervoucherprice | 其他有效凭证价格 | numeric | 23 | 10 | √ | 0 | 其他有效凭证价格 |
| 28 | fcarserialno | 车辆识别代号/车架号 | varchar | 50 |  | √ | ' ' | 车辆识别代号/车架号 |
| 29 | fdeducttaxcode | 免（减）税条件代码 | varchar | 50 |  | √ | ' ' | 免（减）税条件代码 |
| 30 | fdeclaretype | 申报类型 | varchar | 50 |  | √ | ' ' | 申报类型,枚举: zs :征税 ms :免税 js :减税 |
| 31 | freportprice | 申报计税价格 | numeric | 23 | 10 | √ | 0 | 申报计税价格 |
| 32 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 33 | fproducttype | 厂牌型号 | varchar | 50 |  | √ | ' ' | 厂牌型号 |
| 34 | fdetaxamount | 关税完税价格 | numeric | 23 | 10 | √ | 0 | 关税完税价格 |
| 35 | ftariff | 关 税 | numeric | 23 | 10 | √ | 0 | 关 税 |
| 36 | fcarsalebillcode | 机动车销售统一发票代码 | varchar | 50 |  | √ | ' ' | 机动车销售统一发票代码 |
| 37 | fdeucttax | 免(减)税额 | numeric | 23 | 10 | √ | 0 | 免(减)税额 |
| 38 | fcarregiste | 是否办理车辆登记 | varchar | 50 |  | √ | ' ' | 是否办理车辆登记,枚举: y :是 n :否 |
| 39 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 40 | fcerticarno | 合格证编号(货物进口证明书号) | varchar | 50 |  | √ | ' ' | 合格证编号(货物进口证明书号) |
| 41 | fothercouchername | 其他有效凭证名称 | varchar | 50 |  | √ | ' ' | 其他有效凭证名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_clgzs_zb |  | fid |
| 2 | idx_t_tcret_clgzs_zb_sbbid |  | fsbbid,fewblxh |
