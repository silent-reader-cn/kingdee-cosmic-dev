# 车船税纳税申报表-totf_tcvvt_declare

## 车船税纳税申报表-主表 t_totf_tcvvt_declare

- **表名称：** 车船税纳税申报表-主表
- **表名：** t_totf_tcvvt_declare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 |
| 3 | funittax | 单位税额 | numeric | 23 | 10 | √ | 0 | 单位税额 |
| 4 | ftaxyear | 税款所属年度 | varchar | 50 |  | √ | ' ' | 税款所属年度 |
| 5 | fnyjsyfs | 年应缴税月份数 | numeric | 23 | 10 | √ | 0 | 年应缴税月份数 |
| 6 | fvinno | 车船识别代码(车架号/船舶识别号) | varchar | 50 |  | √ | ' ' | 车船识别代码(车架号/船舶识别号) |
| 7 | fbnyjse | 本年已缴税额 | numeric | 23 | 10 | √ | 0 | 本年已缴税额 |
| 8 | fzspm | 征收品目 | varchar | 50 |  | √ | ' ' | 征收品目 |
| 9 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 10 | fjsdw | 计税单位 | varchar | 50 |  | √ | ' ' | 计税单位 |
| 11 | fplatenumber | (车辆)号牌号码/(船舶)登记号码 | varchar | 50 |  | √ | ' ' | (车辆)号牌号码/(船舶)登记号码 |
| 12 | fbnybse | 本期年应补(退)税额 | numeric | 23 | 10 | √ | 0 | 本期年应补(退)税额 |
| 13 | fbnjmse1 | 本年减免税额1 | numeric | 23 | 10 | √ | 0 | 本年减免税额1 |
| 14 | fbnjmse2 | 本年减免税额2 | numeric | 23 | 10 | √ | 0 | 本年减免税额2 |
| 15 | fdnyjse | 当年应缴税额 | numeric | 23 | 10 | √ | 0 | 当年应缴税额 |
| 16 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 17 | fjsdwsl | 计税单位的数量 | numeric | 23 | 10 | √ | 0 | 计税单位的数量 |
| 18 | fjmszmh1 | 减免税证明号1 | varchar | 50 |  | √ | ' ' | 减免税证明号1 |
| 19 | fjmxzdm1 | 减免性质代码1 | varchar | 50 |  | √ | ' ' | 减免性质代码1 |
| 20 | fjmszmh2 | 减免税证明号2 | varchar | 50 |  | √ | ' ' | 减免税证明号2 |
| 21 | fnyjse | 年应缴税额 | numeric | 23 | 10 | √ | 0 | 年应缴税额 |
| 22 | fjmxzdm2 | 减免性质代码2 | varchar | 50 |  | √ | ' ' | 减免性质代码2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_tcvvt_declare |  | fsbbid,fewblxh |
| 2 | pk_totf_tcvvt_declare |  | fid |
