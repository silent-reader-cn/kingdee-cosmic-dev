# 经销协议-occbo_distribtcontract

## 经销协议-分表 t_occbo_dtbcontract_f

- **表名称：** 经销协议-分表
- **表名：** t_occbo_dtbcontract_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispayrate | 按比例(%) | bpchar | 1 |  | √ | '1' | 按比例(%) |
| 3 | ftotalamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 4 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 5 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 6 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 7 | fisentrysumamt | 明细金额汇总 | bpchar | 1 |  | √ | '0' | 明细金额汇总 |
| 8 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 9 | fexchangetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | ftotaltaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 14 | ftotalallamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_dtbcontract_f |  | fid |
| 2 | idx_occbo_dtbcontract_f |  | fsettlecurrencyid |

---

## 经销协议-多语言表 t_occbo_dtbcontract_l

- **表名称：** 经销协议-多语言表
- **表名：** t_occbo_dtbcontract_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fbillname | 协议名称 | varchar | 100 |  | √ | ' ' | 协议名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_dtbcontract_l |  | fpkid |
| 2 | idx_occbo_dtbcontract_l |  | fid,flocaleid |

---

## 经销协议-分表 t_occbo_dtbcontract_o

- **表名称：** 经销协议-分表
- **表名：** t_occbo_dtbcontract_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fterminatorid | 终止人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fterminatedate | 终止日期 | timestamp | 0 |  |  | null | 终止日期 |
| 4 | fsigndate | 签章日期 | timestamp | 0 |  |  | null | 签章日期 |
| 5 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 6 | freviewdate | 评审日期 | timestamp | 0 |  |  | null | 评审日期 |
| 7 | fdocumentid | 电签合同ID | varchar | 50 |  | √ | ' ' | 电签合同ID |
| 8 | fsignerid | 签章人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcancelerid | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | ffreezerid | 冻结人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | femail2nd | 乙方邮箱 | varchar | 100 |  | √ | ' ' | 乙方邮箱 |
| 12 | ffilingerid | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fcanceldate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 14 | fchannelid | 协议渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 15 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ffilingdate | 归档日期 | timestamp | 0 |  |  | null | 归档日期 |
| 17 | femail1st | 甲方邮箱 | varchar | 100 |  | √ | ' ' | 甲方邮箱 |
| 18 | ffreezedate | 冻结日期 | timestamp | 0 |  |  | null | 冻结日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_dtbcontract_o |  | fid |
| 2 | idx_occbo_dtbcontract_o |  | fsignerid |

---

## 经销协议-分表 t_occbo_dtbcontract_s

- **表名称：** 经销协议-分表
- **表名：** t_occbo_dtbcontract_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontactperson1st | 甲方联系人 | varchar | 60 |  | √ | ' ' | 甲方联系人 |
| 3 | fgoalsyearid | 目标年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 4 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdepartmentid | 销售部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fparty2nd | 乙方 | varchar | 255 |  | √ | ' ' | 乙方 |
| 7 | fpartcid | 第三方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 8 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fparty1st | 甲方 | varchar | 255 |  | √ | ' ' | 甲方 |
| 10 | fgoalstype | 目标类型 | bpchar | 1 |  | √ | 'A' | 目标类型,枚举: A :年度目标 B :月度目标 |
| 11 | fphone2nd | 乙方电话 | varchar | 50 |  | √ | ' ' | 乙方电话 |
| 12 | fphone1st | 甲方电话 | varchar | 50 |  | √ | ' ' | 甲方电话 |
| 13 | fgoalsmap | 年月对应分录关系 | varchar | 2000 |  | √ | ' ' | 年月对应分录关系 |
| 14 | fcontactperson2nd | 乙方联系人 | varchar | 60 |  | √ | ' ' | 乙方联系人 |
| 15 | fkpiid | 目标KPI | int8 | 64 |  | √ | 0 | [KPI occbo_kpi_base](../occbo_files/occbo_kpi_base.md) |
| 16 | fcustomerid | 协议客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_dtbcontract_s |  | fid |
| 2 | idx_occbo_dtbcontract_s |  | fparty1st,fparty2nd |

---

## 经销协议-主表 t_occbo_dtbcontract

- **表名称：** 经销协议-主表
- **表名：** t_occbo_dtbcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvaliderid | 生效人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fiselecsignature | 是否电子签章 | bpchar | 1 |  | √ | '0' | 是否电子签章 |
| 4 | forgid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcancelstatus | 作废状态 | bpchar | 1 |  | √ | 'A' | 作废状态,枚举: A :未作废 B :已作废 |
| 6 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | 'B' | 确认状态,枚举: A :未确认 B :已确认 |
| 7 | fcontpartiesid | 协议主体 | int8 | 64 |  | √ | 0 | [合同主体 conm_contparties](../conm_files/conm_contparties.md) |
| 8 | fbiztime | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'A' | 变更状态,枚举: A :正常 B :变更中 C :已变更 |
| 11 | freviewstatus | 评审状态 | bpchar | 1 |  | √ | 'A' | 评审状态,枚举: A :未评审 B :评审中 C :通过 D :不通过 E :未启用 |
| 12 | fterminatestatus | 终止状态 | bpchar | 1 |  | √ | 'A' | 终止状态,枚举: A :未终止 B :已终止 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ffilingstatus | 归档状态 | bpchar | 1 |  | √ | 'A' | 归档状态,枚举: A :未归档 B :已归档 C :未启用 |
| 15 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 16 | fsignstatus | 签章状态 | bpchar | 1 |  | √ | 'A' | 签章状态,枚举: A :未签章 B :签章完成 C :未启用 D :乙方已签 E :甲方已签 F :上传完成 |
| 17 | fcategoryid | 协议种类 | int8 | 64 |  | √ | 0 | [合同种类 conm_category](../conm_files/conm_category.md) |
| 18 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 19 | fbillno | 协议编号 | varchar | 80 |  | √ | ' ' | 协议编号 |
| 20 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 21 | fconfirmdate | 确认日期 | timestamp | 0 |  |  | null | 确认日期 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fbizmode | 业务模式 | bpchar | 1 |  | √ | 'C' | 业务模式,枚举: A :统谈统签 B :统谈分签 C :分谈分签 |
| 24 | fconmprop | 协议属性 | bpchar | 1 |  | √ | 'B' | 协议属性,枚举: A :框架协议 B :合同 |
| 25 | ftemplateid | 协议模板 | int8 | 64 |  | √ | 0 | [合同模板 conm_template](../conm_files/conm_template.md) |
| 26 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 32 | fbiztimeend | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 33 | fbillname | 协议名称 | varchar | 80 |  | √ | ' ' | 协议名称 |
| 34 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 35 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'A' | 关闭状态,枚举: A :未关闭 B :已关闭 |
| 36 | ffreezestatus | 冻结状态 | bpchar | 1 |  | √ | 'A' | 冻结状态,枚举: A :未冻结 B :已冻结 |
| 37 | fpartbid | 协议乙方 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 38 | ftypeid | 协议类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 39 | fsubversion | 子版本号 | varchar | 30 |  | √ | ' ' | 子版本号 |
| 40 | fvalidstatus | 生效状态 | bpchar | 1 |  | √ | 'A' | 生效状态,枚举: A :未生效 B :已生效 C :已失效 |
| 41 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | ftemplateentryid | 模板版本 | int8 | 64 |  | √ | 0 | [模板版本 conm_tempfileentry](../conm_files/conm_tempfileentry.md) |
| 43 | fchangerid | 变更人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fpartaid | 协议甲方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fbiztimebegin | 起始日期 | timestamp | 0 |  |  | null | 起始日期 |
| 46 | fisonlist | 基于清单 | bpchar | 1 |  | √ | '0' | 基于清单 |
| 47 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_dtbcontract |  | fbillno |
| 2 | pk_occbo_dtbcontract |  | fid |

---

## 目标月度-多选基础资料表 t_occbo_dtbcontra_rp

- **表名称：** 目标月度-多选基础资料表
- **表名：** t_occbo_dtbcontra_rp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_entity](../ocdbd_files/ocdbd_assess_entity.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_dtbcontra_rp |  | fpkid |
| 2 | idx_occbo_dtbcontra_rp |  | fid,fbasedataid |

---

## 合同条款-子表 t_occbo_dtbcontra_tentry

- **表名称：** 合同条款-子表
- **表名：** t_occbo_dtbcontra_tentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftermgroupid | 分组 | int8 | 64 |  | √ | 0 | [合同条款分组 conm_termgroup](../conm_files/conm_termgroup.md) |
| 3 | ftermentrychangetype | 变更方式 | bpchar | 1 |  | √ | 'B' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 4 | ftermcontent | 条款内容 | varchar | 2000 |  | √ | ' ' | 条款内容 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftermid | 协议条款 | int8 | 64 |  | √ | 0 | [合同条款 conm_term](../conm_files/conm_term.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_dtbcontra_tentry |  | fentryid |
| 2 | idx_occbo_dtbcontra_tentry |  | fid |

---

## 其他方-多选基础资料表 t_occbo_contpartother

- **表名称：** 其他方-多选基础资料表
- **表名：** t_occbo_contpartother

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_contpartother |  | fpkid |
| 2 | idx_occbo_contpartother |  | fid,fbasedataid |

---

## 商品经营范围-子表 t_occbo_dtbcontra_ientry

- **表名称：** 商品经营范围-子表
- **表名：** t_occbo_dtbcontra_ientry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbrandid | 商品品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 3 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_dtbcontra_ientry |  | fentryid |
| 2 | idx_occbo_dtbcontra_ientry |  | fid |

---

## 目标明细-子表 t_occbo_dtbcontra_gentry

- **表名称：** 目标明细-子表
- **表名：** t_occbo_dtbcontra_gentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoalsnum12 | 目标值12 | numeric | 23 | 10 | √ | 0 | 目标值12 |
| 3 | fgoalsnum11 | 目标值11 | numeric | 23 | 10 | √ | 0 | 目标值11 |
| 4 | fgoalsnum14 | 目标值14 | numeric | 23 | 10 | √ | 0 | 目标值14 |
| 5 | fgoalsnum13 | 目标值13 | numeric | 23 | 10 | √ | 0 | 目标值13 |
| 6 | fentrytotalnum | 合计 | numeric | 23 | 10 | √ | 0 | 合计 |
| 7 | fgoalsnum10 | 目标值10 | numeric | 23 | 10 | √ | 0 | 目标值10 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fgoalsnum8 | 目标值8 | numeric | 23 | 10 | √ | 0 | 目标值8 |
| 10 | fgoalsnum9 | 目标值9 | numeric | 23 | 10 | √ | 0 | 目标值9 |
| 11 | fgoalsnum6 | 目标值6 | numeric | 23 | 10 | √ | 0 | 目标值6 |
| 12 | fgoalsnum7 | 目标值7 | numeric | 23 | 10 | √ | 0 | 目标值7 |
| 13 | fgoalsnum4 | 目标值4 | numeric | 23 | 10 | √ | 0 | 目标值4 |
| 14 | fgoalsnum5 | 目标值5 | numeric | 23 | 10 | √ | 0 | 目标值5 |
| 15 | fgoalsnum2 | 目标值2 | numeric | 23 | 10 | √ | 0 | 目标值2 |
| 16 | fgoalsnum3 | 目标值3 | numeric | 23 | 10 | √ | 0 | 目标值3 |
| 17 | fgoalsnum1 | 目标值1 | numeric | 23 | 10 | √ | 0 | 目标值1 |
| 18 | fgoalsnum16 | 目标值16 | numeric | 23 | 10 | √ | 0 | 目标值16 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 21 | fgoalsnum15 | 目标值15 | numeric | 23 | 10 | √ | 0 | 目标值15 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_dtbcontra_gentry |  | fid |
| 2 | pk_occbo_dtbcontra_gentry |  | fentryid |

---

## 付款计划-子表 t_occbo_dtbcontra_pentry

- **表名称：** 付款计划-子表
- **表名：** t_occbo_dtbcontra_pentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjoinpayamount | 关联付款金额 | numeric | 23 | 10 | √ | 0 | 关联付款金额 |
| 3 | fintervaltime | 间隔时间 | int4 | 32 |  | √ | 0 | 间隔时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpayamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 6 | fpayentrychangetype | 变更方式 | bpchar | 1 |  | √ | 'B' | 变更方式,枚举: A :新增 B :修改 C :删除 |
| 7 | fpayrate | 付款比例(%) | numeric | 23 | 10 | √ | 0 | 付款比例(%) |
| 8 | fisprepay | 是否预付 | bpchar | 1 |  | √ | '0' | 是否预付 |
| 9 | ftimeunit | 时间单位 | bpchar | 1 |  | √ | 'A' | 时间单位,枚举: A :工作日 B :自然日 C :月 |
| 10 | fpaidamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fpaynameid | 款项名称 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 13 | fpaydate | 计划付款日期 | timestamp | 0 |  |  | null | 计划付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_dtbcontra_pentry |  | fid |
| 2 | pk_occbo_dtbcontra_pentry |  | fentryid |
