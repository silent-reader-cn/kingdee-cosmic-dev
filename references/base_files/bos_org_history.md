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
| 17 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 18 | fxkorgdutyid | 部门属性 | int8 | 64 |  |  | null | 部门属性 bos_org_duty |
| 19 | fxkisshrorg | 是否存在s-HR同步映射关系 | bpchar | 1 |  | √ | '0' | 是否存在s-HR同步映射关系 |
| 20 | fishrop | 职能绩效中心 | bpchar | 1 |  | √ | '0' | 职能绩效中心 |
| 21 | ftimezoneid | 时区 | int8 | 64 |  | √ | 0 | 时区 inte_timezone |
| 22 | fxkcurrency | 币别 | int8 | 64 |  |  | null | 币种 bd_currency |
| 23 | fpostcode | 邮编 | varchar | 10 |  | √ | ' ' | 邮编 |
| 24 | fishrwt | 考勤职能 | bpchar | 1 |  | √ | '0' | 考勤职能 |
| 25 | ftaxpayertype | 纳税人类型 | bpchar | 1 |  |  | ' ' | 纳税人类型,枚举: 1 :一般纳税人 2 :小规模纳税人 |
| 26 | fxkadmindivision | 行政区划 | varchar | 50 |  | √ | ' ' | 行政区划 |
| 27 | fishrpay | 算发薪职能 | bpchar | 1 |  | √ | '0' | 算发薪职能 |
| 28 | fishrsi | 社保公积金职能 | bpchar | 1 |  | √ | '0' | 社保公积金职能 |
| 29 | fphone | 电话 | varchar | 255 |  | √ | ' ' | 电话 |
| 30 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 31 | fissale | 销售职能 | bpchar | 1 |  | √ | '0' | 销售职能 |
| 32 | fisdevelopment | 研发职能 | bpchar | 1 |  | √ | '0' | 研发职能 |
| 33 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fishrip | 个人绩效职能 | bpchar | 1 |  | √ | '0' | 个人绩效职能 |
| 35 | fishrbg | 编制/预算职能 | bpchar | 1 |  | √ | '0' | 编制/预算职能 |
| 36 | fisbudget | 预算组织 | bpchar | 1 |  | √ | '0' | 预算组织 |
| 37 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 38 | faccountingtype | 核算组织类型 | varchar | 50 |  | √ | ' ' | 核算组织类型,枚举: 1 :法人 2 :利润中心 |
| 39 | fisfund | 资金职能 | bpchar | 1 |  | √ | '0' | 资金职能 |
| 40 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fregisteredcapital | 注册资本 | int8 | 64 |  | √ | 0 | 注册资本 |
| 42 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 43 | fbusinessterm | 营业期限 | timestamp | 0 |  |  | null | 营业期限 |
| 44 | fishrcmp | 薪酬管理职能 | bpchar | 1 |  | √ | '0' | 薪酬管理职能 |
| 45 | forgpatternid | 形态 | int8 | 64 |  | √ | 0 | 组织形态 bos_org_pattern |
| 46 | fisbizorg | 业务组织 | bpchar | 1 |  | √ | '0' | 业务组织 |
| 47 | faccounting | 核算组织 | bpchar | 1 |  | √ | '1' | 核算组织 |
| 48 | fisplan | 计划组织(旧) | bpchar | 1 |  | √ | '0' | 计划组织(旧) |
| 49 | fbankaccount | 银行账户 | varchar | 255 |  | √ | ' ' | 银行账户 |
| 50 | fisplannew | 计划职能 | bpchar | 1 |  | √ | '0' | 计划职能 |
| 51 | fisaccounting | 货主职能 | bpchar | 1 |  | √ | '0' | 货主职能 |
| 52 | festablishmentdate | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 53 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 54 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 55 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 56 | fispresetbiz10 | 预置职能10 | bpchar | 1 |  | √ | '0' | 预置职能10 |
| 57 | fishr | HR职能 | bpchar | 1 |  | √ | '0' | HR职能 |
| 58 | fisadministrative | 行政组织 | bpchar | 1 |  | √ | '0' | 行政组织 |
| 59 | fishrlti | 长期激励职能 | bpchar | 1 |  | √ | '0' | 长期激励职能 |
| 60 | fishrab | 假期职能 | bpchar | 1 |  | √ | '0' | 假期职能 |
| 61 | fisproduce | 生产职能 | bpchar | 1 |  | √ | '0' | 生产职能 |
| 62 | fxkdatasource | 数据来源 | int8 | 64 |  |  | null | 数据来源 xkbos_data_sources |
| 63 | funiformsocialcreditcode | 统一社会信用代码 | varchar | 100 |  | √ | ' ' | 统一社会信用代码 |
| 64 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 65 | fispresetbiz8 | 预置职能8 | bpchar | 1 |  | √ | '0' | 预置职能8 |
| 66 | fispresetbiz9 | 预置职能9 | bpchar | 1 |  | √ | '0' | 预置职能9 |
| 67 | fispresetbiz6 | 预置职能6 | bpchar | 1 |  | √ | '0' | 预置职能6 |
| 68 | fishrtd | 人才管理职能 | bpchar | 1 |  | √ | '0' | 人才管理职能 |
| 69 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 70 | fispresetbiz7 | 预置职能7 | bpchar | 1 |  | √ | '0' | 预置职能7 |
| 71 | fishrpa | 人事职能 | bpchar | 1 |  | √ | '0' | 人事职能 |
| 72 | fyzjimorted | 是否云之家同步 | bpchar | 1 |  | √ | ' ' | 是否云之家同步 |
| 73 | fispresetbiz4 | 预置职能4 | bpchar | 1 |  | √ | '0' | 预置职能4 |
| 74 | fispresetbiz5 | 预置职能5 | bpchar | 1 |  | √ | '0' | 预置职能5 |
| 75 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 76 | fiscontrolunit | 控制单元 | bpchar | 1 |  | √ | '0' | 控制单元 |
| 77 | fisqc | 质检职能 | bpchar | 1 |  | √ | '0' | 质检职能 |
| 78 | fisinventory | 库存职能 | bpchar | 1 |  | √ | '0' | 库存职能 |
| 79 | forgpattern | forgpattern | varchar | 10 |  | √ | ' ' |  |
| 80 | fisbankroll | 收付职能 | bpchar | 1 |  | √ | '0' | 收付职能 |
| 81 | fispurchase | 采购职能 | bpchar | 1 |  | √ | '0' | 采购职能 |
| 82 | fishrtr | 人才招聘职能 | bpchar | 1 |  | √ | '0' | 人才招聘职能 |
| 83 | fispresetbiz2 | 预置职能2 | bpchar | 1 |  | √ | '0' | 预置职能2 |
| 84 | fispresetbiz3 | 预置职能3 | bpchar | 1 |  | √ | '0' | 预置职能3 |
| 85 | fispresetbiz1 | 预置职能1 | bpchar | 1 |  | √ | '0' | 预置职能1 |
| 86 | fishrssc | HR共享服务职能 | bpchar | 1 |  | √ | '0' | HR共享服务职能 |
| 87 | fxkfullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 88 | ftaxregnum | 纳税识别号 | varchar | 255 |  | √ | ' ' | 纳税识别号 |
| 89 | fishrtl | 培训学习职能 | bpchar | 1 |  | √ | '0' | 培训学习职能 |
| 90 | fcontactphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 91 | fishrlc | 人力成本职能 | bpchar | 1 |  | √ | '0' | 人力成本职能 |

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
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fyzjparentorgid | 上级云之家组织内码 | varchar | 36 |  | √ | ' ' | 上级云之家组织内码 |
| 11 | fenddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fishr | 是否启用HR | bpchar | 1 |  | √ | ' ' | 是否启用HR |
| 15 | fsealuptime | 封存日期 | timestamp | 0 |  |  | null | 封存日期 |
| 16 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fparentid | 上级组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 20 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 21 | fviewid | 组织视图 | int8 | 64 |  | √ | 0 | 组织视图方案 bos_org_viewschema |
| 22 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 23 | fsortcode | 排序码 | varchar | 50 |  | √ | ' ' | 排序码 |
| 24 | fisctrlunit | 管控单元 | bpchar | 1 |  | √ | '1' | 管控单元 |
| 25 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 26 | fstartdate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 27 | fisfreeze | 封存状态 | bpchar | 1 |  | √ | ' ' | 封存状态 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 30 | fisbizunit | 业务实体 | bpchar | 1 |  | √ | '0' | 业务实体 |

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
| 12 | fcontactaddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 13 | fxkfullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 14 | fbizscope | 经营范围 | varchar | 255 |  | √ | ' ' | 经营范围 |

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
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
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
