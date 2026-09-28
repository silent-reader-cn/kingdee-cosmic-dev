# 集团名册-tcvvt_group

## 集团名册-主表 t_tcvvt_group

- **表名称：** 集团名册-主表
- **表名：** t_tcvvt_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | floginaccount | 企业登录账号 | varchar | 50 |  | √ | ' ' | 企业登录账号 |
| 3 | fnsrsbh | fnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 4 | fjtmc | 集团名称 | int8 | 64 |  | √ | 0 | [千户集团 tcvvt_qhjt](../tcvvt_files/tcvvt_qhjt.md) |
| 5 | fsjnsrmc | 上级税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcontactno_enp | fcontactno_enp | text | 0 |  |  | null |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fusername | 填表人姓名 | varchar | 50 |  | √ | ' ' | 填表人姓名 |
| 10 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcellphoneno_enp | fcellphoneno_enp | text | 0 |  |  | null |  |
| 14 | fcity | 成员企业所在地市级 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 15 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fnsrsbh1 | fnsrsbh1 | varchar | 50 |  | √ | ' ' |  |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | ftbsx | 同步生效 | bpchar | 1 |  | √ | '0' | 同步生效 |
| 20 | fisenterpriseabroad | 是否境外企业 | bpchar | 1 |  | √ | '0' | 是否境外企业 |
| 21 | ftaxorgentry | 税务组织信息分录 | int8 | 64 |  | √ | 0 | [税务组织信息分录 bastax_taxorg_entry](../bastax_files/bastax_taxorg_entry.md) |
| 22 | fcurrentstatus | 当前状态 | varchar | 50 |  | √ | ' ' | 当前状态,枚举: 1 :生效 0 :失效 |
| 23 | fnsrmc | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fquoofreview | 企业集团确认情况 | varchar | 50 |  | √ | ' ' | 企业集团确认情况,枚举: 1 :属于 0 :不属于 |
| 25 | fcellphoneno | 填表人联系方式（手机号） | varchar | 50 |  | √ | ' ' | 填表人联系方式（手机号） |
| 26 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 27 | fsjnsrsbh | fsjnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 28 | fbasedatafield | 统一社会信用代码 | int8 | 64 |  | √ | 0 | [税务组织信息 bastax_taxorg](../bastax_files/bastax_taxorg.md) |
| 29 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: sdxz :手动新增 sjtb :数据同步 |
| 31 | fcontactno | 填表人联系方式（电话） | varchar | 50 |  | √ | ' ' | 填表人联系方式（电话） |
| 32 | fnumber | 编号 | varchar | 30 |  | √ | ' ' | 编号 |
| 33 | fycsjnsrmc | 上级企业统一信用代码 | int8 | 64 |  | √ | 0 | [税务组织信息 bastax_taxorg](../bastax_files/bastax_taxorg.md) |
| 34 | fprovince | 成员企业所在省级 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 35 | fcountry | 所属国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_group |  | fnsrmc |
| 2 | pk_tcvvt_group |  | fid |

---

## 集团名册-多语言表 t_tcvvt_group_l

- **表名称：** 集团名册-多语言表
- **表名：** t_tcvvt_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_group_l_0 |  | fid,flocaleid |
| 2 | pk_tcvvt_group_l |  | fpkid |
