# 招标公告组件-src_sourcenotice

## 招标公告组件-多语言表 t_pur_notice_l

- **表名称：** 招标公告组件-多语言表
- **表名：** t_pur_notice_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftitle | 主题 | varchar | 255 |  | √ | ' ' | 主题 |
| 3 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_notice_l_fid |  | fid,flocaleid |
| 2 | t_pur_notice_l_pkey |  | fpkid |

---

## 招标公告组件-分表 t_pur_notice_a

- **表名称：** 招标公告组件-分表
- **表名：** t_pur_notice_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsrcbillno | 源单单号 | varchar | 50 |  | √ | ' ' | 源单单号 |
| 5 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 8 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 11 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | ftitle | ftitle | varchar | 255 |  | √ | ' ' |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_notice_a_pkey |  | fid |
| 2 | idx_pur_notice_a_fcreatetime |  | fcreatetime |

---

## 招标公告组件-主表 t_pur_notice

- **表名称：** 招标公告组件-主表
- **表名：** t_pur_notice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fbillstatus | 发布状态 | bpchar | 1 |  | √ | ' ' | 发布状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | forgid | 发布组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fimportant | 重要性 | bpchar | 1 |  | √ | ' ' | 重要性,枚举: 1 :非常重要 2 :重要 3 :一般 |
| 6 | fbilldate | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 7 | fsupscope | 公告范围 | bpchar | 1 |  | √ | ' ' | 公告范围,枚举: 1 :所有供应商 2 :指定供应商 3 :内部公告 |
| 8 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 9 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 10 | fistop | 置顶 | bpchar | 1 |  | √ | '0' | 置顶 |
| 11 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 12 | fduedate | 到期时间 | timestamp | 0 |  |  | null | 到期时间 |
| 13 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 14 | ftitle | ftitle | varchar | 255 |  | √ | ' ' |  |
| 15 | fnoticetplid | 公告模板 | int8 | 64 |  | √ | 0 | [模板配置 pds_noticetpl](../pds_files/pds_noticetpl.md) |
| 16 | fbiztype | 公告类型 | bpchar | 1 |  | √ | ' ' | 公告类型,枚举: 1 :询价公告 3 :竞价公告 4 :比价公告 6 :招募公告 7 :行业动态 8 :系统公告 A :询价结果公告 B :竞价结果公告 C :招标公告 D :流标公告 5 :中标公告 |
| 17 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 18 | fsourcetype | fsourcetype | int8 | 64 |  | √ | 0 |  |
| 19 | fcontent | 内容 | text | 0 |  |  | null | 内容 |
| 20 | fbillno | 公告编号 | varchar | 80 |  | √ | ' ' | 公告编号 |
| 21 | furgent | 紧急度 | bpchar | 1 |  | √ | ' ' | 紧急度,枚举: 1 :非常紧急 2 :紧急 3 :一般 |
| 22 | fisallowoperate | fisallowoperate | bpchar | 1 |  | √ | '1' |  |
| 23 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_notice_fbilldate |  | fbilldate |
| 2 | idx_pur_notice_fbillno |  | fbillno |
| 3 | t_pur_notice_pkey |  | fid |

---

## 供应商分录-子表 t_pur_noticesupplier

- **表名称：** 供应商分录-子表
- **表名：** t_pur_noticesupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fphone | 手机 | varchar | 50 |  | √ | ' ' | 手机 |
| 3 | fregsupplierid | 注册供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 4 | fcontacter | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 5 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | freplystatus | 状态 | bpchar | 1 |  |  | ' ' | 状态,枚举: 1 : 2 :未读 3 :已读 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_noticesupplier_pkey |  | fentryid |
| 2 | idx_pur_noticesup_fid_fseq |  | fid,fseq |
| 3 | idx_pur_noticesup_fsupplierid |  | fsupplierid |
