# 渠道申请-ocdbd_channelreq

## 渠道职能-多选基础资料表 t_ocdbd_channelreqfun

- **表名称：** 渠道职能-多选基础资料表
- **表名：** t_ocdbd_channelreqfun

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
| 1 | idx_ocdbd_channelreqfun_fbid |  | fid,fbasedataid |
| 2 | pk_ocdbd_channelreqfun |  | fpkid |

---

## 渠道申请-主表 t_ocdbd_channelreq

- **表名称：** 渠道申请-主表
- **表名：** t_ocdbd_channelreq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 6 | fsalerid | 业务员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcontact | 联系人 | varchar | 30 |  | √ | ' ' | 联系人 |
| 9 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 10 | fauthstatus | 认证状态 | bpchar | 1 |  | √ | 'A' | 认证状态,枚举: A :未认证 B :认证成功 C :认证失败 |
| 11 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 12 | fphone | 手机 | varchar | 80 |  | √ | ' ' | 手机 |
| 13 | femail | 邮箱 | varchar | 80 |  | √ | ' ' | 邮箱 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fdivisionid | 省市区 | varchar | 36 |  | √ | ' ' | 省市区 |
| 17 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 18 | flatitude | 纬度 | numeric | 23 | 10 | √ | 0 | 纬度 |
| 19 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 20 | fisstore | 是否门店 | bpchar | 1 |  | √ | '0' | 是否门店 |
| 21 | flogo | LOGO | varchar | 255 |  | √ | ' ' | LOGO |
| 22 | fcontactphone_enp | fcontactphone_enp | text | 0 |  |  | null |  |
| 23 | fchannelproperty | 渠道性质 | bpchar | 1 |  | √ | 'A' | 渠道性质,枚举: A :直接渠道 B :间接渠道 D :混合渠道 |
| 24 | fsalechannelid | 默认供货渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 25 | fcreditcode | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |
| 26 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fusername | 姓名 | varchar | 80 |  | √ | ' ' | 姓名 |
| 28 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 30 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 31 | fsalecontrolmode | 销量管理模式 | bpchar | 1 |  | √ | 'A' | 销量管理模式,枚举: A :POS收银 B :销量开单 C :不管销量 |
| 32 | fbotpstatus | 注册状态 | bpchar | 1 |  | √ | 'A' | 注册状态,枚举: A :未注册 B :已注册 |
| 33 | freqdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 34 | fchannelid | 关联渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 35 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 36 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fparentid | 上级渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 38 | fgradeid | 渠道等级 | int8 | 64 |  | √ | 0 | [渠道等级 ocdbd_channel_grade](../ocdbd_files/ocdbd_channel_grade.md) |
| 39 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 40 | fchanneltypeid | 渠道类型 | int8 | 64 |  | √ | 0 | [渠道类型 ocdbd_channel_type](../ocdbd_files/ocdbd_channel_type.md) |
| 41 | fregisterstatus | 自助注册开通状态 | bpchar | 1 |  | √ | 'A' | 自助注册开通状态,枚举: A :未开通 B :已开通 |
| 42 | fisregister | 开通经销商自助注册服务 | bpchar | 1 |  | √ | '0' | 开通经销商自助注册服务 |
| 43 | fpaytype | 付款方式 | bpchar | 1 |  | √ | ' ' | 付款方式,枚举: 1 :现销（预付款） 2 :赊销 3 :货到付款（现款现结） 4 :在线支付 0 :其他 |
| 44 | fdepartmentid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | '5' |  |
| 47 | flongitude | 经度 | numeric | 23 | 10 | √ | 0 | 经度 |
| 48 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 49 | fcontactphone | 联系人电话 | varchar | 30 |  | √ | ' ' | 联系人电话 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_channelreq |  | fid |
| 2 | idx_ocdbd_channelreq_num |  | fnumber |

---

## 相关负责人-多选基础资料表 t_ocdbd_channelreq_rp

- **表名称：** 相关负责人-多选基础资料表
- **表名：** t_ocdbd_channelreq_rp

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
| 1 | idx_ocdbd_channelreqrp_fid |  | fid,fbasedataid |
| 2 | pk_ocdbd_channelreq_rp |  | fpkid |

---

## 渠道申请-多语言表 t_ocdbd_channelreq_l

- **表名称：** 渠道申请-多语言表
- **表名：** t_ocdbd_channelreq_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
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
| 1 | idx_ocdbd_channelreql_flid |  | fid,flocaleid |
| 2 | pk_ocdbd_channelreq_l |  | fpkid |
