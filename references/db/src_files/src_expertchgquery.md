# 资料变更查询-src_expertchgquery

## 证书分录-多语言表 t_src_expertaptitudechg_l

- **表名称：** 证书分录-多语言表
- **表名：** t_src_expertaptitudechg_l

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
| 1 | idx_src_expertaptchg_l_fid |  | fentryid,flocaleid |
| 2 | pk_src_expertaptitudechg_l |  | fpkid |

---

## 资料变更查询-主表 t_src_exportchg

- **表名称：** 资料变更查询-主表
- **表名：** t_src_exportchg

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
| 9 | fisselfhelp | 是否专家自助 | bpchar | 1 |  | √ | '0' | 是否专家自助 |
| 10 | fexpertawardid | 最近专家奖励 | int8 | 64 |  | √ | 0 | [专家奖励F7 src_expertawardf7](../src_files/src_expertawardf7.md) |
| 11 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 12 | fevaluateid | 最近专家考评 | int8 | 64 |  | √ | 0 | [专家考评F7 src_evaluatef7](../src_files/src_evaluatef7.md) |
| 13 | fevaluatedate | 最近更新时间 | timestamp | 0 |  |  | null | 最近更新时间 |
| 14 | fevaluatefrom | 考评期间从 | timestamp | 0 |  |  | null | 考评期间从 |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 17 | fisconfirm | 是否需要采购方审批 | bpchar | 1 |  | √ | '0' | 是否需要采购方审批 |
| 18 | fofficephone | 单位电话 | varchar | 50 |  | √ | ' ' | 单位电话 |
| 19 | fbillno | 变更单号 | varchar | 30 |  | √ | ' ' | 变更单号 |
| 20 | fname | 专家姓名 | varchar | 300 |  | √ | ' ' | 专家姓名 |
| 21 | fworktime | 从事时间 | timestamp | 0 |  |  | null | 从事时间 |
| 22 | fperiodid | 考评周期 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 23 | femail | E-mail | varchar | 50 |  | √ | ' ' | E-mail |
| 24 | fevaluatescore | 考评得分 | numeric | 23 | 10 | √ | 0 | 考评得分 |
| 25 | ftelephone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 26 | fexpertpunishid | 最近专家处罚 | int8 | 64 |  | √ | 0 | [专家处罚F7 src_expertpunishf7](../src_files/src_expertpunishf7.md) |
| 27 | fevaluategradeid | 考评等级/结果 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 28 | fjob | 职务 | varchar | 300 |  | √ | ' ' | 职务 |
| 29 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 专家编码 | varchar | 30 |  | √ | ' ' | 专家编码 |
| 31 | fsrcbilltype | 最近更新来源 | bpchar | 1 |  | √ | ' ' | 最近更新来源,枚举: 1 :专家考评 2 :专家奖励 3 :专家处罚 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 33 | fpausefrom | 暂停评标期间从 | timestamp | 0 |  |  | null | 暂停评标期间从 |
| 34 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 35 | description | 变更原因 | varchar | 510 |  | √ | ' ' | 变更原因 |
| 36 | foffice | 工作单位 | varchar | 300 |  | √ | ' ' | 工作单位 |
| 37 | fstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :暂存 B :已提交 C :已审核 |
| 38 | fvocationalqualification | 执业资格 | varchar | 300 |  | √ | ' ' | 执业资格 |
| 39 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 41 | fpauseto | 暂停评标期间至 | timestamp | 0 |  |  | null | 暂停评标期间至 |
| 42 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 43 | fevaluatetypeid | 考评类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 44 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fqualifytime | 执业资格取得时间 | timestamp | 0 |  |  | null | 执业资格取得时间 |
| 46 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fexpertld | 专家 | int8 | 64 |  | √ | 0 | [专家资料 src_expert](../src_files/src_expert.md) |
| 49 | fcreatetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 50 | fuserid | 对应的系统用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | fpoliticalstatus | 政治面貌 | bpchar | 1 |  | √ | ' ' | 政治面貌,枚举: 1 :中共党员 2 :共青团员 3 :群众 4 :民主党派成员 5 :其他 |
| 52 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fidnumber | 身份证号码 | varchar | 50 |  | √ | ' ' | 身份证号码 |
| 54 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 55 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 56 | fsex | 性别 | bpchar | 1 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 0 : |
| 57 | fevaluateto | 考评期间至 | timestamp | 0 |  |  | null | 考评期间至 |
| 58 | ftype | 专家来源 | bpchar | 1 |  | √ | ' ' | 专家来源,枚举: 1 :内部专家 2 :外部专家 |
| 59 | fproficientlevelid | 专家级别 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 60 | fproficienttypeid | 专家类型(单选) | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 61 | fworkingmajor | fworkingmajor | varchar | 300 |  | √ | ' ' |  |
| 62 | fbirthdate | 出生年月日 | timestamp | 0 |  |  | null | 出生年月日 |
| 63 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_src_exportchg_master |  | fmasterid |
| 2 | idx_src_exportchg_user |  | fuserid |
| 3 | pk_src_exportchg |  | fid |
| 4 | idx_src_exportchg_expert |  | fexpertld |
| 5 | idx_t_src_exportchg_createorg |  | fcreateorgid |
| 6 | idx_src_exportchg_number |  | fnumber |
| 7 | idx_src_exportchg_telphone |  | ftelephone |
| 8 | idx_src_exportchg_org |  | forgid |

---

## 变更摘要分录-子表 t_src_expertchange

- **表名称：** 变更摘要分录-子表
- **表名：** t_src_expertchange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 变更项目 | varchar | 100 |  | √ | ' ' | 变更项目 |
| 3 | foldvalue | 变更前内容 | varchar | 2000 |  | √ | ' ' | 变更前内容 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fchangetype | 变更类型 | bpchar | 1 |  | √ | '3' | 变更类型,枚举: 1 :新增 2 :删除 3 :修改 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ffieldid | 变更字段ID | varchar | 50 |  | √ | ' ' | 变更字段ID |
| 8 | fnewvalue | 变更后内容 | varchar | 2000 |  | √ | ' ' | 变更后内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_expertchange |  | fentryid |
| 2 | idx_src_expertchange_fid |  | fid |

---

## 教育经历分录-子表 t_src_exporteducationchg

- **表名称：** 教育经历分录-子表
- **表名：** t_src_exporteducationchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgraduateschool | 毕业院校 | varchar | 100 |  | √ | ' ' | 毕业院校 |
| 3 | fdateto | 时间.结束 | timestamp | 0 |  |  | null | 时间.结束 |
| 4 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 5 | feducationdegree | 学历 | varchar | 50 |  | √ | ' ' | 学历 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdatefrom | 时间.开始 | timestamp | 0 |  |  | null | 时间.开始 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmajor | 专业 | varchar | 50 |  | √ | ' ' | 专业 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_exporteducationchg_fid |  | fid |
| 2 | pk_src_exporteducationchg |  | fentryid |

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

## 评审项目分录-子表 t_src_exportprojectchg

- **表名称：** 评审项目分录-子表
- **表名：** t_src_exportprojectchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbidproject | 评标项目 | varchar | 100 |  | √ | ' ' | 评标项目 |
| 3 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 4 | fbidunit | 招标单位 | varchar | 100 |  | √ | ' ' | 招标单位 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fparticipatetime | 日期 | timestamp | 0 |  |  | null | 日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_exportprojectchg_fid |  | fid |
| 2 | pk_src_exportprojectchg |  | fentryid |

---

## 资料变更查询-使用范围表 t_src_exportchg_u

- **表名称：** 资料变更查询-使用范围表
- **表名：** t_src_exportchg_u

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
| 1 | idx_t_src_exportchg_u_uo |  | fuseorgid |
| 2 | pk_t_src_exportchg_u |  | fdataid,fuseorgid |

---

## 资料变更查询-多语言表 t_src_exportchg_l

- **表名称：** 资料变更查询-多语言表
- **表名：** t_src_exportchg_l

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
| 1 | pk_src_exportchg_l |  | fpkid |
| 2 | idx_src_exportchg_l_fid |  | fid,flocaleid |

---

## 证书分录-子表 t_src_expertaptitudechg

- **表名称：** 证书分录-子表
- **表名：** t_src_expertaptitudechg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 3 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 4 | faptitudename | 证书名称 | varchar | 255 |  | √ | ' ' | 证书名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | faptitudenote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fissuedate | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 8 | fexperttrainid | 最近专家培训 | int8 | 64 |  | √ | 0 | [专家培训F7 src_experttrainf7](../src_files/src_experttrainf7.md) |
| 9 | faptitudenumber | 证书编号 | varchar | 50 |  | √ | ' ' | 证书编号 |
| 10 | fissueorg | 签发机构 | varchar | 255 |  | √ | ' ' | 签发机构 |
| 11 | faptitudetypeid | 证书类型 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 12 | fcheckdate | 最近年检日期 | timestamp | 0 |  |  | null | 最近年检日期 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fgrade | 证书等级 | varchar | 20 |  | √ | ' ' | 证书等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_expertaptitudechg_fid |  | fid |
| 2 | pk_src_expertaptitudechg |  | fentryid |

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

## 工作经历分录-子表 t_src_exportworkchg

- **表名称：** 工作经历分录-子表
- **表名：** t_src_exportworkchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fduty | 职务 | varchar | 50 |  | √ | ' ' | 职务 |
| 3 | fdateto | 时间.结束 | timestamp | 0 |  |  | null | 时间.结束 |
| 4 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdatefrom | 时间.开始 | timestamp | 0 |  |  | null | 时间.开始 |
| 7 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fworkunit | 工作单位 | varchar | 100 |  | √ | ' ' | 工作单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_exportworkchg |  | fentryid |
| 2 | idx_src_exportworkchg_fid |  | fid |

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

---

## 供应商分录-子表 t_src_exportsupplierchg

- **表名称：** 供应商分录-子表
- **表名：** t_src_exportsupplierchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsuppliernote | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 6 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_exportsupplierchg |  | fentryid |
| 2 | idx_src_exportsupplierchg_fid |  | fid |
