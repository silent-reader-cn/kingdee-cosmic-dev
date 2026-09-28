# 调查问卷-rdem_questionnaire_set

## 调查问卷-主表 t_rdem_questionnaire

- **表名称：** 调查问卷-主表
- **表名：** t_rdem_questionnaire

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 问卷名称 | varchar | 50 |  | √ | ' ' | 问卷名称 |
| 5 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fispreset | 系统预置 | varchar | 50 |  | √ | ' ' | 系统预置,枚举: 1 :是 0 :否 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fappname | 适用应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
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
| 1 | idx_rdem_questionnaire_m0 |  | fmasterid |
| 2 | pk_rdem_questionnaire |  | fid |
| 3 | idx_t_rdem_questionnaire_createorg |  | fcreateorgid |
| 4 | idx_t_rdem_questionnaire_master |  | fmasterid |

---

## 问卷设置-子表 t_rdem_questionset

- **表名称：** 问卷设置-子表
- **表名：** t_rdem_questionset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fanswer | 答案 | varchar | 200 |  | √ | ' ' | 答案 |
| 3 | ffinalscore | 最终得分 | int8 | 64 |  | √ | 0 | 最终得分 |
| 4 | fstandardscore | 最大分值 | int8 | 64 |  | √ | 0 | 最大分值 |
| 5 | foptionset | 选项设置 | varchar | 2000 |  | √ | ' ' | 选项设置 |
| 6 | fproblemtype | 问题类型 | varchar | 50 |  | √ | ' ' | 问题类型,枚举: choice :选择题 inputscore :填分题 essayque :问答题 oneticketveto :一票否决题 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fproblemdesc | 问题描述 | varchar | 500 |  | √ | ' ' | 问题描述 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_questionset |  | fentryid |
| 2 | idx_rdem_questionset_fk |  | fid |

---

## 问卷设置-多语言表 t_rdem_questionset_l

- **表名称：** 问卷设置-多语言表
- **表名：** t_rdem_questionset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fanswer | 答案 | varchar | 300 |  | √ | ' ' | 答案 |
| 2 | fproblemdesc | 问题描述 | varchar | 755 |  | √ | ' ' | 问题描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_questionset_l |  | fpkid |
| 2 | idx_rdem_questionset_l_0 |  | fentryid,flocaleid |

---

## 选项设置子单据体-子表 t_rdem_questionoption

- **表名称：** 选项设置子单据体-子表
- **表名：** t_rdem_questionoption

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubentry_standardscore | 标准得分 | int8 | 64 |  | √ | 0 | 标准得分 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_questionoption |  | fdetailid |
| 2 | idx_rdem_questionoption_fk |  | fentryid |

---

## 选项设置子单据体-多语言表 t_rdem_questionoption_l

- **表名称：** 选项设置子单据体-多语言表
- **表名：** t_rdem_questionoption_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | foption | 选项 | varchar | 230 |  | √ | ' ' | 选项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdem_questionoption_l_0 |  | fdetailid,flocaleid |
| 2 | pk_rdem_questionoption_l |  | fpkid |

---

## 调查问卷-多语言表 t_rdem_questionnaire_l

- **表名称：** 调查问卷-多语言表
- **表名：** t_rdem_questionnaire_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 问卷名称 | varchar | 255 |  | √ | ' ' | 问卷名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_questionnaire_l |  | fpkid |
| 2 | idx_rdem_questionnaire_l_0 |  | fid,flocaleid |

---

## 调查问卷-使用范围表 t_rdem_questionnaire_u

- **表名称：** 调查问卷-使用范围表
- **表名：** t_rdem_questionnaire_u

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
| 1 | pk_t_rdem_questionnaire_u |  | fdataid,fuseorgid |
| 2 | idx_t_rdem_questionnaire_u_uo |  | fuseorgid |
