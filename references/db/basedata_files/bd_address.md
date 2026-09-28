# 地址-bd_address

## 地址-主表 t_bd_supplieraddress

- **表名称：** 地址-主表
- **表名：** t_bd_supplieraddress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplieraddrsspurpose | 供应商地址用途 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | fadmindivisiondata | 行政区划(后台逻辑字段) | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 4 | ftradeterms | 贸易术语 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 5 | fdimensionality | 纬度 | varchar | 255 |  | √ | ' ' | 纬度 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | finvalid | 失效 | bpchar | 1 |  | √ | '0' | 失效 |
| 13 | fsuppliermasterid | 供应商masterid | int8 | 64 |  | √ | 0 | 供应商masterid |
| 14 | fadmindivision | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 15 | ftimezone | 时区 | int8 | 64 |  | √ | 0 | 时区 inte_timezone |
| 16 | fdetailaddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |
| 17 | fzipcode | 邮政编码 | varchar | 50 |  | √ | ' ' | 邮政编码 |
| 18 | fcustomeraddrsspurpose | 客户地址用途 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 21 | fphone | 联系电话 | varchar | 100 |  | √ | ' ' | 联系电话 |
| 22 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 23 | fforwarderco | 货代公司 | varchar | 255 |  | √ | ' ' | 货代公司 |
| 24 | fcustomermasterid | 客户masterid | int8 | 64 |  | √ | 0 | 客户masterid |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | faddemail | 电子邮箱 | varchar | 100 |  | √ | ' ' | 电子邮箱 |
| 28 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 29 | fclearanceco | 清关公司 | varchar | 255 |  | √ | ' ' | 清关公司 |
| 30 | fsupplierid | 供应商id | varchar | 100 |  | √ | ' ' | 供应商id |
| 31 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | ftransportleadtime | 运输提前期（天） | int8 | 64 |  | √ | 0 | 运输提前期（天） |
| 33 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fissupplieradd | 是否供应商 | bpchar | 1 |  | √ | '0' | 是否供应商 |
| 35 | fiscustomeradd | 是否客户 | bpchar | 1 |  | √ | '0' | 是否客户 |
| 36 | flongitude | 经度 | varchar | 255 |  | √ | ' ' | 经度 |
| 37 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 38 | flinkman | 传真 | varchar | 100 |  | √ | ' ' | 传真 |
| 39 | fcustomerid | 客户id | varchar | 100 |  | √ | ' ' | 客户id |
| 40 | fisdeliveryaddress | 是否全渠道云收货地址 | bpchar | 1 |  | √ | '0' | 是否全渠道云收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_supplieraddress_pkey |  | fid |
| 2 | idx_t_bd_suppadd_number |  | fnumber |
| 3 | idx_t_bd_cusadd_customerid |  | fcustomerid |
| 4 | idx_t_bd_suppadd_supplierid |  | fsupplierid |

---

## 地址-多语言表 t_bd_supplieraddress_l

- **表名称：** 地址-多语言表
- **表名：** t_bd_supplieraddress_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fphone | fphone | varchar | 100 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fdetailaddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_supplieraddress_l_fid |  | fid,flocaleid |
| 2 | t_bd_supplieraddress_l_pkey |  | fpkid |
