# 专家资料-src_expert

## 评审项目分录-子表 t_src_exportproject

- **表名称：** 评审项目分录-子表
- **表名：** t_src_exportproject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidproject | 评标项目 | varchar | 100 |  | √ | ' ' | 评标项目 |
| 3 | fbidunit | 招标单位 | varchar | 100 |  | √ | ' ' | 招标单位 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparticipatetime | 日期 | timestamp | 0 |  |  | null | 日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_exportproject |  | fentryid |
| 2 | idx_src_exportproject_fid |  | fid |

---

## 专家资料-多语言表 t_src_export_l

- **表名称：** 专家资料-多语言表
- **表名：** t_src_export_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foffice | 工作单位 | varchar | 300 |  | √ | ' ' | 工作单位 |
| 3 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 4 | fname | 专家姓名 | varchar | 300 |  | √ | ' ' | 专家姓名 |
| 5 | fvocationalqualification | 执业资格 | varchar | 300 |  | √ | ' ' | 执业资格 |
| 6 | fjobtitle | 职称 | varchar | 300 |  | √ | ' ' | 职称 |
| 7 | fworkingmajor | 现从事专业 | varchar | 300 |  | √ | ' ' | 现从事专业 |
| 8 | fjob | 职务 | varchar | 300 |  | √ | ' ' | 职务 |
| 9 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 10 | fofficeaddress | 单位地址 | varchar | 300 |  | √ | ' ' | 单位地址 |
| 11 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_export_l |  | fpkid |
| 2 | idx_src_export_l_fid |  | fid,flocaleid |

---

## 专家资料-使用范围位图表 t_src_export_m

- **表名称：** 专家资料-使用范围位图表
- **表名：** t_src_export_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_src_export_m |  | forgid |

---

## 专家资料-使用范围表 t_src_export_u

- **表名称：** 专家资料-使用范围表
- **表名：** t_src_export_u

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
| 1 | idx_t_src_export_u_uo |  | fuseorgid |
| 2 | pk_t_src_export_u |  | fdataid,fuseorgid |

---

## 供应商分录-子表 t_src_exportsupplier

- **表名称：** 供应商分录-子表
- **表名：** t_src_exportsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsuppliernote | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 5 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_exportsupplier |  | fentryid |
| 2 | idx_src_exportsupplier_fid |  | fid |

---

## 附件-附件表 t_src_expertaptitude_fj

- **表名称：** 附件-附件表
- **表名：** t_src_expertaptitude_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_expertaptitude_fj |  | fpkid |
| 2 | idx_src_expertaptitude_fj_eid |  | fentryid |
| 3 | idx_src_expertaptitude_fj_bid |  | fbasedataid |

---

## 证书分录-子表 t_src_expertaptitude

- **表名称：** 证书分录-子表
- **表名：** t_src_expertaptitude

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 3 | faptitudename | 证书名称 | varchar | 255 |  | √ | ' ' | 证书名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | faptitudenote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fissuedate | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 7 | fexperttrainid | 最近专家培训 | int8 | 64 |  | √ | 0 | [专家培训F7 src_experttrainf7](../src_files/src_experttrainf7.md) |
| 8 | faptitudenumber | 证书编号 | varchar | 50 |  | √ | ' ' | 证书编号 |
| 9 | fissueorg | 签发机构 | varchar | 255 |  | √ | ' ' | 签发机构 |
| 10 | faptitudetypeid | 证书类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 11 | fcheckdate | 最近年检日期 | timestamp | 0 |  |  | null | 最近年检日期 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fgrade | 证书等级 | varchar | 20 |  | √ | ' ' | 证书等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_expertaptitude |  | fentryid |
| 2 | idx_src_expertaptitude_fid |  | fid |

---

## 专家资料-主表 t_src_export

- **表名称：** 专家资料-主表
- **表名：** t_src_export

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjobtitle | 职称 | varchar | 300 |  | √ | ' ' | 职称 |
| 3 | fcityid | 城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 4 | forgid | 所属组织(后台) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fevaluatetime | 职称评定时间 | timestamp | 0 |  |  | null | 职称评定时间 |
| 6 | fofficeaddress | 单位地址 | varchar | 300 |  | √ | ' ' | 单位地址 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexpertawardid | 最近专家奖励 | int8 | 64 |  | √ | 0 | [专家奖励F7 src_expertawardf7](../src_files/src_expertawardf7.md) |
| 10 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 11 | fevaluateid | 最近专家考评 | int8 | 64 |  | √ | 0 | [专家考评F7 src_evaluatef7](../src_files/src_evaluatef7.md) |
| 12 | fevaluatedate | 最近更新时间 | timestamp | 0 |  |  | null | 最近更新时间 |
| 13 | fevaluatefrom | 考评期间从 | timestamp | 0 |  |  | null | 考评期间从 |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 16 | fofficephone | 单位电话 | varchar | 50 |  | √ | ' ' | 单位电话 |
| 17 | fname | 专家姓名 | varchar | 300 |  | √ | ' ' | 专家姓名 |
| 18 | fworktime | 从事时间 | timestamp | 0 |  |  | null | 从事时间 |
| 19 | fperiodid | 考评周期 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 20 | femail | E-mail | varchar | 50 |  | √ | ' ' | E-mail |
| 21 | fevaluatescore | 考评得分 | numeric | 23 | 10 | √ | 0 | 考评得分 |
| 22 | ftelephone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 23 | fexpertpunishid | 最近专家处罚 | int8 | 64 |  | √ | 0 | [专家处罚F7 src_expertpunishf7](../src_files/src_expertpunishf7.md) |
| 24 | fevaluategradeid | 考评等级/结果 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 25 | fjob | 职务 | varchar | 300 |  | √ | ' ' | 职务 |
| 26 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 专家编码 | varchar | 30 |  | √ | ' ' | 专家编码 |
| 28 | fsrcbilltype | 最近更新来源 | bpchar | 1 |  | √ | ' ' | 最近更新来源,枚举: 1 :专家考评 2 :专家奖励 3 :专家处罚 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fpausefrom | 暂停评标期间从 | timestamp | 0 |  |  | null | 暂停评标期间从 |
| 31 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 32 | foffice | 工作单位 | varchar | 300 |  | √ | ' ' | 工作单位 |
| 33 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fvocationalqualification | 执业资格 | varchar | 300 |  | √ | ' ' | 执业资格 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 37 | fpauseto | 暂停评标期间至 | timestamp | 0 |  |  | null | 暂停评标期间至 |
| 38 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 39 | fevaluatetypeid | 考评类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 40 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fqualifytime | 执业资格取得时间 | timestamp | 0 |  |  | null | 执业资格取得时间 |
| 42 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fuserid | 对应的系统用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fpoliticalstatus | 政治面貌 | bpchar | 1 |  | √ | ' ' | 政治面貌,枚举: 1 :中共党员 2 :共青团员 3 :群众 4 :民主党派成员 5 :其他 |
| 47 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fidnumber | 身份证号码 | varchar | 50 |  | √ | ' ' | 身份证号码 |
| 49 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 50 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 51 | fsex | 性别 | bpchar | 1 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 : |
| 52 | fevaluateto | 考评期间至 | timestamp | 0 |  |  | null | 考评期间至 |
| 53 | ftype | 专家来源 | bpchar | 1 |  | √ | ' ' | 专家来源,枚举: 1 :内部专家 2 :外部专家 |
| 54 | fproficientlevelid | 专家级别 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 55 | fproficienttypeid | 专家类型(单选) | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 56 | fworkingmajor | fworkingmajor | varchar | 300 |  | √ | ' ' |  |
| 57 | fbirthdate | 出生年月日 | timestamp | 0 |  |  | null | 出生年月日 |
| 58 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_src_export_master |  | fmasterid |
| 2 | idx_src_export_org |  | forgid |
| 3 | idx_src_export_telphone |  | ftelephone |
| 4 | pk_src_export |  | fid |
| 5 | idx_t_src_export_createorg |  | fcreateorgid |
| 6 | idx_src_export_user |  | fuserid |
| 7 | idx_src_export_number |  | fnumber |

---

## 专家类型-多选基础资料表 t_src_export_experttype

- **表名称：** 专家类型-多选基础资料表
- **表名：** t_src_export_experttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_export_experttype_bid |  | fbasedataid |
| 2 | pk_src_export_experttype |  | fpkid |
| 3 | idx_src_export_experttype_fid |  | fid |

---

## 关联子实体-子表 t_src_export_lk

- **表名称：** 关联子实体-子表
- **表名：** t_src_export_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_export_lk |  | fpkid |
| 2 | idx_src_export_lk_fk |  | fid |

---

## 教育经历分录-子表 t_src_exporteducation

- **表名称：** 教育经历分录-子表
- **表名：** t_src_exporteducation

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
| 1 | pk_src_exporteducation |  | fentryid |
| 2 | idx_src_exporteducation_fid |  | fid |

---

## 专业分类-多选基础资料表 t_src_expertcategory

- **表名称：** 专业分类-多选基础资料表
- **表名：** t_src_expertcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_expertcategory |  | fpkid |
| 2 | idx_src_expertcategory_fid |  | fid |
| 3 | idx_src_expertcategory_bid |  | fbasedataid |

---

## 证书分录-多语言表 t_src_expertaptitude_l

- **表名称：** 证书分录-多语言表
- **表名：** t_src_expertaptitude_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | faptitudename | 证书名称 | varchar | 300 |  | √ | ' ' | 证书名称 |
| 2 | fissueorg | 签发机构 | varchar | 300 |  | √ | ' ' | 签发机构 |
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
| 1 | idx_src_expertaptitude_l_fid |  | fentryid,flocaleid |
| 2 | pk_src_expertaptitude_l |  | fpkid |

---

## 工作经历分录-子表 t_src_exportwork

- **表名称：** 工作经历分录-子表
- **表名：** t_src_exportwork

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
| 1 | idx_src_exportwork_fid |  | fid |
| 2 | pk_src_exportwork |  | fentryid |

---

## 评标类型-多选基础资料表 t_src_exporttype

- **表名称：** 评标类型-多选基础资料表
- **表名：** t_src_exporttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_exporttype_fid |  | fid |
| 2 | pk_src_exporttype |  | fpkid |
