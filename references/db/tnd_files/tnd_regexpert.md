# 专家资料填写-tnd_regexpert

## 专家资料填写-多语言表 t_src_regexpert_l

- **表名称：** 专家资料填写-多语言表
- **表名：** t_src_regexpert_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foffice | 工作单位 | varchar | 300 |  | √ | ' ' | 工作单位 |
| 3 | fremark | 注册事由 | varchar | 300 |  | √ | ' ' | 注册事由 |
| 4 | fname | 姓名 | varchar | 300 |  | √ | ' ' | 姓名 |
| 5 | fvocationalqualification | 执业资格 | varchar | 300 |  | √ | ' ' | 执业资格 |
| 6 | fjobtitle | 职称 | varchar | 300 |  | √ | ' ' | 职称 |
| 7 | fworkingmajor | 现从事专业 | varchar | 300 |  | √ | ' ' | 现从事专业 |
| 8 | fjob | 职务 | varchar | 300 |  | √ | ' ' | 职务 |
| 9 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 10 | fofficeaddress | 单位地址 | varchar | 300 |  | √ | ' ' | 单位地址 |
| 11 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 12 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_regexpert_l |  | fpkid |
| 2 | idx_src_regexpert_l_fid |  | fid,flocaleid |

---

## 专家资料填写-使用范围表 t_src_regexpert_u

- **表名称：** 专家资料填写-使用范围表
- **表名：** t_src_regexpert_u

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
| 1 | idx_t_src_regexpert_u_uo |  | fuseorgid |
| 2 | pk_t_src_regexpert_u |  | fdataid,fuseorgid |

---

## 教育经历分录-子表 t_src_regexperteducation

- **表名称：** 教育经历分录-子表
- **表名：** t_src_regexperteducation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgraduateschool | 毕业院校 | varchar | 100 |  | √ | ' ' | 毕业院校 |
| 3 | fdateto | 时间.结束 | timestamp | 0 |  |  | null | 时间.结束 |
| 4 | feducationdegree | 学历 | varchar | 50 |  | √ | ' ' | 学历 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdatefrom | 时间.开始 | timestamp | 0 |  |  | null | 时间.开始 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmajor | 专业 | varchar | 50 |  | √ | ' ' | 专业 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_regexperteducation_fid |  | fid |
| 2 | pk_src_regexperteducation |  | fentryid |

---

## 工作经历分录-子表 t_src_regexpertwork

- **表名称：** 工作经历分录-子表
- **表名：** t_src_regexpertwork

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fduty | 职务 | varchar | 50 |  | √ | ' ' | 职务 |
| 3 | fdateto | 时间.结束 | timestamp | 0 |  |  | null | 时间.结束 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdatefrom | 时间.开始 | timestamp | 0 |  |  | null | 时间.开始 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fworkunit | 工作单位 | varchar | 100 |  | √ | ' ' | 工作单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_regexpertwork_fid |  | fid |
| 2 | pk_src_regexpertwork |  | fentryid |

---

## 供应商分录-子表 t_src_regexpertsupplier

- **表名称：** 供应商分录-子表
- **表名：** t_src_regexpertsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsuppliernote | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 5 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_regexpertsupplier |  | fentryid |
| 2 | idx_src_regexpertsupplier_fid |  | fid |

---

## 附件-附件表 t_src_regexpertapt_fj

- **表名称：** 附件-附件表
- **表名：** t_src_regexpertapt_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_regexpertapt_fj_bid |  | fbasedataid |
| 2 | pk_src_regexpertapt_fj |  | fpkid |
| 3 | idx_src_regexpertapt_fj_eid |  | fentryid |

---

## 证书分录-子表 t_src_regexpertaptitude

- **表名称：** 证书分录-子表
- **表名：** t_src_regexpertaptitude

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 3 | faptitudename | 证书名称 | varchar | 255 |  | √ | ' ' | 证书名称 |
| 4 | faptitudenumber | 证书编号 | varchar | 50 |  | √ | ' ' | 证书编号 |
| 5 | fissueorg | 签发机构 | varchar | 255 |  | √ | ' ' | 签发机构 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | faptitudenote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | faptitudetypeid | 证书类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 9 | fissuedate | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 10 | fcheckdate | 最近年检日期 | timestamp | 0 |  |  | null | 最近年检日期 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fgrade | 证书等级 | varchar | 20 |  | √ | ' ' | 证书等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_regexpertaptitude_fid |  | fid |
| 2 | pk_src_regexpertaptitude |  | fentryid |

---

## 评标类型-多选基础资料表 t_src_expert_pbtype

- **表名称：** 评标类型-多选基础资料表
- **表名：** t_src_expert_pbtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_expert_pbtype_fid |  | fid |
| 2 | pk_src_expert_pbtype |  | fpkid |

---

## 专家类型-多选基础资料表 t_src_regexpert_type

- **表名称：** 专家类型-多选基础资料表
- **表名：** t_src_regexpert_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_regexpert_type_fid |  | fid |
| 2 | pk_src_regexpert_type |  | fpkid |
| 3 | idx_src_regexpert_type_bid |  | fbasedataid |

---

## 评审项目分录-子表 t_src_expertproject

- **表名称：** 评审项目分录-子表
- **表名：** t_src_expertproject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidproject | 评标项目 | varchar | 100 |  | √ | ' ' | 评标项目 |
| 3 | fbidunit | 招标单位 | varchar | 100 |  | √ | ' ' | 招标单位 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fprojectnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparticipatetime | 日期 | timestamp | 0 |  |  | null | 日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_expertproject_fid |  | fid |
| 2 | pk_src_expertproject |  | fentryid |

---

## 专家资料填写-主表 t_src_regexpert

- **表名称：** 专家资料填写-主表
- **表名：** t_src_regexpert

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjobtitle | fjobtitle | varchar | 300 |  | √ | ' ' |  |
| 3 | fexecuteresult | 执行结果 | bpchar | 1 |  | √ | ' ' | 执行结果,枚举: 2 :执行中 3 :执行失败 4 :已完成 |
| 4 | fcityid | 城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 5 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fevaluatetime | 职称评定时间 | timestamp | 0 |  |  | null | 职称评定时间 |
| 7 | fofficeaddress | fofficeaddress | varchar | 300 |  | √ | ' ' |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | foffice | foffice | varchar | 300 |  | √ | ' ' |  |
| 11 | fpicture | 头像 | varchar | 300 |  | √ | ' ' | 头像 |
| 12 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | 'A' | 审批状态,枚举: A :填写资料 B :待审批 C :审批通过 D :待修改 E :终止 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fvocationalqualification | fvocationalqualification | varchar | 300 |  | √ | ' ' |  |
| 15 | forigin | 发起方 | bpchar | 1 |  | √ | '2' | 发起方,枚举: 1 :专家 2 :采购方 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fispushexpert | fispushexpert | bpchar | 1 |  | √ | '0' |  |
| 21 | fofficephone | 单位电话 | varchar | 50 |  | √ | ' ' | 单位电话 |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fqualifytime | 执业资格取得时间 | timestamp | 0 |  |  | null | 执业资格取得时间 |
| 24 | fremark | 注册事由 | varchar | 300 |  | √ | ' ' | 注册事由 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fname | 姓名 | varchar | 300 |  | √ | ' ' | 姓名 |
| 27 | fworktime | 从事时间 | timestamp | 0 |  |  | null | 从事时间 |
| 28 | fcreatetime | 申请时间 | timestamp | 0 |  |  | null | 申请时间 |
| 29 | femail | E-mail | varchar | 50 |  | √ | ' ' | E-mail |
| 30 | fuserid | 对应的系统用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fpoliticalstatus | 政治面貌 | bpchar | 1 |  | √ | ' ' | 政治面貌,枚举: 1 :中共党员 2 :共青团员 3 :群众 4 :民主党派成员 5 :其他 |
| 32 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 33 | fidnumber | 身份证号码 | varchar | 50 |  | √ | ' ' | 身份证号码 |
| 34 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 35 | ftelephone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 36 | fsex | 性别 | bpchar | 1 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 :保密 |
| 37 | ftype | 专家来源 | bpchar | 1 |  | √ | ' ' | 专家来源,枚举: 1 :内部专家 2 :外部专家 |
| 38 | fproficientlevelid | 专家级别 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 39 | fworkingmajor | fworkingmajor | varchar | 300 |  | √ | ' ' |  |
| 40 | fproficienttypeid | 专家类型(单选) | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 41 | fbirthdate | 出生年月日 | timestamp | 0 |  |  | null | 出生年月日 |
| 42 | fjob | fjob | varchar | 300 |  | √ | ' ' |  |
| 43 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 44 | fnumber | 审批单编号 | varchar | 30 |  | √ | ' ' | 审批单编号 |
| 45 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_regexpert_user |  | fuserid |
| 2 | idx_src_regexpert_org |  | forgid |
| 3 | pk_src_regexpert |  | fid |
| 4 | idx_src_regexpert_telphone |  | ftelephone |
| 5 | idx_t_src_regexpert_master |  | fmasterid |
| 6 | idx_t_src_regexpert_createorg |  | fcreateorgid |
| 7 | idx_src_regexpert_number |  | fnumber |

---

## 专业分类-多选基础资料表 t_src_regexpertcategory

- **表名称：** 专业分类-多选基础资料表
- **表名：** t_src_regexpertcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_regexpertcategory_fid |  | fid |
| 2 | idx_src_regexpertcategory_bid |  | fbasedataid |
| 3 | pk_src_regexpertcategory |  | fpkid |
