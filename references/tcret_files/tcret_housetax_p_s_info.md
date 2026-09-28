# 从价计征房产税税源明细-tcret_housetax_p_s_info

## 从价计征房产税税源明细-主表 t_tcret_housetax_p_s_info

- **表名称：** 从价计征房产税税源明细-主表
- **表名：** t_tcret_housetax_p_s_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fletarea | 其中：出租房产面积 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：出租房产面积 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | fownername | 所有权人名称 | varchar | 100 |  | √ | ' ' | 所有权人名称 |
| 5 | fvillages | 乡镇（街道） | varchar | 100 |  | √ | ' ' | 乡镇（街道） |
| 6 | flandnumber | 房屋所在土地编号 | varchar | 100 |  | √ | ' ' | 房屋所在土地编号 |
| 7 | flocation | 房产坐落地址（详细地址） | varchar | 100 |  | √ | ' ' | 房产坐落地址（详细地址） |
| 8 | fhousevalue | 房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 房产原值 |
| 9 | fbuildingname | 房产名称 | varchar | 100 |  | √ | ' ' | 房产名称 |
| 10 | ftaxpayertype | 纳税人类型 | varchar | 30 |  | √ | ' ' | 纳税人类型,枚举: owner :产权所有人 manager :经营管理人 pawnee :承典人 agent :房屋代管人 user :房屋使用人 renter :融资租赁承租人 other :其它 |
| 11 | fcity | 市（区） | varchar | 100 |  | √ | ' ' | 市（区） |
| 12 | frealestatenumber | 不动产权证号 | varchar | 100 |  | √ | ' ' | 不动产权证号 |
| 13 | fownernumber | 所有权人纳税人识别号（统一社会信用代码） | varchar | 100 |  | √ | ' ' | 所有权人纳税人识别号（统一社会信用代码） |
| 14 | fbuildingnumber | 房产编号 | varchar | 100 |  | √ | ' ' | 房产编号 |
| 15 | fbuildingusage | 房产用途 | varchar | 30 |  | √ | ' ' | 房产用途,枚举: industry :工业 bussiness :商业及办公 loft :住房 other :其它 |
| 16 | fletvalue | 其中：出租房产原值 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：出租房产原值 |
| 17 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 18 | fbuildingobtaintime | 房产取得时间 | timestamp | 0 |  |  | null | 房产取得时间 |
| 19 | ftaxdutyend | 变更类型（纳税义务终止） | varchar | 30 |  | √ | ' ' | 变更类型（纳税义务终止）,枚举: ownershiptransfer :权属转移 other :其它 |
| 20 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 21 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 22 | frealestateunitnumber | 不动产单元号 | varchar | 100 |  | √ | ' ' | 不动产单元号 |
| 23 | ftaxoffice | 房产所属主管税务所（科、分局） | varchar | 100 |  | √ | ' ' | 房产所属主管税务所（科、分局） |
| 24 | fcoveredarea | 建筑面积 | numeric | 23 | 10 | √ | 0.0000000000 | 建筑面积 |
| 25 | fmessagechange | 变更类型（信息项变更） | varchar | 30 |  | √ | ' ' | 变更类型（信息项变更）,枚举: value :房产原值变更 rent :出租房产原值变更 tax :减免税变更 other :其它 |
| 26 | fprovince | 省（自治区、直辖市） | varchar | 100 |  | √ | ' ' | 省（自治区、直辖市） |
| 27 | fcountry | 县（区） | varchar | 100 |  | √ | ' ' | 县（区） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_housetax_p_s_info_1 |  | fewblxh,fsbbid |
| 2 | idx_tcret_housetax_p_s_info |  | fsbbid |
| 3 | t_tcret_housetax_p_s_info_pkey |  | fid |
