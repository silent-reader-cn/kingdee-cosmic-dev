# 结构化简历-recru_structresume

## 结构化简历-主表 t_recru_structresume

- **表名称：** 结构化简历-主表
- **表名：** t_recru_structresume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fworkingseniority | 工龄 | numeric | 23 | 10 | √ | 0 | 工龄 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fnation | 民族 | varchar | 50 |  | √ | ' ' | 民族 |
| 5 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcontactemail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fpostalcode | 邮政编码 | varchar | 50 |  | √ | ' ' | 邮政编码 |
| 10 | fcity | 城市 | varchar | 50 |  | √ | ' ' | 城市 |
| 11 | fpolitical | 政治面貌 | varchar | 50 |  | √ | ' ' | 政治面貌 |
| 12 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbirthday | 出生日期 | timestamp | 0 |  |  | null | 出生日期 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fgender | 性别 | varchar | 2 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 3 :未知 |
| 17 | fregisteredresidence | 户口所在地 | varchar | 50 |  | √ | ' ' | 户口所在地 |
| 18 | ftopeducation | 最高学历 | varchar | 50 |  | √ | ' ' | 最高学历 |
| 19 | fmarital | 婚姻状况 | varchar | 50 |  | √ | ' ' | 婚姻状况 |
| 20 | fdateofbirth | 出生日期 | varchar | 50 |  | √ | ' ' | 出生日期 |
| 21 | fpersonid | 身份证号码 | varchar | 50 |  | √ | ' ' | 身份证号码 |
| 22 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnativeplace | 籍贯 | varchar | 255 |  | √ | ' ' | 籍贯 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fcellphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 26 | fcountry | 国家 | varchar | 50 |  | √ | ' ' | 国家 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_structresume_phone |  | fcellphone |
| 2 | pk_recru_structresume |  | fid |

---

## 结构化简历-多语言表 t_recru_structresume_l

- **表名称：** 结构化简历-多语言表
- **表名：** t_recru_structresume_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_structresume_l_fid |  | fid,flocaleid |
| 2 | pk_recru_structresume_l |  | fpkid |

---

## 工作经历单据体-子表 t_recru_workexperience

- **表名称：** 工作经历单据体-子表
- **表名：** t_recru_workexperience

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjobtitle | 职位名称 | varchar | 255 |  | √ | ' ' | 职位名称 |
| 3 | fdepartment | 部门名称 | varchar | 255 |  | √ | ' ' | 部门名称 |
| 4 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | femployer | 企业名称 | varchar | 255 |  | √ | ' ' | 企业名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fjobdescription | 工作描述 | varchar | 2000 |  | √ | ' ' | 工作描述 |
| 9 | fendate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_workexperience_fid |  | fid |
| 2 | pk_recru_workexperience |  | fentryid |

---

## 专业技能单据体-子表 t_recru_professionalskill

- **表名称：** 专业技能单据体-子表
- **表名：** t_recru_professionalskill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fleveldesc | 专业技能描述 | varchar | 2000 |  | √ | ' ' | 专业技能描述 |
| 5 | fskill | 技能 | varchar | 1000 |  | √ | ' ' | 技能 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_professionalskill |  | fentryid |
| 2 | idx_recru_professskill_fid |  | fid |

---

## 证书单据体-子表 t_recru_certificates

- **表名称：** 证书单据体-子表
- **表名：** t_recru_certificates

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissuancedate | 颁发日期 | timestamp | 0 |  |  | null | 颁发日期 |
| 3 | fvalidityperiod | 证书有效期 | varchar | 50 |  | √ | ' ' | 证书有效期 |
| 4 | fcertificate | 证书 | varchar | 255 |  | √ | ' ' | 证书 |
| 5 | fissuanceauthority | 颁发机构 | varchar | 1000 |  | √ | ' ' | 颁发机构 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_certificates |  | fentryid |
| 2 | idx_recru_certificates_fid |  | fid |

---

## 项目经历单据体-子表 t_recru_projectexperience

- **表名称：** 项目经历单据体-子表
- **表名：** t_recru_projectexperience

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectname | 项目名称 | varchar | 255 |  | √ | ' ' | 项目名称 |
| 3 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | femployer | 企业名称 | varchar | 255 |  | √ | ' ' | 企业名称 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fprojectdescription | 项目描述 | varchar | 2000 |  | √ | ' ' | 项目描述 |
| 9 | frole | 项目角色 | varchar | 255 |  | √ | ' ' | 项目角色 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_recru_projectexper_fid |  | fid |
| 2 | pk_recru_projectexperience |  | fentryid |

---

## 语言能力单据体-子表 t_recru_languageskills

- **表名称：** 语言能力单据体-子表
- **表名：** t_recru_languageskills

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flanguage | 语言 | varchar | 1000 |  | √ | ' ' | 语言 |
| 3 | fseq | 分录行号 | varchar | 50 |  | √ | ' ' | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fability | 语言能力 | varchar | 2000 |  | √ | ' ' | 语言能力 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_languageskills |  | fentryid |
| 2 | idx_recru_languageskills_fid |  | fid |

---

## 教育经历单据体-子表 t_recru_education

- **表名称：** 教育经历单据体-子表
- **表名：** t_recru_education

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | fdegree | 学位 | varchar | 50 |  | √ | ' ' | 学位 |
| 4 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fschool | 学校 | varchar | 128 |  | √ | ' ' | 学校 |
| 6 | fhighestdegree | 最高学历 | bpchar | 1 |  | √ | '0' | 最高学历 |
| 7 | fmajordesc | 专业描述 | varchar | 2000 |  | √ | ' ' | 专业描述 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | feducation | 学历 | varchar | 50 |  | √ | ' ' | 学历 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmajor | 专业 | varchar | 128 |  | √ | ' ' | 专业 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_education |  | fentryid |
| 2 | idx_recru_education_fid |  | fid |
