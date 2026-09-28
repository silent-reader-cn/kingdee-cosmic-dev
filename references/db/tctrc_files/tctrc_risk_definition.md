# 风险设置-tctrc_risk_definition

## 风险设置-多语言表 t_tctrc_risk_definition_l

- **表名称：** 风险设置-多语言表
- **表名：** t_tctrc_risk_definition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 风险名称 | varchar | 300 |  | √ | ' ' | 风险名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_definition_l_0 |  | fid,flocaleid |
| 2 | t_tctrc_risk_definition_l_pkey |  | fpkid |

---

## 单据体-子表 t_tctrc_risk_label

- **表名称：** 单据体-子表
- **表名：** t_tctrc_risk_label

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | flabelid | 标签 | int8 | 64 |  | √ | 0 | 标签 t_tctb_label_info |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_label_fk |  | fid |
| 2 | t_tctrc_risk_label_pkey |  | fentryid |

---

## 申报表类型-多选基础资料表 t_tctrc_risk_def_sbbtype

- **表名称：** 申报表类型-多选基础资料表
- **表名：** t_tctrc_risk_def_sbbtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_def_sbbtype_fk |  | fid |
| 2 | pk_tctrc_risk_def_sbbtype |  | fpkid |

---

## 税种-多选基础资料表 t_tctrc_taxtypemul

- **表名称：** 税种-多选基础资料表
- **表名：** t_tctrc_taxtypemul

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_taxtypemul_pkey |  | fpkid |
| 2 | idx_tctrc_taxtypemul_fk |  | fid |

---

## 风险设置-主表 t_tctrc_risk_definition

- **表名称：** 风险设置-主表
- **表名：** t_tctrc_risk_definition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjson | 表达式 | varchar | 510 |  | √ | ' ' | 表达式 |
| 3 | fjsonname | fjsonname | varchar | 510 |  | √ | ' ' |  |
| 4 | fdescribe | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | ftaxtypename | 税种名称 | varchar | 30 |  | √ | ' ' | 税种名称 |
| 6 | fhandleguide1 | fhandleguide1 | varchar | 30 |  | √ | ' ' |  |
| 7 | fcollect | 是否收藏 | varchar | 50 |  | √ | ' ' | 是否收藏 |
| 8 | fcaltype | 计算周期 | varchar | 30 |  | √ | ' ' | 计算周期,枚举: 1 :月度 2 :季度 4 :年度 3 :半年度 |
| 9 | fjsonname_tag | fjsonname_tag | text | 0 |  |  | null |  |
| 10 | fisvariable | 是否变量 | bpchar | 1 |  | √ | ' ' | 是否变量 |
| 11 | ftaxtypegroup | 税种分组 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 12 | fmodifytime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 13 | fhandleguide | 处理指引 | varchar | 30 |  | √ | ' ' | 处理指引,枚举: normal :正常因素指引 risk :风险因素指引 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | frisklevel | frisklevel | varchar | 30 |  | √ | ' ' |  |
| 18 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设,枚举: 1 :是 0 :否 |
| 19 | fresultshow | 结果展示 | varchar | 30 |  | √ | ' ' | 结果展示,枚举: 1 :数值展示 2 :比例展示 |
| 20 | fmonth | 运行时间 | varchar | 30 |  | √ | ' ' | 运行时间,枚举: 1 :第一个月 2 :第二个月 3 :第三个月 4 :第四个月 5 :第五个月 6 :第六个月 7 :第七个月 8 :第八个月 9 :第九个月 10 :第十个月 11 :第十一个月 12 :第十二个月 |
| 21 | fday | 运行时间 | varchar | 30 |  | √ | ' ' | 运行时间,枚举: 1 :1号 2 :2号 3 :3号 4 :4号 5 :5号 6 :6号 7 :7号 8 :8号 9 :9号 10 :10号 11 :11号 12 :12号 13 :13号 14 :14号 15 :15号 16 :16号 17 :17号 18 :18号 19 :19号 20 :20号 21 :21号 22 :22号 23 :23号 24 :24号 25 :25号 26 :26号 27 :27号 28 :28号 29 :29号 30 :30号 31 :31号 |
| 22 | ftaxtype | 税种 | varchar | 30 |  | √ | ' ' | 税种,枚举: 1 :增值税 2 :企业所得税 3 :附加税费 4 :房产税 5 :城镇土地使用税 6 :印花税 7 :消费税 8 :环保税 |
| 23 | fbenchmarking | 对标类型 | varchar | 30 |  | √ | ' ' | 对标类型,枚举: 1 :固定值 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fvariableids | 风险变量 | varchar | 1000 |  | √ | ' ' | 风险变量 |
| 27 | fbmvalue | 对标值 | numeric | 23 | 10 | √ | 0.0000000000 | 对标值 |
| 28 | fdeviatedcount | 风险计算偏移量 | varchar | 50 |  | √ | ' ' | 风险计算偏移量,枚举: 0 :0 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 |
| 29 | fsuggestion | fsuggestion | varchar | 2000 |  | √ | ' ' |  |
| 30 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fissbshow | 是否申报显示 | bpchar | 1 |  | √ | ' ' | 是否申报显示 |
| 32 | fenable | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :保存 1 :可用 2 :禁用 |
| 33 | ftaxtype2 | 税种（用于过滤，多选基础资料不支持过滤） | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 34 | fnumber | 编号 | varchar | 60 |  | √ | ' ' | 编号 |
| 35 | fjson_tag | 表达式_详情 | text | 0 |  |  | null | 表达式_详情 |
| 36 | frisktype | 风险类型 | varchar | 30 |  | √ | ' ' | 风险类型,枚举: 1 :数值指标 2 :筛查抽检 3 :数据比对 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_risk_definition_pkey |  | fid |
| 2 | idx_tctrc_risk_definition |  | fnumber |

---

## 单据体-子表 t_tctrc_risk_guide_2

- **表名称：** 单据体-子表
- **表名：** t_tctrc_risk_guide_2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhandledesc | 指引描述 | varchar | 400 |  | √ | ' ' | 指引描述 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_guide_2_fk |  | fid |
| 2 | t_tctrc_risk_guide_2_pkey |  | fentryid |

---

## 单据体-子表 t_tctrc_risk_guide_1

- **表名称：** 单据体-子表
- **表名：** t_tctrc_risk_guide_1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhandledesc | 指引描述 | varchar | 400 |  | √ | ' ' | 指引描述 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_risk_guide_1_pkey |  | fentryid |
| 2 | idx_tctrc_risk_guide_1_fk |  | fid |

---

## 单据体-子表 t_tctrc_risk_offset

- **表名称：** 单据体-子表
- **表名：** t_tctrc_risk_offset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgs_tag | forgs_tag | text | 0 |  |  | null |  |
| 3 | fminborder | 区间括号 | varchar | 30 |  | √ | ' ' | 区间括号,枚举: 1 :( 2 :[ |
| 4 | friskscore | 风险得分 | varchar | 50 |  | √ | ' ' | 风险得分 |
| 5 | forgs | 偏差适用组织 | text | 0 |  |  | null | 偏差适用组织 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbenchmarking1 | 对标类型 | varchar | 30 |  | √ | ' ' | 对标类型 |
| 8 | foffset | 偏差类型 | varchar | 30 |  | √ | ' ' | 偏差类型,枚举: 1 :数值 2 :比例 |
| 9 | fpianchaname | fpianchaname | varchar | 100 |  | √ | ' ' |  |
| 10 | fitemid | 偏差卡片id | varchar | 50 |  | √ | ' ' | 偏差卡片id |
| 11 | frange | 偏差最小值 | varchar | 100 |  | √ | ' ' | 偏差最小值 |
| 12 | fbmvalue1 | fbmvalue1 | varchar | 100 |  | √ | ' ' |  |
| 13 | fbmvalue2 | 对标值 | numeric | 23 | 10 |  | 0 | 对标值 |
| 14 | fmaxborder | 区间括号 | varchar | 30 |  | √ | ' ' | 区间括号,枚举: 1 :) 2 :] |
| 15 | frangemax | 偏差最大值 | varchar | 100 |  | √ | ' ' | 偏差最大值 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | frlevel | 风险等级 | int8 | 64 |  | √ | 0 | 风险等级 tctrc_risk_level |
| 18 | fgrade | 风险等级(弃用) | varchar | 30 |  | √ | ' ' | 风险等级(弃用),枚举: 1 :高 2 :中 3 :低 |
| 19 | fexplain | 风险说明 | varchar | 2000 |  | √ | ' ' | 风险说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_offset_fk |  | fid |
| 2 | t_tctrc_risk_offset_pkey |  | fentryid |

---

## 单据体-子表 t_tctrc_risk_policies

- **表名称：** 单据体-子表
- **表名：** t_tctrc_risk_policies

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpoliciesname | 政策法规名称 | varchar | 200 |  | √ | ' ' | 政策法规名称 |
| 3 | fpolicyarticles | 法规条文 | varchar | 4000 |  | √ | ' ' | 法规条文 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpoliciesurl | 链接地址 | varchar | 2000 |  | √ | ' ' | 链接地址 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_policies_fk |  | fid |
| 2 | t_tctrc_risk_policies_pkey |  | fentryid |
