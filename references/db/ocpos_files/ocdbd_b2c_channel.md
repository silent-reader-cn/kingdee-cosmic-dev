# 店铺档案-ocdbd_b2c_channel

## 关联子实体-子表 t_ocdbd_channel_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocdbd_channel_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_channel_lk_fk |  | fid |
| 2 | pk_ocdbd_channel_lk |  | fpkid |

---

## 线上门店信息-多语言表 t_ocdbd_b2cchannelonline_l

- **表名称：** 线上门店信息-多语言表
- **表名：** t_ocdbd_b2cchannelonline_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 线上店铺名称 | varchar | 50 |  | √ | ' ' | 线上店铺名称 |
| 2 | flocaleid | flocaleid | bpchar | 10 |  | √ | 'zh_CN' | localeid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_b2cchannelonline_l |  | fpkid |
| 2 | idx_ocdbd_b2cchannelonline_l |  | fentryid,flocaleid |

---

## 店铺档案-主表 t_ocdbd_channel

- **表名称：** 店铺档案-主表
- **表名：** t_ocdbd_channel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompanychannelid | 所属集团渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 6 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fhdepartmentid | 所属部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fclosetime | 退出时间 | timestamp | 0 |  |  | null | 退出时间 |
| 11 | fcontact | 店铺联系人 | varchar | 30 |  | √ | ' ' | 店铺联系人 |
| 12 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 13 | fisorderchannel | 是否分配客户 | bpchar | 1 |  | √ | '0' | 是否分配客户 |
| 14 | fcloserid | 退出人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 店铺名称 | varchar | 100 |  | √ | ' ' | 店铺名称 |
| 16 | fphone | 公司电话 | varchar | 30 |  | √ | ' ' | 公司电话 |
| 17 | flongnumber | 长编码(已作废，请使用长主键) | varchar | 500 |  | √ | ' ' | 长编码(已作废，请使用长主键) |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | flongid | 长主键 | varchar | 500 |  | √ | ' ' | 长主键 |
| 20 | fup1channelid | 所属一级 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 21 | fsimplepinyin | 名称简拼 | varchar | 80 |  | √ | ' ' | 名称简拼 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fhregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fdivisionid | 行政区划 | varchar | 36 |  | √ | ' ' | 行政区划 |
| 26 | flatitude | 纬度 | numeric | 23 | 10 | √ | 0 | 纬度 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fcustomerid | 对应客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 29 | fisstore | 是否门店 | bpchar | 1 |  | √ | '0' | 是否门店 |
| 30 | flogo | LOGO | varchar | 255 |  | √ | ' ' | LOGO |
| 31 | fcontactphone_enp | fcontactphone_enp | text | 0 |  |  | null |  |
| 32 | fup2channelid | 所属二级 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 33 | flegalchannelid | 所属法人 | int8 | 64 |  | √ | 0 | [店铺档案 ocdbd_b2c_channel](../ocpos_files/ocdbd_b2c_channel.md) |
| 34 | fsnmanager | 序列号管理 | bpchar | 1 |  | √ | 'A' | 序列号管理,枚举: A :启用商品序列号（强控） C :启用商品序列号（预警） B :不启用商品序列号 |
| 35 | fchannelproperty | 渠道性质 | bpchar | 1 |  | √ | 'A' | 渠道性质,枚举: A :直接渠道 B :间接渠道 D :混合渠道 |
| 36 | fcreditcode | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |
| 37 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 41 | ffax | 公司传真 | varchar | 30 |  | √ | ' ' | 公司传真 |
| 42 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fisinnerorg | 内部组织 | bpchar | 1 |  | √ | '0' | 内部组织 |
| 45 | fparentid | 上级渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 46 | fgradeid | 店铺等级 | int8 | 64 |  | √ | 0 | [渠道等级 ocdbd_channel_grade](../ocdbd_files/ocdbd_channel_grade.md) |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fchanneltypeid | 店铺经营类型 | int8 | 64 |  | √ | 0 | [店铺经营类型 ocdbd_b2c_channel_type](../ocpos_files/ocdbd_b2c_channel_type.md) |
| 49 | fsaleorgid | 所属销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 50 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 51 | fissalechannel | 是否分配供货渠道 | bpchar | 1 |  | √ | '0' | 是否分配供货渠道 |
| 52 | flongitude | 经度 | numeric | 23 | 10 | √ | 0 | 经度 |
| 53 | fhprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 55 | fclosereasonid | 退出原因 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 56 | fcontactphone | 店铺联系人电话 | varchar | 30 |  | √ | ' ' | 店铺联系人电话 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ocdbd_channel_createorg |  | fcreateorgid |
| 2 | idx_t_ocdbd_channel_master |  | fmasterid |
| 3 | pk_ocdbd_channel |  | fid |
| 4 | idx_ocdbd_chl_status |  | fstatus |
| 5 | idx_ocdbd_chl_number |  | fnumber |

---

## 供货关系-子表 t_ocdbd_channelorginfo

- **表名称：** 供货关系-子表
- **表名：** t_ocdbd_channelorginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsaleorgid | 销售组织编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fentrysourcetype | 组织信息来源 | bpchar | 1 |  | √ | 'C' | 组织信息来源,枚举: A :手工创建 B :客户同步 C :未知 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_chlorginfo_fid |  | fid |
| 2 | pk_ocdbd_channelorginfo |  | fentryid |

---

## 店铺档案-使用范围表 t_ocdbd_channel_u

- **表名称：** 店铺档案-使用范围表
- **表名：** t_ocdbd_channel_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ocdbd_channel_u |  | fdataid,fuseorgid |
| 2 | idx_t_ocdbd_channel_u_uo |  | fuseorgid |

---

## 店铺档案-分表 t_ocdbd_channel_x

- **表名称：** 店铺档案-分表
- **表名：** t_ocdbd_channel_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderbilltypeid | 订货单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fisdeliverybystore | 门店配送 | bpchar | 1 |  | √ | '0' | 门店配送 |
| 4 | fisnegativeinventory | 允许负库存 | bpchar | 1 |  | √ | '0' | 允许负库存 |
| 5 | fisdefaultstore | 默认门店 | bpchar | 1 |  | √ | '0' | 默认门店 |
| 6 | fregchannelid | fregchannelid | int8 | 64 |  | √ | 0 |  |
| 7 | fdeliverymile | 配送公里范围 | int4 | 32 |  | √ | 0 | 配送公里范围 |
| 8 | fordercontroltype | 订货单据控制 | bpchar | 1 |  | √ | 'A' | 订货单据控制,枚举: A :可选 B :固定 |
| 9 | fisenableerpinv | 启用ERP库存 | bpchar | 1 |  | √ | '0' | 启用ERP库存 |
| 10 | fdispatchchannelid | 配送渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 11 | fsalechannelid | 默认供货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 12 | fregtype | 渠道身份类型 | bpchar | 1 |  | √ | 'A' | 渠道身份类型,枚举: A :客户 B :渠道身份 |
| 13 | forderchannelid | 收货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 14 | fcreatetype | 店铺来源 | bpchar | 1 |  | √ | 'A' | 店铺来源,枚举: A :手工新增 B :客户下推 C :渠道申请下推 D :导入新增 E :WebAPI新增 |
| 15 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 16 | fsalecontrolmode | 销量管理模式 | bpchar | 1 |  | √ | 'A' | 销量管理模式,枚举: A :POS收银 B :销量开单 C :不管销量 |
| 17 | fisenablecredit | 启用赊销信用管理 | bpchar | 1 |  | √ | '0' | 启用赊销信用管理 |
| 18 | freturncontroltype | 退货单据控制 | bpchar | 1 |  | √ | 'A' | 退货单据控制,枚举: A :可选 B :固定 |
| 19 | fregisterclientid | fregisterclientid | int8 | 64 |  | √ | 0 |  |
| 20 | fisshowcredit | 展示信用余额 | bpchar | 1 |  | √ | '1' | 展示信用余额 |
| 21 | fregstatus | 渠道状态 | bpchar | 1 |  | √ | 'C' | 渠道状态,枚举: D :已认证 Z :已退出 |
| 22 | freturnbilltypeid | 退货单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 23 | festoreworktime | 营业时间.结束 | int4 | 32 |  | √ | '-1' | 营业时间.结束 |
| 24 | fbillcontrolmode | 开单供货模式 | bpchar | 1 |  | √ | 'A' | 开单供货模式,枚举: A :我开单，我供货 |
| 25 | fcountryid | 所属国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 26 | fpaytype | 付款方式 | bpchar | 1 |  | √ | ' ' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 27 | fbstoreworktime | 营业时间.开始 | int4 | 32 |  | √ | '-1' | 营业时间.开始 |
| 28 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 29 | fbusinesschannelid | 业绩归属渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 30 | frebatechannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 31 | fisonlinestore | 线上门店 | bpchar | 1 |  | √ | '0' | 线上门店 |
| 32 | fisdeliveryonecity | 同城配送 | bpchar | 1 |  | √ | '0' | 同城配送 |
| 33 | finvcontrolmode | 库存管理模式 | bpchar | 1 |  | √ | 'A' | 库存管理模式,枚举: A :完整进销存模式 B :库存上报模式 |
| 34 | fiscontrolorderqty | 订货数量可调配 | bpchar | 1 |  | √ | '1' | 订货数量可调配 |
| 35 | fisfetchbyself | 到店自提 | bpchar | 1 |  | √ | '0' | 到店自提 |
| 36 | fpaychannelid | 付款渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 37 | ftxregisterno | 纳税人识别号 | varchar | 80 |  | √ | ' ' | 纳税人识别号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channel_x |  | fid |
| 2 | idx_ocdbd_chlx_sochannel |  | fsalechannelid,forderchannelid |

---

## 相关负责人-多选基础资料表 t_ocdbd_channel_rp

- **表名称：** 相关负责人-多选基础资料表
- **表名：** t_ocdbd_channel_rp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channel_rp |  | fpkid |
| 2 | idx_ocdbd_channelrp_fid |  | fid,fbasedataid |

---

## 渠道职能-多选基础资料表 t_ocdbd_channelfuncs

- **表名称：** 渠道职能-多选基础资料表
- **表名：** t_ocdbd_channelfuncs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道职能 ocdbd_channel_function](../ocdbd_files/ocdbd_channel_function.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channelfuncs |  | fpkid |
| 2 | idx_ocdbd_channelfuncs_fid |  | fid,fbasedataid |

---

## 店铺档案-多语言表 t_ocdbd_channel_l

- **表名称：** 店铺档案-多语言表
- **表名：** t_ocdbd_channel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 店铺名称 | varchar | 100 |  | √ | ' ' | 店铺名称 |
| 3 | faddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channel_l |  | fpkid |
| 2 | idx_ocdbd_chll_fidlid |  | fid,flocaleid |

---

## 店铺档案-分表 t_ocdbd_channel_e

- **表名称：** 店铺档案-分表
- **表名：** t_ocdbd_channel_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbelongcountyid | 店铺所属城市区县 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 3 | fomsstoreno | OMS店铺编码 | varchar | 50 |  | √ | ' ' | OMS店铺编码 |
| 4 | fplatformenabletime | 平台启用日期 | timestamp | 0 |  |  | null | 平台启用日期 |
| 5 | fclosedate | 关店日期 | timestamp | 0 |  |  | null | 关店日期 |
| 6 | fopendate | 开店日期 | timestamp | 0 |  |  | null | 开店日期 |
| 7 | frecordtype | 档案类型 | bpchar | 1 |  | √ | ' ' | 档案类型,枚举: A :平台店铺 B :零售店铺 C :自建商城 D :法人 |
| 8 | flegalidcard | 法人身份证号 | varchar | 100 |  | √ | ' ' | 法人身份证号 |
| 9 | flegalphone | 法人联系电话 | varchar | 50 |  | √ | ' ' | 法人联系电话 |
| 10 | fomschannelname | OMS店铺名称 | varchar | 100 |  | √ | ' ' | OMS店铺名称 |
| 11 | fplatformstoreid | 平台店铺ID | varchar | 100 |  | √ | ' ' | 平台店铺ID |
| 12 | fplatformstorenick | 店铺昵称 | varchar | 100 |  | √ | ' ' | 店铺昵称 |
| 13 | ffinishinittime | 初始化时间 | timestamp | 0 |  |  | null | 初始化时间 |
| 14 | ffulladdress | 店铺完整地址 | varchar | 500 |  | √ | ' ' | 店铺完整地址 |
| 15 | ftradestatus | 营业状态 | bpchar | 1 |  | √ | ' ' | 营业状态,枚举: A :营业中 B :待开业 C :停业中 D :已撤店 E :未开店 |
| 16 | fcommandorgid | 管辖部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fbalanceorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | ffinishinitstatus | 初始化状态 | bpchar | 1 |  | √ | ' ' | 初始化状态,枚举: A :结束初始化 B :未初始化 |
| 19 | fplatformtypeid | 所属平台 | int8 | 64 |  | √ | 0 | [平台类型 rtbd_platformtype](../ocpos_files/rtbd_platformtype.md) |
| 20 | fdeliveryorgid | 默认发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fplatformstroename | 平台店铺名称 | varchar | 100 |  | √ | ' ' | 平台店铺名称 |
| 22 | fintroduction | 店铺简介 | varchar | 255 |  | √ | ' ' | 店铺简介 |
| 23 | fintroduction_tag | 店铺简介_详情 | text | 0 |  |  | null | 店铺简介_详情 |
| 24 | fplatformstoreno | 平台店铺编码 | varchar | 100 |  | √ | ' ' | 平台店铺编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_channel_e_eno |  | fomsstoreno |
| 2 | pk_ocdbd_channel_e |  | fid |

---

## 渠道标签单据体-子表 t_ocdbd_channellabel

- **表名称：** 渠道标签单据体-子表
- **表名：** t_ocdbd_channellabel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flabeltime | 打标签时间 | timestamp | 0 |  |  | null | 打标签时间 |
| 3 | flabeluserid | 打标签人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flabelid | 标签编码 | int8 | 64 |  | √ | 0 | [渠道标签 ocdbd_channellabel](../ocdbd_files/ocdbd_channellabel.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channellabel |  | fentryid |
| 2 | idx_ocdbd_channellabel |  | fid,flabelid |

---

## 线上门店信息-子表 t_ocdbd_b2cchannelonline

- **表名称：** 线上门店信息-子表
- **表名：** t_ocdbd_b2cchannelonline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 线上店铺名称 | varchar | 50 |  | √ | ' ' | 线上店铺名称 |
| 3 | fomssystemid | OMS系统 | int8 | 64 |  | √ | 0 | [OMS系统配置 rtecs_omssystem](../ocpos_files/rtecs_omssystem.md) |
| 4 | fplatformtypeid | 线上平台 | int8 | 64 |  | √ | 0 | [平台类型 rtbd_platformtype](../ocpos_files/rtbd_platformtype.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 7 | fonlinestatus | 营业状态 | bpchar | 1 |  | √ | ' ' | 营业状态,枚举: A :营业中 B :待开业 C :停业中 D :已撤店 E :未开店 |
| 8 | fnumber | 线上店铺编码 | varchar | 100 |  | √ | ' ' | 线上店铺编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fonlinestoreid | 线上店铺id | varchar | 50 |  | √ | ' ' | 线上店铺id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_b2cchannelonline |  | fentryid |
| 2 | idx_ocdbd_online_fid |  | fid |

---

## 渠道分类单据体-子表 t_ocdbd_channelclasses

- **表名称：** 渠道分类单据体-子表
- **表名：** t_ocdbd_channelclasses

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclassstandardid | 分类标准编码 | int8 | 64 |  | √ | 0 | [渠道分类标准 ocdbd_channel_standard](../ocdbd_files/ocdbd_channel_standard.md) |
| 3 | fchannelclassid | 分类编码 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channelclasses |  | fentryid |
| 2 | idx_ocdbd_chlclasses_fid |  | fid |

---

## 店铺仓库-子表 t_ocdbd_channel_stockrec

- **表名称：** 店铺仓库-子表
- **表名：** t_ocdbd_channel_stockrec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenablestatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :可用 0 :禁用 |
| 3 | fwarehousename | 店铺仓库名称 | varchar | 50 |  | √ | ' ' | 店铺仓库名称 |
| 4 | fmanager | 仓库负责人 | varchar | 50 |  | √ | ' ' | 仓库负责人 |
| 5 | ferpwarehouseid | ERP仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fwarehouseid | 店铺仓库ID | int8 | 64 |  | √ | 0 | [渠道仓库 ococic_warehouse](../ococic_files/ococic_warehouse.md) |
| 8 | fwarehouseno | 店铺仓库编码 | varchar | 50 |  | √ | ' ' | 店铺仓库编码 |
| 9 | fwarehouseaddress | 仓库地址 | varchar | 500 |  | √ | ' ' | 仓库地址 |
| 10 | fisdelivery | 默认发货仓库 | bpchar | 1 |  | √ | ' ' | 默认发货仓库 |
| 11 | fautocreateerpstock | 自动创建ERP仓库 | bpchar | 1 |  | √ | ' ' | 自动创建ERP仓库 |
| 12 | fwarehousefulladdress | 详细地址 | varchar | 500 |  | √ | ' ' | 详细地址 |
| 13 | fisreturn | 默认退货仓库 | bpchar | 1 |  | √ | ' ' | 默认退货仓库 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fenablelocation | 允许负库存 | bpchar | 1 |  | √ | ' ' | 允许负库存 |
| 17 | fisdefault | 默认收货仓库 | bpchar | 1 |  | √ | ' ' | 默认收货仓库 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channel_stockrec |  | fentryid |
| 2 | idx_ocdbd_cha_stockrec_fid |  | fid |
