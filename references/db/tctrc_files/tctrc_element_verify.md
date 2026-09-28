# 数据比对-tctrc_element_verify

## 数据比对-多语言表 t_tctrc_risk_definition_l

- **表名称：** 数据比对-多语言表
- **表名：** t_tctrc_risk_definition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
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

## 标签单据体-子表 t_tctrc_risk_label

- **表名称：** 标签单据体-子表
- **表名：** t_tctrc_risk_label

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | flabelid | 标签 | int8 | 64 |  | √ | 0 | [标签 t_tctb_label_info](../tctb_files/t_tctb_label_info.md) |
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

## 风险定义-子表 t_tctrc_risklevel_explain

- **表名称：** 风险定义-子表
- **表名：** t_tctrc_risklevel_explain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | friskscore | 风险得分 | varchar | 50 |  | √ | ' ' | 风险得分 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | frlevel | 风险等级 | int8 | 64 |  | √ | 0 | [风险等级 tctrc_risk_level](../tctrc_files/tctrc_risk_level.md) |
| 6 | fgrade | 风险等级(弃用) | varchar | 30 |  | √ | ' ' | 风险等级(弃用),枚举: 1 :高 2 :中 3 :低 |
| 7 | fexplain | 风险说明 | varchar | 1000 |  | √ | ' ' | 风险说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risklevel_explain_fk |  | fid |
| 2 | t_tctrc_risklevel_explain_pkey |  | fentryid |

---

## 申报表类型-多选基础资料表 t_tctrc_risk_def_sbbtype

- **表名称：** 申报表类型-多选基础资料表
- **表名：** t_tctrc_risk_def_sbbtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [模板类型 tctb_template_type](../tctb_files/tctb_template_type.md) |
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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
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

## 数据比对-主表 t_tctrc_risk_definition

- **表名称：** 数据比对-主表
- **表名：** t_tctrc_risk_definition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjson | fjson | varchar | 2000 |  | √ | ' ' |  |
| 3 | fjsonname | fjsonname | varchar | 510 |  | √ | ' ' |  |
| 4 | fdescribe | 描述 | varchar | 2000 |  | √ | ' ' | 描述 |
| 5 | ftaxtypename | 税种名称 | varchar | 30 |  | √ | ' ' | 税种名称 |
| 6 | fhandleguide1 | fhandleguide1 | varchar | 30 |  | √ | ' ' |  |
| 7 | fcollect | 是否收藏 | varchar | 50 |  | √ | ' ' | 是否收藏 |
| 8 | felement | felement | int8 | 64 |  | √ | 0 |  |
| 9 | fcaltype | 计算周期 | varchar | 30 |  | √ | ' ' | 计算周期,枚举: 1 :月度 2 :季度 3 :半年度 4 :年度 |
| 10 | fjsonname_tag | fjsonname_tag | text | 0 |  |  | null |  |
| 11 | fisvariable | 是否变量 | bpchar | 1 |  | √ | ' ' | 是否变量 |
| 12 | ftaxtypegroup | ftaxtypegroup | int8 | 64 |  | √ | 0 |  |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fhandleguide | fhandleguide | varchar | 30 |  | √ | ' ' |  |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | frisklevel | 单选按钮组 | varchar | 30 |  | √ | ' ' | 单选按钮组,枚举: 1 :高 2 :中 3 :低 |
| 19 | fpreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设,枚举: 1 :是 0 :否 |
| 20 | fresultshow | fresultshow | varchar | 30 |  | √ | ' ' |  |
| 21 | fmonth | 运行时间（月份） | varchar | 30 |  | √ | ' ' | 运行时间（月份）,枚举: 1 :第一个月 2 :第二个月 3 :第三个月 4 :第四个月 5 :第五个月 6 :第六个月 |
| 22 | fday | 运行时间(日期) | varchar | 30 |  | √ | ' ' | 运行时间(日期),枚举: 1 :1号 2 :2号 3 :3号 4 :4号 5 :5号 6 :6号 7 :7号 8 :8号 9 :9号 10 :10号 11 :11号 12 :12号 13 :13号 14 :14号 15 :15号 16 :16号 17 :17号 18 :18号 19 :19号 20 :20号 21 :21号 22 :22号 23 :23号 24 :24号 25 :25号 26 :26号 27 :27号 28 :28号 |
| 23 | ftaxtype | 税种(废弃) | varchar | 30 |  | √ | ' ' | 税种(废弃),枚举: 1 :增值税 2 :企业所得税 3 :附加税费 4 :房产税 5 :城镇土地使用税 6 :印花税 7 :消费税 8 :环保税 |
| 24 | fbenchmarking | fbenchmarking | varchar | 30 |  | √ | ' ' |  |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fvariableids | 风险变量 | varchar | 1000 |  | √ | ' ' | 风险变量 |
| 28 | fbmvalue | fbmvalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 29 | fdeviatedcount | 风险计算偏移量 | varchar | 50 |  | √ | ' ' | 风险计算偏移量,枚举: 0 :0 |
| 30 | fsuggestion | 应对建议 | varchar | 2000 |  | √ | ' ' | 应对建议 |
| 31 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 sbjtThan :计提与申报比对 |
| 32 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fissbshow | 是否申报显示 | bpchar | 1 |  | √ | ' ' | 是否申报显示 |
| 34 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :保存 1 :启用 2 :禁用 |
| 35 | ftaxtype2 | ftaxtype2 | int8 | 64 |  | √ | 0 |  |
| 36 | fnumber | 编号 | varchar | 60 |  | √ | ' ' | 编号 |
| 37 | fjson_tag | fjson_tag | text | 0 |  |  | null |  |
| 38 | frisktype | 风险类型 | varchar | 30 |  | √ | ' ' | 风险类型,枚举: 1 :数值指标 2 :风险抽检 3 :元素核对 |

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

## 低于风险指引单据体-子表 t_tctrc_risk_guide_4

- **表名称：** 低于风险指引单据体-子表
- **表名：** t_tctrc_risk_guide_4

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fhandledesc1 | 指引描述 | varchar | 800 |  | √ | ' ' | 指引描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctrc_risk_guide_4_fk |  | fid |
| 2 | t_tctrc_risk_guide_4_pkey |  | fentryid |

---

## 低于正常指引单据体-子表 t_tctrc_risk_guide_3

- **表名称：** 低于正常指引单据体-子表
- **表名：** t_tctrc_risk_guide_3

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fhandledesc1 | 指引描述 | varchar | 800 |  | √ | ' ' | 指引描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_risk_guide_3_pkey |  | fentryid |
| 2 | idx_tctrc_risk_guide_3_fk |  | fid |

---

## 高于风险指引单据体-子表 t_tctrc_risk_guide_2

- **表名称：** 高于风险指引单据体-子表
- **表名：** t_tctrc_risk_guide_2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhandledesc | 指引描述 | varchar | 800 |  | √ | ' ' | 指引描述 |
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

## 高于正常指引单据体-子表 t_tctrc_risk_guide_1

- **表名称：** 高于正常指引单据体-子表
- **表名：** t_tctrc_risk_guide_1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhandledesc | 指引描述 | varchar | 800 |  | √ | ' ' | 指引描述 |
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

## 核对内容-子表 t_tctrc_risk_entry

- **表名称：** 核对内容-子表
- **表名：** t_tctrc_risk_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ftext | 过滤条件 | varchar | 1000 |  | √ | ' ' | 过滤条件 |
| 4 | fjson | json | varchar | 510 |  | √ | ' ' | json |
| 5 | fexist | 单选按钮组 | varchar | 30 |  | √ | ' ' | 单选按钮组,枚举: 1 :存在 0 :不存在 |
| 6 | ffieldname | ffieldname | varchar | 1000 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fjson_tag | json_详情 | text | 0 |  |  | null | json_详情 |
| 9 | ftableid | ftableid | int8 | 64 |  | √ | 0 |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fieldid | 字段ID | varchar | 1000 |  | √ | ' ' | 字段ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_risk_entry_pkey |  | fentryid |
| 2 | idx_tctrc_risk_entry_fk |  | fid |

---

## 政策法规指引单据体-子表 t_tctrc_risk_policies

- **表名称：** 政策法规指引单据体-子表
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
