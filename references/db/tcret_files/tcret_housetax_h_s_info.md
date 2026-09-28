# 从租计征房产税税源明细-tcret_housetax_h_s_info

## 从租计征房产税税源明细-主表 t_tcret_housetax_h_s_info

- **表名称：** 从租计征房产税税源明细-主表
- **表名：** t_tcret_housetax_h_s_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 3 | fcontractenddate | 合同约定租赁期止 | timestamp | 0 |  |  | null | 合同约定租赁期止 |
| 4 | freducerental | 享受减免税租金收入 | varchar | 100 |  | √ | ' ' | 享受减免税租金收入 |
| 5 | fdeclareenddate | 申报租金所属租赁期止 | timestamp | 0 |  |  | null | 申报租金所属租赁期止 |
| 6 | flocation | 房产坐落地址（详细地址） | varchar | 100 |  | √ | ' ' | 房产坐落地址（详细地址） |
| 7 | fleaseename | 承租方名称 | varchar | 100 |  | √ | ' ' | 承租方名称 |
| 8 | frentarea | 出租面积 | numeric | 23 | 10 | √ | 0.0000000000 | 出租面积 |
| 9 | ftaxreducecode | 减免性质代码 | varchar | 100 |  | √ | ' ' | 减免性质代码 |
| 10 | fcontractstartdate | 合同约定租赁期起 | timestamp | 0 |  |  | null | 合同约定租赁期起 |
| 11 | fdeclarerental | 申报租金收入 | numeric | 23 | 10 | √ | 0.0000000000 | 申报租金收入 |
| 12 | fleaseenumber | 承租方纳税人识别号（统一社会信用代码） | varchar | 100 |  | √ | ' ' | 承租方纳税人识别号（统一社会信用代码） |
| 13 | fdeclarestartdate | 申报租金所属租赁期起 | timestamp | 0 |  |  | null | 申报租金所属租赁期起 |
| 14 | fcontractrental | 合同租金总收入 | numeric | 23 | 10 | √ | 0.0000000000 | 合同租金总收入 |
| 15 | freducetax | 减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 减免税额 |
| 16 | fbuildingname | 房产名称 | varchar | 100 |  | √ | ' ' | 房产名称 |
| 17 | fcity | 市（区） | varchar | 100 |  | √ | ' ' | 市（区） |
| 18 | ftaxreduceproject | 减免项目名称 | varchar | 100 |  | √ | ' ' | 减免项目名称 |
| 19 | fbuildingnumber | 房产编号 | varchar | 100 |  | √ | ' ' | 房产编号 |
| 20 | fewblname | 二维表名称 | varchar | 100 |  | √ | ' ' | 二维表名称 |
| 21 | fvillage | 乡镇（街道） | varchar | 100 |  | √ | ' ' | 乡镇（街道） |
| 22 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 23 | ftaxoffice | 房产所属主管税务所（科、分局） | varchar | 100 |  | √ | ' ' | 房产所属主管税务所（科、分局） |
| 24 | fprovince | 省（自治区、直辖市） | varchar | 100 |  | √ | ' ' | 省（自治区、直辖市） |
| 25 | fbuildingpurpose | 房产用途 | varchar | 30 |  | √ | ' ' | 房产用途,枚举: industry :工业 bussiness :商业及办公 loft :住房 other :其它 |
| 26 | fcountry | 县（区） | varchar | 100 |  | √ | ' ' | 县（区） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcret_housetax_h_s_info_pkey |  | fid |
| 2 | idx_tcret_housetax_h_s_info |  | fsbbid |
| 3 | idx_tcret_housetax_h_s_info_1 |  | fewblxh,fsbbid |
