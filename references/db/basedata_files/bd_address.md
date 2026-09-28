# 地址-bd_address

## 地址-主表 t_bd_supplieraddress

- **表名称：** 地址-主表
- **表名：** t_bd_supplieraddress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplieraddrsspurpose | 供应商地址用途 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 3 | fadmindivisiondata | 行政区划(后台逻辑字段) | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 4 | ftradeterms | 贸易术语 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 5 | fdimensionality | 纬度 | varchar | 255 |  | √ | ' ' | 纬度 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fk_bj73_hihn_clearanceco | fk_bj73_hihn_clearanceco | varchar | 252 |  | √ | ' ' |  |
| 8 | fk_bj73_textfield2 | 区县 | varchar | 50 |  | √ | ' ' | 区县 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fk_bj73_textfield1 | 市 | varchar | 50 |  | √ | ' ' | 市 |
| 11 | fdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | fk_bj73_createdatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | finvalid | 失效 | bpchar | 1 |  | √ | '0' | 失效 |
| 17 | fsuppliermasterid | 供应商masterid | int8 | 64 |  | √ | 0 | 供应商masterid |
| 18 | fadmindivision | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 19 | ftimezone | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 20 | fdetailaddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |
| 21 | fzipcode | 邮政编码 | varchar | 50 |  | √ | ' ' | 邮政编码 |
| 22 | fcustomeraddrsspurpose | 客户地址用途 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fphone | 联系电话 | varchar | 100 |  | √ | ' ' | 联系电话 |
| 26 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 27 | fforwarderco | 物流备注 | varchar | 255 |  | √ | ' ' | 物流备注 |
| 28 | fcustomermasterid | 客户masterid | int8 | 64 |  | √ | 0 | 客户masterid |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | faddemail | 电子邮箱 | varchar | 100 |  | √ | ' ' | 电子邮箱 |
| 32 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 33 | fclearanceco | 清关公司 | varchar | 255 |  | √ | ' ' | 清关公司 |
| 34 | fsupplierid | 供应商id | varchar | 100 |  | √ | ' ' | 供应商id |
| 35 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | ftransportleadtime | 运输提前期（天） | int8 | 64 |  | √ | 0 | 运输提前期（天） |
| 37 | fk_bj73_deliveryremarks | fk_bj73_deliveryremarks | varchar | 252 |  | √ | ' ' |  |
| 38 | fk_bj73_textfield | 省 | varchar | 50 |  | √ | ' ' | 省 |
| 39 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | fissupplieradd | 是否供应商 | bpchar | 1 |  | √ | '0' | 是否供应商 |
| 41 | fiscustomeradd | 是否客户 | bpchar | 1 |  | √ | '0' | 是否客户 |
| 42 | flongitude | 经度 | varchar | 255 |  | √ | ' ' | 经度 |
| 43 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 44 | flinkman | 传真 | varchar | 100 |  | √ | ' ' | 传真 |
| 45 | fcustomerid | 客户id | varchar | 100 |  | √ | ' ' | 客户id |
| 46 | fisdeliveryaddress | 是否全渠道云收货地址 | bpchar | 1 |  | √ | '0' | 是否全渠道云收货地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_suppadd_number |  | fnumber |
| 2 | t_bd_supplieraddress_pkey |  | fid |
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
