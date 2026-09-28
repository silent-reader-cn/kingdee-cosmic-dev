# 供应商信息-srm_supplierinfo

## 附件模板分录-子表 t_pbd_supattachentry

- **表名称：** 附件模板分录-子表
- **表名：** t_pbd_supattachentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flongterm | 长期有效 | bpchar | 1 |  | √ | '0' | 长期有效 |
| 3 | fupdatetime | 更新日期 | timestamp | 0 |  |  | null | 更新日期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fmustsupply | fmustsupply | bpchar | 1 |  | √ | '0' |  |
| 6 | fattdateto | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fqualificationtypeid | 资质类型 | int8 | 64 |  | √ | 0 | [资质类型维护 bd_qualification_type](../basedata_files/bd_qualification_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_supattachentry_fid |  | fid,fseq |
| 2 | pk_pbd_supattachentry |  | fentryid |

---

## 附件-附件表 t_pur_mgatt

- **表名称：** 附件-附件表
- **表名：** t_pur_mgatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_mgatt |  | fpkid |
| 2 | idx_t_pur_mgatt |  | fbasedataid |

---

## 附件-附件表 t_pur_regsupaptitude_fj

- **表名称：** 附件-附件表
- **表名：** t_pur_regsupaptitude_fj

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
| 1 | t_pur_regsupaptitude_fj_pkey |  | fpkid |
| 2 | idx_pur_regsupapt_fj_fbdid |  | fbasedataid |

---

## 供货范围-子表 t_pur_regsupplyscope

- **表名称：** 供货范围-子表
- **表名：** t_pur_regsupplyscope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flongnumber | 长编码 | varchar | 1500 |  | √ | ' ' | 长编码 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_suppliscope_fid_fseq |  | fid,fseq |
| 2 | t_pur_regsupplyscope_pkey |  | fentryid |

---

## 客户信息分录-子表 t_pur_regsucustomer

- **表名称：** 客户信息分录-子表
- **表名：** t_pur_regsucustomer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcooperatscope | 合作范围 | varchar | 255 |  | √ | ' ' | 合作范围 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftradevolume | 近3年交易额（万元） | numeric | 19 | 6 | √ | 0.000000 | 近3年交易额（万元） |
| 5 | ftradecur | 交易币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | ftopcustomer | TOP3客户名称 | varchar | 255 |  | √ | ' ' | TOP3客户名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_regsucustomer |  | fseq,fid |
| 2 | pk_t_pur_regsucustomer |  | fentryid |

---

## 获奖分录-子表 t_pur_regsupaward

- **表名称：** 获奖分录-子表
- **表名：** t_pur_regsupaward

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fawardname | 奖项名称 | varchar | 100 |  | √ | ' ' | 奖项名称 |
| 3 | fawarddate | 获奖时间 | timestamp | 0 |  |  | null | 获奖时间 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fawardorg | 颁奖单位 | varchar | 100 |  | √ | ' ' | 颁奖单位 |
| 7 | fawardrank | 获奖名次 | varchar | 20 |  | √ | ' ' | 获奖名次 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupaward_pkey |  | fentryid |
| 2 | idx_pur_regsupaward_fid_fseq |  | fid,fseq |

---

## 资质分录-子表 t_pur_regsupaptitude

- **表名称：** 资质分录-子表
- **表名：** t_pur_regsupaptitude

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资质名称 | varchar | 255 |  | √ | ' ' | 资质名称 |
| 3 | faptitudetypecfgid | 资质类型配置 | int8 | 64 |  | √ | 0 | [供应商资质要求配置 bd_qualification_config](../basedata_files/bd_qualification_config.md) |
| 4 | fdateto | 有效日期至 | timestamp | 0 |  |  | null | 有效日期至 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fissuedate | 签发日期 | timestamp | 0 |  |  | null | 签发日期 |
| 8 | fcompanytypeid | 供货类型 | int8 | 64 |  | √ | 0 | [供货类型 bd_company_type](../basedata_files/bd_company_type.md) |
| 9 | frequired | 必须提供 | bpchar | 1 |  | √ | '0' | 必须提供 |
| 10 | ftype | 资质类型 | bpchar | 1 |  | √ | ' ' | 资质类型,枚举: 1 :三/五证合一 2 :营业执照 3 :税务登记证 4 :组织机构代码证 5 :社会保险登记证 6 :一般纳税人证明材料 7 :统计登记证 8 :其他证照 |
| 11 | fissueorg | 签发机构 | varchar | 255 |  | √ | ' ' | 签发机构 |
| 12 | fnumber | 资质编号 | varchar | 50 |  | √ | ' ' | 资质编号 |
| 13 | fcheckdate | 最近年检日期 | timestamp | 0 |  |  | null | 最近年检日期 |
| 14 | faptitudetypeid | 资质类型 | int8 | 64 |  | √ | 0 | [资质类型维护 bd_qualification_type](../basedata_files/bd_qualification_type.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fgrade | 资质等级 | varchar | 20 |  | √ | ' ' | 资质等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_regsupaptitude_fid |  | fid,fseq |
| 2 | t_pur_regsupaptitude_pkey |  | fentryid |

---

## 省-多选基础资料表 t_pur_regsupplier_prov

- **表名称：** 省-多选基础资料表
- **表名：** t_pur_regsupplier_prov

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupplier_prov_pkey |  | fpkid |
| 2 | t_pur_regsupplier_prov_fid |  | fentryid,fbasedataid |

---

## 核心雇员-子表 t_pur_regcorestaff

- **表名称：** 核心雇员-子表
- **表名：** t_pur_regcorestaff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcorestaffname | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcoresnationality | 国籍 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fcorestaffpost | 职位 | varchar | 100 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_regcorestaff |  | fid,fseq |
| 2 | pk_t_pur_regcorestaff |  | fentryid |

---

## 供应商信息-分表 t_pur_regsupplier_a

- **表名称：** 供应商信息-分表
- **表名：** t_pur_regsupplier_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fislistedco | 是否上市 | bpchar | 1 |  | √ | ' ' | 是否上市 |
| 3 | faddress | faddress | varchar | 255 |  | √ | ' ' |  |
| 4 | fregaddress | fregaddress | varchar | 255 |  | √ | ' ' |  |
| 5 | fexecuteresult | fexecuteresult | bpchar | 1 |  | √ | ' ' |  |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fidcard | 法人身份证号码 | varchar | 20 |  | √ | ' ' | 法人身份证号码 |
| 8 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fpushsupplier | fpushsupplier | int8 | 64 |  | √ | 0 |  |
| 13 | fadvantage | 产品与服务优势 | varchar | 2000 |  | √ | ' ' | 产品与服务优势 |
| 14 | fstaffnum | 企业员工数 | int8 | 64 |  | √ | 0 | 企业员工数 |
| 15 | frecruitno | 招募单号 | varchar | 80 |  | √ | ' ' | 招募单号 |
| 16 | fbizscope | 经营范围 | varchar | 2000 |  | √ | ' ' | 经营范围 |
| 17 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | flisteddate | 上市日期 | timestamp | 0 |  |  | null | 上市日期 |
| 21 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fauditopinion | 审批意见 | varchar | 255 |  | √ | ' ' | 审批意见 |
| 26 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | '5' |  |
| 28 | fcreditrate | 银行信用级别 | bpchar | 1 |  | √ | ' ' | 银行信用级别,枚举: 1 :AAA |
| 29 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 30 | flistedaddr | 上市地点 | varchar | 100 |  | √ | ' ' | 上市地点 |
| 31 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 32 | fartificialperson | fartificialperson | varchar | 60 |  | √ | ' ' |  |
| 33 | flinkman | flinkman | varchar | 50 |  | √ | ' ' |  |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fsummary | 公司简介 | varchar | 2000 |  | √ | ' ' | 公司简介 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupplier_a_pkey |  | fid |
| 2 | idx_pur_regsupplier_ftime |  | fcreatetime |

---

## 供应商信息-分表 t_pur_regsupplier_c

- **表名称：** 供应商信息-分表
- **表名：** t_pur_regsupplier_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flastyear | 去年 | varchar | 255 |  | √ | ' ' | 去年 |
| 3 | ftechniciannum | 技术人员数 | numeric | 19 |  | √ | 0 | 技术人员数 |
| 4 | ftyear | 今年至今 | varchar | 255 |  | √ | ' ' | 今年至今 |
| 5 | fmanagementstaff | 管理人员数 | numeric | 19 |  | √ | 0 | 管理人员数 |
| 6 | ftaxregistredads | 税务注册地址 | varchar | 255 |  | √ | ' ' | 税务注册地址 |
| 7 | fenterprisetype | 企业类型 | bpchar | 1 |  | √ | ' ' | 企业类型,枚举: A :有限责任公司 B :股份有限公司 C :私营 D :合伙 E :个体 F :其它 |
| 8 | fcertifiapplyid | 供应商认证申请编号 | int8 | 64 |  | √ | 0 | [供应商认证申请编号 pbd_certificationapplyno](../pbd_files/pbd_certificationapplyno.md) |
| 9 | fissuerfiid | 发放RFI | varchar | 80 |  | √ | ' ' | 发放RFI |
| 10 | fmanagecur | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fstandcapacity | 遵守标准 | bpchar | 1 |  | √ | ' ' | 遵守标准,枚举: A :国际标准 B :国家标准 C :行业标准 D :企业标准 |
| 12 | fqualitystaffnum | 质量人员数 | numeric | 19 |  | √ | 0 | 质量人员数 |
| 13 | fdunsnumber | 邓白氏编码 | varchar | 255 |  | √ | ' ' | 邓白氏编码 |
| 14 | fbeforeyear | 前年 | varchar | 255 |  | √ | ' ' | 前年 |
| 15 | fdesigncapacity | 设计能力 | bpchar | 1 |  | √ | ' ' | 设计能力,枚举: A :自主设计研发 B :来料加工 C :贸易/代理 |
| 16 | fsupnameen | 供应商英文名称 | varchar | 255 |  | √ | ' ' | 供应商英文名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_regsupplier_c |  | fissuerfiid |
| 2 | idxcer_t_pur_regsupplier_c |  | fcertifiapplyid |
| 3 | pk_t_pur_regsupplier_c |  | fid |

---

## 供应商信息-使用范围表 t_pur_regsupplier_u

- **表名称：** 供应商信息-使用范围表
- **表名：** t_pur_regsupplier_u

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
| 1 | t_pur_regsupplier_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_pur_regsupplier_u_uo |  | fuseorgid |

---

## 供应商信息-使用范围位图表 t_pur_regsupplier_m

- **表名称：** 供应商信息-使用范围位图表
- **表名：** t_pur_regsupplier_m

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
| 1 | pk_t_pur_regsupplier_m |  | forgid |

---

## 供应商信息-多语言表 t_pur_regsupplier_l

- **表名称：** 供应商信息-多语言表
- **表名：** t_pur_regsupplier_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | faddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 5 | fregaddress | 注册地址 | varchar | 255 |  | √ | ' ' | 注册地址 |
| 6 | fsimplename | 简称 | varchar | 255 |  | √ | ' ' | 简称 |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | flinkman | 用户姓名 | varchar | 255 |  | √ | ' ' | 用户姓名 |
| 9 | fartificialperson | 法人代表 | varchar | 60 |  | √ | ' ' | 法人代表 |
| 10 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_regsupplier_l_fid |  | fid,flocaleid |
| 2 | t_pur_regsupplier_l_pkey |  | fpkid |
| 3 | idx_pur_regsupplier_fname |  | flocaleid,fname |

---

## 产品分录-子表 t_pur_regsupgoods

- **表名称：** 产品分录-子表
- **表名：** t_pur_regsupgoods

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 产品名称 | varchar | 100 |  | √ | ' ' | 产品名称 |
| 3 | fmodel | 品牌/规格 | varchar | 100 |  | √ | ' ' | 品牌/规格 |
| 4 | fmonthlycapacity | 月产能 | varchar | 100 |  | √ | ' ' | 月产能 |
| 5 | fyearcapacity | 年产能 | varchar | 100 |  | √ | ' ' | 年产能 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnumber | 产品编码 | varchar | 30 |  | √ | ' ' | 产品编码 |
| 9 | fdescription | 详细描述 | varchar | 255 |  | √ | ' ' | 详细描述 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_regsupgoods_fid |  | fid |
| 2 | t_pur_regsupgoods_pkey |  | fentryid |

---

## 银行分录-子表 t_pur_regsupbank

- **表名称：** 银行分录-子表
- **表名：** t_pur_regsupbank

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | faccounttype | 账户类型 | bpchar | 1 |  | √ | ' ' | 账户类型,枚举: 1 :基本账户 2 :请款账户 |
| 4 | faccountname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | faccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 8 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fisdefault | 默认 | bpchar | 1 |  | √ | ' ' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_regsupbank_fid_fseq |  | fid,fseq |
| 2 | t_pur_regsupbank_pkey |  | fentryid |

---

## 供应商信息-主表 t_pur_regsupplier

- **表名称：** 供应商信息-主表
- **表名：** t_pur_regsupplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 供应商分类 | int8 | 64 |  | √ | 0 | [供应商分类 bd_suppliergroup](../basedata_files/bd_suppliergroup.md) |
| 3 | faddress | 联系地址 | varchar | 255 |  | √ | ' ' | 联系地址 |
| 4 | forgfield | forgfield | int8 | 64 |  |  | null |  |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 6 | forgid | 审批组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 9 | fareacode | 行政区划 | varchar | 100 |  | √ | ' ' | 行政区划 |
| 10 | fphone | 手机(账号) | varchar | 50 |  | √ | ' ' | 手机(账号) |
| 11 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 12 | femail | 公司邮箱 | varchar | 50 |  | √ | ' ' | 公司邮箱 |
| 13 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 14 | ftaxcode | 税码 | bpchar | 1 |  | √ | ' ' | 税码,枚举: 1 :VAT0 2 :VAT3 3 :VAT6 4 :VAT11 5 :VAT13 6 :VAT17 |
| 15 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 16 | ftelephone | 公司电话 | varchar | 50 |  | √ | ' ' | 公司电话 |
| 17 | fisquitregister | fisquitregister | bpchar | 1 |  | √ | '0' |  |
| 18 | finvoicetype | 出具发票类型（已废弃） | bpchar | 1 |  | √ | ' ' | 出具发票类型（已废弃）,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 6 :电子普票&专票 7 :纸质普票&专票 |
| 19 | fcomplaintel | 投诉电话 | varchar | 50 |  | √ | ' ' | 投诉电话 |
| 20 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fbizregisterno | 工商注册号 | varchar | 60 |  | √ | ' ' | 工商注册号 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fartificialperson | 法人代表 | varchar | 60 |  | √ | ' ' | 法人代表 |
| 24 | flinkman | 用户姓名 | varchar | 255 |  | √ | ' ' | 用户姓名 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 26 | fcentralpurtype | 集采类型 | bpchar | 1 |  | √ | ' ' | 集采类型,枚举: 1 :集采 2 :自由 9 :集采&自由 |
| 27 | fareacodeid | fareacodeid | int8 | 64 |  | √ | 0 |  |
| 28 | fregaddress | 注册地址 | varchar | 255 |  | √ | ' ' | 注册地址 |
| 29 | fsocietycreditcode | 统一社会信用代码 | varchar | 60 |  | √ | ' ' | 统一社会信用代码 |
| 30 | forgcode | 组织机构代码 | varchar | 60 |  | √ | ' ' | 组织机构代码 |
| 31 | ftaxkind | 税种 | bpchar | 1 |  | √ | ' ' | 税种,枚举: 1 :增值税 2 :非增值税 |
| 32 | fsupplierstatus | 供应商状态 | int8 | 64 |  | √ | 0 | [供应商状态 bd_supplierstatus](../basedata_files/bd_supplierstatus.md) |
| 33 | fnewemail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 34 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :填写资料 B :提交审批 C :注册通过 D :注册驳回 E :资审通过 F :资审驳回 G :现场通过 H :现场驳回 I :样品通过 J :样品驳回 K :物料通过 L :物料驳回 Z :正式供应商 M :生效驳回 |
| 35 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | fregtype | 注册类型 | bpchar | 1 |  | √ | ' ' | 注册类型,枚举: 0 :邀约注册 1 :公开注册 |
| 37 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :注册审批 |
| 38 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 39 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 40 | fpost | 邮政编码 | varchar | 10 |  | √ | ' ' | 邮政编码 |
| 41 | ffax | 公司传真 | varchar | 50 |  | √ | ' ' | 公司传真 |
| 42 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 43 | fregsuptplid | fregsuptplid | int8 | 64 |  | √ | 0 |  |
| 44 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 45 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 47 | fcurrid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 48 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 49 | ftaxclass | 纳税人类型 | bpchar | 1 |  | √ | ' ' | 纳税人类型,枚举: 1 :一般纳税人 2 :小规模纳税人 3 :非增值税纳税人 |
| 50 | ftarsupplierstatus | ftarsupplierstatus | bpchar | 1 |  | √ | 'A' |  |
| 51 | fcountryid | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 52 | fauditstatus1 | 资质审查状态 | bpchar | 1 |  | √ | ' ' | 资质审查状态,枚举: A :待审批 E :资审通过 F :资审驳回 |
| 53 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 54 | fauditstatus2 | 现场考察状态 | bpchar | 1 |  | √ | ' ' | 现场考察状态,枚举: A :待审批 G :现场通过 H :现场驳回 |
| 55 | fauditstatus3 | 样品确认状态 | bpchar | 1 |  | √ | ' ' | 样品确认状态,枚举: A :待审批 I :样品通过 J :样品驳回 |
| 56 | fregcapital | 注册资本 | numeric | 19 | 6 | √ | 0.000000 | 注册资本 |
| 57 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 58 | fauditstatus4 | 物料试用状态 | bpchar | 1 |  | √ | ' ' | 物料试用状态,枚举: A :待审批 K :物料通过 L :物料驳回 |
| 59 | fregdate | 企业成立日期 | timestamp | 0 |  |  | null | 企业成立日期 |
| 60 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 61 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 62 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 63 | fnewphone | 手机 | varchar | 50 |  | √ | ' ' | 手机 |
| 64 | ftype | 企业类型 | bpchar | 1 |  | √ | ' ' | 企业类型,枚举: 1 :法人企业 2 :国家机关 3 :事业单位 4 :社会团体 5 :其他组织机构 6 :个体户 7 :个人 8 :非法人企业 |
| 65 | findustryid | 所属行业 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 66 | fsimplename | 简称 | varchar | 255 |  | √ | ' ' | 简称 |
| 67 | furl | 公司网址 | varchar | 100 |  | √ | ' ' | 公司网址 |
| 68 | ftoexam | ftoexam | bpchar | 1 |  | √ | '1' |  |
| 69 | fdeductible | 是否可以抵扣 | bpchar | 1 |  | √ | ' ' | 是否可以抵扣 |
| 70 | ftxregisterno | 纳税人识别号 | varchar | 60 |  | √ | ' ' | 纳税人识别号 |
| 71 | fenterprisespros | 供应商属性 | bpchar | 1 |  | √ | '0' | 供应商属性,枚举: 1 :生产商 2 :代理商 3 :贸易商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_regsupplier_createorg |  | fcreateorgid |
| 2 | idx_pur_regsupplier_fnumber |  | fnumber |
| 3 | idx_pur_regsupplier_fphone |  | fphone |
| 4 | t_pur_regsupplier_pkey |  | fid |
| 5 | idx_t_pur_regsupplier_master |  | fmasterid |

---

## 合同分录-子表 t_pur_regsupcontract

- **表名称：** 合同分录-子表
- **表名：** t_pur_regsupcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconamount | 合同金额 | numeric | 19 | 6 | √ | 0.000000 | 合同金额 |
| 3 | fcustomer | 客户名称 | varchar | 100 |  | √ | ' ' | 客户名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fconname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcondate | 签约时间 | timestamp | 0 |  |  | null | 签约时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupcontract_pkey |  | fentryid |
| 2 | idx_pur_regsupcontract_fid |  | fid,fseq |

---

## 审批分录-子表 t_pur_regsupaudit

- **表名称：** 审批分录-子表
- **表名：** t_pur_regsupaudit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexamtime | 评审时间 | timestamp | 0 |  |  | null | 评审时间 |
| 3 | fexamerid | 评审人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsrcbillno | 评审单号 | varchar | 80 |  | √ | ' ' | 评审单号 |
| 5 | fexamstatus | 评审结果 | bpchar | 1 |  | √ | ' ' | 评审结果,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 E :退回修改 |
| 6 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 7 | fexamnote | 评审意见 | varchar | 510 |  | √ | ' ' | 评审意见 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fexamtype | 评审类型 | bpchar | 1 |  | √ | ' ' | 评审类型,枚举: 1 :注册审批 2 :资质审查 3 :现场评审 4 :样品确认 5 :物料试用 6 :供应商生效 7 :品类变更 8 :供应商退出 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsrctype | 源单类型 | varchar | 20 |  | √ | ' ' | 源单类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupaudit_pkey |  | fentryid |
| 2 | idx_pur_regsupaudit_fid_fseq |  | fid,fseq |

---

## 生产相关情况-子表 t_pur_product

- **表名称：** 生产相关情况-子表
- **表名：** t_pur_product

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductoolname | 生产设备名称 | varchar | 100 |  | √ | ' ' | 生产设备名称 |
| 3 | fstaffnums | 生产线上工人数 | numeric | 19 |  | √ | 0 | 生产线上工人数 |
| 4 | fproduction | 生产设备厂商 | varchar | 255 |  | √ | ' ' | 生产设备厂商 |
| 5 | fqestaffnums | 生产线质控人员数 | numeric | 19 |  | √ | 0 | 生产线质控人员数 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcycle | 正常交货周期 | varchar | 255 |  | √ | ' ' | 正常交货周期 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fputdate | 生产线投产时间 | timestamp | 0 |  |  | null | 生产线投产时间 |
| 10 | ftraffic | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 11 | fproductoolnum | 设备数量 | numeric | 19 |  | √ | 0 | 设备数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_product |  | fentryid |
| 2 | idx_t_pur_product |  | fid,fseq |

---

## 股权信息-子表 t_pur_regstock

- **表名称：** 股权信息-子表
- **表名：** t_pur_regstock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstockremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fnationality | 国籍 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 4 | fstocklevel | 股东层级 | bpchar | 1 |  | √ | ' ' | 股东层级,枚举: A :直接持股 B :间接持股 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fstockratio | 持股比例(%) | numeric | 19 | 6 | √ | 0.000000 | 持股比例(%) |
| 8 | fstockname | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_regstock |  | fid,fseq |
| 2 | pk_t_pur_regstock |  | fentryid |

---

## 附件-附件表 t_pur_regsupgoods_att

- **表名称：** 附件-附件表
- **表名：** t_pur_regsupgoods_att

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
| 1 | t_pur_regsupgoods_att_pkey |  | fpkid |
| 2 | idx_regsupgoods_att_fbdid |  | fbasedataid |
| 3 | idx_regsupgoods_att_fentryid |  | fentryid |

---

## 指标分录-子表 t_pur_regsupindex

- **表名称：** 指标分录-子表
- **表名：** t_pur_regsupindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 指标值 | numeric | 19 | 6 | √ | 0.000000 | 指标值 |
| 3 | ftype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 1 :年营业额 2 :期末净资产 3 :资产负债率 4 :资产收益率 5 :年利润额 |
| 4 | fyear | 指标年度 | varchar | 10 |  | √ | ' ' | 指标年度 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | funit | 指标单位 | varchar | 10 |  | √ | ' ' | 指标单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupindex_pkey |  | fentryid |
| 2 | idx_pur_regsupindex_fid_fseq |  | fid,fseq |

---

## 市-多选基础资料表 t_pur_regsupplier_city

- **表名称：** 市-多选基础资料表
- **表名：** t_pur_regsupplier_city

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_regsupplier_city_pkey |  | fpkid |
| 2 | t_pur_regsupplier_city_fid |  | fentryid,fbasedataid |

---

## 供应商附件-附件表 t_pbd_supattupload

- **表名称：** 供应商附件-附件表
- **表名：** t_pbd_supattupload

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
| 1 | pk_pbd_supattupload |  | fpkid |
| 2 | idx_pbd_supattupload_fbdid |  | fbasedataid |

---

## 附件-附件表 t_pur_regsupcontract_att

- **表名称：** 附件-附件表
- **表名：** t_pur_regsupcontract_att

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
| 1 | pk_regsupcontract_att_fentryid |  | fentryid |
| 2 | t_pur_regsupcontract_att_pkey |  | fpkid |
| 3 | pk_regsupcontract_att_fbdid |  | fbasedataid |

---

## 联系人分录-子表 t_pur_regsuplink

- **表名称：** 联系人分录-子表
- **表名：** t_pur_regsuplink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 姓名 | varchar | 255 |  | √ | ' ' | 姓名 |
| 3 | fphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 4 | faddress | 联系地址 | varchar | 100 |  | √ | ' ' | 联系地址 |
| 5 | fgender | 性别 | bpchar | 1 |  | √ | ' ' | 性别,枚举: 1 :男 2 :女 |
| 6 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 7 | fdept | 部门 | varchar | 50 |  | √ | ' ' | 部门 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fbizscopetype | 负责业务 | bpchar | 1 |  | √ | ' ' | 负责业务,枚举: A :业务 B :财务 C :PO接收 D :其他 |
| 11 | fmobile | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 12 | fduty | 职务 | varchar | 50 |  | √ | ' ' | 职务 |
| 13 | fpost | 邮编 | varchar | 10 |  | √ | ' ' | 邮编 |
| 14 | ffax | 传真 | varchar | 50 |  | √ | ' ' | 传真 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fisdefault | 默认 | bpchar | 1 |  | √ | ' ' | 默认 |
| 17 | fbizscope | 备注 | varchar | 50 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_regsuplink_fid_fseq |  | fid,fseq |
| 2 | t_pur_regsuplink_pkey |  | fentryid |
