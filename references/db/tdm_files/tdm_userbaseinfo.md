# 人员基础信息-tdm_userbaseinfo

## 人员基础信息-主表 t_tdm_user_baseinfo

- **表名称：** 人员基础信息-主表
- **表名：** t_tdm_user_baseinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcardno | 证件号码 | varchar | 50 |  | √ | ' ' | 证件号码 |
| 3 | femploydate | 任职受雇从业日期 | timestamp | 0 |  |  | null | 任职受雇从业日期 |
| 4 | femploytype | 任职受雇从业类型 | varchar | 50 |  | √ | ' ' | 任职受雇从业类型,枚举: 1 :雇员 0 :其他 |
| 5 | fnsrsbh | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |
| 6 | fspecialgrouptype | 特殊群体类型 | varchar | 50 |  | √ | ' ' | 特殊群体类型,枚举: 0 :残疾人 1 :自主退役士兵 2 :建档立卡贫困人口 3 :登记失业半年以上人员 4 :毕业年度内高校毕业生 |
| 7 | finworkcase | 入职年度就业情形 | varchar | 50 |  | √ | ' ' | 入职年度就业情形,枚举: stu :当年首次入职学生 oth :当年首次入职其它人员 |
| 8 | faccount | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 9 | fdisablilitytype | 残疾证件类型 | varchar | 50 |  | √ | ' ' | 残疾证件类型,枚举: 1 :残疾证 2 :残疾军人证 3 :伤残人民警察证 4 :残疾消防救援人员证 5 :伤残预备役人员、伤残民兵民工证 7 :因公伤残人员证 |
| 10 | fspecialcase | 是否存在以下情形 | varchar | 50 |  | √ | ' ' | 是否存在以下情形,枚举: a :残疾 b :烈属 c :孤老 |
| 11 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | finvistmentratio | 个人投资比例 | numeric | 23 | 10 | √ | 0 | 个人投资比例 |
| 14 | feducational | 学历 | varchar | 50 |  | √ | ' ' | 学历,枚举: 3 :研究生 2 :大学本科 1 :大学本科以下 |
| 15 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 16 | fkhyhsf | 开户银行省份 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 17 | fisspecialgroup | 特殊群体 | bpchar | 1 |  | √ | '0' | 特殊群体 |
| 18 | femail | 电子邮箱 | varchar | 50 |  | √ | ' ' | 电子邮箱 |
| 19 | fothercardtype | 其他证件类型 | varchar | 50 |  | √ | ' ' | 其他证件类型,枚举: 3 :港澳居民来往内地通行证 4 :台湾居民来往大陆通行证 7 :外国护照 |
| 20 | fisresignsocialsecurity | 离职当月是否缴纳社保 | varchar | 50 |  | √ | ' ' | 离职当月是否缴纳社保,枚举: 1 :是 0 :否 |
| 21 | ftelephone | 手机号码 | varchar | 50 |  | √ | ' ' | 手机号码 |
| 22 | fpersoninvestamount | 个人投资额 | numeric | 23 | 10 | √ | 0 | 个人投资额 |
| 23 | ftakeeffectdate | 证件生效日期 | timestamp | 0 |  |  | null | 证件生效日期 |
| 24 | fbirthplace | 出生国家（地区） | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 25 | fisdeductfee | 是否扣除减除费用 | varchar | 50 |  | √ | ' ' | 是否扣除减除费用,枚举: 1 :是 0 :否 |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fusualresidence | 经常居住地 | int8 | 64 |  | √ | 0 | 地址 cts_address |
| 28 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 29 | fcountry | 国籍 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 30 | fsocialsecuritydate | 缴纳社保起始月份 | timestamp | 0 |  |  | null | 缴纳社保起始月份 |
| 31 | fdiscardnumber | 证件编号 | varchar | 50 |  | √ | ' ' | 证件编号 |
| 32 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 35 | finnerouter | 境内人员/境外人员 | varchar | 50 |  | √ | ' ' | 境内人员/境外人员,枚举: inner :境内 outer :境外 |
| 36 | fposition | 职务 | varchar | 50 |  | √ | ' ' | 职务,枚举: 1 :高层 2 :普通 |
| 37 | fqtqksm | 其他情况说明 | varchar | 50 |  | √ | ' ' | 其他情况说明,枚举: 1 :扣缴申报利息股息红利所得 2 :扣缴申报偶然所得 3 :申报其他所得 |
| 38 | flieshuzhenghao | 烈属证号 | varchar | 50 |  | √ | ' ' | 烈属证号 |
| 39 | fupdatedate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fbirthday | 出生日期 | timestamp | 0 |  |  | null | 出生日期 |
| 42 | fterminationdate | 离职日期 | timestamp | 0 |  |  | null | 离职日期 |
| 43 | fscrjsj | 首次入境时间 | timestamp | 0 |  |  | null | 首次入境时间 |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fcardtype | 证件类型 | varchar | 50 |  | √ | ' ' | 证件类型,枚举: 1 :居民身份证 2 :中国护照 3 :港澳居民来往内地通行证 4 :台湾居民来往大陆通行证 5 :港澳居民居住证 6 :台湾居民居住证 7 :外国护照 8 :外国人永久居留身份证 9 :外国人工作许可证(A类) 10 :外国人工作许可证(B类) 11 :外国人工作许可证(C类) |
| 46 | fothercardno | 其他证件号码 | varchar | 50 |  | √ | ' ' | 其他证件号码 |
| 47 | fworkno | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
| 48 | fbank | 开户银行 | varchar | 50 |  | √ | ' ' | 开户银行 |
| 49 | fregisteredlresidence | 户籍地址 | int8 | 64 |  | √ | 0 | 地址 cts_address |
| 50 | fdisablilitycardno | 残疾证号 | varchar | 50 |  | √ | ' ' | 残疾证号 |
| 51 | fsex | 性别 | varchar | 50 |  | √ | ' ' | 性别,枚举: 1 :男 0 :女 |
| 52 | floseefficacydate | 证件失效日期 | timestamp | 0 |  |  | null | 证件失效日期 |
| 53 | fyjljsj | 预计离境时间 | timestamp | 0 |  |  | null | 预计离境时间 |
| 54 | fsssy | 涉税事由 | varchar | 50 |  | √ | ' ' | 涉税事由,枚举: 1 :任职受雇 2 :提供临时劳务 3 :转让财产 4 :从事投资和经验活动 5 :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_user_baseinfo |  | fid |
| 2 | idx_tdm_user_baseinfo |  | fnumber |

---

## 人员基础信息-多语言表 t_tdm_user_baseinfo_l

- **表名称：** 人员基础信息-多语言表
- **表名：** t_tdm_user_baseinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_user_baseinfo_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_user_baseinfo_l |  | fpkid |
