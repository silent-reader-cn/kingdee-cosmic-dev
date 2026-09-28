# 纳税主体信息-tctb_tax_main

## 人员信息-子表 t_tctb_per_information

- **表名称：** 人员信息-子表
- **表名：** t_tctb_per_information

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | ffixedtelephone | 固定电话 | varchar | 100 |  | √ | ' ' | 固定电话 |
| 4 | ffullname | 姓名 | varchar | 100 |  | √ | ' ' | 姓名 |
| 5 | fmobilephone | 手机 | varchar | 100 |  | √ | ' ' | 手机 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fposition | 职位 | varchar | 30 |  | √ | ' ' | 职位,枚举: 1 :董事长 2 :总经理 3 :财务负责人 4 :税务会计 6 :税务负责人 5 :其它 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_per_information_fk |  | fid |
| 2 | t_tctb_per_information_pkey |  | fentryid |

---

## 纳税主体信息-主表 t_tctb_tax_main

- **表名称：** 纳税主体信息-主表
- **表名：** t_tctb_tax_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finternalfinance | 集团内部融资 | bpchar | 1 |  | √ | '0' | 集团内部融资 |
| 3 | finstrument | 持有股份或其他权益工具 | bpchar | 1 |  | √ | '0' | 持有股份或其他权益工具 |
| 4 | fregisteraddress | 注册登记区域 | varchar | 50 |  | √ | ' ' | 注册登记区域 |
| 5 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [税务组织信息 bastax_taxorg](../bastax_files/bastax_taxorg.md) |
| 6 | fregisteredcurrency | 注册资金币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fotherbusiness | 其他 | bpchar | 1 |  | √ | '0' | 其他 |
| 9 | fbranchno | 分支机构编码 | varchar | 50 |  | √ | ' ' | 分支机构编码 |
| 10 | fmaincompany | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 11 | finsure | 保险 | bpchar | 1 |  | √ | '0' | 保险 |
| 12 | funifiedsocialcode | 统一社会信用代码（已弃用） | varchar | 100 |  | √ | ' ' | 统一社会信用代码（已弃用） |
| 13 | frestrictbanindustry | 从事国家限制和禁止行业 | bpchar | 1 |  | √ | '0' | 从事国家限制和禁止行业 |
| 14 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fadmindivisionfield | 企业实际经营区域 | varchar | 50 |  | √ | ' ' | 企业实际经营区域 |
| 16 | fregulatedareas | 组织标签 | int8 | 64 |  | √ | 0 | [标签设置 tctb_label_group](../tctb_files/tctb_label_group.md) |
| 17 | factualaddrdetail | 企业实际经营详细地址 | varchar | 255 |  | √ | ' ' | 企业实际经营详细地址 |
| 18 | fqhclique | 千户集团（废弃） | bpchar | 1 |  | √ | '0' | 千户集团（废弃） |
| 19 | fbusinessremark | 补充说明 | varchar | 1000 |  | √ | ' ' | 补充说明 |
| 20 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 21 | ftaxorgentryid | 税务组织分录 | int8 | 64 |  | √ | 0 | [税务组织信息分录 bastax_taxorg_entry](../bastax_files/bastax_taxorg_entry.md) |
| 22 | fretiredsoldiers | 退役士兵 | bpchar | 1 |  | √ | ' ' | 退役士兵 |
| 23 | ffinancialservice | 金融服务 | bpchar | 1 |  | √ | '0' | 金融服务 |
| 24 | fmanufacture | 生产制造 | bpchar | 1 |  | √ | '0' | 生产制造 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fassets | 持有或管理无形资产 | bpchar | 1 |  | √ | '0' | 持有或管理无形资产 |
| 27 | flabor | 向非关联方提供劳务 | bpchar | 1 |  | √ | '0' | 向非关联方提供劳务 |
| 28 | facctcustomer | 对应客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 29 | fisinitial | 是否初始化 | bpchar | 1 |  | √ | ' ' | 是否初始化 |
| 30 | fregistertime | 企业登记时间 | timestamp | 0 |  |  | null | 企业登记时间 |
| 31 | fnonenterprises | 非营运企业 | bpchar | 1 |  | √ | '0' | 非营运企业 |
| 32 | fnewrule | 执行新准则 | varchar | 50 |  | √ | ' ' | 执行新准则,枚举: yes :已执行 no :未执行 empty : |
| 33 | fregistertype | 登记注册类型 | int8 | 64 |  | √ | 0 | [注册登记类型 tax_info_registertype](../tctb_files/tax_info_registertype.md) |
| 34 | fregisteredcapital | 注册资金 | numeric | 23 | 10 | √ | 0.0000000000 | 注册资金 |
| 35 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 36 | fregisteraddrdetail | 注册登记详细地址 | varchar | 255 |  | √ | ' ' | 注册登记详细地址 |
| 37 | ftaxoffice | 主管税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 38 | ffinancialstatement | 财务报表报送（废弃）） | bpchar | 1 |  | √ | '1' | 财务报表报送（废弃）） |
| 39 | ftaxjurisdiction | 税收管辖地 | bpchar | 1 |  | √ | '0' | 税收管辖地 |
| 40 | farmyrelatives | 随军家属 | bpchar | 1 |  | √ | ' ' | 随军家属 |
| 41 | ftras | 重点税源（废弃） | bpchar | 1 |  | √ | '0' | 重点税源（废弃） |
| 42 | fentitytype | 实体类型 | varchar | 50 |  | √ | ' ' | 实体类型,枚举: legal :法人 institution :机构组织 |
| 43 | fpurchase | 采购 | bpchar | 1 |  | √ | '0' | 采购 |
| 44 | fregisternumber | 注册登记人数 | int8 | 64 |  | √ | 0 | 注册登记人数 |
| 45 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 46 | fstatus | 税务组织状态（已弃用） | varchar | 30 |  | √ | ' ' | 税务组织状态（已弃用）,枚举: 2 :可用 3 :禁用 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | ftaxpayer | 纳税人名称（已弃用） | varchar | 100 |  | √ | ' ' | 纳税人名称（已弃用） |
| 49 | fmilitarycadres | 军队干部 | bpchar | 1 |  | √ | ' ' | 军队干部 |
| 50 | faccountingstandards | faccountingstandards | varchar | 30 |  | √ | ' ' |  |
| 51 | fbaseregisteraddress | 登记区域 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 52 | ffinancetaxperiod | 财务报表申报期限（废弃）） | varchar | 50 |  | √ | ' ' | 财务报表申报期限（废弃））,枚举: aysb :按月申报 ajsb :按季申报 |
| 53 | fisentity | 纳税主体（已弃用） | bpchar | 1 |  | √ | '0' | 纳税主体（已弃用） |
| 54 | fregisterassets | 注册登记资产 | numeric | 23 | 10 | √ | 0 | 注册登记资产 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 57 | fcodeandname | 所属行业代码及名称 | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 58 | fcontactinformation | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 59 | fregisterplace | 注册地 | bpchar | 1 |  | √ | '0' | 注册地 |
| 60 | fothers | 其它 | bpchar | 1 |  | √ | ' ' | 其它 |
| 61 | fkeygroup | 重点群体 | bpchar | 1 |  | √ | ' ' | 重点群体 |
| 62 | fdevelopment | 研发 | bpchar | 1 |  | √ | '0' | 研发 |
| 63 | famsservice | 行政、管理或支持服务 | bpchar | 1 |  | √ | '0' | 行政、管理或支持服务 |
| 64 | fsales | 销售、市场营销或分销 | bpchar | 1 |  | √ | '0' | 销售、市场营销或分销 |
| 65 | flegalpeople | 法人代表/负责人 | varchar | 100 |  | √ | ' ' | 法人代表/负责人 |
| 66 | faccountcriterion | 适用会计准则或会计制度 | int8 | 64 |  | √ | 0 | 会计准则业务定义分录 tpo_tccit_bizdef_kjzz |
| 67 | fbusinessscop | 经营范围 | varchar | 1000 |  | √ | ' ' | 经营范围 |
| 68 | facctsupplier | 对应供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_tax_main_pkey |  | fid |
| 2 | idx_tctb_tax_main |  | forgid |

---

## 印花税单据体（勿删）-子表 t_tctb_yhs_entry

- **表名称：** 印花税单据体（勿删）-子表
- **表名：** t_tctb_yhs_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcsd_bizdef_entry |
| 3 | fisverify | 是否核定征收 | bpchar | 1 |  | √ | ' ' | 是否核定征收 |
| 4 | fhdrate | 核定比例 | numeric | 23 | 10 | √ | 0.0000000000 | 核定比例 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdeclaretype | 申报期限类型 | varchar | 50 |  | √ | ' ' | 申报期限类型,枚举: aqsb :按期申报 acsb :按次申报 |
| 7 | fenddate | 核定期限结束日期 | timestamp | 0 |  |  | null | 核定期限结束日期 |
| 8 | fstartdate | 核定期限开始日期 | timestamp | 0 |  |  | null | 核定期限开始日期 |
| 9 | feffectivedate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 10 | fperiod | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: |
| 11 | ftaxrateid | 征收品目 | int8 | 64 |  | √ | 0 | 印花税税率 tpo_tcsd_taxrateentry |
| 12 | fexpirydate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_yhs_entry_pkey |  | fentryid |
| 2 | idx_tctb_yhs_entry_fk |  | fid |

---

## 海外税单据体-子表 t_tctb_hws_entry

- **表名称：** 海外税单据体-子表
- **表名：** t_tctb_hws_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhwsdeadline | 纳税周期 | varchar | 50 |  | √ | ' ' | 纳税周期,枚举: month :月 season :季 halfyear :半年 year :年 |
| 3 | fhwstaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftaxarea | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 6 | fhwsenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_hws_entry |  | fentryid |
| 2 | idx_tctb_hws_entry_fk |  | fid |

---

## 个人所得税单据体（勿删）-子表 t_tctb_grsds_entry

- **表名称：** 个人所得税单据体（勿删）-子表
- **表名：** t_tctb_grsds_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feffectiveend | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | feffectivestart | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcollectrate | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_grsds_entry |  | fentryid |
| 2 | idx_t_tctb_grsds_entry |  | fid |

---

## 消费税单据体（勿删）-子表 t_tctb_xfs_entry

- **表名称：** 消费税单据体（勿删）-子表
- **表名：** t_tctb_xfs_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | ftaxrate | 税种品目 | varchar | 30 |  | √ | ' ' | 税种品目,枚举: |
| 4 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fxfstaxitemrate | 税目 | int8 | 64 |  | √ | 0 | 消费税税收分类编码表 tpo_tcct_taxrateentry |
| 6 | fperiod | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :手工录入 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_xfs_entry_fk |  | fid |
| 2 | t_tctb_xfs_entry_pkey |  | fentryid |

---

## 征收环节-多选基础资料表 t_tctb_taxinfo_point

- **表名称：** 征收环节-多选基础资料表
- **表名：** t_tctb_taxinfo_point

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [征收环节 tctb_taxpoint](../tctb_files/tctb_taxpoint.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_taxinfo_point_fk |  | fentryid |
| 2 | pk_tctb_taxinfo_point |  | fpkid |

---

## 税种单据体-子表 t_tctb_categoryinfo

- **表名称：** 税种单据体-子表
- **表名：** t_tctb_categoryinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 税种信息主键 | int8 | 64 |  | √ | 0 | 税种信息主键 |
| 2 | fresidenttype | 居民企业类型 | varchar | 50 |  | √ | ' ' | 居民企业类型,枚举: jmqy :居民企业 fjmqy :非居民企业 |
| 3 | forgplace | 组织所在地 | varchar | 30 |  | √ | ' ' | 组织所在地,枚举: cityarea :市区 nocityarea :县城、镇 otherarea :其他 |
| 4 | flevytype | 征收方式 | varchar | 30 |  | √ | ' ' | 征收方式,枚举: czzs :查账征收 aqhz :按期汇总 hdzs :核定征收 : : : : |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ffarmdeducttype | 农产品核定扣除 | varchar | 50 |  | √ | ' ' | 农产品核定扣除,枚举: none :不适用 in-out :投入产出法 |
| 7 | fjyffjenable | 教育费附加启用 | varchar | 30 |  | √ | ' ' | 教育费附加启用,枚举: 2 :已启用 5 :未启用 |
| 8 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fcztdsysenable | 城镇土地使用税启用 | varchar | 30 |  | √ | ' ' | 城镇土地使用税启用,枚举: 3 :已启用 6 :未启用 |
| 10 | faddjyffj | 教育费附加 | varchar | 100 |  | √ | ' ' | 教育费附加 |
| 11 | ftaxpayertype | 纳税人类型 | varchar | 30 |  | √ | ' ' | 纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 12 | fsubmissionform | 默认报送表单 | varchar | 50 |  | √ | ' ' | 默认报送表单,枚举: zcfzb :资产负债表 lrb :利润表 xjllb :现金流量表 syzqybdb :所有者权益变动表 scjyxxb :生产经营信息表 qykjzzfz :企业会计准则附注 |
| 13 | ftaxtype | 税种 | varchar | 30 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fjsf :附加税费 fcscztdsys :房产税和城镇土地使用税 xfs :消费税 hjbhs :环境保护税 szys :水资源税 qtsf :其他税费 tdzzs :土地增值税 cwbb :财务报表 qhjt :千户集团 zdsy :重点税源 zys :资源税 grsds :个人所得税 |
| 14 | ffcs | 房产税 | varchar | 50 |  | √ | ' ' | 房产税 |
| 15 | fqsyfdate | 起始月份 | timestamp | 0 |  |  | null | 起始月份 |
| 16 | fyssdtaxrate | 应税所得率 | numeric | 23 | 10 | √ | 0 | 应税所得率 |
| 17 | fcztdsys | 城镇土地使用税 | varchar | 50 |  | √ | ' ' | 城镇土地使用税 |
| 18 | faddcswhjss | 城市建设附加税 | varchar | 100 |  | √ | ' ' | 城市建设附加税 |
| 19 | ffcsenable | 房产税启用 | varchar | 30 |  | √ | ' ' | 房产税启用,枚举: 2 :已启用 5 :未启用 |
| 20 | fadddfjyffj | 地方教育费附加 | varchar | 100 |  | √ | ' ' | 地方教育费附加 |
| 21 | fhdzstype | 核定征收方式 | varchar | 50 |  | √ | ' ' | 核定征收方式,枚举: rate-income :核定应税所得率（能核算收入总额的） rate-cost :核定应税所得率（能核算成本费用总额的） amount-income :核定应纳所得税额 |
| 22 | fdfjyffjenable | 地方教育附加启用 | varchar | 30 |  | √ | ' ' | 地方教育附加启用,枚举: 3 :已启用 6 :未启用 |
| 23 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 24 | fbackgroundpic | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 25 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: acsb :按次申报 aysb :按月申报 ajsb :按季申报 |
| 26 | fenable | 启用 | varchar | 30 |  | √ | ' ' | 启用,枚举: 1 :已启用 0 :未启用 |
| 27 | fdeclareperiod | 申报期限 | varchar | 50 |  | √ | ' ' | 申报期限,枚举: aysb :按月申报 ajsb :按季申报 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fcswhjssenable | 城市维护建设税启用 | varchar | 30 |  | √ | ' ' | 城市维护建设税启用,枚举: 1 :已启用 4 :未启用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_categoryinfo_fk |  | fid |
| 2 | t_tctb_categoryinfo_pkey |  | fentryid |

---

## 纳税信息级别-子表 t_tctb_tax_creditrating

- **表名称：** 纳税信息级别-子表
- **表名：** t_tctb_tax_creditrating

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fcreditlevel | 信用级别 | varchar | 30 |  | √ | ' ' | 信用级别,枚举: A :A B :B M :M C :C D :D |
| 4 | fyear | 年度 | timestamp | 0 |  |  | null | 年度 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fratingscore | 评级分数 | varchar | 100 |  | √ | ' ' | 评级分数 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_tax_creditrating_fk |  | fid |
| 2 | t_tctb_tax_creditrating_pkey |  | fentryid |

---

## 组织标签-多选基础资料表 t_tctb_tax_main_orgattr

- **表名称：** 组织标签-多选基础资料表
- **表名：** t_tctb_tax_main_orgattr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [标签设置 tctb_label_group](../tctb_files/tctb_label_group.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_tax_main_orgattr |  | fpkid |
| 2 | idx_tctb_tax_main_orgattr_fk |  | fid |

---

## 环境保护税单据体（勿删）-子表 t_tctb_hjbhs_entry

- **表名称：** 环境保护税单据体（勿删）-子表
- **表名：** t_tctb_hjbhs_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 3 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | fcshygc | 从事海洋工程 | bpchar | 1 |  | √ | '0' | 从事海洋工程 |
| 5 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 6 | fpollutanttype | 污染物类别 | varchar | 100 |  | √ | ' ' | 污染物类别 |
| 7 | fshljjzclcs | 生活垃圾集中处理场所 | bpchar | 1 |  | √ | '0' | 生活垃圾集中处理场所 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fcxwsjzclcs | 城乡污水集中处理场所 | bpchar | 1 |  | √ | '0' | 城乡污水集中处理场所 |
| 10 | fnumber | 排污许可证编号 | varchar | 200 |  | √ | ' ' | 排污许可证编号 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | facsb | 按次申报 | bpchar | 1 |  | √ | '0' | 按次申报 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_hjbhs_entry_fk |  | fid |
| 2 | pk_tctb_hjbhs_entry |  | fentryid |

---

## 股东信息-子表 t_tctb_shareholder_detail

- **表名称：** 股东信息-子表
- **表名：** t_tctb_shareholder_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvestrate | 投资比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 投资比例(%) |
| 3 | fname | 股东名称 | varchar | 100 |  | √ | ' ' | 股东名称 |
| 4 | ftype | 股东类型 | varchar | 30 |  | √ | ' ' | 股东类型 |
| 5 | fstartdate | 持股起始日 | timestamp | 0 |  |  | null | 持股起始日 |
| 6 | fnationality | 国籍 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | finsto | 持股比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 持股比例(%) |
| 9 | fidtype | 证件类型 | varchar | 30 |  | √ | ' ' | 证件类型,枚举: 1 :居民身份证 2 :中国护照 3 :税务登记证 4 :营业执照 5 :组织机构代码证 6 :其他单位证件 7 :香港特别行政区护照 8 :澳门特别行政区护照 9 :港澳居民来往内地通行证 10 :中华人民共和国往来港澳通行证 11 :台湾居民来往大陆通行证 12 :大陆居民往来台湾通行证 13 :香港永久性居民身份证 14 :台湾身份证 15 :澳门特别行政区永久性居民身份证 16 :外国护照 17 :外国人身份证件 18 :其他个人证件 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fidnumber | 证件号码 | varchar | 100 |  | √ | ' ' | 证件号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_shareholder_detail_pkey |  | fentryid |
| 2 | idx_tctb_shareholder_detail_fk |  | fid |

---

## 其他税费单据体（勿删）-子表 t_tctb_qtsf_entry

- **表名称：** 其他税费单据体（勿删）-子表
- **表名：** t_tctb_qtsf_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxperiod | 缴纳期限 | varchar | 50 |  | √ | ' ' | 缴纳期限,枚举: month :月 season :季 halfyear :半年 year :年 count :次 |
| 3 | famountrate | 费率 | numeric | 23 | 10 | √ | 0 | 费率 |
| 4 | feffectiveend | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fcollectsubrate | 征收子目（旧） | varchar | 50 |  | √ | ' ' | 征收子目（旧） |
| 7 | feffectivestart | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcollectrate | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 10 | fcollectitem | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tysbsf_bizdef_entry |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_qtsf_entry |  | fentryid |
| 2 | idx_tctb_qtsf_entry_fk |  | fid |

---

## 银行信息-子表 t_tctb_bank_info_detail

- **表名称：** 银行信息-子表
- **表名：** t_tctb_bank_info_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctname | 账号名称 | varchar | 100 |  | √ | ' ' | 账号名称 |
| 3 | ftaxacct | 缴税账户 | varchar | 10 |  | √ | '0' | 缴税账户 |
| 4 | ftripleaggrement | 三方协议号 | varchar | 50 |  | √ | ' ' | 三方协议号 |
| 5 | fbankorggan | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fopendate | 开户时间 | timestamp | 0 |  |  | null | 开户时间 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbankname | 开户银行 | varchar | 100 |  | √ | ' ' | 开户银行 |
| 10 | fbankacct | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_bank_info_detail_pkey |  | fentryid |
| 2 | idx_tctb_bank_info_detail_fk |  | fid |

---

## 资质单据体-子表 t_tctb_apitudeinfo

- **表名称：** 资质单据体-子表
- **表名：** t_tctb_apitudeinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcertificateno | 证书编号 | varchar | 50 |  | √ | ' ' | 证书编号 |
| 3 | fcreditrating | fcreditrating | varchar | 30 |  | √ | ' ' |  |
| 4 | fprofitmyear | 开始计算优惠年度： | varchar | 100 |  | √ | ' ' | 开始计算优惠年度： |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsocietytype | fsocietytype | varchar | 30 |  | √ | ' ' |  |
| 7 | fshanghai | 经济特区和上海浦东新区新设立的高新技术企业 | bpchar | 1 |  | √ | ' ' | 经济特区和上海浦东新区新设立的高新技术企业 |
| 8 | fprioritytion | fprioritytion | varchar | 100 |  | √ | ' ' |  |
| 9 | fissuedate | 发证时间 | timestamp | 0 |  |  | null | 发证时间 |
| 10 | fenddate |  | timestamp | 0 |  |  | null |  |
| 11 | fexporttype | fexporttype | varchar | 30 |  | √ | ' ' |  |
| 12 | fannualcome | fannualcome | varchar | 100 |  | √ | ' ' |  |
| 13 | fstartdate |  | timestamp | 0 |  |  | null |  |
| 14 | fcompanytype | 企业类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 15 | fworkertotal | fworkertotal | int8 | 64 |  | √ | 0 |  |
| 16 | fprofittype | 优惠类型： | varchar | 50 |  | √ | ' ' | 优惠类型： |
| 17 | fsocietytotal | fsocietytotal | int8 | 64 |  | √ | 0 |  |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fyxsy | 优先适用 | bpchar | 1 |  | √ | ' ' | 优先适用 |
| 20 | fapitudetype | 资质类型 | varchar | 30 |  | √ | ' ' | 资质类型,枚举: 1 :软件、集成电路类 2 :技术先进型服务类 3 :区域类税收优惠 4 :高新技术类 5 :其他税收优惠 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_apitudeinfo_fk |  | fid |
| 2 | t_tctb_apitudeinfo_pkey |  | fentryid |
