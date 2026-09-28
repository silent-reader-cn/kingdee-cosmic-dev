# 会员档案-ocdbd_user

## 地址单据体-子表 t_ocdbd_user_addr_entry

- **表名称：** 地址单据体-子表
- **表名：** t_ocdbd_user_addr_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypeid | 地址类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | fphone | 联系电话 | varchar | 80 |  | √ | ' ' | 联系电话 |
| 4 | fprovinceid | 省份 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 5 | fcontact | 联系人 | varchar | 80 |  | √ | ' ' | 联系人 |
| 6 | fcityid | 城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 7 | fdistrictid | 所属区域 | varchar | 36 |  | √ | ' ' | 所属区域 |
| 8 | fdetailedaddress | 详细地址 | varchar | 255 |  | √ | ' ' | 详细地址 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fcountryid | 国家 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fisdefault | 是否默认地址 | bpchar | 1 |  | √ | '0' | 是否默认地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_addr_entry |  | fentryid |
| 2 | idx_ocdbd_useraddrentry_fid |  | fid |

---

## 证件信息单据体-子表 t_ocdbd_user_cert_entry

- **表名称：** 证件信息单据体-子表
- **表名：** t_ocdbd_user_cert_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypeid | 证件类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | fname | 证件姓名 | varchar | 80 |  | √ | ' ' | 证件姓名 |
| 4 | fcomment | 备注 | varchar | 80 |  | √ | ' ' | 备注 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnumber | 证件号码 | varchar | 80 |  | √ | ' ' | 证件号码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_cert_entry |  | fentryid |
| 2 | idx_ocdbd_usercertentry_fid |  | fid |
| 3 | idx_ocdbd_usercertentry_fnum |  | fnumber |

---

## 银行卡单据体-子表 t_ocdbd_user_bank_entry

- **表名称：** 银行卡单据体-子表
- **表名：** t_ocdbd_user_bank_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 开户人姓名 | varchar | 80 |  | √ | ' ' | 开户人姓名 |
| 3 | fcomment | 备注 | varchar | 80 |  | √ | ' ' | 备注 |
| 4 | fdepositbankid | 开户银行 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnumber | 银行卡卡号 | varchar | 80 |  | √ | ' ' | 银行卡卡号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_bank_entry |  | fentryid |
| 2 | idx_ocdbd_userbankentry_fid |  | fid |

---

## 用户站内登录信息单据体-子表 t_ocdbd_user_local

- **表名称：** 用户站内登录信息单据体-子表
- **表名：** t_ocdbd_user_local

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flastip | 最后登录IP | varchar | 80 |  | √ | ' ' | 最后登录IP |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fidentifier | 登录标识 | varchar | 80 |  | √ | ' ' | 登录标识 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | flogintype | 登录类型 | bpchar | 1 |  | √ | 'A' | 登录类型,枚举: A :手机号 B :邮箱 C :用户名 |
| 7 | fverified | 验证状态 | bpchar | 1 |  | √ | '1' | 验证状态,枚举: 0 :未验证 1 :已验证 |
| 8 | fpassword | 密码凭证 | varchar | 80 |  | √ | ' ' | 密码凭证 |
| 9 | flasttime | 最后登录时间 | timestamp | 0 |  |  | null | 最后登录时间 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsalt | 密码加盐 | varchar | 80 |  | √ | ' ' | 密码加盐 |
| 12 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_local |  | fentryid |
| 2 | idx_ocdbd_user_local_fidtf |  | fidentifier |
| 3 | idx_ocdbd_user_local_fid |  | fid |

---

## 会员档案-使用范围表 t_ocdbd_user_u

- **表名称：** 会员档案-使用范围表
- **表名：** t_ocdbd_user_u

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
| 1 | pk_t_ocdbd_user_u |  | fdataid,fuseorgid |
| 2 | idx_t_ocdbd_user_u_uo |  | fuseorgid |

---

## 会员档案-多语言表 t_ocdbd_user_l

- **表名称：** 会员档案-多语言表
- **表名：** t_ocdbd_user_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 80 |  | √ | ' ' | 姓名 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_l |  | fpkid |
| 2 | idx_ocdbd_userl_flid |  | fid,flocaleid |

---

## 会员档案-分表 t_ocdbd_user_r

- **表名称：** 会员档案-分表
- **表名：** t_ocdbd_user_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeveloptime | 开发时间 | timestamp | 0 |  |  | null | 开发时间 |
| 3 | fagentid | 经纪人 | int8 | 64 |  | √ | 0 | 会员档案 ocdbd_user |
| 4 | fdeveloperid | 开发人 | int8 | 64 |  | √ | 0 | 渠道用户(已废弃) ocdbd_channeluser |
| 5 | fconsultantid | 专属顾问 | int8 | 64 |  | √ | 0 | 渠道用户(已废弃) ocdbd_channeluser |
| 6 | fassignreasonid | 专属顾问分配原因 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 7 | flastconsultantid | 原专属顾问 | int8 | 64 |  | √ | 0 | 渠道用户(已废弃) ocdbd_channeluser |
| 8 | fassigntime | 专属顾问安排时间 | timestamp | 0 |  |  | null | 专属顾问安排时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_userr_fdevid |  | fdeveloperid |
| 2 | pk_ocdbd_user_r |  | fid |

---

## 标签单据体-子表 t_ocdbd_user_tag_entry

- **表名称：** 标签单据体-子表
- **表名：** t_ocdbd_user_tag_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftagid | 会员标签 | int8 | 64 |  | √ | 0 | 标签定义 ocdbd_user_tag |
| 3 | fcreatetime | 打标时间 | timestamp | 0 |  |  | null | 打标时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_tag_entry |  | fentryid |
| 2 | idx_ocdbd_usertagentry_ct |  | fcreatetime |
| 3 | idx_ocdbd_usertagentry_fid |  | fid |
| 4 | idx_ocdbd_usertagentry_tid |  | ftagid |

---

## 用户微信登录授权信息单据体-子表 t_ocdbd_user_wechat

- **表名称：** 用户微信登录授权信息单据体-子表
- **表名：** t_ocdbd_user_wechat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funionid | unionID | varchar | 80 |  | √ | ' ' | unionID |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | favatarurl | 头像 | varchar | 255 |  | √ | ' ' | 头像 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fapptypeid | 应用类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 7 | fnickname | 昵称 | varchar | 255 |  | √ | ' ' | 昵称 |
| 8 | fappid | 应用ID | varchar | 80 |  | √ | ' ' | 应用ID |
| 9 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 10 | flastip | 最后登录IP | varchar | 80 |  | √ | ' ' | 最后登录IP |
| 11 | fsubscribetime | 授权/关注时间 | timestamp | 0 |  |  | null | 授权/关注时间 |
| 12 | fopenid | openID | varchar | 80 |  | √ | ' ' | openID |
| 13 | fappname | 应用名称 | varchar | 80 |  | √ | ' ' | 应用名称 |
| 14 | fissubscribe | 是否关注公众号 | bpchar | 1 |  | √ | '0' | 是否关注公众号 |
| 15 | flasttime | 最后登录时间 | timestamp | 0 |  |  | null | 最后登录时间 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_user_wechat_fid |  | fid |
| 2 | pk_ocdbd_user_wechat |  | fentryid |
| 3 | idx_ocdbd_user_wechat_faoid |  | fappid,fopenid |

---

## 会员档案-主表 t_ocdbd_user

- **表名称：** 会员档案-主表
- **表名：** t_ocdbd_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 所属业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdistrict | 注册区/县 | varchar | 80 |  | √ | ' ' | 注册区/县 |
| 4 | fauthentication | fauthentication | bpchar | 1 |  | √ | '0' |  |
| 5 | foccupationid | 职业 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrcappname | 来源应用名称 | varchar | 80 |  | √ | ' ' | 来源应用名称 |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmobile | 手机号码 | varchar | 80 |  | √ | ' ' | 手机号码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fshortmobile | 手机号码(不带国际代码) | varchar | 80 |  | √ | ' ' | 手机号码(不带国际代码) |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fcity | 注册城市 | varchar | 80 |  | √ | ' ' | 注册城市 |
| 19 | fchannelid | 来源渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 20 | fidsystem | 入口ID体系 | bpchar | 1 |  | √ | 'A' | 入口ID体系,枚举: A :站内会员ID体系 B :微信授权ID体系 |
| 21 | fnationalityid | 民族 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fname | 姓名 | varchar | 80 |  | √ | ' ' | 姓名 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fbirthday | 生日 | timestamp | 0 |  |  | null | 生日 |
| 26 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 27 | feducationid | 学历 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | favatarurl | 头像 | varchar | 255 |  | √ | ' ' | 头像 |
| 30 | femail | 邮箱 | varchar | 80 |  | √ | ' ' | 邮箱 |
| 31 | fsplitid | 管理区隔 | int8 | 64 |  | √ | 0 | 管理区隔 ocdbd_usersplit |
| 32 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fmonthlyincomeid | 家庭月收入 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 34 | ftelephone | 固定电话 | varchar | 80 |  | √ | ' ' | 固定电话 |
| 35 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 36 | fsex | 性别 | bpchar | 1 |  | √ | '0' | 性别,枚举: 0 :保密 1 :男 2 :女 |
| 37 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 39 | fuserstatus | 会员状态 | bpchar | 1 |  | √ | 'B' | 会员状态,枚举: A :未激活 B :正常 C :已注销 |
| 40 | fsrcapptype | 来源应用类型 | bpchar | 1 |  | √ | 'A' | 来源应用类型,枚举: A :APP B :微信小程序 C :微信公众号 D :PC POS E :APP POS F :H5 G :网站 H :苍穹会员中心 I :企微小程序 |
| 41 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 42 | fprovince | 注册省份 | varchar | 80 |  | √ | ' ' | 注册省份 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fviplevelid | 会员等级 | int8 | 64 |  | √ | 0 | 会员等级定义 ocdbd_vip_level |
| 45 | fviptypeid | 会员类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 46 | fcustomerid | 所属客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 47 | fcountry | 注册国家 | varchar | 80 |  | √ | ' ' | 注册国家 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_user_fmobile |  | fmobile |
| 2 | idx_ocdbd_user_fnum |  | fnumber |
| 3 | pk_ocdbd_user |  | fid |
| 4 | idx_t_ocdbd_user_createorg |  | fcreateorgid |
| 5 | idx_ocdbd_user_fname |  | fname |
| 6 | idx_ocdbd_user_fcorgid |  | fcreateorgid |
| 7 | idx_t_ocdbd_user_master |  | fmasterid |
| 8 | idx_ocdbd_user_forgid |  | forgid |
| 9 | idx_ocdbd_user_fsmobile |  | fshortmobile |

---

## 纪念日单据体-子表 t_ocdbd_user_comm_entry

- **表名称：** 纪念日单据体-子表
- **表名：** t_ocdbd_user_comm_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftypeid | 纪念日类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 3 | fcomment | 备注 | varchar | 80 |  | √ | ' ' | 备注 |
| 4 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_user_comm_entry |  | fentryid |
| 2 | idx_ocdbd_usercommentry_fid |  | fid |
