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
| 4 | fjtmc | 集团名称 | int8 | 64 |  | √ | 0 | 千户集团 tcvvt_qhjt |
| 5 | fsjnsrmc | 上级税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fcontactno_enp | fcontactno_enp | text | 0 |  |  | null |  |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fusername | 填表人姓名 | varchar | 50 |  | √ | ' ' | 填表人姓名 |
| 10 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcellphoneno_enp | fcellphoneno_enp | text | 0 |  |  | null |  |
| 14 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fnsrsbh1 | fnsrsbh1 | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | ftbsx | 同步生效 | bpchar | 1 |  | √ | '0' | 同步生效 |
| 19 | fcurrentstatus | 当前状态 | varchar | 50 |  | √ | ' ' | 当前状态,枚举: 1 :生效 0 :失效 |
| 20 | fnsrmc | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fquoofreview | 企业集团确认情况 | varchar | 50 |  | √ | ' ' | 企业集团确认情况,枚举: 1 :属于 0 :不属于 |
| 22 | fcellphoneno | 填表人联系方式（手机号） | varchar | 50 |  | √ | ' ' | 填表人联系方式（手机号） |
| 23 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 24 | fsjnsrsbh | fsjnsrsbh | varchar | 50 |  | √ | ' ' |  |
| 25 | fbasedatafield | 统一社会信用代码 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: sdxz :手动新增 sjtb :数据同步 |
| 28 | fcontactno | 填表人联系方式（电话） | varchar | 50 |  | √ | ' ' | 填表人联系方式（电话） |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fycsjnsrmc | 上级企业统一信用代码 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |

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
