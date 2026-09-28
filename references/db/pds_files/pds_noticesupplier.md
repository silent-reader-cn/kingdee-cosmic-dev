# 通知书-pds_noticesupplier

## 通知书-主表 t_pds_noticesup

- **表名称：** 通知书-主表
- **表名：** t_pds_noticesup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwinemailtplid | 邮件模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 3 | freplydate | 要求供应商回复时间 | timestamp | 0 |  |  | null | 要求供应商回复时间 |
| 4 | finvitetitle | 邀请函标题 | varchar | 350 |  | √ | ' ' | 邀请函标题 |
| 5 | fprewinemailtpl | 邮件模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 6 | fcultivateweixintpl | 企业微信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 7 | fpentitykey | fpentitykey | varchar | 50 |  | √ | ' ' |  |
| 8 | forigin | forigin | bpchar | 1 |  | √ | ' ' |  |
| 9 | fprewintitle | 预中标标题 | varchar | 350 |  | √ | ' ' | 预中标标题 |
| 10 | fbackuptitle | 备选标题 | varchar | 350 |  | √ | ' ' | 备选标题 |
| 11 | finvitesendtype | 发送方式 | varchar | 100 |  | √ | ' ' | 发送方式,枚举: portal :门户 email :邮件 message :短信 yzj :云之家 weixin :企业微信 |
| 12 | fwinweixintpl | 企业微信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 13 | fprewinsendtype | 发送方式 | varchar | 30 |  | √ | ' ' | 发送方式,枚举: portal :门户 email :邮件 message :短信 yzj :云之家 weixin :企业微信 |
| 14 | fprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 寻源项目 pds_projectf7 |
| 15 | fcultivatesoundtplid | 云之家模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 |
| 17 | finviteweixintpl | 企业微信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 18 | finviteemailtplid | 邮件模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 19 | fsrcbillid | 源单id | varchar | 50 |  | √ | ' ' | 源单id |
| 20 | ffaildoctplid | 门户模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 21 | fbackupsoundtplid | 云之家模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 22 | fbackupweixintpl | 企业微信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 23 | fcultivateemailtplid | 邮件模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 24 | finvitedoctplid | 门户模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 25 | fwinsoundtplid | 云之家模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 26 | fbackupemailtplid | 邮件模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 27 | fprewinweixintpl | 企业微信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 28 | fsrcbilltype | 源单标识 | varchar | 50 |  | √ | ' ' | 源单标识 |
| 29 | ffailmessagetplid | 短信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 30 | fwinmessagetplid | 短信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 31 | fwintitle | 中标标题 | varchar | 350 |  | √ | ' ' | 中标标题 |
| 32 | fbackupsendtype | 发送方式 | varchar | 100 |  | √ | ' ' | 发送方式,枚举: portal :门户 email :邮件 message :短信 yzj :云之家 weixin :企业微信 |
| 33 | ffailweixintpl | 企业微信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 34 | finvitemessagetplid | 短信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 35 | ffailsendtype | 发送方式 | varchar | 100 |  | √ | ' ' | 发送方式,枚举: portal :门户 email :邮件 message :短信 yzj :云之家 weixin :企业微信 |
| 36 | fcultivatedoctplid | 门户模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 37 | fcultivatemessagetplid | 短信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 38 | fprewinsoundtpl | 云之家模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 39 | fpublisherid | 发布人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fcultivatesendtypeid | 发送方式 | varchar | 100 |  | √ | ' ' | 发送方式,枚举: portal :门户 email :邮件 message :短信 yzj :云之家 weixin :企业微信 |
| 41 | fparentid | fparentid | varchar | 50 |  | √ | ' ' |  |
| 42 | ffailsoundtplid | 云之家模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 43 | fwindoctplid | 门户模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 44 | fbackupmessagetplid | 短信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 45 | fentitykey | fentitykey | varchar | 50 |  | √ | ' ' |  |
| 46 | fbackupdoctplid | 门户模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 47 | fcultivatetitle | 培养标题 | varchar | 350 |  | √ | ' ' | 培养标题 |
| 48 | fprewinmessagetpl | 短信模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 49 | fprewindoctpl | 门户模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 50 | ffailtitle | 未中标标题 | varchar | 350 |  | √ | ' ' | 未中标标题 |
| 51 | finvitesoundtpl | 云之家模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 52 | ffailemailtplid | 邮件模板 | int8 | 64 |  | √ | 0 | 函件模板 pds_doctpl |
| 53 | fwinsendtype | 发送方式 | varchar | 100 |  | √ | ' ' | 发送方式,枚举: portal :门户 email :邮件 message :短信 yzj :云之家 weixin :企业微信 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_noticesup_fpid |  | fprojectid |
| 2 | pk_pds_noticesup |  | fid |

---

## 函件信息-子表 t_pds_noticesup_letters

- **表名称：** 函件信息-子表
- **表名：** t_pds_noticesup_letters

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffstitle | 云之家标题 | varchar | 350 |  | √ | ' ' | 云之家标题 |
| 3 | femailparamjson_tag | 邮件参数_详情 | text | 0 |  |  | ' ' | 邮件参数_详情 |
| 4 | fsmsparamjson | 短信参数 | text | 0 |  |  | ' ' | 短信参数 |
| 5 | ffscontent | 云之家 | text | 0 |  |  | ' ' | 云之家 |
| 6 | femailcontent | 邮件 | text | 0 |  |  | ' ' | 邮件 |
| 7 | fportalparamjson_tag | 门户参数_详情 | text | 0 |  |  | ' ' | 门户参数_详情 |
| 8 | ffsparamjson | 云之家参数 | text | 0 |  |  | ' ' | 云之家参数 |
| 9 | fworknumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | faddressid | 主送人 | varchar | 500 |  | √ | ' ' | 主送人 |
| 12 | fportaltitle | 门户标题 | varchar | 350 |  | √ | ' ' | 门户标题 |
| 13 | fweixinparamjson | 企业微信参数 | text | 0 |  |  | ' ' | 企业微信参数 |
| 14 | fletterstype | 函件类型 | bpchar | 1 |  | √ | ' ' | 函件类型,枚举: 1 :中标 2 :备选 3 :未中标 4 :邀请函 5 :培养 6 :不推荐 9 :预中标 |
| 15 | fweixincontent | 企业微信 | text | 0 |  |  | ' ' | 企业微信 |
| 16 | fphonenumber | 手机号 | varchar | 500 |  | √ | ' ' | 手机号 |
| 17 | ffsparamjson_tag | 云之家参数_详情 | text | 0 |  |  | ' ' | 云之家参数_详情 |
| 18 | fsccid | 密送人 | varchar | 50 |  | √ | ' ' | 密送人 |
| 19 | fweixinparamjson_tag | 企业微信参数_详情 | text | 0 |  |  | null | 企业微信参数_详情 |
| 20 | fdoccontent | 门户 | text | 0 |  |  | ' ' | 门户 |
| 21 | fportalparamjson | 门户参数 | text | 0 |  |  | ' ' | 门户参数 |
| 22 | fletterssupplier | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 23 | fdoccontent_tag | 门户_详情 | text | 0 |  |  | ' ' | 门户_详情 |
| 24 | fccid | 抄送人 | varchar | 500 |  | √ | ' ' | 抄送人 |
| 25 | femailcontent_tag | 邮件_详情 | text | 0 |  |  | ' ' | 邮件_详情 |
| 26 | femailparamjson | 邮件参数 | text | 0 |  |  | ' ' | 邮件参数 |
| 27 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 28 | fweixincontent_tag | 企业微信_详情 | text | 0 |  |  | null | 企业微信_详情 |
| 29 | ffscontent_tag | 云之家_详情 | text | 0 |  |  | ' ' | 云之家_详情 |
| 30 | fweixintitle | 企业微信标题 | varchar | 350 |  | √ | ' ' | 企业微信标题 |
| 31 | fsmscontent | 短信 | text | 0 |  |  | ' ' | 短信 |
| 32 | fmessagetitle | 短信标题 | varchar | 350 |  | √ | ' ' | 短信标题 |
| 33 | femailtitle | 邮件标题 | varchar | 350 |  | √ | ' ' | 邮件标题 |
| 34 | fsmscontent_tag | 短信_详情 | text | 0 |  |  | ' ' | 短信_详情 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fsmsparamjson_tag | 短信参数_详情 | text | 0 |  |  | ' ' | 短信参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_noticesup_letters_flsu |  | fletterssupplier |
| 2 | idx_pds_noticesup_letters_fid |  | fid |
| 3 | pk_pds_noticesup_letters |  | fentryid |

---

## 供应商回复附件-附件表 t_pds_noticesup_sup_fj2

- **表名称：** 供应商回复附件-附件表
- **表名：** t_pds_noticesup_sup_fj2

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
| 1 | idx_pds_noticesup_sup_fj2_bid |  | fbasedataid |
| 2 | pk_pds_noticesup_sup_fj2 |  | fpkid |
| 3 | idx_pds_noticesup_sup_fj2_fid |  | fentryid |

---

## 限定供应商用户-多选基础资料表 t_src_supplierusers

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplierusers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supplierusers |  | fpkid |
| 2 | idx_src_supplierusers_eid |  | fentryid |
| 3 | idx_src_supplierusers_bid |  | fbasedataid |

---

## 附件-附件表 t_pds_noticesup_sup_fj

- **表名称：** 附件-附件表
- **表名：** t_pds_noticesup_sup_fj

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
| 1 | idx_pds_noticesup_sup_fj_bid |  | fbasedataid |
| 2 | pk_pds_noticesup_sup_fj |  | fpkid |
| 3 | idx_pds_noticesup_sup_fj_eid |  | fentryid |

---

## 内部抄送人员-多选基础资料表 t_pds_letterpeople

- **表名称：** 内部抄送人员-多选基础资料表
- **表名：** t_pds_letterpeople

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_letterpeople_bid |  | fbasedataid |
| 2 | pk_pds_letterpeople |  | fpkid |
| 3 | idx_pds_letterpeople_fid |  | fid |

---

## 供应商信息-子表 t_pds_noticesup_sup

- **表名称：** 供应商信息-子表
- **表名：** t_pds_noticesup_sup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faddress | 联系地址 | varchar | 50 |  | √ | ' ' | 联系地址 |
| 3 | freplydate | 要求回复时间 | timestamp | 0 |  |  | null | 要求回复时间 |
| 4 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fentrystatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: A :待发布 B :已提交 C :已发布 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 8 | fsupletterstype | 函件类型 | bpchar | 1 |  | √ | ' ' | 函件类型,枚举: 1 :中标 2 :备选 3 :未中标 4 :邀请函 5 :培养 6 :不推荐 9 :预中标 7 :资审不合格 0 :流标 |
| 9 | ffsstatus | 云之家发送状态 | bpchar | 1 |  | √ | ' ' | 云之家发送状态,枚举: A :待发送 B :已发送 C :发送失败 |
| 10 | femailstatus | 邮件发送状态 | varchar | 30 |  | √ | ' ' | 邮件发送状态,枚举: A :待发送 B :已发送 C :发送失败 |
| 11 | fentryprojectid | 招标项目 | int8 | 64 |  | √ | 0 | 寻源项目 pds_projectf7 |
| 12 | fpurpublisher | 发布人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 14 | femail | 电子邮件 | varchar | 50 |  | √ | ' ' | 电子邮件 |
| 15 | frefusenote | 拒绝原因 | varchar | 255 |  | √ | ' ' | 拒绝原因 |
| 16 | fissend | 是否发送 | bpchar | 1 |  | √ | '0' | 是否发送 |
| 17 | fuserid | 供应商用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 19 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 20 | fduty | 职位 | varchar | 50 |  | √ | ' ' | 职位 |
| 21 | fcfmstatus | 供应商确认 | bpchar | 1 |  | √ | ' ' | 供应商确认,枚举: A :待确认 B :已确认 C :已拒绝 D :未回复 E :已定标 |
| 22 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 23 | fmainsend | 是否主送 | bpchar | 1 |  | √ | '1' | 是否主送 |
| 24 | fweixinstatus | 微信发送状态 | bpchar | 1 |  | √ | 'A' | 微信发送状态,枚举: A :待发送 B :已发送 C :发送失败 |
| 25 | fsenddate | 函件发送时间 | timestamp | 0 |  |  | null | 函件发送时间 |
| 26 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 27 | fsystemtset | 是否系统自带 | bpchar | 1 |  | √ | ' ' | 是否系统自带 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fsmsstatus | 短信发送状态 | bpchar | 1 |  | √ | ' ' | 短信发送状态,枚举: A :待发送 B :已发送 C :发送失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_noticesup_sup_fid |  | fid |
| 2 | idx_pds_noticesup_sup_feid |  | fentryprojectid |
| 3 | idx_pds_noticesup_sup_fsup |  | fsupplierid |
| 4 | idx_pds_noticesup_sup_ftpye |  | fsupletterstype |
| 5 | pk_pds_noticesup_sup |  | fentryid |
