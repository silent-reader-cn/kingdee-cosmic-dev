# 服务商设置-er_biz_info

## 服务商设置-多语言表 t_er_biz_info_l

- **表名称：** 服务商设置-多语言表
- **表名：** t_er_biz_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 服务商 | varchar | 100 |  | √ | ' ' | 服务商 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_biz_info_l_pkey |  | fpkid |
| 2 | idx_er_bizl_fid |  | fid,flocaleid |

---

## 组织-多选基础资料表 t_er_syncapplybiiorg

- **表名称：** 组织-多选基础资料表
- **表名：** t_er_syncapplybiiorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_syncapplybiiorg |  | fpkid |
| 2 | idx_er_entryid_basedataid |  | fentryid,fbasedataid |

---

## 单据体-子表 t_er_syncuserbyorg

- **表名称：** 单据体-子表
- **表名：** t_er_syncuserbyorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flastsyncstamp | 最后人员同步时间 | timestamp | 0 |  |  | null | 最后人员同步时间 |
| 3 | fentrystatus | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :可用 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_syncuserbyorg |  | fentryid |
| 2 | idx_er_subo_fid |  | fid,fseq |

---

## 商旅公司账号设置单据体-子表 t_er_tripcompanyinfo

- **表名称：** 商旅公司账号设置单据体-子表
- **表名：** t_er_tripcompanyinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | frealname | 真实姓名 | varchar | 50 |  | √ | ' ' | 真实姓名 |
| 4 | fstaffcode | 接口对接工号 | varchar | 50 |  | √ | ' ' | 接口对接工号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsignkey | 秘钥 | varchar | 255 |  | √ | ' ' | 秘钥 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcompanyid | 公司id | varchar | 100 |  | √ | ' ' | 公司id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_tripcompanyinfo_fid |  | fid,fseq |
| 2 | pk_t_er_tripcompanyinfo |  | fentryid |

---

## 服务商设置-主表 t_er_biz_info

- **表名称：** 服务商设置-主表
- **表名：** t_er_biz_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckingcurrency | 结算币种 | int8 | 64 |  | √ | 1 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fauthorizresyncuser | 员工授权再同步人员 | varchar | 1 |  | √ | '0' | 员工授权再同步人员 |
| 4 | flastsyncaccountorgtamp | 最后差量同步核算主体时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 最后差量同步核算主体时间戳 |
| 5 | fsyncapplybilltype | 申请单同步方式 | bpchar | 1 |  | √ | ' ' | 申请单同步方式,枚举: 1 :不控制 2 :全组织申请单同步 3 :部分组织申请单同步 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 修改时间 |
| 7 | fplatformid | 渠道ID | varchar | 255 |  | √ | ' ' | 渠道ID |
| 8 | fpayername | fpayername | varchar | 100 |  | √ | ' ' |  |
| 9 | flastsyncpeopletamp | 最后差量同步人员时间戳 | varchar | 50 |  | √ | ' ' | 最后差量同步人员时间戳 |
| 10 | fitemtrainid | fitemtrainid | int8 | 64 |  | √ | 0 |  |
| 11 | fsetcostorg | 费用承担获取 | bpchar | 1 |  | √ | '0' | 费用承担获取,枚举: 0 :按差旅报销单获取 1 :按服务商获取 |
| 12 | fbillingandtax | 根据订单的发票类型进行计税 | varchar | 1 |  | √ | '0' | 根据订单的发票类型进行计税,枚举: 1 :是 0 :否 |
| 13 | fmulticompanyid | 多公司账号 | bpchar | 1 |  | √ | '0' | 多公司账号 |
| 14 | flastsyncimagetamp | 影像信息同步时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 影像信息同步时间戳 |
| 15 | fname | 服务商 | varchar | 100 |  | √ | ' ' | 服务商 |
| 16 | fappkey | 接入appkey | varchar | 100 |  | √ | ' ' | 接入appkey |
| 17 | fenabledomestic | fenabledomestic | bpchar | 1 |  | √ | '0' |  |
| 18 | fcartype | 用车类型(废弃) | varchar | 100 |  | √ | ' ' | 用车类型(废弃),枚举: 1 :差旅用车 2 :公务出行用车 3 :工作日加班用车 4 :周末/节假日加班用车 |
| 19 | fappsecurity | 接入app秘钥 | varchar | 2000 |  | √ | ' ' | 接入app秘钥 |
| 20 | flastsyncorderbilltamp | 最后差量同步订单时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 最后差量同步订单时间戳 |
| 21 | fpayernum | fpayernum | varchar | 80 |  | √ | ' ' |  |
| 22 | forationid | 公司id | varchar | 100 |  | √ | ' ' | 公司id |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | flastsyncbusitamp | 最后消费记录获取时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 最后消费记录获取时间戳 |
| 26 | frsakey | 影像地址解密 | varchar | 1000 |  | √ | ' ' | 影像地址解密 |
| 27 | fitemcarid | fitemcarid | int8 | 64 |  | √ | 0 |  |
| 28 | fsyncreqbillsettleorg | 出差申请单/人员同步核算组织取值 | bpchar | 1 |  | √ | '0' | 出差申请单/人员同步核算组织取值,枚举: 0 :费用承担公司 1 :申请人公司 2 :无 |
| 29 | fsyncusertype | 人员同步方式 | bpchar | 1 |  | √ | '1' | 人员同步方式,枚举: 1 :全组织人员同步 2 :部分组织人员同步 |
| 30 | fdaily | 每月__日 | int8 | 64 |  | √ | 0 | 每月__日,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 24 :24 25 :25 26 :26 27 :27 28 :28 29 :29 30 :30 31 :31 |
| 31 | fpayerbank | fpayerbank | varchar | 100 |  | √ | ' ' |  |
| 32 | fplatformsn | 渠道秘钥 | varchar | 255 |  | √ | ' ' | 渠道秘钥 |
| 33 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :未审核 C :已审核 |
| 34 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fauthroziedcontent | 员工授权界面内容 | varchar | 600 |  | √ | ' ' | 员工授权界面内容 |
| 37 | fenablecar | fenablecar | bpchar | 1 |  | √ | '0' |  |
| 38 | fiteminternationalid | fiteminternationalid | int8 | 64 |  | √ | 0 |  |
| 39 | fauthroziedcontent_tag | 员工授权界面内容_详情 | text | 0 |  |  | null | 员工授权界面内容_详情 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 创建时间 |
| 42 | fautoopened | 自助开通 | varchar | 1 |  | √ | '0' | 自助开通 |
| 43 | fproviderid | 服务商关联 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 44 | fitemdomesticid | fitemdomesticid | int8 | 64 |  | √ | 0 |  |
| 45 | fenablehotel | fenablehotel | bpchar | 1 |  | √ | '0' |  |
| 46 | freservedfield1 | 自定义字段1 | varchar | 500 |  | √ | ' ' | 自定义字段1 |
| 47 | freservedfield2 | 自定义字段2 | varchar | 500 |  | √ | ' ' | 自定义字段2 |
| 48 | freservedfield3 | 自定义字段3 | varchar | 1500 |  | √ | ' ' | 自定义字段3 |
| 49 | fitemhotelid | fitemhotelid | int8 | 64 |  | √ | 0 |  |
| 50 | fpayeraccount | fpayeraccount | varchar | 100 |  | √ | ' ' |  |
| 51 | fenabletrain | fenabletrain | bpchar | 1 |  | √ | '0' |  |
| 52 | freservedfield4 | 自定义字段4 | varchar | 100 |  | √ | ' ' | 自定义字段4 |
| 53 | flastsyncorgtamp | 最后差量同步组织时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 最后差量同步组织时间戳 |
| 54 | freservedfield5 | 自定义字段5 | varchar | 100 |  | √ | ' ' | 自定义字段5 |
| 55 | fenableinternational | fenableinternational | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_biz_info_pkey |  | fid |
| 2 | idx_er_bizin_fnumber |  | fnumber |

---

## 同步申请单类型-多选基础资料表 t_er_applybilltype

- **表名称：** 同步申请单类型-多选基础资料表
- **表名：** t_er_applybilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_entryid_basedataid |  | fentryid,fbasedataid |
| 2 | pk_t_er_applybilltype |  | fpkid |

---

## 申请单同步方式单据体-子表 t_er_syncapplybilltype

- **表名称：** 申请单同步方式单据体-子表
- **表名：** t_er_syncapplybilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fbookproducts | 出差申请单可预订产品 | varchar | 50 |  | √ | ' ' | 出差申请单可预订产品,枚举: 1 :国内机票 2 :国际机票 3 :国内酒店 4 :国际酒店 5 :火车预订 6 :用车预订 7 :用餐预定 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_syncapplybilltype |  | fentryid |
| 2 | idx_er_seq_fid |  | fid,fseq |
