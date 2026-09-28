# 城镇土地使用税税源明细-tcret_landtax_sour_info

## 城镇土地使用税税源明细-主表 t_tcret_landtax_sour_info

- **表名称：** 城镇土地使用税税源明细-主表
- **表名：** t_tcret_landtax_sour_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftextfield1 | 土地使用权人名称 | varchar | 100 |  | √ | ' ' | 土地使用权人名称 |
| 3 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 4 | flandstatus | 土地性质 | varchar | 30 |  | √ | ' ' | 土地性质,枚举: stateowned :国有 collectivity :集体 |
| 5 | fvillages | 乡镇（街道） | varchar | 100 |  | √ | ' ' | 乡镇（街道） |
| 6 | fobtainlandprice | 其中：取得土地使用权支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：取得土地使用权支付金额 |
| 7 | flandnumber | 土地编号 | varchar | 100 |  | √ | ' ' | 土地编号 |
| 8 | flocation | 土地坐落地址（详细地址） | varchar | 100 |  | √ | ' ' | 土地坐落地址（详细地址） |
| 9 | ftaxstandard | 税额标准 | varchar | 100 |  | √ | ' ' | 税额标准 |
| 10 | flandparcelnumber | 宗地号 | varchar | 100 |  | √ | ' ' | 宗地号 |
| 11 | ftaxpayertype | 纳税人类型 | varchar | 30 |  | √ | ' ' | 纳税人类型,枚举: landholder :土地使用权人 collectivelanduser :集体土地使用人 freeuser :无偿使用人 agent :代管人 actualuser :实际使用人 |
| 12 | fcity | 市（区） | varchar | 100 |  | √ | ' ' | 市（区） |
| 13 | frealestatenumber | 不动产权证号 | varchar | 100 |  | √ | ' ' | 不动产权证号 |
| 14 | flanddevelopmentcost | 其中：土地开发成本 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：土地开发成本 |
| 15 | flandownernumber | 土地使用权人纳税人识别号（统一社会信用代码） | varchar | 100 |  | √ | ' ' | 土地使用权人纳税人识别号（统一社会信用代码） |
| 16 | flandacquiretime | 土地取得时间 | timestamp | 0 |  |  | null | 土地取得时间 |
| 17 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 18 | ftaxdutyend | 变更类型（纳税义务终止） | varchar | 30 |  | √ | ' ' | 变更类型（纳税义务终止）,枚举: ownershiptransfer :权属转移 other :其它 |
| 19 | flandacquireway | 土地取得方式 | varchar | 30 |  | √ | ' ' | 土地取得方式,枚举: assign :划拨 sell :出让 transfer :转让 hire :租赁 other :其它 |
| 20 | flandlevel | 土地等级 | varchar | 100 |  | √ | ' ' | 土地等级 |
| 21 | flandname | 土地名称 | varchar | 100 |  | √ | ' ' | 土地名称 |
| 22 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 23 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 24 | foccupylandarea | 占用土地面积 | numeric | 23 | 10 | √ | 0.0000000000 | 占用土地面积 |
| 25 | frealestateunitnumber | 不动产单元号 | varchar | 100 |  | √ | ' ' | 不动产单元号 |
| 26 | ftaxoffice | 土地所属主管税务所（科、分局） | varchar | 100 |  | √ | ' ' | 土地所属主管税务所（科、分局） |
| 27 | flandpurpose | 土地用途 | varchar | 30 |  | √ | ' ' | 土地用途,枚举: industry :工业 bussiness :商业 live :居住 overall :综合 development :房地产开发企业的开发用地 other :其它 |
| 28 | fmessagechange | 变更类型（信息项变更） | varchar | 30 |  | √ | ' ' | 变更类型（信息项变更）,枚举: area :土地面积变更 level :土地等级变更 tax :减免税变更 other :其它 |
| 29 | flandprice | 地价 | numeric | 23 | 10 | √ | 0.0000000000 | 地价 |
| 30 | fprovince | 省（自治区、直辖市） | varchar | 100 |  | √ | ' ' | 省（自治区、直辖市） |
| 31 | fcountry | 县（区） | varchar | 100 |  | √ | ' ' | 县（区） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_landtax_sour_info |  | fsbbid |
| 2 | t_tcret_landtax_sour_info_pkey |  | fid |
| 3 | idx_tcret_landtax_sour_info_1 |  | fewblxh,fsbbid |
