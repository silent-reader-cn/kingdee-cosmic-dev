# 调查问卷-bdtaxr_questionnaire_set

## 调查问卷-主表 t_bdtaxr_questionnaire

- **表名称：** 调查问卷-主表
- **表名：** t_bdtaxr_questionnaire

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 问卷名称 | varchar | 50 |  | √ | ' ' | 问卷名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fispreset | 系统预置 | varchar | 50 |  | √ | ' ' | 系统预置,枚举: 1 :是 0 :否 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fappname | 适用应用 | varchar | 50 |  | √ | '0' | 业务应用实体 bos_devportal_bizapp |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_questionnaire |  | fid |
| 2 | idx_bdtaxr_naireorg |  | forg,fappname |
| 3 | idx_t_bdtaxr_questionnaire_master |  | fmasterid |
| 4 | idx_t_bdtaxr_questionnaire_createorg |  | fcreateorgid |

---

## 问卷设置-子表 t_bdtaxr_questionset

- **表名称：** 问卷设置-子表
- **表名：** t_bdtaxr_questionset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fanswer | fanswer | varchar | 50 |  | √ | ' ' |  |
| 3 | ffinalscore | 最终得分 | int8 | 64 |  | √ | 0 | 最终得分 |
| 4 | fstandardscore | 最大分值 | int8 | 64 |  | √ | 0 | 最大分值 |
| 5 | foptionset | 选项设置 | varchar | 2000 |  | √ | ' ' | 选项设置 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fproblemtype | 问题类型 | varchar | 50 |  | √ | ' ' | 问题类型,枚举: choice :选择题 inputscore :填分题 essayque :问答题 oneticketveto :一票否决题 |
| 8 | fproblemdesc | fproblemdesc | varchar | 2000 |  | √ | ' ' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fquesclassif | fquesclassif | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_questionset |  | fentryid |
| 2 | idx_bdtaxr_questionset_fk |  | fid |

---

## 调查问卷-使用范围表 t_bdtaxr_questionnaire_u

- **表名称：** 调查问卷-使用范围表
- **表名：** t_bdtaxr_questionnaire_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bdtaxr_questionnaire_u |  | fdataid,fuseorgid |
| 2 | idx_t_bdtaxr_questionnaire_u_uo |  | fuseorgid |

---

## 调查问卷-多语言表 t_bdtaxr_questionnaire_l

- **表名称：** 调查问卷-多语言表
- **表名：** t_bdtaxr_questionnaire_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 问卷名称 | varchar | 500 |  | √ | ' ' | 问卷名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_questionnaire_l_0 |  | fid,flocaleid |
| 2 | pk_bdtaxr_questionnaire_l |  | fpkid |

---

## 选项设置子单据体-子表 t_bdtaxr_questionoption

- **表名称：** 选项设置子单据体-子表
- **表名：** t_bdtaxr_questionoption

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fsubentry_standardscore | 标准得分 | int8 | 64 |  | √ | 0 | 标准得分 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_questionoption |  | fdetailid |
| 2 | idx_bdtaxr_questionoption_fk |  | fentryid |

---

## 问卷设置-多语言表 t_bdtaxr_questionset_l

- **表名称：** 问卷设置-多语言表
- **表名：** t_bdtaxr_questionset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fanswer | 答案 | varchar | 2000 |  | √ | ' ' | 答案 |
| 2 | fproblemdesc | 问题描述 | varchar | 2000 |  | √ | ' ' | 问题描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fquesclassif | fquesclassif | varchar | 2000 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_questionset_l_0 |  | fentryid,flocaleid |
| 2 | pk_bdtaxr_questionset_l |  | fpkid |

---

## 选项设置子单据体-多语言表 t_bdtaxr_questionoption_l

- **表名称：** 选项设置子单据体-多语言表
- **表名：** t_bdtaxr_questionoption_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | foption | 选项 | varchar | 2000 |  | √ | ' ' | 选项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_questionoption_l_0 |  | fdetailid,flocaleid |
| 2 | pk_bdtaxr_questionoption_l |  | fpkid |
