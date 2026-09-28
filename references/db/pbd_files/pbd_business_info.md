# 企业查询结果-pbd_business_info

## 被执行人-子表 t_pbd_busi_exeentity

- **表名称：** 被执行人-子表
- **表名：** t_pbd_busi_exeentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexeccaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |
| 3 | fexecmoney | 执行标的 | varchar | 50 |  | √ | ' ' | 执行标的 |
| 4 | fexecthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |
| 5 | fexecpname | 被执行人 | varchar | 255 |  | √ | ' ' | 被执行人 |
| 6 | fexeccasetime | 立案日期 | timestamp | 0 |  |  | null | 立案日期 |
| 7 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 8 | fexeccourt | 执行法院 | varchar | 200 |  | √ | ' ' | 执行法院 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fexecid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 12 | fexechistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_exeentity |  | fentryid |
| 2 | idx_pbd_busi_exe_fid_fseq |  | fid,fseq |

---

## 市场监管抽查-子表 t_pbd_busi_comcheckentity

- **表名称：** 市场监管抽查-子表
- **表名：** t_pbd_busi_comcheckentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomchecktype | 类型 | varchar | 10 |  | √ | ' ' | 类型 |
| 3 | fcomcheckresult | 结果 | varchar | 255 |  | √ | ' ' | 结果 |
| 4 | fcomcheckdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 5 | fcomremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 6 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 7 | fcomcheckorg | 检查实施机关 | varchar | 100 |  | √ | ' ' | 检查实施机关 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fcomcheckresult_tag | 结果_详情 | text | 0 |  |  | null | 结果_详情 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_budi_comcheck_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_comcheckentity |  | fentryid |

---

## 企业联系方式-子表 t_pbd_busi_contactentity

- **表名称：** 企业联系方式-子表
- **表名：** t_pbd_busi_contactentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontactemail | 邮件 | varchar | 50 |  | √ | ' ' | 邮件 |
| 3 | fcontactwebsite | 网址 | varchar | 50 |  | √ | ' ' | 网址 |
| 4 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcontactprovince | 省份 | varchar | 50 |  | √ | ' ' | 省份 |
| 7 | fcontactarea | 区/县 | varchar | 50 |  | √ | ' ' | 区/县 |
| 8 | fcontactaddress | 地址 | varchar | 255 |  | √ | ' ' | 地址 |
| 9 | fcontactcity | 城市 | varchar | 50 |  | √ | ' ' | 城市 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcontactphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_contact_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_contactentity |  | fentryid |

---

## 产品质量抽查-子表 t_pbd_busi_procheckentity

- **表名称：** 产品质量抽查-子表
- **表名：** t_pbd_busi_procheckentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprodate | 生产日期/批号 | varchar | 50 |  | √ | ' ' | 生产日期/批号 |
| 3 | fspecnum | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 4 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 5 | finspectionorg | 承检机构 | varchar | 50 |  | √ | ' ' | 承检机构 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fprocheckresult | 抽查结果 | varchar | 100 |  | √ | ' ' | 抽查结果 |
| 8 | fresultreleasetime | 结果发布日期 | timestamp | 0 |  |  | null | 结果发布日期 |
| 9 | fproname | 产品名称 | varchar | 50 |  | √ | ' ' | 产品名称 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmajordisquproject | 主要不合格项目 | varchar | 50 |  | √ | ' ' | 主要不合格项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_proc_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_procheckentity |  | fentryid |

---

## 经营异常-子表 t_pbd_busi_abnentity

- **表名称：** 经营异常-子表
- **表名：** t_pbd_busi_abnentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremovedepartment | 移出决定机关 | varchar | 200 |  | √ | ' ' | 移出决定机关 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fputdepartment | 作出决定机关 | varchar | 200 |  | √ | ' ' | 作出决定机关 |
| 5 | fabnhistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |
| 6 | fabnremovereason | 移出经营异常名录原因 | varchar | 255 |  | √ | ' ' | 移出经营异常名录原因 |
| 7 | fabnremovereason_tag | 移出经营异常名录原因_详情 | text | 0 |  |  | null | 移出经营异常名录原因_详情 |
| 8 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 9 | fremovedate | 移出日期 | timestamp | 0 |  |  | null | 移出日期 |
| 10 | fabnputreason_tag | 列入异常名录原因_详情 | text | 0 |  |  | null | 列入异常名录原因_详情 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fputdate | 列入日期 | timestamp | 0 |  |  | null | 列入日期 |
| 13 | fabnputreason | 列入异常名录原因 | varchar | 255 |  | √ | ' ' | 列入异常名录原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_abn_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_abnentity |  | fentryid |

---

## 认证抽查-子表 t_pbd_busi_ccheckentity

- **表名称：** 认证抽查-子表
- **表名：** t_pbd_busi_ccheckentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheckproname | 产品名称 | varchar | 50 |  | √ | ' ' | 产品名称 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcheckyear | 抽查年度 | varchar | 11 |  | √ | ' ' | 抽查年度 |
| 5 | fcheckproducttype | 产品种类 | varchar | 50 |  | √ | ' ' | 产品种类 |
| 6 | fcheckcanceldate | 证书撤销日期 | timestamp | 0 |  |  | null | 证书撤销日期 |
| 7 | fcheckspecnum | 规格型号 | varchar | 100 |  | √ | ' ' | 规格型号 |
| 8 | fcertiorg | 认证机构名称 | varchar | 100 |  | √ | ' ' | 认证机构名称 |
| 9 | fcheckunqualifiitem | 不符合项目 | varchar | 200 |  | √ | ' ' | 不符合项目 |
| 10 | fcheckresult | 证书处理结果 | varchar | 200 |  | √ | ' ' | 证书处理结果 |
| 11 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 12 | fcertino | 认证证书号 | varchar | 100 |  | √ | ' ' | 认证证书号 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_ccheck_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_ccheckentity |  | fentryid |

---

## 分支机构-子表 t_pbd_busi_branchentity

- **表名称：** 分支机构-子表
- **表名：** t_pbd_busi_branchentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbranthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |
| 3 | fbranchname | 分支机构名称 | varchar | 255 |  | √ | ' ' | 分支机构名称 |
| 4 | flegalpersonname | 法人 | varchar | 100 |  | √ | ' ' | 法人 |
| 5 | fregstatus | 企业状态 | varchar | 50 |  | √ | ' ' | 企业状态 |
| 6 | festiblishtime | 成立时间 | timestamp | 0 |  |  | null | 成立时间 |
| 7 | fbranchid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 8 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_branchentity |  | fentryid |
| 2 | idx_pbd_busi_branch_fid_fseq |  | fid,fseq |

---

## 行政处罚-子表 t_pbd_busi_punishentity

- **表名称：** 行政处罚-子表
- **表名：** t_pbd_busi_punishentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fpunishstatus | 处罚状态 | varchar | 100 |  | √ | ' ' | 处罚状态 |
| 4 | fpunishthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |
| 5 | fpunishhistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |
| 6 | fpunishname | 处罚名称 | varchar | 100 |  | √ | ' ' | 处罚名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fevidence | 处罚依据 | varchar | 1000 |  | √ | ' ' | 处罚依据 |
| 9 | freason | 处罚事由 | varchar | 255 |  | √ | ' ' | 处罚事由 |
| 10 | freason_tag | 处罚事由_详情 | text | 0 |  |  | null | 处罚事由_详情 |
| 11 | fcontent_tag | 处罚结果/内容_详情 | text | 0 |  |  | null | 处罚结果/内容_详情 |
| 12 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 13 | flegalpersonname1 | 法定代表人 | varchar | 120 |  | √ | ' ' | 法定代表人 |
| 14 | fdecisiondate | 处罚日期 | timestamp | 0 |  |  | null | 处罚日期 |
| 15 | fdepartmentname | 处罚单位 | varchar | 512 |  | √ | ' ' | 处罚单位 |
| 16 | fcontent | 处罚结果/内容 | varchar | 255 |  | √ | ' ' | 处罚结果/内容 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fpunishnumber | 决定文书号 | varchar | 500 |  | √ | ' ' | 决定文书号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_punish_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_punishentity |  | fentryid |

---

## 开庭公告-子表 t_pbd_busi_ktanentity

- **表名称：** 开庭公告-子表
- **表名：** t_pbd_busi_ktanentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkthistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |
| 3 | fktdefendant | 被告 | varchar | 255 |  | √ | ' ' | 被告 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fktlitigant | 当事人 | varchar | 1000 |  | √ | ' ' | 当事人 |
| 6 | fktcourtroom | 法庭 | varchar | 50 |  | √ | ' ' | 法庭 |
| 7 | fktcourt | 法院 | varchar | 200 |  | √ | ' ' | 法院 |
| 8 | fktcaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |
| 9 | fktcourtregreason | 案由 | varchar | 200 |  | √ | ' ' | 案由 |
| 10 | fktdefendant_tag | 被告_详情 | text | 0 |  |  | null | 被告_详情 |
| 11 | fktplaintiff | 原告 | varchar | 255 |  | √ | ' ' | 原告 |
| 12 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fktannouncementid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 15 | fktdate | 开庭日期 | timestamp | 0 |  |  | null | 开庭日期 |
| 16 | fktplaintiff_tag | 原告_详情 | text | 0 |  |  | null | 原告_详情 |
| 17 | fktthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_ktanentity |  | fentryid |
| 2 | idx_pbd_busi_kean_fid_fseq |  | fid,fseq |

---

## 法律诉讼-子表 t_pbd_busi_lawsuitentity

- **表名称：** 法律诉讼-子表
- **表名：** t_pbd_busi_lawsuitentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcasetitle | 案件名称 | varchar | 2000 |  | √ | ' ' | 案件名称 |
| 3 | fjudgetime | 裁判日期 | timestamp | 0 |  |  | null | 裁判日期 |
| 4 | fcasepersons_tag | 涉案方_详情 | text | 0 |  |  | null | 涉案方_详情 |
| 5 | fcasetype | 案件类型 | varchar | 50 |  | √ | ' ' | 案件类型 |
| 6 | fsubmittime | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcaseid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 9 | fcasereason | 案由 | varchar | 500 |  | √ | ' ' | 案由 |
| 10 | fcasecourt | 审理法院 | varchar | 100 |  | √ | ' ' | 审理法院 |
| 11 | fcasemoney | 案件金额 | varchar | 50 |  | √ | ' ' | 案件金额 |
| 12 | fcaseno | 案号 | varchar | 1000 |  | √ | ' ' | 案号 |
| 13 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 14 | fcasepersons | 涉案方 | varchar | 2000 |  | √ | ' ' | 涉案方 |
| 15 | furl | URL | varchar | 255 |  | √ | ' ' | URL |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_lawsuitentity |  | fentryid |
| 2 | idx_pur_busi_laws_fid_fseq |  | fid,fseq |

---

## 变更记录-子表 t_pbd_busi_changeentity

- **表名称：** 变更记录-子表
- **表名：** t_pbd_busi_changeentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontentbefore_tag | 变更前_详情 | text | 0 |  |  | null | 变更前_详情 |
| 3 | fchangeid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 4 | fchangeitem_tag | 变更事项_详情 | text | 0 |  |  | null | 变更事项_详情 |
| 5 | fcontentafter | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |
| 6 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 7 | fcontentbefore | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 8 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fcontentafter_tag | 变更后_详情 | text | 0 |  |  | null | 变更后_详情 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fchangeitem | 变更事项 | varchar | 255 |  | √ | ' ' | 变更事项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_change_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_changeentity |  | fentryid |

---

## 企业查询结果-主表 t_pbd_business_info

- **表名称：** 企业查询结果-主表
- **表名：** t_pbd_business_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 所属地区 | varchar | 255 |  | √ | ' ' | 所属地区 |
| 3 | flegalpersonname | 法人代表 | varchar | 255 |  | √ | ' ' | 法人代表 |
| 4 | fpercentilescore | 企业评分 | numeric | 23 | 10 | √ | 0 | 企业评分 |
| 5 | fillegalinfototal | 严重违法总数 | int4 | 32 |  | √ | 0 | 严重违法总数 |
| 6 | fexecuteetotal | 被执行人总数 | int4 | 32 |  | √ | 0 | 被执行人总数 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcasetotal | 诉讼总数 | int4 | 32 |  | √ | 0 | 诉讼总数 |
| 9 | fcompanyintro | 公司简介 | varchar | 500 |  | √ | ' ' | 公司简介 |
| 10 | fcompanychecktotal | 市场监管抽查总数 | int4 | 32 |  | √ | 0 | 市场监管抽查总数 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fwebsitelist_tag | 公司网址_详情 | text | 0 |  |  | null | 公司网址_详情 |
| 13 | fbusinessscope | 经营范围 | varchar | 255 |  | √ | ' ' | 经营范围 |
| 14 | fislistedcompany | 是否上市 | bpchar | 1 |  | √ | ' ' | 是否上市 |
| 15 | foperatingperiodfrom | 营业期限始 | timestamp | 0 |  |  | null | 营业期限始 |
| 16 | fhistorynames | 曾用名 | varchar | 255 |  | √ | ' ' | 曾用名 |
| 17 | fstafftotal | 主要人员总数 | int4 | 32 |  | √ | 0 | 主要人员总数 |
| 18 | findustry | 所属行业 | varchar | 255 |  | √ | ' ' | 所属行业 |
| 19 | fcourtregistertotal | 立案总数 | int4 | 32 |  | √ | 0 | 立案总数 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fwebsitelist | 公司网址 | varchar | 255 |  | √ | ' ' | 公司网址 |
| 22 | freginstitute | 登记机关 | varchar | 255 |  | √ | ' ' | 登记机关 |
| 23 | fholdertotal | 股东总数 | int4 | 32 |  | √ | 0 | 股东总数 |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcertchecktotal | 认证抽查总数 | int4 | 32 |  | √ | 0 | 认证抽查总数 |
| 26 | fsocialstaffnum | 参保人数 | int8 | 64 |  | √ | 0 | 参保人数 |
| 27 | forgnumber | 组织机构代码 | varchar | 50 |  | √ | ' ' | 组织机构代码 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 30 | festiblishtime | 成立日期 | timestamp | 0 |  |  | null | 成立日期 |
| 31 | factualcapital | 实缴资本 | varchar | 50 |  | √ | ' ' | 实缴资本 |
| 32 | fktannouncementtotal | 开庭总数 | int4 | 32 |  | √ | 0 | 开庭总数 |
| 33 | fcanceldate | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 34 | fregnumber | 注册号 | varchar | 50 |  | √ | ' ' | 注册号 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fbusinessscope_tag | 经营范围_详情 | text | 0 |  |  | null | 经营范围_详情 |
| 37 | fchangetotal | 变更总数 | int4 | 32 |  | √ | 0 | 变更总数 |
| 38 | fcompanyid | 公司Id | varchar | 50 |  | √ | ' ' | 公司Id |
| 39 | foperatingperiodto | 营业期限至 | timestamp | 0 |  |  | null | 营业期限至 |
| 40 | fcreditcode | 统一社会信用代码 | varchar | 255 |  | √ | ' ' | 统一社会信用代码 |
| 41 | ftaxnumber | 纳税人识别号 | varchar | 255 |  | √ | ' ' | 纳税人识别号 |
| 42 | freglocation | 企业注册地址 | varchar | 255 |  | √ | ' ' | 企业注册地址 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fdishonesttotal | 失信人总数 | int4 | 32 |  | √ | 0 | 失信人总数 |
| 45 | fabntotal | 经营异常总数 | int4 | 32 |  | √ | 0 | 经营异常总数 |
| 46 | frevokedate | 吊销日期 | timestamp | 0 |  |  | null | 吊销日期 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fregstatus | 经营状态 | varchar | 50 |  | √ | ' ' | 经营状态 |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fstaffnumrange | 人员规模 | varchar | 255 |  | √ | ' ' | 人员规模 |
| 51 | fsuppliername | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 52 | fproductchecktotal | 产品质量抽查总数 | int4 | 32 |  | √ | 0 | 产品质量抽查总数 |
| 53 | fapprovedtime | 核准日期 | timestamp | 0 |  |  | null | 核准日期 |
| 54 | fregcapital | 注册资本 | varchar | 50 |  | √ | ' ' | 注册资本 |
| 55 | fnewstotal | 新闻总数 | int4 | 32 |  | √ | 0 | 新闻总数 |
| 56 | fbranchtotal | 分支机构总数 | int4 | 32 |  | √ | 0 | 分支机构总数 |
| 57 | fpunishmentinfototal | 行政处罚总数 | int4 | 32 |  | √ | 0 | 行政处罚总数 |
| 58 | fcancelreason | 注销原因 | varchar | 500 |  | √ | ' ' | 注销原因 |
| 59 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 60 | frevokereason | 吊销原因 | varchar | 500 |  | √ | ' ' | 吊销原因 |
| 61 | fcompanyorgtype | 企业类型 | varchar | 255 |  | √ | ' ' | 企业类型 |
| 62 | fcourtannototal | 法院公告总数 | int4 | 32 |  | √ | 0 | 法院公告总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_business_info |  | fid |
| 2 | idx_pbd_business_info_fbillno |  | fbillno |
| 3 | idx_pbd_busi_info_fsupname |  | fsuppliername |
| 4 | idx_pbd_busi_info_fcreattime |  | fcreatetime |

---

## 严重违法-子表 t_pbd_busi_illegalentity

- **表名称：** 严重违法-子表
- **表名：** t_pbd_busi_illegalentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fputreason_tag | 列入原因_详情 | text | 0 |  |  | null | 列入原因_详情 |
| 3 | fputhistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |
| 4 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 5 | fputreason | 列入原因 | varchar | 255 |  | √ | ' ' | 列入原因 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fputdepartment | 决定列入部门 | varchar | 200 |  | √ | ' ' | 决定列入部门 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fputdate | 列入日期 | timestamp | 0 |  |  | null | 列入日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_illegalentity |  | fentryid |
| 2 | idx_pbd_busi_illegal_fid_fseq |  | fid,fseq |

---

## 失信人-子表 t_pbd_busi_dishonentity

- **表名称：** 失信人-子表
- **表名：** t_pbd_busi_dishonentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fperformance | 履行情况 | varchar | 200 |  | √ | ' ' | 履行情况 |
| 3 | fdishonestid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 4 | fdishonesthistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |
| 5 | fdishonestcasetime | 立案日期 | timestamp | 0 |  |  | null | 立案日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdishonestthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |
| 8 | fdishonestregdate | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 9 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 10 | fgistid | 执行依据文号 | varchar | 200 |  | √ | ' ' | 执行依据文号 |
| 11 | fdishonestcaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |
| 12 | fdishonestcourt | 执行法院 | varchar | 200 |  | √ | ' ' | 执行法院 |
| 13 | fdisrupttypename | 行为具体情形 | varchar | 2000 |  | √ | ' ' | 行为具体情形 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fdishonestiname | 失信人名称 | varchar | 255 |  | √ | ' ' | 失信人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_dishonentity |  | fentryid |

---

## 新闻舆情-子表 t_pbd_busi_newsentity

- **表名称：** 新闻舆情-子表
- **表名：** t_pbd_busi_newsentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnewsrtm | 发布日期 | timestamp | 0 |  |  | null | 发布日期 |
| 3 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 4 | fnewstitle | 新闻标题 | varchar | 200 |  | √ | ' ' | 新闻标题 |
| 5 | fnewsurl | 新闻URL | varchar | 300 |  | √ | ' ' | 新闻URL |
| 6 | fnewsemotion | 新闻分类 | varchar | 50 |  | √ | ' ' | 新闻分类,枚举: 1 :正面 0 :中性 -1 :负面 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnewsabstracts | 简介 | varchar | 255 |  | √ | ' ' | 简介 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fnewsthirdpk | 第三方数据主键 | bpchar | 1 |  | √ | '0' | 第三方数据主键 |
| 11 | fdocid | 新闻唯一标识符 | varchar | 255 |  | √ | ' ' | 新闻唯一标识符 |
| 12 | fnewsabstracts_tag | 简介_详情 | text | 0 |  |  | null | 简介_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_news_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_newsentity |  | fentryid |

---

## 法院公告-子表 t_pbd_busi_courtanentity

- **表名称：** 法院公告-子表
- **表名：** t_pbd_busi_courtanentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbltncourt | 受理法院 | varchar | 200 |  | √ | ' ' | 受理法院 |
| 3 | fbltnthistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |
| 4 | fbitnthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |
| 5 | fbltncontent | 案件内容 | varchar | 2000 |  | √ | ' ' | 案件内容 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbltntype | 公告类型 | varchar | 50 |  | √ | ' ' | 公告类型 |
| 8 | fbltndefendant | 被告 | varchar | 2000 |  | √ | ' ' | 被告 |
| 9 | fparty2 | 公告人 | varchar | 2000 |  | √ | ' ' | 公告人 |
| 10 | fbltnno | 公告号 | varchar | 50 |  | √ | ' ' | 公告号 |
| 11 | fbltnpublishdate | 刊登日期 | timestamp | 0 |  |  | null | 刊登日期 |
| 12 | fcourtannoid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 13 | fbltncaseno | 案号 | varchar | 200 |  | √ | ' ' | 案号 |
| 14 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 15 | fparty1 | 原告 | varchar | 2000 |  | √ | ' ' | 原告 |
| 16 | fbltnreason | 案由 | varchar | 500 |  | √ | ' ' | 案由 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fbltncontent_tag | 案件内容_详情 | text | 0 |  |  | null | 案件内容_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_courtanentity |  | fentryid |
| 2 | idx_pbd_busi_courtan_fid_fseq |  | fid,fseq |

---

## 主要人员-子表 t_pbd_busi_staffentity

- **表名称：** 主要人员-子表
- **表名：** t_pbd_busi_staffentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstaffname | 姓名 | varchar | 100 |  | √ | ' ' | 姓名 |
| 3 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 4 | fstaffid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fstaffposition | 职位 | varchar | 255 |  | √ | ' ' | 职位 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_busi_staffentity |  | fentryid |
| 2 | idx_pbd_busi_staff_fid_fseq |  | fid,fseq |

---

## 立案信息-子表 t_pbd_busi_courtregentity

- **表名称：** 立案信息-子表
- **表名：** t_pbd_busi_courtregentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcourtregid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 3 | fcourtregcontent_tag | 案件内容_详情 | text | 0 |  |  | null | 案件内容_详情 |
| 4 | flitigant | 当事人 | varchar | 255 |  | √ | ' ' | 当事人 |
| 5 | fcourtregdefendant | 被告 | varchar | 255 |  | √ | ' ' | 被告 |
| 6 | fcourtregcasetype | 案件类型 | varchar | 50 |  | √ | ' ' | 案件类型 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fcourtregplaintiff | 原告 | varchar | 255 |  | √ | ' ' | 原告 |
| 9 | fcourtregcourt | 受理法院 | varchar | 200 |  | √ | ' ' | 受理法院 |
| 10 | fcourtregcontent | 案件内容 | varchar | 255 |  | √ | ' ' | 案件内容 |
| 11 | fcasestatus | 案件状态 | varchar | 50 |  | √ | ' ' | 案件状态 |
| 12 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 13 | fcourtthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |
| 14 | fcourtregreason | 案由 | varchar | 50 |  | √ | ' ' | 案由 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ffilingdate | 立案日期 | timestamp | 0 |  |  | null | 立案日期 |
| 17 | fcourtregcaseno | 案号 | varchar | 50 |  | √ | ' ' | 案号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_courtreg_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_courtregentity |  | fentryid |

---

## 股权信息-子表 t_pbd_busi_holderentity

- **表名称：** 股权信息-子表
- **表名：** t_pbd_busi_holderentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fholderhistory | 历史 | bpchar | 1 |  | √ | '0' | 历史 |
| 3 | fholderid | 合作方Id | int8 | 64 |  | √ | 0 | 合作方Id |
| 4 | ficholderpercent | 持股比例 | varchar | 50 |  | √ | ' ' | 持股比例 |
| 5 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 6 | fholderthirdpk | 第三方数据主键 | varchar | 100 |  | √ | ' ' | 第三方数据主键 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fholdername | 股东 | varchar | 255 |  | √ | ' ' | 股东 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_busi_holder_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_busi_holderentity |  | fentryid |
