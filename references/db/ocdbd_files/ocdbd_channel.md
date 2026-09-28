# 渠道-ocdbd_channel

## 渠道-使用范围表 t_ocdbd_channel_u

- **表名称：** 渠道-使用范围表
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

## 渠道-分表 t_ocdbd_channel_x

- **表名称：** 渠道-分表
- **表名：** t_ocdbd_channel_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderbilltypeid | 订货单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 3 | fisdeliverybystore | 门店配送 | bpchar | 1 |  | √ | '0' | 门店配送 |
| 4 | fisnegativeinventory | 允许负库存 | bpchar | 1 |  | √ | '0' | 允许负库存 |
| 5 | fisdefaultstore | 默认门店 | bpchar | 1 |  | √ | '0' | 默认门店 |
| 6 | fregchannelid | fregchannelid | int8 | 64 |  | √ | 0 |  |
| 7 | fdeliverymile | 配送公里范围 | int4 | 32 |  | √ | 0 | 配送公里范围 |
| 8 | fordercontroltype | 订货单据控制 | bpchar | 1 |  | √ | 'A' | 订货单据控制,枚举: A :可选 B :固定 |
| 9 | fdispatchchannelid | 配送渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 10 | fsalechannelid | 默认供货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 11 | fregtype | 渠道身份类型 | bpchar | 1 |  | √ | 'A' | 渠道身份类型,枚举: A :客户 B :渠道身份 |
| 12 | forderchannelid | 收货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 13 | fcreatetype | 渠道来源 | bpchar | 1 |  | √ | 'A' | 渠道来源,枚举: A :手工新增 B :客户下推 C :渠道申请下推 D :导入新增 E :WebAPI新增 |
| 14 | fbalancechannelid | 结算渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | fsalecontrolmode | 销量管理模式 | bpchar | 1 |  | √ | 'A' | 销量管理模式,枚举: A :POS收银 B :销量开单 C :不管销量 |
| 16 | fisenablecredit | 启用赊销信用管理 | bpchar | 1 |  | √ | '0' | 启用赊销信用管理 |
| 17 | freturncontroltype | 退货单据控制 | bpchar | 1 |  | √ | 'A' | 退货单据控制,枚举: A :可选 B :固定 |
| 18 | fregisterclientid | fregisterclientid | int8 | 64 |  | √ | 0 |  |
| 19 | fregstatus | 渠道状态 | bpchar | 1 |  | √ | 'C' | 渠道状态,枚举: D :已认证 Z :已退出 |
| 20 | freturnbilltypeid | 退货单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 21 | festoreworktime | 营业时间.结束 | int4 | 32 |  | √ | '-1' | 营业时间.结束 |
| 22 | fbillcontrolmode | 开单供货模式 | bpchar | 1 |  | √ | 'A' | 开单供货模式,枚举: A :我开单，我供货 |
| 23 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 24 | fpaytype | 付款方式 | bpchar | 1 |  | √ | ' ' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 25 | fbstoreworktime | 营业时间.开始 | int4 | 32 |  | √ | '-1' | 营业时间.开始 |
| 26 | fpricechannelid | 取价渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 27 | fbusinesschannelid | 业绩归属渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 28 | frebatechannelid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 29 | fisonlinestore | 线上门店 | bpchar | 1 |  | √ | '0' | 线上门店 |
| 30 | fisdeliveryonecity | 同城配送 | bpchar | 1 |  | √ | '0' | 同城配送 |
| 31 | finvcontrolmode | 库存管理模式 | bpchar | 1 |  | √ | 'A' | 库存管理模式,枚举: A :完整进销存模式 B :库存上报模式 |
| 32 | fiscontrolorderqty | 订货数量可调配 | bpchar | 1 |  | √ | '1' | 订货数量可调配 |
| 33 | fisfetchbyself | 到店自提 | bpchar | 1 |  | √ | '0' | 到店自提 |
| 34 | fpaychannelid | 付款渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 35 | ftxregisterno | 纳税人识别号 | varchar | 80 |  | √ | ' ' | 纳税人识别号 |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
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

## 渠道-多语言表 t_ocdbd_channel_l

- **表名称：** 渠道-多语言表
- **表名：** t_ocdbd_channel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
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

## 渠道-主表 t_ocdbd_channel

- **表名称：** 渠道-主表
- **表名：** t_ocdbd_channel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompanychannelid | 所属集团渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 6 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fclosetime | 退出时间 | timestamp | 0 |  |  | null | 退出时间 |
| 10 | fcontact | 联系人 | varchar | 30 |  | √ | ' ' | 联系人 |
| 11 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 12 | fisorderchannel | 是否分配客户 | bpchar | 1 |  | √ | '0' | 是否分配客户 |
| 13 | fcloserid | 退出人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 15 | fphone | 公司电话 | varchar | 30 |  | √ | ' ' | 公司电话 |
| 16 | flongnumber | 长编码(已作废，请使用长主键) | varchar | 500 |  | √ | ' ' | 长编码(已作废，请使用长主键) |
| 17 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | flongid | 长主键 | varchar | 500 |  | √ | ' ' | 长主键 |
| 19 | fup1channelid | 所属一级 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 20 | fsimplepinyin | 名称简拼 | varchar | 80 |  | √ | ' ' | 名称简拼 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fdivisionid | 行政区划 | varchar | 36 |  | √ | ' ' | 行政区划 |
| 24 | flatitude | 纬度 | numeric | 23 | 10 | √ | 0 | 纬度 |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 26 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 27 | fisstore | 是否门店 | bpchar | 1 |  | √ | '0' | 是否门店 |
| 28 | flogo | LOGO | varchar | 255 |  | √ | ' ' | LOGO |
| 29 | fcontactphone_enp | fcontactphone_enp | text | 0 |  |  | null |  |
| 30 | fup2channelid | 所属二级 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 31 | flegalchannelid | 所属法人 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 32 | fsnmanager | 序列号管理 | bpchar | 1 |  | √ | 'A' | 序列号管理,枚举: A :启用商品序列号（强控） C :启用商品序列号（预警） B :不启用商品序列号 |
| 33 | fchannelproperty | 渠道性质 | bpchar | 1 |  | √ | 'A' | 渠道性质,枚举: A :直接渠道 B :间接渠道 D :混合渠道 |
| 34 | fcreditcode | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |
| 35 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 39 | ffax | 公司传真 | varchar | 30 |  | √ | ' ' | 公司传真 |
| 40 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fisinnerorg | 内部组织 | bpchar | 1 |  | √ | '0' | 内部组织 |
| 43 | fparentid | 上级渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 44 | fgradeid | 渠道等级 | int8 | 64 |  | √ | 0 | 渠道等级 ocdbd_channel_grade |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fchanneltypeid | 渠道类型 | int8 | 64 |  | √ | 0 | 渠道类型 ocdbd_channel_type |
| 47 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 49 | fissalechannel | 是否分配供货渠道 | bpchar | 1 |  | √ | '0' | 是否分配供货渠道 |
| 50 | flongitude | 经度 | numeric | 23 | 10 | √ | 0 | 经度 |
| 51 | fcurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 52 | fclosereasonid | 退出原因 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 53 | fcontactphone | 联系人电话 | varchar | 30 |  | √ | ' ' | 联系人电话 |

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

## 销售组织信息单据体-子表 t_ocdbd_channelorginfo

- **表名称：** 销售组织信息单据体-子表
- **表名：** t_ocdbd_channelorginfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsaleorgid | 销售组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

## 渠道职能-多选基础资料表 t_ocdbd_channelfuncs

- **表名称：** 渠道职能-多选基础资料表
- **表名：** t_ocdbd_channelfuncs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 渠道职能 ocdbd_channel_function |
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

## 渠道分类单据体-子表 t_ocdbd_channelclasses

- **表名称：** 渠道分类单据体-子表
- **表名：** t_ocdbd_channelclasses

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclassstandardid | 分类标准编码 | int8 | 64 |  | √ | 0 | 渠道分类标准 ocdbd_channel_standard |
| 3 | fchannelclassid | 分类编码 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
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
