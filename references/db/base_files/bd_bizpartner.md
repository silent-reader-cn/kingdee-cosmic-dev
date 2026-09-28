# 商务伙伴-bd_bizpartner

## 商务伙伴-主表 t_bd_bizpartner

- **表名称：** 商务伙伴-主表
- **表名：** t_bd_bizpartner

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fapproverid | fapproverid | int8 | 64 |  |  | null |  |
| 3 | flogo | 图片 | varchar | 255 |  |  | null | 图片 |
| 4 | fmodifyorgid | fmodifyorgid | int8 | 64 |  |  | null |  |
| 5 | faddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |
| 6 | fissupplier | 供应商 | bpchar | 1 |  |  | null | 供应商 |
| 7 | fsocietycreditcode | 统一社会信用代码 | varchar | 255 |  |  | null | 统一社会信用代码 |
| 8 | forgcode | 组织机构代码 | varchar | 255 |  |  | null | 组织机构代码 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fcuregcapital | 注册资本币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fbusilicence | fbusilicence | varchar | 255 |  |  | null |  |
| 12 | fidno | 身份证号 | varchar | 50 |  | √ | ' ' | 身份证号 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbusinessscope | 经营范围 | varchar | 2000 |  | √ | ' ' | 经营范围 |
| 15 | fstatus | 数据状态 | varchar | 30 |  |  | null | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fpostalcode | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 19 | finternalcompanyid | 内部业务单元 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fcorporation | 集团总公司 | bpchar | 1 |  | √ | '0' | 集团总公司 |
| 21 | festablishdate | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 22 | ffax | 传真 | varchar | 40 |  |  | null | 传真 |
| 23 | fadmindivision | 行政区划 | varchar | 100 |  | √ | ' ' | 行政区划 |
| 24 | faffiliatedgroup | 所属集团 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 25 | fapprovedate | fapprovedate | timestamp | 0 |  |  | null |  |
| 26 | fphone | 联系电话 | varchar | 60 |  |  | null | 联系电话 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fcountryid | 国家/地区 | int8 | 64 |  |  | null | [国家和地区 bd_country](../base_files/bd_country.md) |
| 31 | fdisablerid | 禁用人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fregcapital | 注册资本 | varchar | 40 |  | √ | ' ' | 注册资本 |
| 33 | fyzjid | 云之家内码 | varchar | 36 |  |  | null | 云之家内码 |
| 34 | fbackgroundimg | fbackgroundimg | varchar | 255 |  |  | null |  |
| 35 | fbusiexequatur | fbusiexequatur | varchar | 255 |  |  | null |  |
| 36 | fduns | 邓白氏编码 | varchar | 9 |  | √ | ' ' | 邓白氏编码 |
| 37 | ftype | 伙伴类型 | varchar | 30 |  |  | null | 伙伴类型,枚举: 1 :法人企业 2 :非法人企业 3 :非企业单位 4 :个人 5 :个体户 |
| 38 | fiscustomer | 客户 | bpchar | 1 |  |  | null | 客户 |
| 39 | fsimplename | 简称 | varchar | 255 |  | √ | ' ' | 简称 |
| 40 | fpartnerrole | 伙伴角色 | varchar | 30 |  | √ | ' ' | 伙伴角色,枚举: 1 :供应商 2 :客户 3 :渠道 |
| 41 | furl | 公司网址 | varchar | 255 |  |  | null | 公司网址 |
| 42 | fenable | 使用状态 | bpchar | 1 |  |  | null | 使用状态,枚举: 0 :禁用 1 :可用 |
| 43 | fbizregisterno | 工商登记号 | varchar | 255 |  |  | null | 工商登记号 |
| 44 | fnumber | 编码 | varchar | 80 |  |  | null | 编码 |
| 45 | fbusinessterm | 营业期限 | varchar | 60 |  | √ | ' ' | 营业期限 |
| 46 | ftxregisterno | 纳税人识别号 | varchar | 255 |  |  | null | 纳税人识别号 |
| 47 | flinkman | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 48 | fartificialperson | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_bizpartner_number |  | fnumber |
| 2 | idx_t_bd_bizpartner_fpartnerro |  | fpartnerrole |
| 3 | t_bd_bizpartner_pkey |  | fid |
| 4 | idx_t_bd_bizpartner_intcmpid |  | finternalcompanyid |

---

## 商务伙伴-多语言表 t_bd_bizpartner_l

- **表名称：** 商务伙伴-多语言表
- **表名：** t_bd_bizpartner_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fbusinessscope | 经营范围 | varchar | 2000 |  | √ | ' ' | 经营范围 |
| 3 | fname | 名称 | varchar | 255 |  | √ | null | 名称 |
| 4 | faddress | 详细地址 | varchar | 300 |  | √ | ' ' | 详细地址 |
| 5 | fsimplename | 简称 | varchar | 255 |  |  | null | 简称 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 7 | fbusinessterm | 营业期限 | varchar | 60 |  | √ | ' ' | 营业期限 |
| 8 | flinkman | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 9 | fartificialperson | 法人代表 | varchar | 255 |  |  | null | 法人代表 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 11 | fregcapital | 注册资本 | varchar | 40 |  | √ | ' ' | 注册资本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_bizpartner_l_fid |  | fid,flocaleid |
| 2 | idx_bd_bizpartner_l_fname |  | fname |
| 3 | t_bd_bizpartner_l_pkey |  | fpkid |
