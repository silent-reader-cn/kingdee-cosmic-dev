# 企业信息-bdm_enterprise_info

## 监控信息-子表 t_bdm_ep_monitor_info

- **表名称：** 监控信息-子表
- **表名：** t_bdm_ep_monitor_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foffposlimit | 离线正数累计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 离线正数累计金额 |
| 3 | fdeclaredate | 最新报税日期 | timestamp | 0 |  |  | null | 最新报税日期 |
| 4 | fnegativecountlimit | 负数发票累计张数限制 | int8 | 64 |  | √ | 0 | 负数发票累计张数限制 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | foffnegalimit | 离线负数累计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 离线负数累计金额 |
| 7 | fdeclaretime | 最新报税时间 | timestamp | 0 |  |  | null | 最新报税时间 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | frsptime | 最新回送时间 | timestamp | 0 |  |  | null | 最新回送时间 |
| 10 | fissuestarttime | 开票启用时间 | timestamp | 0 |  |  | null | 开票启用时间 |
| 11 | fcountlimit | 发票累计张数限制 | int8 | 64 |  | √ | 0 | 发票累计张数限制 |
| 12 | fdatadeclareendtime | 数据报送终止日期 | timestamp | 0 |  |  | null | 数据报送终止日期 |
| 13 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fuploadendtime | 上传截止日期 | timestamp | 0 |  |  | null | 上传截止日期 |
| 15 | fpositivecountlimit | 正数发票累计张数限制 | int8 | 64 |  | √ | 0 | 正数发票累计张数限制 |
| 16 | fissuelimit | 单张开票限额 | numeric | 23 | 10 | √ | 0.0000000000 | 单张开票限额 |
| 17 | fpositivelimit | 正数发票累计限额 | numeric | 23 | 10 | √ | 0.0000000000 | 正数发票累计限额 |
| 18 | fnegativelimit | 负数发票累计限额 | numeric | 23 | 10 | √ | 0.0000000000 | 负数发票累计限额 |
| 19 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :增值税电子专用发票 |
| 20 | fofflinecount | 离线开票张数 | int8 | 64 |  | √ | 0 | 离线开票张数 |
| 21 | fofflineduration | 离线开票时长 | numeric | 23 | 10 | √ | 0.0000000000 | 离线开票时长 |
| 22 | fdatadeclarestarttime | 数据报送起始日期 | timestamp | 0 |  |  | null | 数据报送起始日期 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fissueendtime | 开票截止时间 | timestamp | 0 |  |  | null | 开票截止时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_ep_monitor_info |  | fentryid |
| 2 | idx_bdm_ep_monitor_info_fk |  | fid |

---

## 发票申领经办人-子表 t_bdm_invoice_apply_agent

- **表名称：** 发票申领经办人-子表
- **表名：** t_bdm_invoice_apply_agent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 经办人姓名 | varchar | 50 |  | √ | ' ' | 经办人姓名 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcerttype | 证件类型 | varchar | 30 |  | √ | ' ' | 证件类型,枚举: 10 :身份证 20 :护照 30 :军官证 90 :其他证件 101 :组织机构代码证 199 :其他单位证件 201 :居民身份证 202 :军官证 203 :武警警官证 204 :士兵证 205 :军队离退休干部证 206 :残疾人证 207 :残疾军人证（1-8 级） 208 :外国护照 210 :港澳居民来往内地通行证 212 :中华人民共和国往来港澳通行证 213 :台湾居民来往大陆通行证 214 :大陆居民往来台湾通行证 215 :外国人居留证 216 :外交官证 217 :领事馆证 218 :海员证 219 :香港身份证 220 :台湾身份证 221 :澳门身份证 222 :外国人身份证件 |
| 6 | fcertno | 证件号码 | varchar | 50 |  | √ | ' ' | 证件号码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_invoice_apply_agent_fk |  | fid |
| 2 | pk_bdm_invoice_apply_agent |  | fentryid |

---

## 核定税率-子表 t_bdm_ep_checked_tax

- **表名称：** 核定税率-子表
- **表名：** t_bdm_ep_checked_tax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoicetype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :增值税电子专用发票 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ftaxratename | 税率名称 | varchar | 50 |  | √ | ' ' | 税率名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftaxflag | 含税标识 | varchar | 30 |  | √ | ' ' | 含税标识,枚举: 0 :不含税 1 :含税 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_ep_checked_tax |  | fentryid |
| 2 | idx_bdm_ep_checked_tax_fk |  | fid |

---

## 企业信息-主表 t_bdm_enterprise_info

- **表名称：** 企业信息-主表
- **表名：** t_bdm_enterprise_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxgmkjzpbs | 小规模开具专票标识 | varchar | 30 |  | √ | ' ' | 小规模开具专票标识,枚举: 00 :不可开具专票 01 :可以开具专票 |
| 3 | foilexpirestarttime | 成品油标识有效期.开始 | timestamp | 0 |  |  | null | 成品油标识有效期.开始 |
| 4 | foilwlistexpstarttime | 成品油白名单标识有效期.开始 | timestamp | 0 |  |  | null | 成品油白名单标识有效期.开始 |
| 5 | foilexpireendtime | 成品油标识有效期.结束 | timestamp | 0 |  |  | null | 成品油标识有效期.结束 |
| 6 | fzgswjgdm | 税务机关代码： | varchar | 50 |  | √ | ' ' | 税务机关代码： |
| 7 | foilwhitelistmark | 成品油白名单标识 | varchar | 30 |  | √ | ' ' | 成品油白名单标识,枚举: 00 :非成品油白名单企业 01 :成品油白名单企业 |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fepinfo | 企业基础信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |
| 11 | fissuemark | 控制开票标志 | varchar | 30 |  | √ | ' ' | 控制开票标志,枚举: 00 :允许 01 :禁止 |
| 12 | fregisterseq | 征管系统登记序号 | varchar | 50 |  | √ | ' ' | 征管系统登记序号 |
| 13 | fversionno | 版本号 | varchar | 50 |  | √ | ' ' | 版本号 |
| 14 | ftobaccoexpirestarttime | 卷烟标识有效期.开始 | timestamp | 0 |  |  | null | 卷烟标识有效期.开始 |
| 15 | ftobaccoexpireendtime | 卷烟标识有效期.结束 | timestamp | 0 |  |  | null | 卷烟标识有效期.结束 |
| 16 | frareearthepmark | 稀土企业 | varchar | 30 |  | √ | ' ' | 稀土企业,枚举: 00 :非稀土企业 01 :稀土企业-矿产品 02 :稀土企业-冶炼分离 03 :稀土企业-其它 |
| 17 | fissuedevno | 开票机号 | varchar | 50 |  | √ | ' ' | 开票机号 |
| 18 | foilmark | 成品油标识 | varchar | 30 |  | √ | ' ' | 成品油标识,枚举: 00 :非成品油 01 :成品油生产企业 02 :成品油批发企业 |
| 19 | finputauthmark | 进项授权标志 | varchar | 30 |  | √ | ' ' | 进项授权标志,枚举: 00 :未授权 01 :已授权 |
| 20 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 21 | faroprodepmark | 农产品销售收购发票企业标识 | varchar | 30 |  | √ | ' ' | 农产品销售收购发票企业标识,枚举: 00 :非农产品销售收购发票企业 01 :收购企业 |
| 22 | ftobaccomark | 卷烟企业标识 | varchar | 4 |  | √ | ' ' | 卷烟企业标识,枚举: 0 :非卷烟 1 :卷烟生产企业 2 :卷烟批发企业 |
| 23 | fspecificepmark | 特定企业 | varchar | 30 |  | √ | ' ' | 特定企业,枚举: 00 :非特定企业 01 :特定企业 |
| 24 | ftelecomepmark | 电信企业 | varchar | 30 |  | √ | ' ' | 电信企业,枚举: 00 :非电信企业 01 :电信企业 |
| 25 | fsecondcarmark | 二手机动车标识 | varchar | 30 |  | √ | ' ' | 二手机动车标识,枚举: 00 :非二手机动车纳税人 01 :经营单位 02 :拍卖单位 03 :二手车市场 |
| 26 | fzgswjgmc | 税务机关名称： | varchar | 80 |  | √ | ' ' | 税务机关名称： |
| 27 | foilwlistexpendtime | 成品油白名单标识有效期.结束 | timestamp | 0 |  |  | null | 成品油白名单标识有效期.结束 |
| 28 | feptype | 企业类型 | varchar | 30 |  | √ | ' ' | 企业类型,枚举: 01 :一般纳税人 08 :小规模纳税人 05 :转登记纳税人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_enterprise_info |  | fid |
| 2 | idx_bdm_enterprise_info_edx |  | fzgswjgdm |
