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

## 单据体-子表 t_er_syncuserbyorg

- **表名称：** 单据体-子表
- **表名：** t_er_syncuserbyorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flastsyncstamp | 最后人员同步时间 | timestamp | 0 |  |  | null | 最后人员同步时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

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

## 服务商设置-主表 t_er_biz_info

- **表名称：** 服务商设置-主表
- **表名：** t_er_biz_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemcarid | fitemcarid | int8 | 64 |  | √ | 0 |  |
| 3 | fsyncreqbillsettleorg | 出差申请单/人员同步核算组织取值 | bpchar | 1 |  | √ | '0' | 出差申请单/人员同步核算组织取值,枚举: 0 :费用承担公司 1 :申请人公司 2 :无 |
| 4 | fcheckingcurrency | 结算币别 | int8 | 64 |  | √ | 1 | 币种 bd_currency |
| 5 | fsyncusertype | 人员同步方式 | bpchar | 1 |  | √ | '1' | 人员同步方式,枚举: 1 :全组织人员同步 2 :部分组织人员同步 |
| 6 | fauthorizresyncuser | 员工授权再同步人员 | varchar | 1 |  | √ | '0' | 员工授权再同步人员 |
| 7 | fdaily | 每月__日 | int8 | 64 |  | √ | 0 | 每月__日,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 24 :24 25 :25 26 :26 27 :27 28 :28 29 :29 30 :30 31 :31 |
| 8 | fpayerbank | fpayerbank | varchar | 100 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :未审核 C :已审核 |
| 11 | fpayername | fpayername | varchar | 100 |  | √ | ' ' |  |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | flastsyncpeopletamp | 最后差量同步人员时间戳 | varchar | 50 |  | √ | ' ' | 最后差量同步人员时间戳 |
| 15 | fitemtrainid | fitemtrainid | int8 | 64 |  | √ | 0 |  |
| 16 | fauthroziedcontent | 员工授权界面内容 | varchar | 600 |  | √ | ' ' | 员工授权界面内容 |
| 17 | fenablecar | fenablecar | bpchar | 1 |  | √ | '0' |  |
| 18 | fiteminternationalid | fiteminternationalid | int8 | 64 |  | √ | 0 |  |
| 19 | fsetcostorg | 费用承担获取 | bpchar | 1 |  | √ | '0' | 费用承担获取,枚举: 0 :按差旅报销单获取 1 :按服务商获取 |
| 20 | fauthroziedcontent_tag | 员工授权界面内容_详情 | text | 0 |  |  | null | 员工授权界面内容_详情 |
| 21 | fbillingandtax | 根据订单票价的实际发票类型进行开票与计税 | varchar | 1 |  | √ | '0' | 根据订单票价的实际发票类型进行开票与计税,枚举: 1 :是 0 :否 |
| 22 | flastsyncimagetamp | 影像信息同步时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 影像信息同步时间戳 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fname | 服务商 | varchar | 100 |  | √ | ' ' | 服务商 |
| 25 | fappkey | 接入appkey | varchar | 100 |  | √ | ' ' | 接入appkey |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 创建时间 |
| 27 | fenabledomestic | fenabledomestic | bpchar | 1 |  | √ | '0' |  |
| 28 | fproviderid | 服务商关联 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | fcartype | 用车类型(废弃) | varchar | 100 |  | √ | ' ' | 用车类型(废弃),枚举: 1 :差旅用车 2 :公务出行用车 3 :工作日加班用车 4 :周末/节假日加班用车 |
| 30 | fitemdomesticid | fitemdomesticid | int8 | 64 |  | √ | 0 |  |
| 31 | fappsecurity | 接入app秘钥 | varchar | 100 |  | √ | ' ' | 接入app秘钥 |
| 32 | fenablehotel | fenablehotel | bpchar | 1 |  | √ | '0' |  |
| 33 | freservedfield1 | 自定义字段1 | varchar | 100 |  | √ | ' ' | 自定义字段1 |
| 34 | freservedfield2 | 自定义字段2 | varchar | 100 |  | √ | ' ' | 自定义字段2 |
| 35 | flastsyncorderbilltamp | 最后差量同步订单时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 最后差量同步订单时间戳 |
| 36 | freservedfield3 | 自定义字段3 | varchar | 1500 |  | √ | ' ' | 自定义字段3 |
| 37 | fpayernum | fpayernum | varchar | 80 |  | √ | ' ' |  |
| 38 | fitemhotelid | fitemhotelid | int8 | 64 |  | √ | 0 |  |
| 39 | forationid | 公司id | varchar | 100 |  | √ | ' ' | 公司id |
| 40 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fpayeraccount | fpayeraccount | varchar | 100 |  | √ | ' ' |  |
| 42 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 43 | fenabletrain | fenabletrain | bpchar | 1 |  | √ | '0' |  |
| 44 | freservedfield4 | 自定义字段4 | varchar | 100 |  | √ | ' ' | 自定义字段4 |
| 45 | flastsyncorgtamp | 最后差量同步组织时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 最后差量同步组织时间戳 |
| 46 | freservedfield5 | 自定义字段5 | varchar | 100 |  | √ | ' ' | 自定义字段5 |
| 47 | flastsyncbusitamp | 最后消费记录获取时间戳 | varchar | 50 |  | √ | '1900-01-01 00:00:00' | 最后消费记录获取时间戳 |
| 48 | fenableinternational | fenableinternational | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_biz_info_pkey |  | fid |
| 2 | idx_er_bizin_fnumber |  | fnumber |
