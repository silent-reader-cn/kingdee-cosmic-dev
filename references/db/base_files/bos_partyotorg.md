# 党群团队-bos_partyotorg

## 曾用名列表-多语言表 t_org_orgnh_l

- **表名称：** 曾用名列表-多语言表
- **表名：** t_org_orgnh_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_orgnh_l |  | fentryid,flocaleid |
| 2 | pk_t_org_orgnh_l |  | fpkid |

---

## 党群团队-多语言表 t_org_org_l

- **表名称：** 党群团队-多语言表
- **表名：** t_org_org_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepositbank | 开户行 | varchar | 255 |  | √ | ' ' | 开户行 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | faddress | 住所 | varchar | 255 |  | √ | ' ' | 住所 |
| 5 | fcomment | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | ffirmname | 公司名称 | varchar | 255 |  | √ | ' ' | 公司名称 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 9 | frepresentative | 法定代表人 | varchar | 255 |  | √ | ' ' | 法定代表人 |
| 10 | fsimplename | 简称 | varchar | 100 |  | √ | ' ' | 简称 |
| 11 | ffirmtype | 公司类型 | varchar | 255 |  | √ | ' ' | 公司类型 |
| 12 | fxkcontacts | 联系人 | varchar | 255 |  | √ | ' ' | 联系人 |
| 13 | fcontactaddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 14 | fxkfullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 15 | fbizscope | 经营范围 | varchar | 255 |  | √ | ' ' | 经营范围 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_org_l_fid |  | fid,flocaleid |
| 2 | t_org_org_l_pkey |  | fpkid |

---

## 组织结构-多语言表 t_org_structure_l

- **表名称：** 组织结构-多语言表
- **表名：** t_org_structure_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 3 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_structure_fid |  | fid,flocaleid |
| 2 | t_org_structure_l_pkey |  | fpkid |

---

## 组织结构-子表 t_org_structure

- **表名称：** 组织结构-子表
- **表名：** t_org_structure

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisstatsum | 统计汇总 | bpchar | 1 |  | √ | '1' | 统计汇总 |
| 3 | fmodifyorgid | fmodifyorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fyzjorgid | 云之家组织内码 | varchar | 36 |  | √ | ' ' | 云之家组织内码 |
| 5 | fisleaf | 叶子节点 | bpchar | 1 |  | √ | ' ' | 叶子节点 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fyzjparentorgid | 上级云之家组织内码 | varchar | 36 |  | √ | ' ' | 上级云之家组织内码 |
| 11 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fishr | 是否启用HR | bpchar | 1 |  | √ | ' ' | 是否启用HR |
| 15 | fsealuptime | 封存日期 | timestamp | 0 |  |  | null | 封存日期 |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 21 | fviewid | 组织视图 | int8 | 64 |  | √ | 0 | [组织视图方案 bos_org_viewschema](../base_files/bos_org_viewschema.md) |
| 22 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 23 | fsortcode | 字符串排序码 | varchar | 50 |  | √ | ' ' | 字符串排序码 |
| 24 | fisctrlunit | 管控单元 | bpchar | 1 |  | √ | '0' | 管控单元 |
| 25 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 26 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 27 | fisfreeze | 封存状态 | bpchar | 1 |  | √ | ' ' | 封存状态 |
| 28 | fsortnumber | 排序码 | int8 | 64 |  | √ | 0 | 排序码 |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 31 | fisbizunit | 业务实体 | bpchar | 1 |  | √ | '0' | 业务实体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_structure_parent |  | fparentid |
| 2 | t_org_structure_pkey |  | fid |
| 3 | ux_org_struc_vieworglongnum |  | fviewid,forgid,flongnumber |
| 4 | idx_t_org_structure_longnum |  | flongnumber |
| 5 | idx_t_org_structure_view |  | fviewid |
| 6 | ux_org_struc_vieworg |  | fviewid,forgid |
| 7 | idx_t_org_structure_org |  | forgid |

---

## 党群团队-主表 t_org_org

- **表名称：** 党群团队-主表
- **表名：** t_org_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyzjorgid | 云之家组织内码 | varchar | 36 |  | √ | ' ' | 云之家组织内码 |
| 3 | fishrod | 职能规划责任单位 | bpchar | 1 |  | √ | '0' | 职能规划责任单位 |
| 4 | fishrtax | 个税职能 | bpchar | 1 |  | √ | '0' | 个税职能 |
| 5 | fxksyncorgid | 同步组织内码 | varchar | 100 |  |  | ' ' | 同步组织内码 |
| 6 | fcityid | 城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 7 | fisproject | 项目管理 | bpchar | 1 |  | √ | '0' | 项目管理 |
| 8 | fishrbs | 定调薪职能 | bpchar | 1 |  | √ | '0' | 定调薪职能 |
| 9 | fisscc | 共享中心 | bpchar | 1 |  | √ | '0' | 共享中心 |
| 10 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 11 | fishrbm | 奖金职能 | bpchar | 1 |  | √ | '0' | 奖金职能 |
| 12 | fissettlement | 结算职能 | bpchar | 1 |  | √ | '0' | 结算职能 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fisasset | 资产职能 | bpchar | 1 |  | √ | '0' | 资产职能 |
| 15 | fistax | 税务职能 | bpchar | 1 |  | √ | '0' | 税务职能 |
| 16 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 17 | fxkorgdutyid | 部门属性 | int8 | 64 |  | √ | 0 | [部门属性 bos_org_duty](../base_files/bos_org_duty.md) |
| 18 | fxkisshrorg | 是否存在s-HR同步映射关系 | bpchar | 1 |  | √ | '0' | 是否存在s-HR同步映射关系 |
| 19 | fishrop | 职能绩效中心 | bpchar | 1 |  | √ | '0' | 职能绩效中心 |
| 20 | ftimezoneid | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 21 | fxkcurrency | 币种 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fpostcode | 邮编 | varchar | 10 |  | √ | ' ' | 邮编 |
| 23 | fishrwt | 考勤职能 | bpchar | 1 |  | √ | '0' | 考勤职能 |
| 24 | ftaxpayertype | 纳税人类型 | bpchar | 1 |  |  | ' ' | 纳税人类型,枚举: 1 :一般纳税人 2 :小规模纳税人 |
| 25 | fxkadmindivision | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 26 | fishrpay | 算发薪职能 | bpchar | 1 |  | √ | '0' | 算发薪职能 |
| 27 | fishrsi | 社保公积金职能 | bpchar | 1 |  | √ | '0' | 社保公积金职能 |
| 28 | fxkemail | 邮箱 | varchar | 100 |  | √ | ' ' | 邮箱 |
| 29 | fphone | 电话 | varchar | 255 |  | √ | ' ' | 电话 |
| 30 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 31 | fissale | 销售职能 | bpchar | 1 |  | √ | '0' | 销售职能 |
| 32 | fisdevelopment | 研发职能 | bpchar | 1 |  | √ | '0' | 研发职能 |
| 33 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fishrip | 个人绩效职能 | bpchar | 1 |  | √ | '0' | 个人绩效职能 |
| 35 | fishrbg | 编制/预算职能 | bpchar | 1 |  | √ | '0' | 编制/预算职能 |
| 36 | fisbudget | 预算组织 | bpchar | 1 |  | √ | '0' | 预算组织 |
| 37 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 38 | faccountingtype | 核算组织类型 | varchar | 50 |  | √ | '1' | 核算组织类型,枚举: 1 :法人 2 :利润中心 |
| 39 | fisfund | 资金职能 | bpchar | 1 |  | √ | '0' | 资金职能 |
| 40 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fregisteredcapital | 注册资本 | int8 | 64 |  | √ | 0 | 注册资本 |
| 42 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 43 | fbusinessterm | 营业期限 | timestamp | 0 |  |  | null | 营业期限 |
| 44 | fishrcmp | 薪酬管理职能 | bpchar | 1 |  | √ | '0' | 薪酬管理职能 |
| 45 | forgpatternid | 形态 | int8 | 64 |  | √ | 0 | [组织形态 bos_org_pattern](../base_files/bos_org_pattern.md) |
| 46 | fisbizorg | 业务组织 | bpchar | 1 |  | √ | '0' | 业务组织 |
| 47 | faccounting | 核算组织 | bpchar | 1 |  | √ | '1' | 核算组织 |
| 48 | fisplan | 计划组织(旧) | bpchar | 1 |  | √ | '0' | 计划组织(旧) |
| 49 | fbankaccount | 银行账户 | varchar | 255 |  | √ | ' ' | 银行账户 |
| 50 | fisplannew | 计划职能 | bpchar | 1 |  | √ | '0' | 计划职能 |
| 51 | fisaccounting | 货主职能 | bpchar | 1 |  | √ | '0' | 货主职能 |
| 52 | festablishmentdate | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 53 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 54 | xkadmindivision | xkadmindivision | varchar | 255 |  | √ | ' ' |  |
| 55 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 57 | fispresetbiz10 | 预置职能10 | bpchar | 1 |  | √ | '0' | 预置职能10 |
| 58 | fishr | HR职能 | bpchar | 1 |  | √ | '0' | HR职能 |
| 59 | fisadministrative | 行政组织 | bpchar | 1 |  | √ | '0' | 行政组织 |
| 60 | fishrlti | 长期激励职能 | bpchar | 1 |  | √ | '0' | 长期激励职能 |
| 61 | fishrab | 假期职能 | bpchar | 1 |  | √ | '0' | 假期职能 |
| 62 | xkcurrency | xkcurrency | int8 | 64 |  | √ | 0 |  |
| 63 | fisproduce | 生产职能 | bpchar | 1 |  | √ | '0' | 生产职能 |
| 64 | fxkdatasource | 数据来源 | int8 | 64 |  | √ | 0 | [数据来源 xkbos_data_sources](../xkbase_files/xkbos_data_sources.md) |
| 65 | funiformsocialcreditcode | 统一社会信用代码 | varchar | 100 |  | √ | ' ' | 统一社会信用代码 |
| 66 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 67 | fispresetbiz8 | 预置职能8 | bpchar | 1 |  | √ | '0' | 预置职能8 |
| 68 | fispresetbiz9 | 预置职能9 | bpchar | 1 |  | √ | '0' | 预置职能9 |
| 69 | fispresetbiz6 | 预置职能6 | bpchar | 1 |  | √ | '0' | 预置职能6 |
| 70 | fishrtd | 人才管理职能 | bpchar | 1 |  | √ | '0' | 人才管理职能 |
| 71 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 72 | fispresetbiz7 | 预置职能7 | bpchar | 1 |  | √ | '0' | 预置职能7 |
| 73 | fishrpa | 人事职能 | bpchar | 1 |  | √ | '0' | 人事职能 |
| 74 | fyzjimorted | 是否云之家同步 | bpchar | 1 |  | √ | ' ' | 是否云之家同步 |
| 75 | fispresetbiz4 | 预置职能4 | bpchar | 1 |  | √ | '0' | 预置职能4 |
| 76 | fispresetbiz5 | 预置职能5 | bpchar | 1 |  | √ | '0' | 预置职能5 |
| 77 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 78 | fiscontrolunit | 控制单元 | bpchar | 1 |  | √ | '0' | 控制单元 |
| 79 | fisqc | 质检职能 | bpchar | 1 |  | √ | '0' | 质检职能 |
| 80 | fisinventory | 库存职能 | bpchar | 1 |  | √ | '0' | 库存职能 |
| 81 | forgpattern | forgpattern | varchar | 10 |  | √ | ' ' |  |
| 82 | fisbankroll | 收付职能 | bpchar | 1 |  | √ | '0' | 收付职能 |
| 83 | fispurchase | 采购职能 | bpchar | 1 |  | √ | '0' | 采购职能 |
| 84 | fishrtr | 人才招聘职能 | bpchar | 1 |  | √ | '0' | 人才招聘职能 |
| 85 | fxkdunsnumber | 邓白氏编码 | varchar | 100 |  | √ | ' ' | 邓白氏编码 |
| 86 | fispresetbiz2 | 预置职能2 | bpchar | 1 |  | √ | '0' | 预置职能2 |
| 87 | fxkcontacts | 联系人 | varchar | 100 |  | √ | ' ' | 联系人 |
| 88 | fispresetbiz3 | 预置职能3 | bpchar | 1 |  | √ | '0' | 预置职能3 |
| 89 | fispresetbiz1 | 预置职能1 | bpchar | 1 |  | √ | '0' | 预置职能1 |
| 90 | fishrssc | HR共享服务职能 | bpchar | 1 |  | √ | '0' | HR共享服务职能 |
| 91 | fxkfullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 92 | ftaxregnum | 纳税识别号 | varchar | 255 |  | √ | ' ' | 纳税识别号 |
| 93 | fishrtl | 培训学习职能 | bpchar | 1 |  | √ | '0' | 培训学习职能 |
| 94 | fcontactphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 95 | fishrlc | 人力成本职能 | bpchar | 1 |  | √ | '0' | 人力成本职能 |
| 96 | fxkfax | 传真 | varchar | 100 |  | √ | ' ' | 传真 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sync_org_id |  | fxksyncorgid |
| 2 | idx_t_org_org_forgid |  | fyzjorgid |
| 3 | t_org_org_pkey |  | fid |
| 4 | ux_t_org_org_number |  | fnumber |
| 5 | idx_t_org_org_parentid |  | forgpatternid |
| 6 | idx_t_org_org_status |  | fstatus,fenable |

---

## 曾用名列表-子表 t_org_orgnh

- **表名称：** 曾用名列表-子表
- **表名：** t_org_orgnh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fenable | 是否生效 | bpchar | 1 |  | √ | '1' | 是否生效 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_org_orgnh |  | fentryid |
| 2 | idx_t_org_orgnh_fid |  | fid |
