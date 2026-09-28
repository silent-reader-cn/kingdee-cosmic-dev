# 业务单元历史-bos_org_history

## 业务单元历史-主表 t_org_org_h

- **表名称：** 业务单元历史-主表
- **表名：** t_org_org_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyzjorgid | 云之家组织内码 | varchar | 36 |  | √ | ' ' | 云之家组织内码 |
| 3 | fishrod | 职能规划责任单位 | bpchar | 1 |  | √ | '0' | 职能规划责任单位 |
| 4 | fishrtax | 个税职能 | bpchar | 1 |  | √ | '0' | 个税职能 |
| 5 | fxksyncorgid | 同步组织内码 | varchar | 100 |  | √ | ' ' | 同步组织内码 |
| 6 | fcityid | 城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 7 | fisproject | 项目管理 | bpchar | 1 |  | √ | '0' | 项目管理 |
| 8 | fishrbs | 定调薪职能 | bpchar | 1 |  | √ | '0' | 定调薪职能 |
| 9 | forgid | 业务单元内码 | int8 | 64 |  | √ | 0 | 业务单元内码 |
| 10 | fisscc | 共享中心 | bpchar | 1 |  | √ | '0' | 共享中心 |
| 11 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 12 | fishrbm | 奖金职能 | bpchar | 1 |  | √ | '0' | 奖金职能 |
| 13 | fissettlement | 结算职能 | bpchar | 1 |  | √ | '0' | 结算职能 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fisasset | 资产职能 | bpchar | 1 |  | √ | '0' | 资产职能 |
| 16 | fistax | 税务职能 | bpchar | 1 |  | √ | '0' | 税务职能 |
| 17 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 18 | fxkorgdutyid | 部门属性 | int8 | 64 |  |  | null | [部门属性 bos_org_duty](../base_files/bos_org_duty.md) |
| 19 | fxkisshrorg | 是否存在s-HR同步映射关系 | bpchar | 1 |  | √ | '0' | 是否存在s-HR同步映射关系 |
| 20 | fishrop | 职能绩效中心 | bpchar | 1 |  | √ | '0' | 职能绩效中心 |
| 21 | ftimezoneid | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 22 | fxkcurrency | 币种 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | fpostcode | 邮编 | varchar | 10 |  | √ | ' ' | 邮编 |
| 24 | fishrwt | 考勤职能 | bpchar | 1 |  | √ | '0' | 考勤职能 |
| 25 | ftaxpayertype | 纳税人类型 | bpchar | 1 |  |  | ' ' | 纳税人类型,枚举: 1 :一般纳税人 2 :小规模纳税人 |
| 26 | fxkadmindivision | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 27 | fishrpay | 算发薪职能 | bpchar | 1 |  | √ | '0' | 算发薪职能 |
| 28 | fishrsi | 社保公积金职能 | bpchar | 1 |  | √ | '0' | 社保公积金职能 |
| 29 | fxkemail | 邮箱 | varchar | 254 |  | √ | ' ' | 邮箱 |
| 30 | fphone | 电话 | varchar | 255 |  | √ | ' ' | 电话 |
| 31 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 32 | fissale | 销售职能 | bpchar | 1 |  | √ | '0' | 销售职能 |
| 33 | fisdevelopment | 研发职能 | bpchar | 1 |  | √ | '0' | 研发职能 |
| 34 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fishrip | 个人绩效职能 | bpchar | 1 |  | √ | '0' | 个人绩效职能 |
| 36 | fishrbg | 编制/预算职能 | bpchar | 1 |  | √ | '0' | 编制/预算职能 |
| 37 | fisbudget | 预算组织 | bpchar | 1 |  | √ | '0' | 预算组织 |
| 38 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 39 | faccountingtype | 核算组织类型 | varchar | 50 |  | √ | ' ' | 核算组织类型,枚举: 1 :法人 2 :利润中心 |
| 40 | fisfund | 资金职能 | bpchar | 1 |  | √ | '0' | 资金职能 |
| 41 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 42 | fregisteredcapital | 注册资本 | int8 | 64 |  | √ | 0 | 注册资本 |
| 43 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 44 | fbusinessterm | 营业期限 | timestamp | 0 |  |  | null | 营业期限 |
| 45 | fishrcmp | 薪酬管理职能 | bpchar | 1 |  | √ | '0' | 薪酬管理职能 |
| 46 | forgpatternid | 形态 | int8 | 64 |  | √ | 0 | [组织形态 bos_org_pattern](../base_files/bos_org_pattern.md) |
| 47 | fisbizorg | 业务组织 | bpchar | 1 |  | √ | '0' | 业务组织 |
| 48 | faccounting | 核算组织 | bpchar | 1 |  | √ | '1' | 核算组织 |
| 49 | fisplan | 计划组织(旧) | bpchar | 1 |  | √ | '0' | 计划组织(旧) |
| 50 | fbankaccount | 银行账户 | varchar | 255 |  | √ | ' ' | 银行账户 |
| 51 | fisplannew | 计划职能 | bpchar | 1 |  | √ | '0' | 计划职能 |
| 52 | fisaccounting | 货主职能 | bpchar | 1 |  | √ | '0' | 货主职能 |
| 53 | festablishmentdate | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 54 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 55 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 57 | fispresetbiz10 | 预置职能10 | bpchar | 1 |  | √ | '0' | 预置职能10 |
| 58 | fishr | HR职能 | bpchar | 1 |  | √ | '0' | HR职能 |
| 59 | fisadministrative | 行政组织 | bpchar | 1 |  | √ | '0' | 行政组织 |
| 60 | fishrlti | 长期激励职能 | bpchar | 1 |  | √ | '0' | 长期激励职能 |
| 61 | fishrab | 假期职能 | bpchar | 1 |  | √ | '0' | 假期职能 |
| 62 | fisproduce | 生产职能 | bpchar | 1 |  | √ | '0' | 生产职能 |
| 63 | fxkdatasource | 数据来源 | int8 | 64 |  |  | null | [数据来源 xkbos_data_sources](../xkbase_files/xkbos_data_sources.md) |
| 64 | funiformsocialcreditcode | 统一社会信用代码 | varchar | 100 |  | √ | ' ' | 统一社会信用代码 |
| 65 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 66 | fispresetbiz8 | 预置职能8 | bpchar | 1 |  | √ | '0' | 预置职能8 |
| 67 | fispresetbiz9 | 预置职能9 | bpchar | 1 |  | √ | '0' | 预置职能9 |
| 68 | fispresetbiz6 | 预置职能6 | bpchar | 1 |  | √ | '0' | 预置职能6 |
| 69 | fishrtd | 人才管理职能 | bpchar | 1 |  | √ | '0' | 人才管理职能 |
| 70 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 71 | fispresetbiz7 | 预置职能7 | bpchar | 1 |  | √ | '0' | 预置职能7 |
| 72 | fishrpa | 人事职能 | bpchar | 1 |  | √ | '0' | 人事职能 |
| 73 | fyzjimorted | 是否云之家同步 | bpchar | 1 |  | √ | ' ' | 是否云之家同步 |
| 74 | fispresetbiz4 | 预置职能4 | bpchar | 1 |  | √ | '0' | 预置职能4 |
| 75 | fispresetbiz5 | 预置职能5 | bpchar | 1 |  | √ | '0' | 预置职能5 |
| 76 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 77 | fiscontrolunit | 控制单元 | bpchar | 1 |  | √ | '0' | 控制单元 |
| 78 | fisqc | 质检职能 | bpchar | 1 |  | √ | '0' | 质检职能 |
| 79 | fisinventory | 库存职能 | bpchar | 1 |  | √ | '0' | 库存职能 |
| 80 | forgpattern | forgpattern | varchar | 10 |  | √ | ' ' |  |
| 81 | fisbankroll | 收付职能 | bpchar | 1 |  | √ | '0' | 收付职能 |
| 82 | fispurchase | 采购职能 | bpchar | 1 |  | √ | '0' | 采购职能 |
| 83 | fishrtr | 人才招聘职能 | bpchar | 1 |  | √ | '0' | 人才招聘职能 |
| 84 | fxkdunsnumber | 邓白氏编码 | varchar | 50 |  | √ | ' ' | 邓白氏编码 |
| 85 | fispresetbiz2 | 预置职能2 | bpchar | 1 |  | √ | '0' | 预置职能2 |
| 86 | fxkcontacts | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 87 | fispresetbiz3 | 预置职能3 | bpchar | 1 |  | √ | '0' | 预置职能3 |
| 88 | fispresetbiz1 | 预置职能1 | bpchar | 1 |  | √ | '0' | 预置职能1 |
| 89 | fishrssc | HR共享服务职能 | bpchar | 1 |  | √ | '0' | HR共享服务职能 |
| 90 | fxkfullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 91 | ftaxregnum | 纳税识别号 | varchar | 255 |  | √ | ' ' | 纳税识别号 |
| 92 | fishrtl | 培训学习职能 | bpchar | 1 |  | √ | '0' | 培训学习职能 |
| 93 | fcontactphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 94 | fishrlc | 人力成本职能 | bpchar | 1 |  | √ | '0' | 人力成本职能 |
| 95 | fxkfax | 传真 | varchar | 50 |  | √ | ' ' | 传真 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_org_org_h_orgnum |  | forgid,fnumber |
| 2 | t_org_org_h_pkey |  | fid |
| 3 | idx_org_org_h_time |  | fcreatetime |

---

## 组织结构-子表 t_org_structure_h

- **表名称：** 组织结构-子表
- **表名：** t_org_structure_h

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
| 24 | fisctrlunit | 管控单元 | bpchar | 1 |  | √ | '1' | 管控单元 |
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
| 1 | idx_t_org_structure_h_parent |  | fparentid |
| 2 | idx_org_struct_h_orgviewlnum |  | forgid,fviewid,flongnumber |
| 3 | idx_org_structure_h_time |  | fcreatetime |
| 4 | t_org_structure_h_pkey |  | fid |

---

## 业务单元历史-多语言表 t_org_org_h_l

- **表名称：** 业务单元历史-多语言表
- **表名：** t_org_org_h_l

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
| 12 | fxkcontacts | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 13 | fcontactaddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 14 | fxkfullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 15 | fbizscope | 经营范围 | varchar | 255 |  | √ | ' ' | 经营范围 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_org_h_l_pkey |  | fpkid |
| 2 | idx_t_org_org_h_l_fid |  | fid,flocaleid |

---

## 组织结构-多语言表 t_org_structure_h_l

- **表名称：** 组织结构-多语言表
- **表名：** t_org_structure_h_l

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
| 1 | t_org_structure_h_l_pkey |  | fpkid |
| 2 | idx_t_org_structure_h_fid |  | fid,flocaleid |
