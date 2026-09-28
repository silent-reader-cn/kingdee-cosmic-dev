# 预缴项目信息-tcvat_prepay_project_info

## 预缴项目信息-多语言表 t_tcvat_prepay_project_l

- **表名称：** 预缴项目信息-多语言表
- **表名：** t_tcvat_prepay_project_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 预缴项目名称 | varchar | 100 |  | √ | ' ' | 预缴项目名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_prepay_project_l_0 |  | fid,flocaleid |
| 2 | pk_tcvat_prepay_project_l |  | fpkid |

---

## 合同信息目录-子表 t_tcvat_contract_info

- **表名称：** 合同信息目录-子表
- **表名：** t_tcvat_contract_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpartnername | 合同相对方名称 | varchar | 50 |  | √ | ' ' | 合同相对方名称 |
| 3 | fpartnertaxno | 合同相对方税号 | varchar | 50 |  | √ | ' ' | 合同相对方税号 |
| 4 | ftotalamount | ftotalamount | numeric | 23 | 10 | √ | 0 |  |
| 5 | fsigndate | 合同签订时间 | timestamp | 0 |  |  | null | 合同签订时间 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcontractname | 合同名称 | varchar | 200 |  | √ | ' ' | 合同名称 |
| 8 | famount | 合同签订金额（元） | numeric | 23 | 10 | √ | 0.0000000000 | 合同签订金额（元） |
| 9 | fplanend | 合同有效期止 | timestamp | 0 |  |  | null | 合同有效期止 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcontractno | 合同编码 | varchar | 50 |  | √ | ' ' | 合同编码 |
| 12 | fplanstart | 合同有效期始 | timestamp | 0 |  |  | null | 合同有效期始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_contract_info |  | fentryid |
| 2 | idx_tcvat_contract_info_fk |  | fid |

---

## 分包合同信息-子表 t_tcvat_split_contract

- **表名称：** 分包合同信息-子表
- **表名：** t_tcvat_split_contract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspartnername | 合同相对方名称 | varchar | 50 |  | √ | ' ' | 合同相对方名称 |
| 3 | fspartnertaxno | 合同相对方税号 | varchar | 50 |  | √ | ' ' | 合同相对方税号 |
| 4 | fsplanstart | 合同有效期始 | timestamp | 0 |  |  | null | 合同有效期始 |
| 5 | fscontractname | 合同名称 | varchar | 50 |  | √ | ' ' | 合同名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fscontractno | 合同编码 | varchar | 50 |  | √ | ' ' | 合同编码 |
| 8 | fsamount | 合同签订金额（元） | numeric | 23 | 10 | √ | 0.0000000000 | 合同签订金额（元） |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fssigndate | 合同签订时间 | timestamp | 0 |  |  | null | 合同签订时间 |
| 11 | fsplanend | 合同有效期止 | timestamp | 0 |  |  | null | 合同有效期止 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_split_contract |  | fentryid |
| 2 | idx_tcvat_split_contract_fk |  | fid |

---

## 预缴项目信息-主表 t_tcvat_prepay_project

- **表名称：** 预缴项目信息-主表
- **表名：** t_tcvat_prepay_project

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flocaledufjsfs | 地方教育附加费 | bpchar | 1 |  | √ | ' ' | 地方教育附加费 |
| 3 | faddress | 项目详细地址 | varchar | 100 |  | √ | ' ' | 项目详细地址 |
| 4 | fyhsratio | 印花税适用预征率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 印花税适用预征率(%) |
| 5 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fzone | 附加税费项目所在地 | varchar | 30 |  | √ | ' ' | 附加税费项目所在地,枚举: cityarea :市区 nocityarea :县城、镇 otherarea :其他 |
| 7 | ftccit | 企业所得税 | bpchar | 1 |  | √ | ' ' | 企业所得税 |
| 8 | fpersonaltax | 个人所得税 | bpchar | 1 |  | √ | ' ' | 个人所得税 |
| 9 | flevytype | 征收方式 | varchar | 30 |  | √ | ' ' | 征收方式,枚举: normal :一般计税 simple :简易计税 |
| 10 | fprojectzone | 项目所在地 | varchar | 100 |  | √ | ' ' | 项目所在地 |
| 11 | forg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fghjf | 工会经费 | bpchar | 1 |  | √ | '0' | 工会经费 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbaseproject | 系统项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flicensecode | 建筑工程施工许可证编号 | varchar | 50 |  | √ | ' ' | 建筑工程施工许可证编号 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fsljsjj | 水利建设基金 | bpchar | 1 |  | √ | '0' | 水利建设基金 |
| 20 | fend | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 21 | fhjbhsratio | 环境保护税预征率(%) | numeric | 23 | 10 | √ | 0 | 环境保护税预征率(%) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fsplit | 是否对外分包 | varchar | 30 |  | √ | ' ' | 是否对外分包,枚举: 1 :是 0 :否 |
| 24 | fpersonalratio | 个人所得税适用预征率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 个人所得税适用预征率(%) |
| 25 | fsljsjjratio | 水利建设基金预征率(%) | numeric | 23 | 10 | √ | 0 | 水利建设基金预征率(%) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fstart | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 28 | ftcvat | 增值税 | bpchar | 1 |  | √ | ' ' | 增值税 |
| 29 | fcross | 是否跨区报验 | varchar | 30 |  | √ | ' ' | 是否跨区报验,枚举: 1 :是 0 :否 |
| 30 | fyhs | 印花税 | bpchar | 1 |  | √ | ' ' | 印花税 |
| 31 | ffjsf | ffjsf | bpchar | 1 |  | √ | ' ' |  |
| 32 | fprepaytype | 预缴项目类型 | varchar | 30 |  | √ | ' ' | 预缴项目类型,枚举: VAT_YJXMLX_001 :异地建筑服务 VAT_YJXMLX_002 :建筑服务预收款 VAT_YJXMLX_003 :房地产项目预售 VAT_YJXMLX_004 :不动产转让 VAT_YJXMLX_005 :异地不动产出租 |
| 33 | fedufjsf | 教育费附加 | bpchar | 1 |  | √ | ' ' | 教育费附加 |
| 34 | fghjfratio | 工会经费预征率(%) | numeric | 23 | 10 | √ | 0 | 工会经费预征率(%) |
| 35 | fprojectstatus | 预缴状态 | varchar | 30 |  | √ | ' ' | 预缴状态,枚举: going :进行中 close :关闭 |
| 36 | fcswhjss | 城市维护建设税 | bpchar | 1 |  | √ | ' ' | 城市维护建设税 |
| 37 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 预缴项目编码 | varchar | 30 |  | √ | ' ' | 预缴项目编码 |
| 39 | fdesc | 项目描述 | varchar | 255 |  | √ | ' ' | 项目描述 |
| 40 | ftaxoffice | 项目所在地主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 41 | fhjbhs | 环境保护税 | bpchar | 1 |  | √ | '0' | 环境保护税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_prepay_project |  | fid |
| 2 | idx_tcvat_prepay_project |  | fnumber |
