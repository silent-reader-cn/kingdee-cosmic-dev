# 地址-cts_address

## 地址-主表 t_cts_address

- **表名称：** 地址-主表
- **表名：** t_cts_address

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress1 | 自定义地址字段1 | varchar | 255 |  | √ | ' ' | 自定义地址字段1 |
| 3 | fpostcode2 | 邮编2 | varchar | 10 |  | √ | ' ' | 邮编2 |
| 4 | faddress2 | 自定义地址字段2 | varchar | 255 |  | √ | ' ' | 自定义地址字段2 |
| 5 | fpostcode1 | 邮编1 | varchar | 10 |  | √ | ' ' | 邮编1 |
| 6 | faddress3 | 自定义地址字段3 | varchar | 255 |  | √ | ' ' | 自定义地址字段3 |
| 7 | faddress4 | 自定义地址字段4 | varchar | 255 |  | √ | ' ' | 自定义地址字段4 |
| 8 | faddress5 | 自定义地址字段5 | varchar | 255 |  | √ | ' ' | 自定义地址字段5 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fadmindivisionid6 | 行政区划6级 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 11 | fhousenum2 | 门牌号补充信息 | varchar | 255 |  | √ | ' ' | 门牌号补充信息 |
| 12 | fadmindivisionid5 | 行政区划5级 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 13 | fadmindivisionid4 | 行政区划4级 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 14 | fsource | 地址来源表单 | varchar | 30 |  | √ | ' ' | 地址来源表单 |
| 15 | fadmindivisionid3 | 行政区划3级 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 16 | fadmindivisionid2 | 行政区划2级 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 17 | fadmindivisionid1 | 行政区划1级 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 18 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 19 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | froomnum | 房间号 | varchar | 255 |  | √ | ' ' | 房间号 |
| 21 | fdetail | 详细地址 | varchar | 512 |  | √ | ' ' | 详细地址 |
| 22 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 24 | fpostcodeext | 邮编1扩展 | varchar | 10 |  | √ | ' ' | 邮编1扩展 |
| 25 | fname | 地址名称 | varchar | 1024 |  | √ | ' ' | 地址名称 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fstreet1 | 街道 | varchar | 255 |  | √ | ' ' | 街道 |
| 28 | fbuilding | 大厦 | varchar | 255 |  | √ | ' ' | 大厦 |
| 29 | fstreet2 | 街道补充信息 | varchar | 255 |  | √ | ' ' | 街道补充信息 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fcountryid | 国家或地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 32 | fpobox | PO box | varchar | 255 |  | √ | ' ' | PO box |
| 33 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fvalid | 状态 | varchar | 32 |  | √ | ' ' | 状态,枚举: 1 :已使用 0 :未使用 2 :检查中 |
| 35 | fhousenum | 门牌号 | varchar | 255 |  | √ | ' ' | 门牌号 |
| 36 | fconfigid | 地址格式 | int8 | 64 |  | √ | 0 | 地址格式 cts_addressconfig |
| 37 | ffloor | 楼层 | varchar | 255 |  | √ | ' ' | 楼层 |
| 38 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 39 | flongitude | 经度 | numeric | 23 | 10 | √ | 0 | 经度 |
| 40 | fpostcode3 | 邮编3 | varchar | 10 |  | √ | ' ' | 邮编3 |
| 41 | fnumber | 地址编码 | varchar | 1024 |  | √ | ' ' | 地址编码 |
| 42 | flatitude | 纬度 | numeric | 23 | 10 | √ | 0 | 纬度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_address |  | fid |
| 2 | idx_cts_addr_fadmin |  | fcountryid,fadmindivisionid1,fadmindivisionid2,fadmindivisionid3 |
